function isRenderConsistentWithExternalStores(param0, param1) {
    // Block 0
    r10 = param1
    r5 = undefined
    r6 = undefined
    r7 = undefined
    r8 = undefined
    r9 = undefined
    r4 = null
    r3 = 16384
    r2 = 0
    r1 = getEnvironment(0)
    r0 = r10
    // Block 6
    r11 = false
    return false;
    // Block 16
    r11 = true
    return true;
    // Block 17
    r11 = true
    return true;
    // Block 19
    r0 = caughtException
    r0 = false
    return false;
    // Loop (while)
        // Block 5
        r13 = r6
        r11 = r7
        r11 = r13[r11]
        r8 = r11
        r9 = r13[r11].getSnapshot
        r8 = r13[r11].value
        r14 = r1[73]
        r11 = r9
        r13 = r9()
        r11 = r8
        r11 = r14(r9(), r8)
        if (r14(r9(), r8)) { /* jump to label_137 */ }
    // EndLoop
    // Loop (while)
        // Block 12
        r15 = r12.return
        r13 = r14
        if (null === r12.return) { /* jump to label_269 */ }
    // EndLoop
    // Loop (while)
        // Block 1
        r11 = r10.flags
        r11 = r10.flags & 16384
        r12 = r0
        if (!r10.flags & 16384) { /* jump to label_158 */ }
        // Block 2
        r11 = r0.updateQueue
        r6 = r11
        if (null === r0.updateQueue) { /* jump to label_158 */ }
        // Block 3
        r11 = r6
        r11 = r6.stores
        r6 = r11
        if (null === r6.stores) { /* jump to label_158 */ }
        // Block 4
        r7 = 0
        r11 = r6
        r11 = r6.length
        if (0 >= r6.length) { /* jump to label_158 */ }
        // Block 5
        r13 = r6
        r11 = r7
        r11 = r13[r11]
        r8 = r11
        r9 = r13[r11].getSnapshot
        r8 = r13[r11].value
        r14 = r1[73]
        r11 = r9
        r13 = r9()
        r11 = r8
        r11 = r14(r9(), r8)
        if (r14(r9(), r8)) { /* jump to label_137 */ }
        // Block 7
        r11 = r7
        r13 = r7 + 1
        r7 = r13
        r11 = r6
        r11 = r6.length
        if (r7 + 1 < r6.length) { /* jump to label_86 */ }
        // Block 8
        r6 = r0.child
        r11 = r0.subtreeFlags
        r11 = r0.subtreeFlags & 16384
        if (!r0.subtreeFlags & 16384) { /* jump to label_183 */ }
        // Block 9
        r11 = r6
        if (null !== r6) { /* jump to label_277 */ }
        // Block 10
        if (r0 === param1) { /* jump to label_273 */ }
        // Block 11
        r13 = r0.sibling
        r14 = r12
        r11 = r14
        if (null !== r0.sibling) { /* jump to label_243 */ }
        // Block 12
        r15 = r12.return
        r13 = r14
        if (null === r12.return) { /* jump to label_269 */ }
        // Block 13
        r15 = r14.return
        if (r14.return === param1) { /* jump to label_269 */ }
        // Block 14
        r15 = r14.return
        r13 = r14.return.sibling
        r14 = r15
        r11 = r14
        if (null === r14.return.sibling) { /* jump to label_202 */ }
        // Block 15
        r14 = r14.sibling
        r13 = r14.return
        r14 = { return: r14.return }
        r0 = r14.sibling
        goto label_29;
        // Block 18
        r11 = r6
        r11 = { return: r0 }
        r0 = r11
        goto label_29;
    // EndLoop
}