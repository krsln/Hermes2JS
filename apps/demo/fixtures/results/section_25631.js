function function_25631(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // LINE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500
    // LINE → <GreaterEq>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = param1 >= 500
    // LINE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 0000001a
    if (param1 >= 500) { /* jump to label_26 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <LoadConstInt>: <Reg8: 1, Imm32: 408>
    // USED → r1 = 408
    // LINE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r0 = param1 === 408
    // ──────────────── Block 2 ──────────────── 
    // LINE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 00000027
    if (param1 === 408) { /* jump to label_39 */ }
    // ──────────────── Block 3 ──────────────── 
    // LINE → <LoadConstInt>: <Reg8: 1, Imm32: 429>
    // USED → r1 = 429
    // LINE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r0 = param1 === 429
    // ──────────────── Block 4 ──────────────── 
    // LINE → <Ret>: <Reg8: 0>
    return param1 === 429;
}