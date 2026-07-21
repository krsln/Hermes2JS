function function_25631(param0, param1) {
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500
    // CODE → <GreaterEq>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = param1 >= 500
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 0000001a
    if (param1 >= 500) {
    } else {
        // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 408>
        // USED → r1 = 408
        // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
        // USED → r0 = param1 === 408
    }
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 00000027
    if (param1 === 408) {
    } else {
        // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 429>
        // USED → r1 = 429
        // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
        // USED → r0 = param1 === 429
    }
    // CODE → <Ret>: <Reg8: 0>
    return param1 === 429;
}