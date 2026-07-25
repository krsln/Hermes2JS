function isRenderConsistentWithExternalStores(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    // USED → r9 = undefined
    // CODE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null
    // CODE → <LoadConstInt>: <Reg8: 3, Imm32: 16384>
    // USED → r3 = 16384
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0)
    // CODE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = Identifier(name='r10')
    // LOOP → START (while)
    while (Identifier(name='r4') === BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <Mov>: <Reg8: 12, Reg8: 0>
        // USED → r12 = Identifier(name='r10')
        // CODE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (Identifier(name='r4') === BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) { /* jump to label_158 */ }
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (Identifier(name='r4') === BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) { /* jump to label_158 */ }
        // ──────────────── Block 3 ──────────────── 
        // CODE → <LoadConstZero>: <Reg8: 7>
        // USED → r7 = 0
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
        if (Identifier(name='r2') >= BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) { /* jump to label_158 */ }
        // ──────────────── Block 4 ──────────────── 
        // CODE → <Mov>: <Reg8: 13, Reg8: 6>
        // USED → r13 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = Identifier(name='r7')
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 8, Reg8: 11>
        // USED → r8 = Identifier(name='r7')
        // CODE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 11, Reg8: 9>
        // USED → r11 = Identifier(name='r9')
        // CODE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <Mov>: <Reg8: 11, Reg8: 8>
        // USED → r11 = Identifier(name='r7')
        // CODE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <JmpTrue>: <Addr8: 7, Reg8: 11>  # Address: 00000089
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstFalse>: <Reg8: 11>
        r11 = false
        // CODE → <Ret>: <Reg8: 11>
        // Unhandled opcode: Ret
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = Identifier(name='r7')
        // CODE → <Inc>: <Reg8: 13, Reg8: 11>
        // USED → r13 = BinaryExpression(left=Identifier(name='r7'), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
        // CODE → <Mov>: <Reg8: 7, Reg8: 13>
        r7 = BinaryExpression(left=Identifier(name='r7'), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <JLess>: <Addr8: -68, Reg8: 13, Reg8: 11>  # Address: 00000056
        if (BinaryExpression(left=Identifier(name='r7'), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) { /* jump to label_86 */ }
        // ──────────────── Block 5 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = BinaryExpression(left=BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3')), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
        // Error: 'BinaryExpression' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
        // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
        if (Identifier(name='r4') !== BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))) { /* jump to label_277 */ }
        // ──────────────── Block 6 ──────────────── 
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
        if (Identifier(name='r10') === Identifier(name='r10')) { /* jump to label_273 */ }
        // ──────────────── Block 7 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 14, Reg8: 12>
        // USED → r14 = Identifier(name='r10')
        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
        r11 = Identifier(name='r10')
        // CODE → <JStrictNotEqual>: <Addr8: 45, Reg8: 4, Reg8: 13>  # Address: 000000f3
        if (Identifier(name='r4') !== BinaryExpression(left=Identifier(name='r7'), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))) { /* jump to label_243 */ }
        // ──────────────── Block 8 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 13, Reg8: 14>
        // USED → r13 = Identifier(name='r10')
        // CODE → <JStrictEqual>: <Addr8: 59, Reg8: 4, Reg8: 15>  # Address: 0000010d
        if (Identifier(name='r4') === Identifier(name='r15')) { /* jump to label_269 */ }
        // ──────────────── Block 9 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
        if (Identifier(name='r15') === Identifier(name='r10')) { /* jump to label_269 */ }
        // ──────────────── Block 10 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 14, Reg8: 15>
        // USED → r14 = Identifier(name='r15')
        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
        // USED → r11 = Identifier(name='r15')
        // CODE → <JStrictEqual>: <Addr8: -37, Reg8: 4, Reg8: 13>  # Address: 000000ca
        if (Identifier(name='r4') === Identifier(name='r10')) { /* jump to label_202 */ }
        // ──────────────── Block 11 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
        goto label_29;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 14 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
            // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
            // Error: 'BinaryExpression' object has no attribute 'render'
            // CODE → <Mov>: <Reg8: 0, Reg8: 11>
            r0 = BinaryExpression(left=Identifier(name='r11'), operator=<BinaryOperator.BITWISE_AND: '&'>, right=Identifier(name='r3'))
            // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
            goto label_29;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 13 ──────────────── 
                // CODE → <LoadConstTrue>: <Reg8: 11>
                r11 = true
                // CODE → <Ret>: <Reg8: 11>
                // Unhandled opcode: Ret
                // ──────────────── Block 12 ──────────────── 
                // CODE → <LoadConstTrue>: <Reg8: 11>
                r11 = true
                // CODE → <Ret>: <Reg8: 11>
                // Unhandled opcode: Ret
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 15 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}