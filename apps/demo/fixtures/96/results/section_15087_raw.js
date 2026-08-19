function mayThrow(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <JLess>: <Addr8: 13, Reg8: 1, Reg8: 0>  # Address: 00000012
    if (param1 < 0) goto label_18;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:  9 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr: 12 | <Mul>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 * 2;
    // CODE → addr: 16 | <Ret>: <Reg8: 0>
    return param1 * 2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 18 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 20 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r2 = Error;
    // CODE → addr: 26 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = Error.prototype;
    // CODE → addr: 31 | <CreateThis>: <Reg8: 1, Reg8: 0, Reg8: 2>
    // USED → r1 = CreateThis(r0);
    // CODE → addr: 35 | <LoadConstString>: <Reg8: 3, string_id: 1323>  # String: 'negative' (String)
    // USED → r3 = "negative";
    // CODE → addr: 39 | <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = CreateThis(r0);
    // CODE → addr: 42 | <Construct>: <Reg8: 0, Reg8: 2, UInt8: 2>
    // USED → r0 = new Error("negative");
    // CODE → addr: 46 | <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = new Error("negative");
    // CODE → addr: 50 | <Throw>: <Reg8: 0>
    throw new Error("negative");
}