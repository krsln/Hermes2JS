function _asyncTryCatchTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 1>
    // USED → r2 = getEnvironment(0)[1];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(0)[1].default;
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <CreateGeneratorClosure>: <Reg8: 2, Reg8: 2, function_id: 15180>  # Function: [#15180  of 9 bytes]: 1 params @ offset 0x0026b31b
    // USED → r2 = function_15180;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r3 = getEnvironment(0)[1].default.call(undefined, function_15180);
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 3>
    getEnvironment(0)[6] = getEnvironment(0)[1].default.call(undefined, function_15180)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 65>  # String: 'apply' (Identifier)
    // USED → r2 = getEnvironment(0)[1].default.call(undefined, function_15180).apply;
    // CODE → <ReifyArguments>: <Reg8: 0>
    // USED → r0 = arguments;
    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = arguments;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r0 = getEnvironment(0)[1].default.call(undefined, function_15180).apply(this, arguments);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[1].default.call(undefined, function_15180).apply(this, arguments);
}