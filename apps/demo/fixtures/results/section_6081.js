function processColorsInProps(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // LINE → <Mov>: <Reg8: 5, Reg8: 10>
    // USED → r5 = r10
    // LINE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    r1 = getEnvironment(1)
    // LINE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // USED → r6 = HermesPropertyIterator(r10)
    // LINE → <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    if (HermesPropertyIterator(r10) === undefined) { /* jump to label_183 */ }
    // LOOP → START (while)
    while (HermesPropertyIterator(r10).next() === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // LINE → <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // USED → r2 = HermesPropertyIterator(r10).next()
        // LINE → <JmpUndefinedLong>: <Addr32: 149, Reg8: 2>  # Address: 000000b7
        if (HermesPropertyIterator(r10).next() === undefined) { /* jump to label_183 */ }
        // ──────────────── Block 2 ──────────────── 
        // LINE → <Mov>: <Reg8: 13, Reg8: 2>
        // USED → r13 = r2
        // LINE → <Mov>: <Reg8: 7, Reg8: 13>
        r7 = r13
        // LINE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 17>
        r12 = r1[17]
        // LINE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 148>  # String: 'includes' (Identifier)
        // USED → r11 = r12.includes
        // LINE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 13>
        // USED → r11 = r12.includes(r2)
        // LINE → <JmpTrue>: <Addr8: 98, Reg8: 11>  # Address: 0000009e
        if (r12.includes(r2)) { /* jump to label_158 */ }
        // ──────────────── Block 3 ──────────────── 
        // LINE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
        r12 = r1[18]
        // LINE → <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // LINE → <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
        // USED → r11 = r12[r11]
        // LINE → <JmpFalse>: <Addr8: -46, Reg8: 11>  # Address: 0000001c
        if (!r12[r11]) { /* jump to label_28 */ }
        // ──────────────── Block 4 ──────────────── 
        // LINE → <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // LINE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
        r13 = r10[r11]
        // LINE → <Mov>: <Reg8: 11, Reg8: 13>
        // USED → r11 = r13
        // LINE → <IteratorBegin>: <Reg8: 12, Reg8: 11>
        // USED → r12 = GetIterator(r13)
        // LOOP → START (while)
        while (r12 === undefined) {
            // ──────────────── Block 5 ──────────────── 
            // LINE → <IteratorNext>: <Reg8: 14, Reg8: 12, Reg8: 11>
            r14 = GetIterator(r13).next()
            // LINE → <Mov>: <Reg8: 13, Reg8: 12>
            // USED → r13 = r12
            // LINE → <JStrictEqual>: <Addr8: -69, Reg8: 13, Reg8: 0>  # Address: 0000001c
            if (r12 === undefined) { /* jump to label_28 */ }
            // ──────────────── Block 6 ──────────────── 
            // LINE → <Mov>: <Reg8: 8, Reg8: 14>
            r8 = r14
            // LINE → <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 18>
            r15 = r1[18]
            // LINE → <Mov>: <Reg8: 13, Reg8: 7>
            r13 = r7
            // LINE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 13>
            r13 = r15[r13]
            // LINE → <Mov>: <Reg8: 9, Reg8: 13>
            r9 = r13
            // LINE → <GetByVal>: <Reg8: 13, Reg8: 14, Reg8: 13>
            // USED → r13 = r14[r13]
            // LINE → <JStrictEqual>: <Addr8: 27, Reg8: 13, Reg8: 0>  # Address: 00000095
            if (r14[r13] === undefined) { /* jump to label_149 */ }
            // ──────────────── Block 7 ──────────────── 
            // LINE → <Mov>: <Reg8: 15, Reg8: 8>
            // USED → r15 = r8
            // LINE → <Mov>: <Reg8: 14, Reg8: 9>
            // USED → r14 = r9
            // LINE → <LoadFromEnvironment>: <Reg8: 16, Reg8: 1, UInt8: 36>
            r16 = r1[36]
            // LINE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 14>
            // USED → r13 = r15[r14]
            // LINE → <Call2>: <Reg8: 13, Reg8: 16, Reg8: 0, Reg8: 13>
            // USED → r13 = r16(r15[r14])
            // LINE → <PutByVal>: <Reg8: 15, Reg8: 14, Reg8: 13>
            r8[r9] = r16(r15[r14])
            // ──────────────── Block 8 ──────────────── 
            // LINE → <Jmp>: <Addr8: -59>  # Address: 0000005a
            goto label_90;
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 10 ──────────────── 
            // LINE → <Mov>: <Reg8: 12, Reg8: 7>
            // USED → r12 = r7
            // LINE → <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
            r13 = r1[36]
            // LINE → <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
            // USED → r11 = r10[r12]
            // LINE → <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
            // USED → r11 = r13(r10[r12])
            // LINE → <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
            param1[r7] = r13(r10[r12])
            // LINE → <JmpLong>: <Addr32: -150>  # Address: 0000001c
            goto label_28;
            // ──────────────── Block 9 ──────────────── 
            // LINE → <Catch>: <Reg8: 11>
            // USED → r11 = caughtException
            // LINE → <IteratorClose>: <Reg8: 12, UInt8: 1>
            // Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1
            // LINE → <Throw>: <Reg8: 11>
            r11 = throw caughtException
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 11 ──────────────── 
    // LINE → <Ret>: <Reg8: 0>
    return undefined;
}