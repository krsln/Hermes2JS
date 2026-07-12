function request(param0, param1, param2) {
    // CODE -> <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0);
    // CODE -> <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 0>
    r3 = r1[0]
    // CODE -> <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 86>  # String: 'apply' (Identifier)
    // USED -> r2 = r3.apply
    // CODE -> <ReifyArguments>: <Reg8: 0>
    r0 = arguments
    // CODE -> <Mov>: <Reg8: 1, Reg8: 0>
    // USED -> r1 = r0
    // CODE -> <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED -> r0 = param0
    // CODE -> <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED -> r0 = r3.apply(param0, r0)
    // CODE -> <Ret>: <Reg8: 0>
    return r3.apply(param0, r0);
}