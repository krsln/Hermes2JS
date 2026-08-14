function asyncTryCatchTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → <ReifyArgumentsStrict>: <Reg8: 1>
    // USED → r1 = arguments;
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = arguments;
    // CODE → <GetBuiltinClosure>: <Reg8: 3, UInt8: 57>  # Built-in function: [#57 spawnAsync]
    // USED → r3 = spawnAsync;
    // CODE → <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 12486>  # Function: [#12486 ?anon_0_asyncTryCatchTest of 24 bytes]: 1 params @ offset 0x00244394
    // USED → r2 = ?anon_0_asyncTryCatchTest;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <Call4>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1, Reg8: 4>
    // USED → r1 = spawnAsync.call(undefined, r2, r1, r4);
    // CODE → <Ret>: <Reg8: 1>
    return spawnAsync.call(undefined, r2, r1, r4);
}