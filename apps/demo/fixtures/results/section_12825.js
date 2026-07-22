function function_12825(param0, param1, param2, param3, param4) {
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 2>
    r7 = param2
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 3>
    r8 = param3
    // CODE → <LoadParam>: <Reg8: 9, UInt8: 4>
    r9 = param4
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 10>
    r10 = undefined
    // CODE → <LoadConstFalse>: <Reg8: 5>
    // USED → r5 = false
    // CODE → <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r1 = param1.slice
    // CODE → <Call1>: <Reg8: 10, Reg8: 1, Reg8: 2>
    r10 = param1.slice()
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3614>  # String: 'Error occurred in ' (String)
    // USED → r3 = "Error occurred in "
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 11214>  # String: ' callback, continuing anyway…' (String)
    // USED → r2 = " callback, continuing anyway…"
    while (!r10.length) {
        try {
            // CODE → <Mov>: <Reg8: 11, Reg8: 10>
            // USED → r11 = r10
            // CODE → <GetById>: <Reg8: 1, Reg8: 11, UInt8: 3, string_id: 16799>  # String: 'pop' (Identifier)
            // USED → r1 = r10.pop
            // CODE → <Call1>: <Reg8: 11, Reg8: 1, Reg8: 11>
            // USED → r11 = r10.pop()
            // CODE → <Mov>: <Reg8: 1, Reg8: 7>
            // USED → r1 = r7
            // CODE → <Call2>: <Reg8: 1, Reg8: 11, Reg8: 6, Reg8: 1>
            // USED → r1 = r10.pop()(r7)
            // CODE → <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 5>
            // USED → r0 = r10.pop()(r7) === false
            // CODE → <Jmp>: <Addr8: 47>  # Address: 0000007a
            // CODE → <Mov>: <Reg8: 1, Reg8: 0>
            // USED → r1 = r0
            // CODE → <JmpFalse>: <Addr8: -86, Reg8: 1>  # Address: 00000027
            if (!r0) {
                continue;
            }
            // CODE → <Ret>: <Reg8: 0>
            return r10.pop()(r7) === false;
        } catch (r12) {
            // CODE → <Catch>: <Reg8: 12>
            // USED → r12 = caughtException
            // CODE → <Mov>: <Reg8: 11, Reg8: 9>
            // USED → r11 = r9
            // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
            // USED → r13 = r9.error
            // CODE → <Mov>: <Reg8: 14, Reg8: 8>
            // USED → r14 = r8
            // CODE → <TryGetById>: <Reg8: 1, Reg8: 4, UInt8: 5, string_id: 21>  # String: 'HermesInternal' (Identifier)
            // USED → r1 = globalThis.HermesInternal
            // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 98>  # String: 'concat' (Identifier)
            // USED → r1 = globalThis.HermesInternal.concat
            // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 3, Reg8: 14, Reg8: 2>
            // USED → r1 = globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…")
            // CODE → <Call2>: <Reg8: 1, Reg8: 13, Reg8: 11, Reg8: 1>
            r1 = r9.error(globalThis.HermesInternal.concat.call(this, "Error occurred in ", r8, " callback, continuing anyway…"))
            // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
            // USED → r1 = r9.error
            // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 11, Reg8: 12>
            r1 = r9.error(caughtException)
        }
        // CODE → <Mov>: <Reg8: 1, Reg8: 0>
        // USED → r1 = r0
        // CODE → <JmpFalse>: <Addr8: -86, Reg8: 1>  # Address: 00000027
        if (!r0) {
            continue;
        }
    }
    // CODE → <Ret>: <Reg8: 0>
}