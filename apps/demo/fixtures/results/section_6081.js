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
    // USED → r5 = r10;
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    // USED → r1 = getEnvironment(1)
    // CODE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // USED → r6 = HermesPropertyIterator(r10)
    // CODE → <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    if (r6 === undefined) goto label_183;
    // LOOP → START (while)
    while (r2 === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // USED → r2 = r6.next()
        // CODE → <JmpUndefinedLong>: <Addr32: 149, Reg8: 2>  # Address: 000000b7
        if (r2 === undefined) goto label_183;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Mov>: <Reg8: 13, Reg8: 2>
        // USED → r13 = r2;
        // CODE → <Mov>: <Reg8: 7, Reg8: 13>
        // USED → r7 = r2;
        // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 17>
        // USED → r12 = r1[17]
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 148>  # String: 'includes' (Identifier)
        // USED → r11 = r12.includes
        // CODE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 13>
        // USED → r11 = r11(r12, r2);
        // CODE → <JmpTrue>: <Addr8: 98, Reg8: 11>  # Address: 0000009e
        if (r11(r12, r2)) goto label_158;
        // ──────────────── Block 3 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
        // USED → r12 = r1[18]
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = r2;
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
        // USED → r11 = r12[r2]
        // CODE → <JmpFalse>: <Addr8: -46, Reg8: 11>  # Address: 0000001c
        if (!r11) goto label_28;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 10 ──────────────── 
            // CODE → <Mov>: <Reg8: 12, Reg8: 7>
            // USED → r12 = r2;
            // CODE → <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
            // USED → r13 = r1[36]
            // CODE → <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
            // USED → r11 = r10[r2]
            // CODE → <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
            // USED → r11 = r13(r0, r11);
            // CODE → <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
            r10[r2] = r13(r0, r11);
            // CODE → <JmpLong>: <Addr32: -150>  # Address: 0000001c
            goto label_28;
            // ──────────────── Block 9 ──────────────── 
            // CODE → <Catch>: <Reg8: 11>
            // USED → r11 = caughtException
            // CODE → <IteratorClose>: <Reg8: 12, UInt8: 1>
            // Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1;
            // CODE → <Throw>: <Reg8: 11>
            throw r11;
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Mov>: <Reg8: 11, Reg8: 7>
    // USED → r11 = r2;
    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
    // USED → r13 = r10[r2]
    // CODE → <Mov>: <Reg8: 11, Reg8: 13>
    // USED → r11 = r13;
    // CODE → <IteratorBegin>: <Reg8: 12, Reg8: 11>
    // USED → r12 = GetIterator(r13)
    // LOOP → START (while)
    while (Identifier(name='r12') === Identifier(name='r0')) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <IteratorNext>: <Reg8: 14, Reg8: 12, Reg8: 11>
        // USED → r14 = r12.next()
        // CODE → <Mov>: <Reg8: 13, Reg8: 12>
        // USED → r13 = r12;
        // CODE → <JStrictEqual>: <Addr8: -69, Reg8: 13, Reg8: 0>  # Address: 0000001c
        if (Identifier(name='r12') === Identifier(name='r0')) { /* jump to label_28 */ }
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Mov>: <Reg8: 8, Reg8: 14>
        // USED → r8 = r14;
        // CODE → <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 18>
        // USED → r15 = r1[18]
        // CODE → <Mov>: <Reg8: 13, Reg8: 7>
        // USED → r13 = r2;
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 13>
        // USED → r13 = r15[r2]
        // CODE → <Mov>: <Reg8: 9, Reg8: 13>
        // USED → r9 = r13;
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 14, Reg8: 13>
        // USED → r13 = r14[r13]
        // CODE → <JStrictEqual>: <Addr8: 27, Reg8: 13, Reg8: 0>  # Address: 00000095
        if (Identifier(name='r13') === Identifier(name='r0')) { /* jump to label_149 */ }
        // ──────────────── Block 7 ──────────────── 
        // CODE → <Mov>: <Reg8: 15, Reg8: 8>
        // USED → r15 = r14;
        // CODE → <Mov>: <Reg8: 14, Reg8: 9>
        // USED → r14 = r13;
        // CODE → <LoadFromEnvironment>: <Reg8: 16, Reg8: 1, UInt8: 36>
        // USED → r16 = r1[36]
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 14>
        // USED → r13 = r14[r13]
        // CODE → <Call2>: <Reg8: 13, Reg8: 16, Reg8: 0, Reg8: 13>
        // USED → r13 = r16(r0, r13);
        // CODE → <PutByVal>: <Reg8: 15, Reg8: 14, Reg8: 13>
        r14[r13] = r16(r0, r13);
        // ──────────────── Block 8 ──────────────── 
        // CODE → <Jmp>: <Addr8: -59>  # Address: 0000005a
        goto label_90;
    }
    // LOOP → END
    // ──────────────── Block 11 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}