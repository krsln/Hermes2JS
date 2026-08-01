function function_25631(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500;
    // CODE → <GreaterEq>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = param1 >= 500 || param1 === 408 || param1 === 429;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    return param1 >= 500 || param1 === 408 || param1 === 429;
}