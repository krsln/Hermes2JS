function processColorsInProps(param0, param1) {
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
    // USED → r5 = r10
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    r1 = getEnvironment(1)
    // CODE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // USED → r6 = Object.keys(r10) /* for-in property list */
    // CODE → <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    if (Object.keys(r10) {
        // CODE → <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // label_28:
        // USED → r2 = Object.keys(r10) /* for-in property list */.next() /* for-in step */
        // CODE → <JmpUndefinedLong>: <Addr32: 149, Reg8: 2>  # Address: 000000b7
        if (Object.keys(r10) {
            // CODE → <Mov>: <Reg8: 13, Reg8: 2>
            // USED → r13 = r2
            // CODE → <Mov>: <Reg8: 7, Reg8: 13>
            r7 = r13
            // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 17>
            r12 = r1[17]
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 148>  # String: 'includes' (Identifier)
            // USED → r11 = r12.includes
            // CODE → <Call2>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 13>
            // USED → r11 = r12.includes(r2)
            // CODE → <JmpTrue>: <Addr8: 98, Reg8: 11>  # Address: 0000009e
            if (r12.includes(r2) {
                // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
                r12 = r1[18]
                // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                r11 = r7
                // CODE → <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
                // USED → r11 = r12[r11]
                // CODE → <JmpFalse>: <Addr8: -46, Reg8: 11>  # Address: 0000001c
                if (!r12[r11]) {
                    // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                    r11 = r7
                    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
                    r13 = r10[r11]
                    // CODE → <Mov>: <Reg8: 11, Reg8: 13>
                    // USED → r11 = r13
                    // CODE → <IteratorBegin>: <Reg8: 12, Reg8: 11>
                    // USED → r12 = GetIterator(r13)
                    // CODE → <IteratorNext>: <Reg8: 14, Reg8: 12, Reg8: 11>
                    // label_90:
                    r14 = GetIterator(r13).next()
                    // CODE → <Mov>: <Reg8: 13, Reg8: 12>
                    // USED → r13 = r12
                    // CODE → <JStrictEqual>: <Addr8: -69, Reg8: 13, Reg8: 0>  # Address: 0000001c
                    if (r12 === undefined) {
                        // CODE → <Mov>: <Reg8: 8, Reg8: 14>
                        r8 = r14
                        // CODE → <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 18>
                        r15 = r1[18]
                        // CODE → <Mov>: <Reg8: 13, Reg8: 7>
                        r13 = r7
                        // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 13>
                        r13 = r15[r13]
                        // CODE → <Mov>: <Reg8: 9, Reg8: 13>
                        r9 = r13
                        // CODE → <GetByVal>: <Reg8: 13, Reg8: 14, Reg8: 13>
                        // USED → r13 = r14[r13]
                        // CODE → <JStrictEqual>: <Addr8: 27, Reg8: 13, Reg8: 0>  # Address: 00000095
                        if (r14[r13] === undefined) {
                            // CODE → <Mov>: <Reg8: 15, Reg8: 8>
                            // USED → r15 = r8
                            // CODE → <Mov>: <Reg8: 14, Reg8: 9>
                            // USED → r14 = r9
                            // CODE → <LoadFromEnvironment>: <Reg8: 16, Reg8: 1, UInt8: 36>
                            r16 = r1[36]
                            // CODE → <GetByVal>: <Reg8: 13, Reg8: 15, Reg8: 14>
                            // USED → r13 = r15[r14]
                            // CODE → <Call2>: <Reg8: 13, Reg8: 16, Reg8: 0, Reg8: 13>
                            // USED → r13 = r16(r15[r14])
                            // CODE → <PutByVal>: <Reg8: 15, Reg8: 14, Reg8: 13>
                            r8[r9] = r16(r15[r14])
                        }
                        // CODE → <Jmp>: <Addr8: -59>  # Address: 0000005a
                        // label_149:
                        goto label_90;
                        // CODE → <Catch>: <Reg8: 11>
                        // USED → r11 = caughtException
                        // CODE → <IteratorClose>: <Reg8: 12, UInt8: 1>
                        // Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1
                        // CODE → <Throw>: <Reg8: 11>
                        r11 = throw caughtException
                    }
                    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
                    // label_158:
                    // USED → r12 = r7
                    // CODE → <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
                    r13 = r1[36]
                    // CODE → <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
                    // USED → r11 = r10[r12]
                    // CODE → <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
                    // USED → r11 = r13(r10[r12])
                    // CODE → <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
                    param1[r7] = r13(r10[r12])
                    // CODE → <JmpLong>: <Addr32: -150>  # Address: 0000001c
                    goto label_28;
                }
            }
            // CODE → <Ret>: <Reg8: 0>
            // label_183:
            return undefined;
        }
    }
}