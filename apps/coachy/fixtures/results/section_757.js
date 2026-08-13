function isRenderConsistentWithExternalStores(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null;
    // CODE → <LoadConstInt>: <Reg8: 3, Imm32: 16384>
    // USED → r3 = 16384;
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = param1;
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
            // USED → r11 = param1.flags;
            // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
            // USED → r11 = param1.flags & 16384;
            // CODE → <Mov>: <Reg8: 12, Reg8: 0>
            // USED → r12 = param1;
            if (!(param1.flags & 16384)) {
                // ──────────────── Block 8 ──────────────── 
                // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
                // USED → r6 = param1.child;
                // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
                // USED → r11 = param1.subtreeFlags;
                // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
                // USED → r11 = param1.subtreeFlags & 16384;
                if (!(param1.subtreeFlags & 16384)) {
                    if (r12 !== r10) {
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                        // USED → r13 = param1.sibling;
                        // CODE → <Mov>: <Reg8: 14, Reg8: 12>
                        // USED → r14 = param1;
                        // CODE → <Mov>: <Reg8: 11, Reg8: 14>
                        r11 = param1
                        // → r13 = param1.sibling
                        if (null !== r13) {
                            // ──────────────── Block 15 ──────────────── 
                            // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                            // USED → r14 = param1.return.sibling;
                            // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                            // USED → r13 = param1.return.return;
                            // CODE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
                            param1.return.sibling.return = param1.return.return
                            // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                            r0 = param1.return.sibling
                            // CODE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
                            goto label_29;
                        } else {
                            // LOOP → START (for)
                            // → r13 = param1
                            for (; null === r13; r11 = param1.return) {
                                // ──────────────── Block 12 ──────────────── 
                                // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                                // USED → r15 = param1.return;
                                // CODE → <Mov>: <Reg8: 13, Reg8: 14>
                                // USED → r13 = param1;
                                // → r15 = param1.return
                                if (null !== r15) {
                                    // ──────────────── Block 13 ──────────────── 
                                    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                                    // USED → r15 = param1.return;
                                    // CODE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
                                    // → r15 = param1.return
                                    if (r15 === r10) goto label_269;
                                    // ──────────────── Block 14 ──────────────── 
                                    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                                    // USED → r15 = param1.return;
                                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                                    // USED → r13 = param1.return.sibling;
                                    // CODE → <Mov>: <Reg8: 14, Reg8: 15>
                                    // USED → r14 = param1.return;
                                }
                            }
                            // LOOP → END
                        }
                    }
                // → r11 = param1.child
                } else if (null === r11) {
                    // ──────────────── Block 18 ──────────────── 
                    // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                    // USED → r11 = param1.child;
                    // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
                    param1.child.return = param1
                    // CODE → <Mov>: <Reg8: 0, Reg8: 11>
                    r0 = param1.child
                    // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
                    goto label_29;
                }
            // → r11 = param1.updateQueue
            } else if (null !== r11) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = param1.updateQueue;
                // CODE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
                // USED → r11 = param1.updateQueue.stores;
                // CODE → <Mov>: <Reg8: 6, Reg8: 11>
                // USED → r6 = param1.updateQueue.stores;
                // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
                // → r11 = param1.updateQueue.stores
                if (null === r11) goto label_158;
                // ──────────────── Block 4 ──────────────── 
                // CODE → <LoadConstZero>: <Reg8: 7>
                // USED → r7 = 0;
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = param1.updateQueue.stores;
                // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
                // USED → r11 = param1.updateQueue.stores.length;
                // CODE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
                // → r11 = param1.updateQueue.stores.length
                if (!(0 < r11)) goto label_158;
                // LOOP → START (for)
                // → r11 = getEnvironment(0)[73].call(undefined, r13, r11); r13 = param1.updateQueue.stores[0].getSnapshot.call(undefined)
                for (; r13 < r11; r11 = param1.updateQueue.stores.length) {
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <Mov>: <Reg8: 13, Reg8: 6>
                    // USED → r13 = param1.updateQueue.stores;
                    // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                    // USED → r11 = 0;
                    // CODE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
                    // USED → r11 = param1.updateQueue.stores[0];
                    // CODE → <Mov>: <Reg8: 8, Reg8: 11>
                    r8 = param1.updateQueue.stores[0]
                    // CODE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
                    // USED → r9 = param1.updateQueue.stores[0].getSnapshot;
                    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
                    // USED → r8 = param1.updateQueue.stores[0].value;
                    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
                    // USED → r14 = getEnvironment(0)[73];
                    // CODE → <Mov>: <Reg8: 11, Reg8: 9>
                    // USED → r11 = param1.updateQueue.stores[0].getSnapshot;
                    // CODE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
                    // USED → r13 = param1.updateQueue.stores[0].getSnapshot.call(undefined);
                    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
                    // USED → r11 = param1.updateQueue.stores[0].value;
                    // CODE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
                    // USED → r11 = getEnvironment(0)[73].call(undefined, r13, r11);
                    // → r11 = getEnvironment(0)[73].call(undefined, r13, r11); r13 = param1.updateQueue.stores[0].getSnapshot.call(undefined)
                    if (!getEnvironment(0)[73].call(undefined, r13, r11)) {
                        // ──────────────── Block 7 ──────────────── 
                        // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                        r11 = 0
                        // CODE → <Inc>: <Reg8: 13, Reg8: 11>
                        // USED → r13 = r11 + 1;
                        // CODE → <Mov>: <Reg8: 7, Reg8: 13>
                        r7 = r11 + 1
                        // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                        // USED → r11 = param1.updateQueue.stores;
                    }
                }
                // LOOP → END
            }
        }
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → <LoadConstFalse>: <Reg8: 11>
        // USED → r11 = false;
        // CODE → <Ret>: <Reg8: 11>
        return false;
        // ──────────────── Block 16 ──────────────── 
        // CODE → <LoadConstTrue>: <Reg8: 11>
        // USED → r11 = true;
        // CODE → <Ret>: <Reg8: 11>
        return true;
        // ──────────────── Block 17 ──────────────── 
        // CODE → <LoadConstTrue>: <Reg8: 11>
        // USED → r11 = true;
        // CODE → <Ret>: <Reg8: 11>
        return true;
    } catch (caughtException) {
        // ──────────────── Block 19 ──────────────── 
        // CODE → <LoadConstFalse>: <Reg8: 0>
        // USED → r0 = false;
        // CODE → <Ret>: <Reg8: 0>
        return false;
    }
}