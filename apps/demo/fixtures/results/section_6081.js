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
    for (const key in r10) {
        // CODE → <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
        // USED → r2 = Object.keys(r10) /* for-in property list */.next() /* for-in step */
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
        // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 18>
        r12 = r1[18]
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 12, Reg8: 11>
        // USED → r11 = r12[r11]
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        r11 = r7
        // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 11>
        r13 = r10[r11]
        // CODE → <Mov>: <Reg8: 11, Reg8: 13>
        // USED → r11 = r13
        // CODE → <Mov>: <Reg8: 13, Reg8: 12>
        // USED → r13 = r12
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
        // CODE → <Mov>: <Reg8: 12, Reg8: 7>
        // USED → r12 = r7
        // CODE → <LoadFromEnvironment>: <Reg8: 13, Reg8: 1, UInt8: 36>
        r13 = r1[36]
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 10, Reg8: 12>
        // USED → r11 = r10[r12]
        // CODE → <Call2>: <Reg8: 11, Reg8: 13, Reg8: 0, Reg8: 11>
        // USED → r11 = r13(r10[r12])
        // CODE → <PutByVal>: <Reg8: 10, Reg8: 12, Reg8: 11>
        param1[r7] = r13(r10[r12])
    }
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}