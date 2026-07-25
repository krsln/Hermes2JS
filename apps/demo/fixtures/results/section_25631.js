function function_25631(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <LoadConstInt>: <Reg8: 0, Imm32: 500>
    // USED → r0 = 500
    // CODE → <GreaterEq>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.GREATER_EQUAL: '>='>, right=Identifier(name='r0'))
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 0000001a
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 408>
    // USED → r1 = 408
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    // USED → r0 = BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.STRICT_EQUAL: '==='>, right=Identifier(name='r1'))
    // CODE → <JmpTrue>: <Addr8: 13, Reg8: 0>  # Address: 00000027
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <LoadConstInt>: <Reg8: 1, Imm32: 429>
    // USED → r1 = 429
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
    r0 = BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.STRICT_EQUAL: '==='>, right=Identifier(name='r1'))
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}