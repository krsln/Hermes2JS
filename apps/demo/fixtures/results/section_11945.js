function request(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 86>  # String: 'apply' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <ReifyArguments>: <Reg8: 0>
    // USED → r0 = arguments
    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = Identifier(name='r0')
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}