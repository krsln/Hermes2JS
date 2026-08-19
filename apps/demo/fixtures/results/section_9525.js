function asyncLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr:  4 | <ReifyArgumentsStrict>: <Reg8: 1>
    // USED → r1 = arguments;
    // CODE → addr:  6 | <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = arguments;
    // CODE → addr:  9 | <GetBuiltinClosure>: <Reg8: 3, UInt8: 57>  # Built-in function: [#57 spawnAsync]
    // USED → r3 = spawnAsync;
    // CODE → addr: 12 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr: 15 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 12487>  # Function: [#12487 ?anon_0_asyncLoopTest of 31 bytes]: 2 params @ offset 0x002443ac
    // USED → r2 = ?anon_0_asyncLoopTest(param1);
    // CODE → addr: 20 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr: 23 | <Call4>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1, Reg8: 4>
    r1 = spawnAsync.call(undefined, ?anon_0_asyncLoopTest(param1), this, r4)
    // CODE → addr: 30 | <Ret>: <Reg8: 1>
    return r1;
}