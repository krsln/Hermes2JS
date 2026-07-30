function function_15090(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = getEnvironment(0)[0];
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <Mul>: <Reg8: 0, Reg8: 0, Reg8: 1>
    // USED → r0 = param1 * getEnvironment(0)[0];
    // CODE → <Ret>: <Reg8: 0>
    return param1 * getEnvironment(0)[0];
}