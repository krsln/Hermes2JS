from __future__ import annotations

import re
from typing import Iterable

from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

# ==> 00000002: <CreateEnvironment>: <Reg8: 4>
_CREATE_ENV_RE = re.compile(r"<CreateEnvironment>:\s*<Reg8:\s*(\d+)>")

# ==> 00000005: <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 3>
_CREATE_FUNC_ENV_RE = re.compile(r"<CreateFunctionEnvironment>:\s*<Reg8:\s*(\d+),")

# ==> 00000030: <GetEnvironment>: <Reg8: 1, UInt8: 0>                    (2-operand form)
# ==> 00000030: <GetEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 1>           (3-operand form, hbc97+)
# level = 0 -> THIS function's own frame, 1 -> parent, 2 -> grandparent,
# ... (see GetEnv.py) - unlike GetParentEnvironment below, level 0 here
# means "no hop at all", not "one hop".
_GET_ENV_RE = re.compile(
    r"<GetEnvironment>:\s*<Reg8:\s*(\d+),\s*(?:Reg8:\s*\d+,\s*)?UInt8:\s*(\d+)>"
)

# ==> 00000000: <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
# "N levels up the ENCLOSING scope chain" (see GetParentEnv.py). Whether
# level 0 already means one hop up, or is the same as
# GetEnvironment(0)'s "no hop at all", depends on whether the CURRENT
# function has its own depth-0 frame to skip past in the first place -
# see owner()'s docstring on `frame_offset` and _scan_function's use of
# it here.
_GET_PARENT_ENV_RE = re.compile(r"<GetParentEnvironment>:\s*<Reg8:\s*(\d+),\s*UInt8:\s*(\d+)>")

# ==> 00000002: <CreateClosure>: <Reg8: 3, Reg8: 4, function_id: 15198>
# ==> 00000002: <CreateClosureLongIndex>: <Reg8: 3, Reg8: 4, function_id: 15198>
_CREATE_CLOSURE_RE = re.compile(
    r"<CreateClosure(?:LongIndex)?>:\s*<Reg8:\s*\d+,\s*Reg8:\s*(\d+),\s*function_id:\s*(\d+)>"
)

_MAX_HOPS = 32


class EnvironmentOriginTable:
    """
    Batch-level answer to "which function's own frame does (function id,
    depth) actually refer to", built the same way CreatorTable resolves
    generator/async bodies: by scanning every section's raw text for
    `CreateClosure`/`CreateClosureLongIndex` edges, rather than by giving
    any one function's own bytecode a CFG-level analysis (the linkage a
    given `GetEnvironment`/`GetParentEnvironment` depth actually resolves
    to was established by a *different* function - whichever one created
    this one as a closure - so, like CreatorTable's generator/async edge,
    no per-section pass can reach it alone).

    Exists as shared infrastructure for PrivateNameTable and
    ClassEnvironmentTable, both of which need to turn a
    `LoadFromEnvironment(depth, slot)` read in the function currently
    being decompiled into "which function actually populated that slot"
    before they can look the name up. Kept separate from both of them
    (and from CreatorTable) rather than folded into a single do-everything
    table - see CreatorTable's own docstring on why that generic-index
    shape was tried before and removed.

    Hermes threads closures together like this: `CreateClosure(dest,
    env_reg, target_id)` makes `target_id` a closure over whatever
    environment `env_reg` currently holds in the CREATING function - so
    target's own depth-0 (its own frame, from its own
    CreateEnvironment/CreateFunctionEnvironment) is unrelated to any of
    this, but target's depth-1 (its immediate lexical parent) is exactly
    whatever `env_reg` pointed to. If `env_reg` was the creator's OWN
    frame (`effective_depth` 0, from a plain CreateEnvironment/
    CreateFunctionEnvironment in the creator with no further hop), then
    target's depth-1 IS the creator's own frame directly - depth-2 is
    the creator's depth-1, and so on, one hop further out for every extra
    level target asks for. If `env_reg` was itself some ancestor the
    creator reached via GetEnvironment/GetParentEnvironment (`linkage_depth`
    hops up from the creator's own frame), the same shift applies with
    that many extra hops folded in. `owner()` below is exactly that
    shift, applied recursively until depth 0 is reached.
    """

    def __init__(self, creation_info: dict[int, tuple[int, int]], has_own_frame: set[int]):
        #: target_function_id -> (creator_function_id, linkage_depth),
        #: where linkage_depth is creator_function_id's OWN effective
        #: depth (0 = creator's own frame) for whatever environment
        #: register the creator passed to CreateClosure.
        self._creation_info = creation_info
        #: function ids that execute their own CreateEnvironment/
        #: CreateFunctionEnvironment - see owner()'s docstring for why
        #: a function that DOESN'T is missing a frame layer other
        #: functions have, and needs different depth arithmetic.
        self._has_own_frame = has_own_frame

    def owner(self, function_id: int, depth: int) -> int | None:
        """
        Which function's own frame (`function_id`, 0) does
        (`function_id`, `depth`) actually refer to.

        A function that never executes its own CreateEnvironment/
        CreateFunctionEnvironment has no frame layer of its own at all -
        its depth 0 ("current environment") is literally the SAME
        environment object its creator handed it, not a new one it
        allocated (confirmed against ClassTests.ts's `classTest`, whose
        own body never creates an environment yet reads Animal/Dog via
        `GetEnvironment(0)`). Every depth this table resolves is
        adjusted by whether the function in question has that layer -
        `frame_offset` below - rather than assuming every function's
        depth 0 is its own, the way a function that DOES create one
        would suggest.

        Returns None the moment the chain can't be followed any further -
        an entry function with no creator, a section missing from the
        batch this table was built from, or a genuinely malformed/cyclic
        chain (guarded by `_MAX_HOPS` rather than trusted to terminate on
        its own) - rather than guess. Callers treat that exactly like "no
        name known here": degrade to whatever numeric/symbolic fallback
        they'd otherwise use.
        """
        for _ in range(_MAX_HOPS):
            frame_offset = 1 if function_id in self._has_own_frame else 0

            if depth < frame_offset:
                return function_id

            info = self._creation_info.get(function_id)
            if info is None:
                return None

            creator_id, linkage_depth = info
            function_id, depth = creator_id, linkage_depth + depth - frame_offset

        logger.debug(
            "EnvironmentOriginTable: owner() gave up after %d hops resolving "
            "function %s - possible cycle in the CreateClosure chain.",
            _MAX_HOPS, function_id,
        )
        return None

    @classmethod
    def empty(cls) -> "EnvironmentOriginTable":
        return cls({}, set())

    @classmethod
    def from_sections(cls, sections: Iterable[tuple[int, str]]) -> "EnvironmentOriginTable":
        sections = list(sections)

        # Two passes: GetParentEnvironment's own level count is relative
        # to whatever this function's OWN depth-0 already is (see its
        # handling below and owner()'s docstring on `frame_offset`) -
        # which needs `has_own_frame` already known for a function
        # before that function's own GetParentEnvironment lines can be
        # interpreted correctly. In practice frame setup always happens
        # once, at the very start of a function, before anything else
        # runs - so scanning the whole function once just for this
        # first would work too - but building it as an explicit first
        # pass over every section removes the assumption entirely
        # rather than relying on it.
        has_own_frame: set[int] = set()
        for function_id, text in sections:
            if _CREATE_ENV_RE.search(text) or _CREATE_FUNC_ENV_RE.search(text):
                has_own_frame.add(function_id)

        creation_info: dict[int, tuple[int, int]] = {}
        for function_id, text in sections:
            cls._scan_function(function_id, text, creation_info, has_own_frame)

        return cls(creation_info, has_own_frame)

    @staticmethod
    def _scan_function(
            function_id: int,
            text: str,
            creation_info: dict[int, tuple[int, int]],
            has_own_frame: set[int],
    ) -> None:
        """
        Walks one function's `.hasm` text top-to-bottom (bytecode is
        already laid out in address order, so textual order is
        instruction order here), tracking which register currently holds
        which environment as an "effective depth" relative to this
        function's OWN frame - 0 for a freshly-established own frame, N
        for its Nth lexical ancestor - and records a `creation_info`
        entry for every CreateClosure/CreateClosureLongIndex this
        function executes whose environment register resolves to a known
        depth at that point.

        `has_own_frame` is an INPUT here (built by a prior pass over
        every section - see from_sections), used only to normalize
        GetParentEnvironment's level count onto the same "hops from my
        own depth 0" scale GetEnvironment's already uses - see
        owner()'s docstring for why the two need different treatment.

        A register whose depth isn't yet known (nothing here has set it,
        or its last known value was overwritten by something this scan
        doesn't track - a Mov, say) is simply absent from the running
        map; a CreateClosure using such a register is skipped rather than
        guessed at, same "bail rather than guess" policy as everywhere
        else this table degrades.
        """
        register_depth: dict[int, int] = {}
        frame_offset = 1 if function_id in has_own_frame else 0

        for line in text.splitlines():
            match = _CREATE_ENV_RE.search(line)
            if match:
                register_depth[int(match.group(1))] = 0
                continue

            match = _CREATE_FUNC_ENV_RE.search(line)
            if match:
                register_depth[int(match.group(1))] = 0
                continue

            match = _GET_ENV_RE.search(line)
            if match:
                register_depth[int(match.group(1))] = int(match.group(2))
                continue

            match = _GET_PARENT_ENV_RE.search(line)
            if match:
                register_depth[int(match.group(1))] = int(match.group(2)) + frame_offset
                continue

            match = _CREATE_CLOSURE_RE.search(line)
            if match:
                env_reg, target_id = int(match.group(1)), int(match.group(2))
                depth = register_depth.get(env_reg)

                if depth is not None:
                    creation_info[target_id] = (function_id, depth)

                continue
