function isRenderConsistentWithExternalStores(param0, param1) {
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
    r1 = getEnvironment(0)
    // CODE → <Mov>: <Reg8: 0, Reg8: 10>
    // USED → r0 = r10
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
    // label_29:
    // USED → r11 = r10.flags
    // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
    // USED → r11 = r10.flags & 16384
    // CODE → <Mov>: <Reg8: 12, Reg8: 0>
    // USED → r12 = r0
    // CODE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
    if (!r10.flags & 16384) {
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
        // USED → r11 = r0.updateQueue
        // CODE → <Mov>: <Reg8: 6, Reg8: 11>
        r6 = r11
        // CODE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
        if (null === r0.updateQueue) {
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = r6
            // CODE → <GetById>: <Reg8: 11, Reg8: 11, UInt8: 3, string_id: 20340>  # String: 'stores' (Identifier)
            // USED → r11 = r6.stores
            // CODE → <Mov>: <Reg8: 6, Reg8: 11>
            r6 = r11
            // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 4, Reg8: 11>  # Address: 0000009e
            if (null === r6.stores) {
                // CODE → <LoadConstZero>: <Reg8: 7>
                r7 = 0
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = r6
                // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
                // USED → r11 = r6.length
                // CODE → <JNotLess>: <Addr8: 76, Reg8: 2, Reg8: 11>  # Address: 0000009e
                if (0 >= r6.length) {
                    // CODE → <Mov>: <Reg8: 13, Reg8: 6>
                    // label_86:
                    r13 = r6
                    // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                    r11 = r7
                    // CODE → <GetByVal>: <Reg8: 11, Reg8: 13, Reg8: 11>
                    // USED → r11 = r13[r11]
                    // CODE → <Mov>: <Reg8: 8, Reg8: 11>
                    r8 = r11
                    // CODE → <GetById>: <Reg8: 9, Reg8: 11, UInt8: 5, string_id: 23581>  # String: 'getSnapshot' (Identifier)
                    r9 = r13[r11].getSnapshot
                    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 11, UInt8: 6, string_id: 249>  # String: 'value' (Identifier)
                    r8 = r13[r11].value
                    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 73>
                    r14 = r1[73]
                    // CODE → <Mov>: <Reg8: 11, Reg8: 9>
                    // USED → r11 = r9
                    // CODE → <Call1>: <Reg8: 13, Reg8: 11, Reg8: 5>
                    // USED → r13 = r9()
                    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
                    // USED → r11 = r8
                    // CODE → <Call3>: <Reg8: 11, Reg8: 14, Reg8: 5, Reg8: 13, Reg8: 11>
                    // USED → r11 = r14(r9(), r8)
                    // CODE → <JmpTrue>: <Addr8: 7, Reg8: 11>  # Address: 00000089
                    if (r14(r9() {
                        // CODE → <LoadConstFalse>: <Reg8: 11>
                        // USED → r11 = false
                        // CODE → <Ret>: <Reg8: 11>
                        return false;
                    }
                    // CODE → <Mov>: <Reg8: 11, Reg8: 7>
                    // label_137:
                    // USED → r11 = r7
                    // CODE → <Inc>: <Reg8: 13, Reg8: 11>
                    // USED → r13 = r7 + 1
                    // CODE → <Mov>: <Reg8: 7, Reg8: 13>
                    r7 = r13
                    // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                    // USED → r11 = r6
                    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 4, string_id: 139>  # String: 'length' (Identifier)
                    // USED → r11 = r6.length
                    // CODE → <JLess>: <Addr8: -68, Reg8: 13, Reg8: 11>  # Address: 00000056
                    if (r7 + 1 < r6.length) {
                    }
                }
            }
        }
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
        // label_158:
        r6 = r0.child
        // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
        // USED → r11 = r0.subtreeFlags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r0.subtreeFlags & 16384
        // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
        if (!r0.subtreeFlags & 16384) {
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // USED → r11 = r6
            // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
            if (null !== r6) {
            }
            // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
            // label_183:
            if (r0 === param1) {
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 12, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                // USED → r13 = r0.sibling
                // CODE → <Mov>: <Reg8: 14, Reg8: 12>
                // USED → r14 = r12
                // CODE → <Mov>: <Reg8: 11, Reg8: 14>
                r11 = r14
                // CODE → <JStrictNotEqual>: <Addr8: 45, Reg8: 4, Reg8: 13>  # Address: 000000f3
                if (null !== r0.sibling) {
                    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                    // label_202:
                    // USED → r15 = r12.return
                    // CODE → <Mov>: <Reg8: 13, Reg8: 14>
                    // USED → r13 = r14
                    // CODE → <JStrictEqual>: <Addr8: 59, Reg8: 4, Reg8: 15>  # Address: 0000010d
                    if (null === r12.return) {
                        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                        // USED → r15 = r14.return
                        // CODE → <JStrictEqual>: <Addr8: 50, Reg8: 15, Reg8: 10>  # Address: 0000010d
                        if (r14.return === param1) {
                            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 13, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                            // USED → r15 = r14.return
                            // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 15, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                            // USED → r13 = r14.return.sibling
                            // CODE → <Mov>: <Reg8: 14, Reg8: 15>
                            r14 = r15
                            // CODE → <Mov>: <Reg8: 11, Reg8: 14>
                            // USED → r11 = r14
                            // CODE → <JStrictEqual>: <Addr8: -37, Reg8: 4, Reg8: 13>  # Address: 000000ca
                            if (null === r14.return.sibling) {
                            }
                            // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                            // label_243:
                            // USED → r14 = r14.sibling
                            // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 10, string_id: 209>  # String: 'return' (Identifier)
                            // USED → r13 = r14.return
                            // CODE → <PutById>: <Reg8: 14, Reg8: 13, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
                            r14 = { return: r14.return }
                            // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 11, UInt8: 9, string_id: 215>  # String: 'sibling' (Identifier)
                            r0 = r14.sibling
                            // CODE → <JmpLong>: <Addr32: -235>  # Address: 0000001d
                            goto label_29;
                        }
                    }
                    // CODE → <LoadConstTrue>: <Reg8: 11>
                    // label_269:
                    // USED → r11 = true
                    // CODE → <Ret>: <Reg8: 11>
                    return true;
                }
                // CODE → <LoadConstTrue>: <Reg8: 11>
                // label_273:
                // USED → r11 = true
                // CODE → <Ret>: <Reg8: 11>
                return true;
            }
            // CODE → <Mov>: <Reg8: 11, Reg8: 6>
            // label_277:
            // USED → r11 = r6
            // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
            r11 = { return: r0 }
            // CODE → <Mov>: <Reg8: 0, Reg8: 11>
            r0 = r11
            // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
            goto label_29;
            // CODE → <Catch>: <Reg8: 0>
            r0 = caughtException
            // CODE → <LoadConstFalse>: <Reg8: 0>
            // USED → r0 = false
            // CODE → <Ret>: <Reg8: 0>
            return false;
        }
    }
}