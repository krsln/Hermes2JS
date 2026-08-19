function _runAllTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  4 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr:  7 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2 = r1[0]
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r2.default;
    // CODE → addr: 16 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr: 18 | <CreateGeneratorClosure>: <Reg8: 2, Reg8: 2, function_id: 15044>  # Function: [#15044  of 9 bytes]: 1 params @ offset 0x0026777f
    // USED → r2 = function_15044;
    // CODE → addr: 23 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2>
    r3 = r2.default.call(r4, r2)
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 1, UInt8: 29, Reg8: 3>
    r1[29] = r3
    // CODE → addr: 32 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 65>  # String: 'apply' (Identifier)
    // USED → r2 = r3.apply;
    // CODE → addr: 37 | <ReifyArguments>: <Reg8: 0>
    // USED → r0 = arguments;
    // CODE → addr: 39 | <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = arguments;
    // CODE → addr: 42 | <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → addr: 45 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    r0 = r3.apply(this, r1)
    // CODE → addr: 51 | <Ret>: <Reg8: 0>
    return r0;
}