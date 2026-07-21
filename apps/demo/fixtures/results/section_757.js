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
    while (true) {
        // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 130>  # String: 'flags' (Identifier)
        // USED → r11 = r10.flags
        // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = r10.flags & 16384
        // CODE → <Mov>: <Reg8: 12, Reg8: 0>
        // USED → r12 = r0
        // CODE → <JmpFalse>: <Addr8: 117, Reg8: 11>  # Address: 0000009e
        if (!r10.flags & 16384) {
            // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
            r6 = r0.child
            // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
            // USED → r11 = r0.subtreeFlags
            // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
            // USED → r11 = r0.subtreeFlags & 16384
            // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
            if (!r0.subtreeFlags & 16384) {
                // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
                if (r0 === param1) { /* jump to label_273 */ }
            } else {
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = r6
                // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
                if (null !== r6) { /* jump to label_277 */ }
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = r6
                // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
                r11 = { return: r0 }
                // CODE → <Mov>: <Reg8: 0, Reg8: 11>
                r0 = r11
                // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
                continue;
            }
        } else {
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'updateQueue' (Identifier)
            // USED → r11 = r0.updateQueue
            // CODE → <Mov>: <Reg8: 6, Reg8: 11>
            r6 = r11
            // CODE → <JStrictEqual>: <Addr8: 106, Reg8: 4, Reg8: 11>  # Address: 0000009e
            if (null === r0.updateQueue) { /* jump to label_158 */ }
            // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 12, UInt8: 7, string_id: 96>  # String: 'child' (Identifier)
            r6 = r0.child
            // CODE → <GetById>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 20552>  # String: 'subtreeFlags' (Identifier)
            // USED → r11 = r0.subtreeFlags
            // CODE → <BitAnd>: <Reg8: 11, Reg8: 11, Reg8: 3>
            // USED → r11 = r0.subtreeFlags & 16384
            // CODE → <JmpFalse>: <Addr8: 10, Reg8: 11>  # Address: 000000b7
            if (!r0.subtreeFlags & 16384) {
                // CODE → <JStrictEqual>: <Addr8: 90, Reg8: 12, Reg8: 10>  # Address: 00000111
                if (r0 === param1) { /* jump to label_273 */ }
            } else {
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = r6
                // CODE → <JStrictNotEqual>: <Addr8: 98, Reg8: 4, Reg8: 11>  # Address: 00000115
                if (null !== r6) { /* jump to label_277 */ }
                // CODE → <Mov>: <Reg8: 11, Reg8: 6>
                // USED → r11 = r6
                // CODE → <PutById>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 209>  # String: 'return' (Identifier)
                r11 = { return: r0 }
                // CODE → <Mov>: <Reg8: 0, Reg8: 11>
                r0 = r11
                // CODE → <JmpLong>: <Addr32: -260>  # Address: 0000001d
                continue;
            }
        }
    }
    // CODE → <LoadConstTrue>: <Reg8: 11>
    // USED → r11 = true
    // CODE → <Ret>: <Reg8: 11>
    return true;
}