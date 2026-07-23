function function_25631(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500
    // CODE → <GreaterEq>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = r2 >= 500
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 0000001a
    if (r2 >= 500) { /* jump to label_26 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 408>
    // USED → r1 = 408
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r0 = r2 === 408
    // ──────────────── Block 2 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 00000027
    if (r2 === 408) { /* jump to label_39 */ }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 429>
    // USED → r1 = 429
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r0 = r2 === 429
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    return r2 === 429;
}