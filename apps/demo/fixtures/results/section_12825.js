function function_12825(param0, param1, param2, param3, param4) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 2>
    // USED → r7 = param2
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 3>
    // USED → r8 = param3
    // CODE → <LoadParam>: <Reg8: 9, UInt8: 4>
    // USED → r9 = param4
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 10>
    // USED → r10 = undefined
    // CODE → <LoadConstFalse>: <Reg8: 5>
    // USED → r5 = false
    // CODE → <LoadConstFalse>: <Reg8: 0>
    // USED → r0 = false
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 217>  # String: 'slice' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call1>: <Reg8: 10, Reg8: 1, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3614>  # String: 'Error occurred in ' (String)
    // USED → r3 = "Error occurred in "
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 11214>  # String: ' callback, continuing anyway…' (String)
    // USED → r2 = " callback, continuing anyway\u2026"
    // CODE → <Mov>: <Reg8: 1, Reg8: 10>
    // USED → r1 = r10;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 139>  # String: 'length' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <JmpFalse>: <Addr8: 81, Reg8: 1>  # Address: 00000080
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 11, Reg8: 10>
    // USED → r11 = r10;
    // CODE → <GetById>: <Reg8: 1, Reg8: 11, UInt8: 3, string_id: 16799>  # String: 'pop' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call1>: <Reg8: 11, Reg8: 1, Reg8: 11>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Mov>: <Reg8: 1, Reg8: 7>
    // USED → r1 = r7;
    // CODE → <Call2>: <Reg8: 1, Reg8: 11, Reg8: 6, Reg8: 1>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 5>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Jmp>: <Addr8: 47>  # Address: 0000007a
    goto label_122;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Mov>: <Reg8: 1, Reg8: 0>
        // USED → r1 = r0;
        // CODE → <JmpFalse>: <Addr8: -86, Reg8: 1>  # Address: 00000027
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Ret>: <Reg8: 0>
        // Unhandled opcode: Ret
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Catch>: <Reg8: 12>
        // USED → r12 = caughtException
        // CODE → <Mov>: <Reg8: 11, Reg8: 9>
        // USED → r11 = r9;
        // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 14, Reg8: 8>
        // USED → r14 = r8;
        // CODE → <TryGetById>: <Reg8: 1, Reg8: 4, UInt8: 5, string_id: 21>  # String: 'HermesInternal' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 98>  # String: 'concat' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 3, Reg8: 14, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <Call2>: <Reg8: 1, Reg8: 13, Reg8: 11, Reg8: 1>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 11, UInt8: 4, string_id: 123>  # String: 'error' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 11, Reg8: 12>
        // Error: sequence item 0: expected str instance, Identifier found
    }
    // LOOP → END
}