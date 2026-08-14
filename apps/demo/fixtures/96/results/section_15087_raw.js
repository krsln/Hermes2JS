function mayThrow(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <JLess>: <Addr8: 13, Reg8: 1, Reg8: 0>  # Address: 00000012
    // → r1 = param1
    if (r1 < 0) goto label_18;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <Mul>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 * 2;
    // CODE → <Ret>: <Reg8: 0>
    return param1 * 2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r2 = globalThis.Error;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
    r0 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 2>
    // USED → r1 = CreateThis(r0);
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1323>  # String: 'negative' (String)
    // USED → r3 = "negative";
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = CreateThis(r0);
    // CODE → <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // USED → r0 = new globalThis.Error("negative");
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new globalThis.Error("negative");
    // CODE → <Throw>: <Reg8: 0>
    throw new globalThis.Error("negative");
}