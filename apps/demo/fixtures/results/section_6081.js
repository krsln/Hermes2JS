function processColorsInProps(param0, param1) {
    // ───── Block 0 ───── 
    // <LoadParam>: <Reg8: 10, UInt8: 1>
    // ELIDED → r10 = param1
    // <LoadConstUndefined>: <Reg8: 0>
    // ELIDED → r0 = undefined
    // <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // <Mov>: <Reg8: 5, Reg8: 10>
    // ELIDED → r5 = r10
    // <GetEnvironment>: <Reg8: 1, UInt8: 1>
    r1 = getEnvironment(1)
    // <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // ELIDED → r6 = HermesPropertyIterator(r10)
    // <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    if (HermesPropertyIterator(r10) === undefined) { /* jump to label_183 */ }
    // Loop (while)
    while (HermesPropertyIterator(r10).next() === undefined) {
        // ───── Block 1 ───── 
        // <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // ELIDED → r2 = HermesPropertyIterator(r10).next()
        // <JmpUndefinedLong>: <Addr32: 149, Reg8: 2>  # Address: 000000b7
        if (HermesPropertyIterator(r10).next() === undefined) { /* jump to label_183 */ }
        // ───── Block 2 ───── 
        // <Mov>: <Reg8: 13, Reg8: 2>
        // ELIDED → r13 = r2
        // <Mov>: <Reg8: 7, Reg8: 13>
        r7 = r13
        // <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 17>
        r12 = r1[17]
        // <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 148>  # String: 'includes' (Identifier)
        // ELIDED → r11 = r12.includes
        // <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 13>
        // ELIDED → r11 = r12.includes(r2)
        // <JmpTrue>: <Addr8: 98, Reg8: 11>  # Address: 0000009e
        if (r12.includes(r2)) { /* jump to label_158 */ }
        // ───── Block 3 ───── 
        // <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
        r12 = r1[18]
        // <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
        // ELIDED → r11 = r12[r11]
        // <JmpFalse>: <Addr8: -46, Reg8: 11>  # Address: 0000001c
        if (!r12[r11]) { /* jump to label_28 */ }
        // ───── Block 4 ───── 
        // <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
        r13 = r10[r11]
        // <Mov>: <Reg8: 11, Reg8: 13>
        // ELIDED → r11 = r13
        // <IteratorBegin>: <Reg8: 12, Reg8: 11>
        // ELIDED → r12 = GetIterator(r13)
        // Loop (while)
        while (r12 === undefined) {
            // ───── Block 5 ───── 
            // <IteratorNext>: <Reg8: 14, Reg8: 12, Reg8: 11>
            r14 = GetIterator(r13).next()
            // <Mov>: <Reg8: 13, Reg8: 12>
            // ELIDED → r13 = r12
            // <JStrictEqual>: <Addr8: -69, Reg8: 13, Reg8: 0>  # Address: 0000001c
            if (r12 === undefined) { /* jump to label_28 */ }
            // ───── Block 6 ───── 
            // <Mov>: <Reg8: 8, Reg8: 14>
            r8 = r14
            // <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 18>
            r15 = r1[18]
            // <Mov>: <Reg8: 13, Reg8: 7>
            r13 = r7
            // <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 13>
            r13 = r15[r13]
            // <Mov>: <Reg8: 9, Reg8: 13>
            r9 = r13
            // <GetByVal>: <Reg8: 13, Reg8: 14, Reg8: 13>
            // ELIDED → r13 = r14[r13]
            // <JStrictEqual>: <Addr8: 27, Reg8: 13, Reg8: 0>  # Address: 00000095
            if (r14[r13] === undefined) { /* jump to label_149 */ }
            // ───── Block 7 ───── 
            // <Mov>: <Reg8: 15, Reg8: 8>
            // ELIDED → r15 = r8
            // <Mov>: <Reg8: 14, Reg8: 9>
            // ELIDED → r14 = r9
            // <LoadFromEnvironment>: <Reg8: 16, Reg8: 1, UInt8: 36>
            r16 = r1[36]
            // <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 14>
            // ELIDED → r13 = r15[r14]
            // <Call2>: <Reg8: 13, Reg8: 16, Reg8: 0, Reg8: 13>
            // ELIDED → r13 = r16(r15[r14])
            // <PutByVal>: <Reg8: 15, Reg8: 14, Reg8: 13>
            r8[r9] = r16(r15[r14])
            // ───── Block 8 ───── 
            // <Jmp>: <Addr8: -59>  # Address: 0000005a
            goto label_90;
        } /* EndLoop */
        // Loop (while)
        while (true) {
            // ───── Block 10 ───── 
            // <Mov>: <Reg8: 12, Reg8: 7>
            // ELIDED → r12 = r7
            // <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
            r13 = r1[36]
            // <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
            // ELIDED → r11 = r10[r12]
            // <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
            // ELIDED → r11 = r13(r10[r12])
            // <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
            param1[r7] = r13(r10[r12])
            // <JmpLong>: <Addr32: -150>  # Address: 0000001c
            goto label_28;
            // ───── Block 9 ───── 
            // <Catch>: <Reg8: 11>
            // ELIDED → r11 = caughtException
            // <IteratorClose>: <Reg8: 12, UInt8: 1>
            // Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1
            // <Throw>: <Reg8: 11>
            r11 = throw caughtException
        } /* EndLoop */
    } /* EndLoop */
    // ───── Block 11 ───── 
    // <Ret>: <Reg8: 0>
    return undefined;
}