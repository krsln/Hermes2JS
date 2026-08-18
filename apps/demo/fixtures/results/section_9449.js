function forTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4767>  # String: '__BC:ControlFlow/ForTests/forTest/start' (String)
    // USED → r8 = "__BC:ControlFlow/ForTests/forTest/start";
    // CODE → <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/ForTests/forTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 10>
    // USED → r3 = 10;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4766>  # String: '__BC:ControlFlow/ForTests/forTest/if-continue' (String)
    // USED → r8 = "__BC:ControlFlow/ForTests/forTest/if-continue";
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 8>
    // USED → r4 = 8;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
    // USED → r5 = 3;
    // LOOP → START (for)
    for (r0 = 0; r0 < 10; r0 = r1 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 1, Reg8: 0>
        // USED → r1 = 0;
        // → r1 = 0
        if (r1 === 3) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r10 = console;
            // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r9 = console.log;
            // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 8>
            console.log("__BC:ControlFlow/ForTests/forTest/if-continue")
        } else {
            if (r1 === 8) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r11 = console;
                // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r10 = console.log;
                // CODE → <LoadConstString>: <Reg8: 9, string_id: 4765>  # String: '__BC:ControlFlow/ForTests/forTest/if-break' (String)
                // USED → r9 = "__BC:ControlFlow/ForTests/forTest/if-break";
                // CODE → <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
                console.log("__BC:ControlFlow/ForTests/forTest/if-break")
                // CODE → <Jmp>: <Addr8: 26>  # Address: 00000073
                break;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r10 = console;
            // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r9 = console.log;
            // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 1>
            console.log(r1)
            // CODE → <Jmp>: <Addr8: 40>  # Address: 0000006b
            continue;
        }
        // ──────────────── Block 6 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4763>  # String: '__BC:ControlFlow/ForTests/forTest/end' (String)
    // USED → r7 = "__BC:ControlFlow/ForTests/forTest/end";
    // CODE → <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:ControlFlow/ForTests/forTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined;
    // CODE → <Ret>: <Reg8: 6>
    return undefined;
}