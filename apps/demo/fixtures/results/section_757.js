function isRenderConsistentWithExternalStores(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1
    // LINE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // LINE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null
    // LINE → <LoadConstInt>: <Reg8: 3, Imm32: 16384>
    // USED → r3 = 16384
    // LINE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0
    // LINE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // LINE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = r10
    // LOOP → START (while)
    while (!r10.flags & 16384) {
        // ──────────────── Block 1 ──────────────── 
        // LINE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
        // USED → r11 = r10.flags
        // LINE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r10.flags & 16384
        // LINE → <Mov>: <Reg8: 12, Reg8: 0>
        // USED → r12 = r0
        // LINE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
        if (!r10.flags & 16384) { /* jump to label_158 */ }
        // ──────────────── Block 2 ──────────────── 
        // LINE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
        // USED → r11 = r0.updateQueue
        // LINE → <Mov>: <Reg8: 6, Reg8: 11>
        r6 = r11
        // LINE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (null === r0.updateQueue) { /* jump to label_158 */ }
        // ──────────────── Block 3 ──────────────── 
        // LINE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r6
        // LINE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
        // USED → r11 = r6.stores
        // LINE → <Mov>: <Reg8: 6, Reg8: 11>
        r6 = r11
        // LINE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (null === r6.stores) { /* jump to label_158 */ }
        // ──────────────── Block 4 ──────────────── 
        // LINE → <LoadConstZero>: <Reg8: 7>
        r7 = 0
        // LINE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r6
        // LINE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // USED → r11 = r6.length
        // LINE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
        if (0 >= r6.length) { /* jump to label_158 */ }
        // ──────────────── Block 8 ──────────────── 
        // LINE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
        r6 = r0.child
        // LINE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
        // USED → r11 = r0.subtreeFlags
        // LINE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r0.subtreeFlags & 16384
        // LINE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
        if (!r0.subtreeFlags & 16384) { /* jump to label_183 */ }
        // ──────────────── Block 9 ──────────────── 
        // LINE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r6
        // LINE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
        if (null !== r6) { /* jump to label_277 */ }
        // ──────────────── Block 10 ──────────────── 
        // LINE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
        if (r0 === param1) { /* jump to label_273 */ }
        // ──────────────── Block 11 ──────────────── 
        // LINE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r13 = r0.sibling
        // LINE → <Mov>: <Reg8: 14, Reg8: 12>
        // USED → r14 = r12
        // LINE → <Mov>: <Reg8: 11, Reg8: 14>
        r11 = r14
        // LINE → <JStrictNotEqual>: <Addr8: 45, Reg8: 4, Reg8: 13>  # Address: 000000f3
        if (null !== r0.sibling) { /* jump to label_243 */ }
        // ──────────────── Block 15 ──────────────── 
        // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r14 = r14.sibling
        // LINE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r13 = r14.return
        // LINE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        r14 = { return: r14.return }
        // LINE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        r0 = r14.sibling
        // LINE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
        goto label_29;
        // ──────────────── Block 18 ──────────────── 
        // LINE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r6
        // LINE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        r11 = { return: r0 }
        // LINE → <Mov>: <Reg8: 0, Reg8: 11>
        r0 = r11
        // LINE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
        goto label_29;
        // LOOP → START (while)
        while (r14(r9(), r8)) {
            // ──────────────── Block 5 ──────────────── 
            // LINE → <Mov>: <Reg8: 13, Reg8: 6>
            r13 = r6
            // LINE → <Mov>: <Reg8: 11, Reg8: 7>
            r11 = r7
            // LINE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
            // USED → r11 = r13[r11]
            // LINE → <Mov>: <Reg8: 8, Reg8: 11>
            r8 = r11
            // LINE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
            r9 = r13[r11].getSnapshot
            // LINE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
            r8 = r13[r11].value
            // LINE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
            r14 = r1[73]
            // LINE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = r9
            // LINE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
            // USED → r13 = r9()
            // LINE → <Mov>: <Reg8: 11, Reg8: 8>
            // USED → r11 = r8
            // LINE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
            // USED → r11 = r14(r9(), r8)
            // LINE → <JmpTrue>: <Addr8: 7, Reg8: 11>  # Address: 00000089
            if (r14(r9(), r8)) { /* jump to label_137 */ }
            // ──────────────── Block 7 ──────────────── 
            // LINE → <Mov>: <Reg8: 11, Reg8: 7>
            // USED → r11 = r7
            // LINE → <Inc>: <Reg8: 13, Reg8: 11>
            // USED → r13 = r7 + 1
            // LINE → <Mov>: <Reg8: 7, Reg8: 13>
            r7 = r13
            // LINE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = r6
            // LINE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
            // USED → r11 = r6.length
            // LINE → <JLess>: <Addr8: -68, Reg8: 13, Reg8: 11>  # Address: 00000056
            if (r7 + 1 < r6.length) { /* jump to label_86 */ }
        }
        // LOOP → END
        // LOOP → START (while)
        while (null === r12.return) {
            // ──────────────── Block 12 ──────────────── 
            // LINE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r12.return
            // LINE → <Mov>: <Reg8: 13, Reg8: 14>
            // USED → r13 = r14
            // LINE → <JStrictEqual>: <Addr8: 59, Reg8: 4, Reg8: 15>  # Address: 0000010d
            if (null === r12.return) { /* jump to label_269 */ }
            // ──────────────── Block 13 ──────────────── 
            // LINE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r14.return
            // LINE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
            if (r14.return === param1) { /* jump to label_269 */ }
            // ──────────────── Block 14 ──────────────── 
            // LINE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r14.return
            // LINE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
            // USED → r13 = r14.return.sibling
            // LINE → <Mov>: <Reg8: 14, Reg8: 15>
            r14 = r15
            // LINE → <Mov>: <Reg8: 11, Reg8: 14>
            // USED → r11 = r14
            // LINE → <JStrictEqual>: <Addr8: -37, Reg8: 4, Reg8: 13>  # Address: 000000ca
            if (null === r14.return.sibling) { /* jump to label_202 */ }
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // LINE → <LoadConstFalse>: <Reg8: 11>
    // USED → r11 = false
    // LINE → <Ret>: <Reg8: 11>
    return false;
    // ──────────────── Block 16 ──────────────── 
    // LINE → <LoadConstTrue>: <Reg8: 11>
    // USED → r11 = true
    // LINE → <Ret>: <Reg8: 11>
    return true;
    // ──────────────── Block 17 ──────────────── 
    // LINE → <LoadConstTrue>: <Reg8: 11>
    // USED → r11 = true
    // LINE → <Ret>: <Reg8: 11>
    return true;
    // ──────────────── Block 19 ──────────────── 
    // LINE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // LINE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false
    // LINE → <Ret>: <Reg8: 0>
    return false;
}