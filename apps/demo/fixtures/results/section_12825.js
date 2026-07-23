function function_12825(param0, param1, param2, param3, param4) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // LINE → <LoadParam>: <Reg8: 7, UInt8: 2>
    r7 = param2
    // LINE → <LoadParam>: <Reg8: 8, UInt8: 3>
    r8 = param3
    // LINE → <LoadParam>: <Reg8: 9, UInt8: 4>
    r9 = param4
    // LINE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 10>
    r10 = undefined
    // LINE → <LoadConstFalse>: <Reg8: 5>
    // USED → r5 = false
    // LINE → <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // LINE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r1 = param1.slice
    // LINE → <Call1>: <Reg8: 10, Reg8: 1, Reg8: 2>
    r10 = param1.slice()
    // LINE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis
    // LINE → <LoadConstString>: <Reg8: 3, string_id: 3614>  # String: 'Error occurred in ' (String)
    // USED → r3 = "Error occurred in "
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 11214>  # String: ' callback, continuing anyway…' (String)
    // USED → r2 = " callback, continuing anyway…"
    // LOOP → START (while)
    while (!r10.length) {
        // ──────────────── Block 1 ──────────────── 
        // LINE → <Mov>: <Reg8: 1, Reg8: 10>
        // USED → r1 = r10
        // LINE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 139>  # String: 'length' (Identifier)
        // USED → r1 = r10.length
        // LINE → <JmpFalse>: <Addr8: 81, Reg8: 1>  # Address: 00000080
        if (!r10.length) { /* jump to label_128 */ }
        // ──────────────── Block 2 ──────────────── 
        // LINE → <Mov>: <Reg8: 11, Reg8: 10>
        // USED → r11 = r10
        // LINE → <GetById>: <Reg8: 1, Reg8: 11, UInt8: 3, string_id: 16799>  # String: 'pop' (Identifier)
        // USED → r1 = r10.pop
        // LINE → <Call1>: <Reg8: 11, Reg8: 1, Reg8: 11>
        // USED → r11 = r10.pop()
        // LINE → <Mov>: <Reg8: 1, Reg8: 7>
        // USED → r1 = r7
        // LINE → <Call2>: <Reg8: 1, Reg8: 11, Reg8: 6, Reg8: 1>
        // USED → r1 = r10.pop()(r7)
        // LINE → <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 5>
        // USED → r0 = r10.pop()(r7) === false
        // LINE → <Jmp>: <Addr8: 47>  # Address: 0000007a
        goto label_122;
        // LOOP → START (while)
        while (!r0) {
            // ──────────────── Block 4 ──────────────── 
            // LINE → <Mov>: <Reg8: 1, Reg8: 0>
            // USED → r1 = r0
            // LINE → <JmpFalse>: <Addr8: -86, Reg8: 1>  # Address: 00000027
            if (!r0) { /* jump to label_39 */ }
            // ──────────────── Block 3 ──────────────── 
            // LINE → <Catch>: <Reg8: 12>
            // USED → r12 = caughtException
            // LINE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = r9
            // LINE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
            // USED → r13 = r9.error
            // LINE → <Mov>: <Reg8: 14, Reg8: 8>
            // USED → r14 = r8
            // LINE → <TryGetById>: <Reg8: 1, Reg8: 4, UInt8: 5, string_id: 21>  # String: 'HermesInternal' (Identifier)
            // USED → r1 = globalThis.HermesInternal
            // LINE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 98>  # String: 'concat' (Identifier)
            // USED → r1 = globalThis.HermesInternal.concat
            // LINE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 3, Reg8: 14, Reg8: 2>
            // USED → r1 = globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…")
            // LINE → <Call2>: <Reg8: 1, Reg8: 13, Reg8: 11, Reg8: 1>
            r1 = r9.error(globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…"))
            // LINE → <GetByIdShort>: <Reg8: 1, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
            // USED → r1 = r9.error
            // LINE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 11, Reg8: 12>
            r1 = r9.error(caughtException)
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // LINE → <Ret>: <Reg8: 0>
    return r10.pop()(r7) === false;
}