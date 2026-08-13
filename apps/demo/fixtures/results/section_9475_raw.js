function mayThrow(param0, param1) {
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
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r3 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 1>
    // USED → r2 = __uninitialized_this_for_new__;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1300>  # String: 'negative' (String)
    // USED → r4 = "negative";
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 1, Reg8: 3, UInt8: 2>
    // USED → r1 = new globalThis.Error("negative", __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 1, Reg8: 2, Reg8: 1>
    // USED → r1 = new globalThis.Error("negative", __uninitialized_this_for_new__);
    // CODE → <Throw>: <Reg8: 1>
    throw new globalThis.Error("negative", __uninitialized_this_for_new__);
}