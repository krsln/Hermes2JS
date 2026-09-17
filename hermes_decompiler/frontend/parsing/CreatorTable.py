from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

_HEADER_RE = re.compile(
    r'^=>\s+\[(Async |Generator )?[Ff]unction #(\d+) "([^"]*)"',
    re.MULTILINE,
)
_CREATION_EDGE_RE = re.compile(r"<(Create[A-Za-z0-9]*)>:[^#\n]*function_id:\s*(\d+)")

#: The one opcode that identifies a generator/async *body* on every
#: bytecode version seen so far, hbc96 and hbc98 alike: whatever function
#: this targets is where the actual suspend/resume state machine lives -
#: see CreatorTable's docstring. Never used for anything but generator
#: bodies, so propagation through it is unconditional.
_BODY_OPS = ("CreateGenerator", "CreateGeneratorLongIndex")

#: hbc96-only opcodes (absent from 98.json - hbc97+ dropped them in favor
#: of the header Kind bits `header_kind` reads instead) that identify an
#: intermediate generator/async *stub* by opcode identity alone, exactly
#: the way vendor/hermes-dec's pass2_transform_code.py tags its own
#: function_table. Like `_BODY_OPS`, these opcodes are never used to
#: create an unrelated closure, so propagation through them is
#: unconditional too.
_GENERATOR_STUB_OPS = ("CreateGeneratorClosure", "CreateGeneratorClosureLongIndex")
_ASYNC_STUB_OPS = ("CreateAsyncClosure", "CreateAsyncClosureLongIndex")

#: The generic closure-creation opcode, used for every closure in a
#: bundle - callbacks, helpers, all of it - not just generator/async
#: stubs. Propagating through this one unconditionally would mark
#: unrelated closures created inside an async function as async
#: themselves, so it is only followed when the *target*'s own header
#: independently confirms it belongs to a generator/async chain - see
#: CreatorTable._propagate.
_CLOSURE_OPS = ("CreateClosure", "CreateClosureLongIndex")

_MAX_ITERATIONS = 8


@dataclass(frozen=True)
class CreatorFacts:
    is_generator: bool = False
    is_async: bool = False


class CreatorTable:
    """
    Batch-level answer to "is function #N a generator/async body", built
    the way vendor/hermes-dec's pass2_transform_code.py builds its own
    function_table: by tagging whatever a creation opcode's `function_id`
    operand points at, rather than inspecting that function's own bytecode
    (which on hbc97+ contains no trace of being a generator/async body at
    all - see SignatureStage).

    Two things hermes-dec's exact mechanism doesn't cover, both handled
    here instead:

      - hbc97+ dropped CreateGeneratorClosure/CreateAsyncClosure - the
        very opcodes hermes-dec's tagging depends on - in favor of a
        plain CreateClosure into a function whose own header carries a
        Kind tag (`header_kind`). Seeding from that header, in addition
        to the hbc96 opcodes, is what makes this work on both versions.

      - Async-ness has to reach the *body*, which sits one hop further
        than whatever CreateAsyncClosure/a non-normal header tags
        directly. `_propagate` carries it the rest of the way along
        CreateGenerator, since that opcode's target is always the real
        body, on every version.

    Deliberately narrow: no stub/body role, no chain bookkeeping, no CFG
    involvement. It answers exactly two booleans per function id and
    nothing else - see FunctionKindIndex (removed) for what happens when
    this scope creeps.
    """

    def __init__(self, generator_bodies: set[int], async_bodies: set[int]):
        self._generator_bodies = generator_bodies
        self._async_bodies = async_bodies

    def facts_for(self, function_id: int) -> CreatorFacts:
        return CreatorFacts(
            is_generator=function_id in self._generator_bodies,
            is_async=function_id in self._async_bodies,
        )

    @property
    def generator_body_count(self) -> int:
        return len(self._generator_bodies)

    @classmethod
    def empty(cls) -> "CreatorTable":
        return cls(set(), set())

    @classmethod
    def from_sections(cls, sections: Iterable[tuple[int, str]]) -> "CreatorTable":
        header_kind: dict[int, str] = {}
        edges: list[tuple[int, str, int]] = []

        for section_index, text in sections:
            header = _HEADER_RE.search(text)

            if not header:
                logger.debug("Section #%s has no parseable header line; skipped.", section_index)
                continue

            function_id = int(header.group(2))
            header_kind[function_id] = (header.group(1) or "normal").strip().lower()

            for op, target in _CREATION_EDGE_RE.findall(text):
                edges.append((function_id, op, int(target)))

        is_async: dict[int, bool] = {
            fid: True for fid, kind in header_kind.items() if kind == "async"
        }
        is_generator_body: set[int] = set()

        for source, op, target in edges:
            if op in _ASYNC_STUB_OPS:
                is_async[target] = True

        cls._propagate(edges, header_kind, is_async, is_generator_body)

        return cls(is_generator_body, {fid for fid, flag in is_async.items() if flag})

    @staticmethod
    def _propagate(
            edges: list[tuple[int, str, int]],
            header_kind: dict[int, str],
            is_async: dict[int, bool],
            is_generator_body: set[int],
    ) -> None:
        """
        Carries `is_async` forward along creation edges to the body
        `_BODY_OPS` identifies, and marks that body's id in
        `is_generator_body` - both mutated in place.

        Runs to a fixed point rather than one pass: the hbc98 async case
        is two hops (outer's header -> CreateClosure into a
        Kind-tagged stub -> CreateGenerator into the body), and nothing
        here assumes a chain is exactly that long.
        """
        for _ in range(_MAX_ITERATIONS):
            changed = False

            for source, op, target in edges:
                if op in _BODY_OPS:
                    if target not in is_generator_body:
                        is_generator_body.add(target)
                        changed = True

                    if is_async.get(source) and not is_async.get(target):
                        is_async[target] = True
                        changed = True

                elif op in _GENERATOR_STUB_OPS:
                    if is_async.get(source) and not is_async.get(target):
                        is_async[target] = True
                        changed = True

                elif op in _CLOSURE_OPS:
                    # Only followed when the target's own header
                    # independently confirms it belongs to a
                    # generator/async chain - see `_CLOSURE_OPS`'s
                    # docstring for why an unconditional version of this
                    # branch is wrong.
                    if header_kind.get(target, "normal") == "normal":
                        continue

                    if is_async.get(source) and not is_async.get(target):
                        is_async[target] = True
                        changed = True

            if not changed:
                break
