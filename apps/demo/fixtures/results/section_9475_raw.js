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
    r0 = param1 * 2
    // CODE → addr: 16 | <Ret>: <Reg8: 0>
    return r0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 18 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 20 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = Error;
    // CODE → addr: 26 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 1>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 30 | <LoadConstString>: <Reg8: 4, string_id: 1300>  # String: 'negative' (String)
    // USED → r4 = "negative";
    // CODE → addr: 34 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = CreateThisForNew(r3);
    // CODE → addr: 37 | <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new Error("negative");
    // CODE → addr: 41 | <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    r1 = new Error("negative")
    // CODE → addr: 45 | <Throw>: <Reg8: 1>
    throw r1;
}