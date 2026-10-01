from __future__ import annotations

import re
from typing import Iterable

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.batch_pipeline.tables.EnvironmentOriginTable import EnvironmentOriginTable

logger = get_logger(__name__)

# ==> 0000005e: <CreatePrivateName>: <Reg8: 2, string_id: 14278>  # String: '#x' (Identifier)
_CREATE_PRIVATE_NAME_RE = re.compile(
    r"<CreatePrivateName>:\s*<Reg8:\s*(\d+),[^#\n]*#\s*String:\s*(?:'([^']*)'|\"([^\"]*)\")\s*\(Identifier\)"
)

# ==> 00000064: <StoreToEnvironment>: <Reg8: 4, UInt8: 2, Reg8: 2>
# ==> 00000064: <StoreToEnvironmentL>: <Reg8: 4, UInt16: 2, Reg8: 2>
_STORE_TO_ENV_RE = re.compile(
    r"<StoreToEnvironment[L]?>:\s*<Reg8:\s*(\d+),\s*U(?:Int8|Int16):\s*(\d+),\s*Reg8:\s*(\d+)>"
)


class PrivateNameTable:
    """
    Batch-level `(owning function id, slot) -> real '#fieldName' string`
    lookup for private class fields, resolved the same way
    EnvironmentOriginTable resolves environment ownership: by scanning
    every section's raw text rather than any one function's own bytecode.

    A private field's real name only exists at the ONE point Hermes
    executes `CreatePrivateName` for it - inside whatever function runs
    the class's own field-declaration code - immediately followed by a
    `StoreToEnvironment` into the class's shared closure environment.
    Every method/constructor that later touches that field only ever
    sees `LoadFromEnvironment(depth, slot)` pulling the already-created
    symbol back out - the name itself never appears in ITS bytecode (see
    AddOwnPrivateBySym.py/PrivateProperty.py, which fall back to a
    numeric `#__private_N__` for exactly this reason). Recovering the
    real name means finding the ONE function that ran CreatePrivateName
    for that field and reading it from there instead - which needs
    EnvironmentOriginTable to translate "depth from the function
    currently being decompiled" into "which function's own frame that
    actually is" first.

    Degrades gracefully, same as EnvironmentOriginTable and CreatorTable:
    a field whose declaring function isn't part of the batch this table
    was built from (a common case - the class-declaration code usually
    lives in a module-scope function nowhere near the section id range a
    hand-picked test subset extracts; see this table's own tests) simply
    has no entry, and callers fall back to the numeric placeholder they
    always have.
    """

    def __init__(self, slot_names: dict[int, dict[int, str]], environment_origins: EnvironmentOriginTable):
        #: owning_function_id -> {slot: '#fieldName'}
        self._slot_names = slot_names
        self._environment_origins = environment_origins

    def name_for(self, function_id: int, depth: int, slot: int) -> str | None:
        """
        The real `#fieldName` a private-field opcode's `LoadFromEnvironment
        (depth, slot)`-sourced register holds, if this table can trace it -
        None otherwise (the declaring function wasn't part of the batch, or
        this specific slot was never seen carrying a CreatePrivateName
        value at all, e.g. because it holds something else entirely).
        """
        owner_id = self._environment_origins.owner(function_id, depth)

        if owner_id is None:
            return None

        return self._slot_names.get(owner_id, {}).get(slot)

    @classmethod
    def empty(cls) -> "PrivateNameTable":
        return cls({}, EnvironmentOriginTable.empty())

    @classmethod
    def from_sections(
            cls,
            sections: Iterable[tuple[int, str]],
            environment_origins: EnvironmentOriginTable,
    ) -> "PrivateNameTable":
        sections = list(sections)
        slot_names: dict[int, dict[int, str]] = {}

        for function_id, text in sections:
            cls._scan_function(function_id, text, slot_names)

        return cls(slot_names, environment_origins)

    @staticmethod
    def _scan_function(
            function_id: int,
            text: str,
            slot_names: dict[int, dict[int, str]],
    ) -> None:
        """
        Walks one function's `.hasm` text top-to-bottom, tracking which
        register currently holds a pending `CreatePrivateName` value (and
        which name), and records `slot_names[function_id][slot] = name`
        for every `StoreToEnvironment` that writes such a register
        straight into an environment slot.

        Deliberately doesn't restrict which register the store targets to
        "this function's own frame" the way EnvironmentOriginTable's own
        scan does for CreateClosure edges - class field declaration code
        stores private names into an environment it just created for
        exactly this purpose (see ClassTests.ts-style class bodies), so
        by the time `StoreToEnvironment` runs, that register already IS
        the function's own frame; nothing here needs to re-derive that.
        """
        pending_names: dict[int, str] = {}

        for line in text.splitlines():
            match = _CREATE_PRIVATE_NAME_RE.search(line)
            if match:
                reg = int(match.group(1))
                name = match.group(2) if match.group(2) is not None else match.group(3)
                pending_names[reg] = name
                continue

            match = _STORE_TO_ENV_RE.search(line)
            if match:
                _env_reg, slot, value_reg = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
                name = pending_names.get(value_reg)

                if name is not None:
                    slot_names.setdefault(function_id, {})[slot] = name
                    # Consumed - a later store of the SAME register
                    # (unrelated to this private name) shouldn't be
                    # mistaken for another copy of it.
                    del pending_names[value_reg]

                continue
