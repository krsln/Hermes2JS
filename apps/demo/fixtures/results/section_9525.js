function asyncLoopTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → <ReifyArgumentsStrict>: <Reg8: 1>
    // USED → r1 = arguments;
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = arguments;
    // CODE → <GetBuiltinClosure>: <Reg8: 3, UInt8: 57>  # Built-in function: [#57 makeAsyncIterator]
    // USED → r3 = builtin_57;
    // CODE → <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 12487>  # Function: [#12487 ?anon_0_asyncLoopTest of 31 bytes]: 2 params @ offset 0x002443ac
    // USED → r2 = ?anon_0_asyncLoopTest;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <Call4>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1, Reg8: 4>
    // USED → r1 = builtin_57.call(undefined, ?anon_0_asyncLoopTest, this, arguments);
    // CODE → <Ret>: <Reg8: 1>
    return builtin_57.call(undefined, ?anon_0_asyncLoopTest, this, arguments);
}