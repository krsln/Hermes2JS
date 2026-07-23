function function_11949(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 1>
    r1 = r0[1]
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1
    // CODE → <DelByVal>: <Reg8: 0, Reg8: 1, Reg8: 0>
    r0 = delete r1[param1]
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}