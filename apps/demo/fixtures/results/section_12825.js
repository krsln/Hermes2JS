function function_12825(param0, param1, param2, param3, param4) {
    // Block 0
    r2 = param1
    r7 = param2
    r8 = param3
    r9 = param4
    r6 = undefined
    r10 = undefined
    r5 = false
    r0 = false
    r1 = param1.slice
    r10 = param1.slice()
    r4 = globalThis
    r3 = "Error occurred in "
    r2 = " callback, continuing anyway…"
    // Block 3
    r12 = caughtException
    r11 = r9
    r13 = r9.error
    r14 = r8
    r1 = globalThis.HermesInternal
    r1 = globalThis.HermesInternal.concat
    r1 = globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…")
    r1 = r9.error(globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…"))
    r1 = r9.error
    r1 = r9.error(caughtException)
    // Block 4
    r1 = r0
    if (!r0) { /* jump to label_39 */ }
    // Block 5
    return r10.pop()(r7) === false;
    // Loop
        // Block 1
        r1 = r10
        r1 = r10.length
        if (!r10.length) { /* jump to label_128 */ }
        // Block 2
        r11 = r10
        r1 = r10.pop
        r11 = r10.pop()
        r1 = r7
        r1 = r10.pop()(r7)
        r0 = r10.pop()(r7) === false
        goto label_122;
    // EndLoop
}