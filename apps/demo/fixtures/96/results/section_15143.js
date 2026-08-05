function function_15143(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
    r1 = getEnvironment(0)[0]
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    r0 = param1
    // CODE → <Mul>: <Reg8: 0, Reg8: 0, Reg8: 1>
    // USED → r0 = r0 * r1;
    // CODE → <Ret>: <Reg8: 0>
    return r0 * r1;
}