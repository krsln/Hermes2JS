function request(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // LINE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // LINE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 0>
    r3 = r1[0]
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r2 = r3.apply
    // LINE → <ReifyArguments>: <Reg8: 0>
    r0 = arguments
    // LINE → <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = r0
    // LINE → <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this
    // LINE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r0 = r3.apply(this, r0)
    // LINE → <Ret>: <Reg8: 0>
    return r3.apply(this, r0);
}