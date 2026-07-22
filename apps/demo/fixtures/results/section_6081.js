function processColorsInProps(param0, param1) {
    // Block 0
    r10 = param1
    r0 = undefined
    r7 = undefined
    r8 = undefined
    r9 = undefined
    r5 = r10
    r1 = getEnvironment(1)
    r6 = Object.keys(r10) /* for-in property list */
    if (Object.keys(r10) { /* jump to 183 */ }
    // Loop (header=1)
        // Block 1
        r2 = Object.keys(r10) /* for-in property list */.next() /* for-in step */
        if (Object.keys(r10) /* for-in property list */.next() /* for-in step */ === undefined) { /* jump to label_183 */ }
        // Block 2
        r13 = r2
        r7 = r13
        r12 = r1[17]
        r11 = r12.includes
        r11 = r12.includes(r2)
        if (r12.includes(r2)) { /* jump to label_158 */ }
        // Block 3
        r12 = r1[18]
        r11 = r7
        r11 = r12[r11]
        if (!r12[r11]) { /* jump to label_28 */ }
        // Block 4
        r11 = r7
        r13 = r10[r11]
        r11 = r13
        r12 = GetIterator(r13)
        // Block 5
        r14 = GetIterator(r13).next()
        r13 = r12
        if (r12 === undefined) { /* jump to label_28 */ }
        // Block 6
        r8 = r14
        r15 = r1[18]
        r13 = r7
        r13 = r15[r13]
        r9 = r13
        r13 = r14[r13]
        if (r14[r13] === undefined) { /* jump to label_149 */ }
        // Block 7
        r15 = r8
        r14 = r9
        r16 = r1[36]
        r13 = r15[r14]
        r13 = r16(r15[r14])
        r8[r9] = r16(r15[r14])
        // Block 8
        goto label_90;
        // Block 9
        r11 = caughtException
        // Error: IteratorClose at address 153: Invalid arguments: Reg8: 12, UInt8: 1
        r11 = throw caughtException
        // Block 10
        r12 = r7
        r13 = r1[36]
        r11 = r10[r12]
        r11 = r13(r10[r12])
        param1[r7] = r13(r10[r12])
        goto label_28;
    // EndLoop
    // Block 11
    return undefined;
}