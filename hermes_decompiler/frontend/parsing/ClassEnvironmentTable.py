from __future__ import annotations

import re
from typing import Iterable

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.parsing.EnvironmentOriginTable import EnvironmentOriginTable

logger = get_logger(__name__)

# ==> 00000002: <CreateClosure>: <Reg8: 3, Reg8: 4, function_id: 15198>  # Function: [#15198 Animal of 72 bytes]: 3 params @ ...
# ==> 00000002: <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15197>  # Function: [#15197  of 83 bytes]: 1 params @ ...
# The name group is empty for an anonymous target (two spaces between the
# id and "of") - only a non-empty match is a usable name below.
_CREATE_CLOSURE_NAMED_RE = re.compile(
    r"<CreateClosure(?:LongIndex)?>:\s*<Reg8:\s*(\d+),\s*Reg8:\s*\d+,\s*function_id:\s*(\d+)>"
    r"\s*#\s*Function:\s*\[#\d+\s(.*?)\sof\s\d+\sbytes\]"
)

# Same instruction shape (dest reg, then callee reg) across Call/Call1-4 -
# the ones actually observed calling a class-factory helper. Deliberately
# doesn't match CallBuiltin/CallDirect/CallLong etc. (letters, not just
# digits, after "Call") - those either don't take a callee register at
# all or aren't how this pattern is compiled in practice.
_CALL_RE = re.compile(r"<Call\d*>:\s*<Reg8:\s*(\d+),\s*Reg8:\s*(\d+)")

# ==> 00000064: <StoreToEnvironment>: <Reg8: 4, UInt8: 2, Reg8: 2>
_STORE_TO_ENV_RE = re.compile(
    r"<StoreToEnvironment[L]?>:\s*<Reg8:\s*(\d+),\s*U(?:Int8|Int16):\s*(\d+),\s*Reg8:\s*(\d+)>"
)

# ==> 00000002: <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15197>
_CREATE_CLOSURE_RE = re.compile(
    r"<CreateClosure(?:LongIndex)?>:\s*<Reg8:\s*(\d+),\s*Reg8:\s*\d+,\s*function_id:\s*(\d+)>"
)


class ClassEnvironmentTable:
    """
    Batch-level `(owning function id, slot) -> real class name` lookup,
    for classes compiled through a Babel/TS-style "class factory helper"
    rather than Hermes's own CreateBaseClass/CreateDerivedClass opcodes
    (see CreateBaseClass.py's own docstring - that opcode pair already
    resolves names correctly when it's what actually gets emitted, but
    neither appears anywhere in ClassTests.ts's own compiled output; only
    this helper-call shape does).

    The shape (see ClassTests.ts / function_15194_anonymous.hasm):

        CreateClosure   helper_reg, env, function_id=HELPER
        Call1           class_reg = helper_reg(...)
        StoreToEnvironment  env, slot, class_reg

    where HELPER's OWN body creates the real, named constructor closure
    as (heuristically, but consistently with how this compiler emits it -
    the constructor always comes first, prototype methods after) the
    FIRST CreateClosure in its body whose target has a real function-table
    name:

        CreateClosure   ctor_reg, _, function_id=REAL   # Function: [#REAL Animal ...]
        ... (prototype methods attached to ctor_reg here) ...
        Ret             ctor_reg-derived class object

    So the class stored at (declaring function, slot) is named after
    whichever function HELPER's own first named CreateClosure points at -
    "Animal", not whatever `Call1`'s own return value would otherwise be
    called.

    Same degrade-gracefully behavior as PrivateNameTable: a class whose
    declaring/helper functions aren't part of the batch this table was
    built from simply has no entry.
    """

    def __init__(self, slot_names: dict[int, dict[int, str]], environment_origins: EnvironmentOriginTable):
        #: owning_function_id -> {slot: 'Animal'}
        self._slot_names = slot_names
        self._environment_origins = environment_origins

    def name_for(self, function_id: int, depth: int, slot: int) -> str | None:
        """
        The real class name a `LoadFromEnvironment(depth, slot)`-sourced
        register holds, if this table can trace it - None otherwise.
        """
        owner_id = self._environment_origins.owner(function_id, depth)

        if owner_id is None:
            return None

        return self._slot_names.get(owner_id, {}).get(slot)

    @classmethod
    def empty(cls) -> "ClassEnvironmentTable":
        return cls({}, EnvironmentOriginTable.empty())

    @classmethod
    def from_sections(
            cls,
            sections: Iterable[tuple[int, str]],
            environment_origins: EnvironmentOriginTable,
    ) -> "ClassEnvironmentTable":
        sections = list(sections)

        # Pass 1: which function ids are usable as a "class factory
        # helper", and what real name calling them (and storing the
        # result) actually represents - needed before pass 2 can
        # recognize a Call to one.
        named_result_of: dict[int, str] = {}
        for function_id, text in sections:
            match = _CREATE_CLOSURE_NAMED_RE.search(text)
            if match and match.group(3):
                named_result_of[function_id] = match.group(3)

        slot_names: dict[int, dict[int, str]] = {}
        for function_id, text in sections:
            cls._scan_function(function_id, text, named_result_of, slot_names)

        return cls(slot_names, environment_origins)

    @staticmethod
    def _scan_function(
            function_id: int,
            text: str,
            named_result_of: dict[int, str],
            slot_names: dict[int, dict[int, str]],
    ) -> None:
        """
        Walks one function's `.hasm` text top-to-bottom, tracking:

        - which register holds a closure over a known helper function
          (from CreateClosure), so a later Call through that register can
          be recognized as "calling the Animal-factory", not just some
          opaque function;
        - which register then holds THAT call's result, carrying the
          resolved name forward;

        and records `slot_names[function_id][slot] = name` for every
        `StoreToEnvironment` that writes such a register into an
        environment slot. Same "bail rather than guess" policy as
        PrivateNameTable/EnvironmentOriginTable throughout: a register
        this scan can't currently attribute to a known helper/name is
        just absent from the running maps.
        """
        pending_helper: dict[int, int] = {}  # register -> helper function id
        pending_names: dict[int, str] = {}  # register -> resolved name

        for line in text.splitlines():
            match = _CREATE_CLOSURE_RE.search(line)
            if match:
                dest_reg, target_id = int(match.group(1)), int(match.group(2))

                if target_id in named_result_of:
                    pending_helper[dest_reg] = target_id
                else:
                    pending_helper.pop(dest_reg, None)

                continue

            match = _CALL_RE.search(line)
            if match:
                dest_reg, callee_reg = int(match.group(1)), int(match.group(2))
                helper_id = pending_helper.get(callee_reg)

                if helper_id is not None:
                    pending_names[dest_reg] = named_result_of[helper_id]

                continue

            match = _STORE_TO_ENV_RE.search(line)
            if match:
                _env_reg, slot, value_reg = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
                name = pending_names.get(value_reg)

                if name is not None:
                    slot_names.setdefault(function_id, {})[slot] = name
                    del pending_names[value_reg]

                continue
