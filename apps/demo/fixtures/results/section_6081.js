function processColorsInProps(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → <Mov>: <Reg8: 5, Reg8: 10>
    // USED → r5 = Identifier(name='r10')
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    // USED → r1 = getEnvironment(1)
    // CODE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    // Error: 'Identifier' object has no attribute 'render'
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpUndefinedLong>: <Addr32: 149, Reg8: 2>  # Address: 000000b7
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 13, Reg8: 2>
        // USED → r13 = Identifier(name='r2')
        // CODE → <Mov>: <Reg8: 7, Reg8: 13>
        // USED → r7 = Identifier(name='r2')
        // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 17>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 148>  # String: 'includes' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 13>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <JmpTrue>: <Addr8: 98, Reg8: 11>  # Address: 0000009e
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = Identifier(name='r2')
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpFalse>: <Addr8: -46, Reg8: 11>  # Address: 0000001c
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = Identifier(name='r2')
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 11, Reg8: 13>
        // USED → r11 = Identifier(name='r2')
        // CODE → <IteratorBegin>: <Reg8: 12, Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Catch>: <Reg8: 11>
        // USED → r11 = caughtException
        // CODE → <IteratorClose>: <Reg8: 12, UInt8: 1>
        RawExpression(source='// Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1')
        // CODE → <Throw>: <Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 12, Reg8: 7>
        // USED → r12 = Identifier(name='r2')
        // CODE → <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpLong>: <Addr32: -150>  # Address: 0000001c
        goto label_28;
    }
    // LOOP → END
    // LOOP → START (while)
    while (Identifier(name='r12') === Identifier(name='r0')) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <IteratorNext>: <Reg8: 14, Reg8: 12, Reg8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 13, Reg8: 12>
        // USED → r13 = Identifier(name='r12')
        // CODE → <JStrictEqual>: <Addr8: -69, Reg8: 13, Reg8: 0>  # Address: 0000001c
        if (Identifier(name='r12') === Identifier(name='r0')) { /* jump to label_28 */ }
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 8, Reg8: 14>
        // USED → r8 = Identifier(name='r14')
        // CODE → <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 18>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 13, Reg8: 7>
        // USED → r13 = Identifier(name='r2')
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 13>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 9, Reg8: 13>
        // USED → r9 = Identifier(name='r2')
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 14, Reg8: 13>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JStrictEqual>: <Addr8: 27, Reg8: 13, Reg8: 0>  # Address: 00000095
        if (Identifier(name='r2') === Identifier(name='r0')) { /* jump to label_149 */ }
        // ──────────────── Block 4 ──────────────── 
        // CODE → <Mov>: <Reg8: 15, Reg8: 8>
        // USED → r15 = Identifier(name='r14')
        // CODE → <Mov>: <Reg8: 14, Reg8: 9>
        // USED → r14 = Identifier(name='r2')
        // CODE → <LoadFromEnvironment>: <Reg8: 16, Reg8: 1, UInt8: 36>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 14>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 13, Reg8: 16, Reg8: 0, Reg8: 13>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutByVal>: <Reg8: 15, Reg8: 14, Reg8: 13>
        // Error: 'Identifier' object has no attribute 'render'
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Jmp>: <Addr8: -59>  # Address: 0000005a
        goto label_90;
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}