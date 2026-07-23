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
    // USED → r1 = getEnvironment(0)
    // CODE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = param1
    // LOOP → START (while)
    while (!r0.flags & 16384) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
        // USED → r11 = r0.flags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r0.flags & 16384
        // CODE → <Mov>: <Reg8: 12, Reg8: 0>
        // USED → r12 = param1
        // CODE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
        if (!r0.flags & 16384) { /* jump to label_158 */ }
        // ──────────────── Block 2 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
        // USED → r11 = r12.updateQueue
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = r12.updateQueue
        // CODE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (null === r12.updateQueue) { /* jump to label_158 */ }
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r12.updateQueue
        // CODE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
        // USED → r11 = r12.updateQueue.stores
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        // USED → r6 = r12.updateQueue.stores
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (null === r12.updateQueue.stores) { /* jump to label_158 */ }
        // ──────────────── Block 4 ──────────────── 
        // CODE → <LoadConstZero>: <Reg8: 7>
        // USED → r7 = 0
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r12.updateQueue.stores
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
        // USED → r11 = r12.updateQueue.stores.length
        // CODE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
        if (0 >= r12.updateQueue.stores.length) { /* jump to label_158 */ }
        // ──────────────── Block 8 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
        // USED → r6 = r12.child
        // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
        // USED → r11 = r12.subtreeFlags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r12.subtreeFlags & 16384
        // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
        if (!r12.subtreeFlags & 16384) { /* jump to label_183 */ }
        // ──────────────── Block 9 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r12.child
        // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
        if (null !== r12.child) { /* jump to label_277 */ }
        // ──────────────── Block 10 ──────────────── 
        // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
        if (param1 === param1) { /* jump to label_273 */ }
        // ──────────────── Block 11 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r13 = r12.sibling
        // CODE → <Mov>: <Reg8: 14, Reg8: 12>
        // USED → r14 = param1
        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
        r11 = param1
        // CODE → <JStrictNotEqual>: <Addr8: 45, Reg8: 4, Reg8: 13>  # Address: 000000f3
        if (null !== r12.sibling) { /* jump to label_243 */ }
        // ──────────────── Block 15 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        // USED → r14 = r13.return.sibling
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
        // USED → r13 = r13.return.return
        // CODE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        r14 = { return: r13.return.return }
        // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
        r0 = r13.return.sibling
        // CODE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
        goto label_29;
        // ──────────────── Block 18 ──────────────── 
        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
        // USED → r11 = r12.child
        // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
        // USED → r11 = { return: param1 }
        // CODE → <Mov>: <Reg8: 0, Reg8: 11>
        r0 = { return: param1 }
        // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
        goto label_29;
        // LOOP → START (while)
        while (getEnvironment(0)[73](undefined, r12.updateQueue.stores[0].getSnapshot(undefined), r12.updateQueue.stores[0].value)) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <Mov>: <Reg8: 13, Reg8: 6>
            // USED → r13 = r12.updateQueue.stores
            // CODE → <Mov>: <Reg8: 11, Reg8: 7>
            // USED → r11 = 0
            // CODE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
            // USED → r11 = r12.updateQueue.stores[0]
            // CODE → <Mov>: <Reg8: 8, Reg8: 11>
            r8 = r12.updateQueue.stores[0]
            // CODE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
            // USED → r9 = r12.updateQueue.stores[0].getSnapshot
            // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
            // USED → r8 = r12.updateQueue.stores[0].value
            // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
            // USED → r14 = getEnvironment(0)[73]
            // CODE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = r12.updateQueue.stores[0].getSnapshot
            // CODE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
            // USED → r13 = r12.updateQueue.stores[0].getSnapshot(undefined)
            // CODE → <Mov>: <Reg8: 11, Reg8: 8>
            // USED → r11 = r12.updateQueue.stores[0].value
            // CODE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
            // USED → r11 = getEnvironment(0)[73](undefined, r12.updateQueue.stores[0].getSnapshot(undefined), r12.updateQueue.stores[0].value)
            // CODE → <JmpTrue>: <Addr8: 7, Reg8: 11>  # Address: 00000089
            if (getEnvironment(0)[73](undefined, r12.updateQueue.stores[0].getSnapshot(undefined), r12.updateQueue.stores[0].value)) { /* jump to label_137 */ }
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 7>
            // USED → r11 = 0
            // CODE → <Inc>: <Reg8: 13, Reg8: 11>
            // USED → r13 = 0 + 1
            // CODE → <Mov>: <Reg8: 7, Reg8: 13>
            r7 = 0 + 1
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = r12.updateQueue.stores
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
            // USED → r11 = r12.updateQueue.stores.length
            // CODE → <JLess>: <Addr8: -68, Reg8: 13, Reg8: 11>  # Address: 00000056
            if (0 + 1 < r12.updateQueue.stores.length) { /* jump to label_86 */ }
        }
        // LOOP → END
        // LOOP → START (while)
        while (null === r14.return) {
            // ──────────────── Block 12 ──────────────── 
            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r14.return
            // CODE → <Mov>: <Reg8: 13, Reg8: 14>
            // USED → r13 = param1
            // CODE → <JStrictEqual>: <Addr8: 59, Reg8: 4, Reg8: 15>  # Address: 0000010d
            if (null === r14.return) { /* jump to label_269 */ }
            // ──────────────── Block 13 ──────────────── 
            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r13.return
            // CODE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
            if (r13.return === param1) { /* jump to label_269 */ }
            // ──────────────── Block 14 ──────────────── 
            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
            // USED → r15 = r13.return
            // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
            // USED → r13 = r13.return.sibling
            // CODE → <Mov>: <Reg8: 14, Reg8: 15>
            // USED → r14 = r13.return
            // CODE → <Mov>: <Reg8: 11, Reg8: 14>
            // USED → r11 = r13.return
            // CODE → <JStrictEqual>: <Addr8: -37, Reg8: 4, Reg8: 13>  # Address: 000000ca
            if (null === r13.return.sibling) { /* jump to label_202 */ }
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadConstFalse>: <Reg8: 11>
    // USED → r11 = false
    // CODE → <Ret>: <Reg8: 11>
    return false;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 11>
    // USED → r11 = true
    // CODE → <Ret>: <Reg8: 11>
    return true;
    // ──────────────── Block 17 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 11>
    // USED → r11 = true
    // CODE → <Ret>: <Reg8: 11>
    return true;
    // ──────────────── Block 19 ──────────────── 
    // CODE → <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false
    // CODE → <Ret>: <Reg8: 0>
    return false;
}