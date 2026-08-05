function function_15141(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    r1 = param1
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    r0 = 2
    // CODE → <Mul>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = r1 * r0;
    // CODE → <Ret>: <Reg8: 0>
    return r1 * r0;
}