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
    r9 = undefined
    // CODE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null
    // CODE → <LoadConstInt>: <Reg8: 3, Imm32: 16384>
    // USED → r3 = 16384
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = r10;
    // LOOP → START (while)
    while (!(r11 & r3)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
        // USED → r11 = r10.flags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r11 & r3;
        // CODE → <Mov>: <Reg8: 12, Reg8: 0>
        // USED → r12 = r10;
        // CODE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
        if (!(r11 & r3)) goto label_158;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
        // USED → r11 = r10.updateQueue
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = r11;
        // CODE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (r4 === r11) goto label_158;
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r11;
        // CODE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
        // USED → r11 = r11.stores
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = r11;
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (r4 === r11) goto label_158;
        // ──────────────── Block 4 ──────────────── 
        // CODE → <LoadConstZero>: <Reg8: 7>
        // USED → r7 = 0
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r11;
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // USED → r11 = r11.length
        // CODE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
        if (r2 >= r11) goto label_158;
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Mov>: <Reg8: 13, Reg8: 6>
        // USED → r13 = r11;
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = r7;
        // CODE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
        // USED → r11 = r11[r7]
        // CODE → <Mov>: <Reg8: 8, Reg8: 11>
        r8 = r11;
        // CODE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
        // USED → r9 = r11.getSnapshot
        // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
        // USED → r8 = r11.value
        // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
        // USED → r14 = getEnvironment(0)[73];
        // CODE → <Mov>: <Reg8: 11, Reg8: 9>
        // USED → r11 = r9;
        // CODE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
        // USED → r13 = r9(r5);
        // CODE → <Mov>: <Reg8: 11, Reg8: 8>
        // USED → r11 = r8;
        // CODE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
        // USED → r11 = getEnvironment(0)[73](r5, r9(r5), r8);
        // CODE → <JmpTrue>: <Addr8: 7, Reg8: 11>  # Address: 00000089
        if (getEnvironment(0)[73](r5, r9(r5), r8)) goto label_137;
        // ──────────────── Block 6 ──────────────── 
        // CODE → <LoadConstFalse>: <Reg8: 11>
        r11 = false
        // CODE → <Ret>: <Reg8: 11>
        // Unhandled opcode: Ret
        // ──────────────── Block 7 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
        // USED → r11 = r7;
        // CODE → <Inc>: <Reg8: 13, Reg8: 11>
        // USED → r13 = r7 + 1;
        // CODE → <Mov>: <Reg8: 7, Reg8: 13>
        r7 = r7 + 1;
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r11;
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // USED → r11 = r11.length
        // CODE → <JLess>: <Addr8: -68, Reg8: 13, Reg8: 11>  # Address: 00000056
        if (r7 + 1 < r11) goto label_86;
        // ──────────────── Block 8 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
        // USED → r6 = r10.child
        // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
        // USED → r11 = r10.subtreeFlags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r11 & r3;
        // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
        if (!(r11 & r3)) goto label_183;
        // ──────────────── Block 9 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r6;
        // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
        if (r4 !== r6) goto label_277;
        // ──────────────── Block 10 ──────────────── 
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
        if (r10 === r10) goto label_273;
        // ──────────────── Block 11 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r13 = r10.sibling
        // CODE → <Mov>: <Reg8: 14, Reg8: 12>
        // USED → r14 = r10;
        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
        r11 = r10;
        // CODE → <JStrictNotEqual>: <Addr8: 45, Reg8: 4, Reg8: 13>  # Address: 000000f3
        if (r4 !== r13) goto label_243;
        // ──────────────── Block 12 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r15 = r10.return
        // CODE → <Mov>: <Reg8: 13, Reg8: 14>
        // USED → r13 = r10;
        // CODE → <JStrictEqual>: <Addr8: 59, Reg8: 4, Reg8: 15>  # Address: 0000010d
        if (r4 === r15) goto label_269;
        // ──────────────── Block 13 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r15 = r10.return
        // CODE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
        if (r15 === r10) goto label_269;
        // ──────────────── Block 14 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r15 = r10.return
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r13 = r15.sibling
        // CODE → <Mov>: <Reg8: 14, Reg8: 15>
        // USED → r14 = r15;
        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
        // USED → r11 = r15;
        // CODE → <JStrictEqual>: <Addr8: -37, Reg8: 4, Reg8: 13>  # Address: 000000ca
        if (r4 === r13) goto label_202;
        // ──────────────── Block 15 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r14 = r15.sibling
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r13 = r15.return
        // CODE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        r14.return = r13;
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        r0 = r15.sibling
        // CODE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
        goto label_29;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 18 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = r6;
            // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
            r6.return = r10;
            // CODE → <Mov>: <Reg8: 0, Reg8: 11>
            r0 = r6;
            // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
            goto label_29;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 17 ──────────────── 
                // CODE → <LoadConstTrue>: <Reg8: 11>
                r11 = true
                // CODE → <Ret>: <Reg8: 11>
                // Unhandled opcode: Ret
                // ──────────────── Block 16 ──────────────── 
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
    // ──────────────── Block 19 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}