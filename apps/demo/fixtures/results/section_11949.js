function function_11949(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // LINE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 1>
    r1 = r0[1]
    // LINE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1
    // LINE → <DelByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
    r0 = delete r1[param1]
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // LINE → <Ret>: <Reg8: 0>
    return undefined;
}