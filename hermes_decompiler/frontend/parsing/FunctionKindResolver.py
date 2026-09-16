from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable, Iterator

from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

#: Creation opcodes whose target is the *body* of a generator/async
#: function - i.e. the function that actually holds the suspend/resume
#: state machine. True on every bytecode version seen so far; see
#: FunctionKindIndex's docstring for why this, and not the per-function
#: signals, is the load-bearing one.
_BODY_CREATING_OPS = ("CreateGenerator",)

#: Creation opcodes whose target is an intermediate *stub* - a function
#: that exists only to construct something and return it, never to run
#: user code. LAYOUT_V96 spells the generator stub explicitly
#: (CreateGeneratorClosure); v97+ dropped that opcode and marks stubs via
#: the header Kind bits instead, reaching them through a plain
#: CreateClosure.
_STUB_CREATING_OPS = ("CreateGeneratorClosure",)

#: Every creation opcode we follow when walking the creation graph.
_CREATION_OPS = _BODY_CREATING_OPS + _STUB_CREATING_OPS + ("CreateClosure", "CreateAsyncFunction")

_HEADER_RE = re.compile(
    r'^=>\s+\[(Async |Generator )?[Ff]unction #(\d+) "([^"]*)"',
    re.MULTILINE,
)

_CREATION_EDGE_RE = re.compile(
    r"<(Create[A-Za-z0-9]*)>:[^#\n]*function_id:\s*(\d+)"
)

#: Guard against pathological/cyclic input when climbing creation chains.
#: Chains observed in practice are at most 2 links deep (async stub ->
#: generator stub -> body), so this is generous.
_MAX_CHAIN_DEPTH = 8


@dataclass(frozen=True)
class FunctionKindFacts:
    """
    What the *batch* knows about one function's generator/async nature.

    Every field here is a resolved fact, not a guess: see
    FunctionKindIndex for how each is derived and why none of the
    per-function signals can produce them on its own.
    """

    function_id: int

    #: 'normal' | 'generator' | 'async' - this function's own header
    #: FuncKind. Only ever non-'normal' on layouts that have Kind bits
    #: (v97+); always 'normal' under LAYOUT_V96 regardless of the truth.
    header_kind: str = "normal"

    #: 'body' | 'stub' | 'normal'.
    #:   body   - holds the actual suspend/resume state machine
    #:   stub   - only constructs the next link and returns it
    #:   normal - an ordinary function
    role: str = "normal"

    #: 'generator' | 'async' | 'unknown' - the *source-level* keyword this
    #: chain came from. 'unknown' means the batch carried no evidence
    #: either way (the normal case on LAYOUT_V96, which has no Kind bits),
    #: NOT that the function is ordinary - check `role` for that.
    source_kind: str = "unknown"

    #: For a stub: the body it eventually reaches. None otherwise.
    body_id: int | None = None

    #: For a body: the stub chain above it, outermost first.
    stub_ids: tuple[int, ...] = ()

    #: True iff this function's own bytecode contains <StartGenerator>.
    #: A LAYOUT_V96-only signal - v97+ emits no such opcode at all.
    has_start_generator: bool = False

    @property
    def is_generator_body(self) -> bool:
        """True iff this function holds a suspend/resume state machine."""
        return self.role == "body"

    @property
    def is_async_source(self) -> bool:
        """
        True iff this chain came from an `async` keyword in the source.

        False for a plain `function*` AND for 'unknown' - callers that
        need to distinguish "known not async" from "no evidence" must
        read `source_kind` directly.
        """
        return self.source_kind == "async"


@dataclass
class _RawSection:
    """One section's per-function signals, before cross-section resolution."""

    function_id: int
    name: str
    header_kind: str
    has_start_generator: bool
    edges: list[tuple[str, int]] = field(default_factory=list)

    def targets(self, ops: Iterable[str]) -> Iterator[int]:
        for op, target in self.edges:
            if op in ops:
                yield target


class FunctionKindIndex:
    """
    Cross-section index of which functions are generator/async bodies.

    Why this cannot be done per-section
    -----------------------------------
    Hermes compiles `function* f()` / `async function f()` into a *chain*
    of functions, not one:

        v96:  f [normal] --CreateGeneratorClosure--> stub [normal]
                         --CreateGenerator--> body [normal, <StartGenerator>]

        v98:  f [generator] --CreateGenerator--> body [normal]
        v98:  f [async] --CreateClosure--> stub [generator]
                        --CreateGenerator--> body [normal]

    Each *individual* signal is an artifact of one bytecode version:

      - <StartGenerator> exists only on LAYOUT_V96. v97+ lowers generators
        into a hand-rolled state-dispatch machine and emits no
        suspend/resume opcodes whatsoever, so any check for them silently
        reports "not a generator" for every generator in the bundle.

      - Header Kind bits exist only on v97+. And even there they sit on
        the *stub*, never on the body - so reading a function's own Kind
        tells you nothing about whether that function holds the state
        machine.

    The one invariant that holds across every version seen so far is the
    *edge*: the target of a CreateGenerator is the body. That edge lives
    in a different section than the body it identifies, which is why this
    is a batch-level index and not another pipeline stage.

    Async-ness is recovered the same way. It is readable only from the
    outermost stub's Kind (v97+), so it is propagated *down* the chain to
    the body. On LAYOUT_V96 no Kind bits exist and `source_kind` stays
    'unknown', leaving callers on their existing heuristics - this index
    never fabricates an answer it has no evidence for.
    """

    def __init__(self, facts: dict[int, FunctionKindFacts]):
        self._facts = facts

    def __len__(self) -> int:
        return len(self._facts)

    def __contains__(self, function_id: int) -> bool:
        return function_id in self._facts

    def facts_for(self, function_id: int) -> FunctionKindFacts | None:
        """Resolved facts for `function_id`, or None if it wasn't in the batch."""
        return self._facts.get(function_id)

    def bodies(self) -> list[FunctionKindFacts]:
        """All resolved generator/async bodies, ordered by function id."""
        return [f for _, f in sorted(self._facts.items()) if f.role == "body"]

    # -- construction ----------------------------------------------------

    @classmethod
    def from_sections(cls, sections: Iterable[tuple[int, str]]) -> "FunctionKindIndex":
        """
        Build the index from `(section_index, hasm_text)` pairs.

        `section_index` is only a fallback identity: the authoritative
        function id comes from each section's own header line, since the
        two can disagree (a section file may be renamed, and only the
        header id is what creation edges actually reference).
        """
        raw = cls._scan(sections)
        return cls(cls._resolve(raw))

    @classmethod
    def empty(cls) -> "FunctionKindIndex":
        """An index that knows nothing - every lookup returns None."""
        return cls({})

    @staticmethod
    def _scan(sections: Iterable[tuple[int, str]]) -> dict[int, _RawSection]:
        raw: dict[int, _RawSection] = {}

        for section_index, text in sections:
            header = _HEADER_RE.search(text)
            if not header:
                logger.debug("Section #%s has no parseable header line; skipped.", section_index)
                continue

            function_id = int(header.group(2))
            edges = [
                (op, int(target))
                for op, target in _CREATION_EDGE_RE.findall(text)
                if op in _CREATION_OPS
            ]

            raw[function_id] = _RawSection(
                function_id=function_id,
                name=header.group(3),
                header_kind=(header.group(1) or "normal").strip().lower(),
                has_start_generator="<StartGenerator>" in text,
                edges=edges,
            )

        return raw

    @classmethod
    def _resolve(cls, raw: dict[int, _RawSection]) -> dict[int, FunctionKindFacts]:
        # A body is whatever a CreateGenerator points at. <StartGenerator>
        # is unioned in rather than relied on: it corroborates the edge on
        # LAYOUT_V96 and still identifies a body if that body's creator
        # happens to sit outside the batch.
        body_ids = {t for s in raw.values() for t in s.targets(_BODY_CREATING_OPS)}
        body_ids |= {fid for fid, s in raw.items() if s.has_start_generator}

        stub_ids = {t for s in raw.values() for t in s.targets(_STUB_CREATING_OPS)}
        stub_ids |= {fid for fid, s in raw.items() if s.header_kind != "normal"}
        stub_ids -= body_ids  # a body is never also a stub

        creators = cls._creator_map(raw)

        facts: dict[int, FunctionKindFacts] = {}
        for function_id, section in raw.items():
            if function_id in body_ids:
                role = "body"
            elif function_id in stub_ids:
                role = "stub"
            else:
                role = "normal"

            chain = cls._stub_chain(function_id, raw, creators) if role == "body" else ()
            source_kind = cls._source_kind(section, chain, raw)

            facts[function_id] = FunctionKindFacts(
                function_id=function_id,
                header_kind=section.header_kind,
                role=role,
                source_kind=source_kind,
                body_id=cls._body_of(function_id, raw) if role == "stub" else None,
                stub_ids=chain,
                has_start_generator=section.has_start_generator,
            )

        return facts

    @staticmethod
    def _creator_map(raw: dict[int, _RawSection]) -> dict[int, list[int]]:
        """target function id -> ids of the functions that create it."""
        creators: dict[int, list[int]] = {}
        for function_id, section in raw.items():
            for _, target in section.edges:
                creators.setdefault(target, []).append(function_id)
        return creators

    @staticmethod
    def _stub_chain(
            body_id: int,
            raw: dict[int, _RawSection],
            creators: dict[int, list[int]],
    ) -> tuple[int, ...]:
        """
        Climb from a body up through its stubs, outermost first.

        Only non-'normal' Kind parents are followed. That bound is what
        keeps an ordinary enclosing function - which reaches the stub
        through the very same CreateClosure opcode used for every
        unrelated closure in the bundle - from being mistaken for part of
        the chain. It also means the chain is empty on LAYOUT_V96, where
        no function ever reports a non-'normal' Kind; `_source_kind`
        handles that case rather than guessing here.
        """
        chain: list[int] = []
        current = body_id
        seen = {body_id}

        for _ in range(_MAX_CHAIN_DEPTH):
            parents = [
                p for p in creators.get(current, [])
                if p not in seen and raw[p].header_kind != "normal"
            ]
            if not parents:
                break
            # Deterministic when a stub is (unexpectedly) created twice.
            parent = min(parents)
            chain.append(parent)
            seen.add(parent)
            current = parent

        return tuple(reversed(chain))

    @staticmethod
    def _source_kind(
            section: _RawSection,
            chain: tuple[int, ...],
            raw: dict[int, _RawSection],
    ) -> str:
        """
        The source keyword this function's chain came from.

        'async' outranks 'generator': an async function is lowered as an
        async stub wrapping a *generator* stub, so both kinds appear in
        one chain and only the outermost one reflects what was written.
        """
        kinds = [raw[s].header_kind for s in chain] + [section.header_kind]

        if "async" in kinds:
            return "async"
        if "generator" in kinds:
            return "generator"
        return "unknown"

    @staticmethod
    def _body_of(stub_id: int, raw: dict[int, _RawSection]) -> int | None:
        """Walk down a stub's creation chain to the body it produces."""
        current = stub_id
        seen = {stub_id}

        for _ in range(_MAX_CHAIN_DEPTH):
            section = raw.get(current)
            if section is None:
                return None

            body = next(section.targets(_BODY_CREATING_OPS), None)
            if body is not None:
                return body

            # No direct body yet - step through the next stub down.
            nxt = next(
                (
                    t for t in section.targets(_CREATION_OPS)
                    if t not in seen and raw.get(t) is not None and raw[t].header_kind != "normal"
                ),
                None,
            )
            if nxt is None:
                return None
            seen.add(nxt)
            current = nxt

        return None
