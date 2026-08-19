function forTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4585>  # String: '__BC:ControlFlow/ForTests/forTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ForTests/forTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ForTests/forTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
    // USED → r4 = 10;
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 3, string_id: 4584>  # String: '__BC:ControlFlow/ForTests/forTest/if-continue' (String)
    // USED → r3 = "__BC:ControlFlow/ForTests/forTest/if-continue";
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 2, UInt8: 8>
    // USED → r2 = 8;
    // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // LOOP → START (for)
    for (r5 = 0; r5 < 10; r5 = r5 + 1) {
        // ──────────────── Block 1 ──────────────── 
        if (r5 === 3) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr: 88 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r8 = console;
            // CODE → addr: 94 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r7 = console.log;
            // CODE → addr: 99 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
            console.log("__BC:ControlFlow/ForTests/forTest/if-continue")
        } else {
            if (r5 === 8) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 66 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r9 = console;
                // CODE → addr: 72 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r8 = console.log;
                // CODE → addr: 77 | <LoadConstString>: <Reg8: 7, string_id: 4583>  # String: '__BC:ControlFlow/ForTests/forTest/if-break' (String)
                // USED → r7 = "__BC:ControlFlow/ForTests/forTest/if-break";
                // CODE → addr: 81 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
                console.log("__BC:ControlFlow/ForTests/forTest/if-break")
                // CODE → addr: 86 | <Jmp>: <Addr8: 25>  # Address: 0000006f
                break;
            }
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 48 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r8 = console;
            // CODE → addr: 54 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r7 = console.log;
            // CODE → addr: 59 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 6>
            console.log(r5)
            // CODE → addr: 64 | <Jmp>: <Addr8: 40>  # Address: 00000068
            continue;
        }
        // ──────────────── Block 6 ──────────────── 
    }
    // LOOP → END
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:111 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:117 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:122 | <LoadConstString>: <Reg8: 0, string_id: 3936>  # String: '__BC:ControlFlow/ForTests/forTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ForTests/forTest/end";
    // CODE → addr:126 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/ForTests/forTest/end")
    // CODE → addr:131 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:133 | <Ret>: <Reg8: 0>
    return undefined;
}