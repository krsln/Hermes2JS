function forTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 8, string_id: 4767>  # String: '__BC:ControlFlow/ForTests/forTest/start' (String)
    // USED → r8 = "__BC:ControlFlow/ForTests/forTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/ForTests/forTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 3, UInt8: 10>
    // USED → r3 = 10;
    // CODE → addr: 28 | <LoadConstString>: <Reg8: 8, string_id: 4766>  # String: '__BC:ControlFlow/ForTests/forTest/if-continue' (String)
    // USED → r8 = "__BC:ControlFlow/ForTests/forTest/if-continue";
    // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 4, UInt8: 8>
    // USED → r4 = 8;
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
    // USED → r5 = 3;
    // LOOP → START (for)
    for (r0 = 0; r0 < 10; r0 = r1 + 1) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 40 | <Mov>: <Reg8: 1, Reg8: 0>
        r1 = r0
        // → r1 = r0
        if (r1 === 3) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr: 91 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r10 = console;
            // CODE → addr: 97 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r9 = console.log;
            // CODE → addr:102 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 8>
            console.log("__BC:ControlFlow/ForTests/forTest/if-continue")
        } else {
            if (r1 === 8) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 69 | <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r11 = console;
                // CODE → addr: 75 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r10 = console.log;
                // CODE → addr: 80 | <LoadConstString>: <Reg8: 9, string_id: 4765>  # String: '__BC:ControlFlow/ForTests/forTest/if-break' (String)
                // USED → r9 = "__BC:ControlFlow/ForTests/forTest/if-break";
                // CODE → addr: 84 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
                console.log("__BC:ControlFlow/ForTests/forTest/if-break")
                // CODE → addr: 89 | <Jmp>: <Addr8: 26>  # Address: 00000073
                break;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 51 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r10 = console;
            // CODE → addr: 57 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r9 = console.log;
            // CODE → addr: 62 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 1>
            console.log(r1)
            // CODE → addr: 67 | <Jmp>: <Addr8: 40>  # Address: 0000006b
            continue;
        }
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:115 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 7, string_id: 4763>  # String: '__BC:ControlFlow/ForTests/forTest/end' (String)
    // USED → r7 = "__BC:ControlFlow/ForTests/forTest/end";
    // CODE → addr:130 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:ControlFlow/ForTests/forTest/end")
    // CODE → addr:135 | <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined;
    // CODE → addr:137 | <Ret>: <Reg8: 6>
    return undefined;
}