function loopBreakCrossesTryBoundaryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 8, UInt8: 1>
    r8 = param1
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 0, string_id: 4831>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start")
    // CODE → addr: 25 | <GetByIdShort>: <Reg8: 0, Reg8: 8, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r0 = r8.length;
    // CODE → addr: 30 | <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → addr: 32 | <Less>: <Reg8: 0, Reg8: 7, Reg8: 0>
    // USED → r0 = 0 < r8.length;
    // CODE → addr: 36 | <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → addr: 39 | <LoadConstString>: <Reg8: 3, string_id: 4828>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally";
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 5, string_id: 4824>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue";
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 4, string_id: 4830>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item";
    // → r8 = param1
    if (0 < r8.length) {
        // LOOP → START (for)
        // → r0 = 0
        for (r2 = 0; r2 < r0; r2 = r0 + 1) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 59 | <Mov>: <Reg8: 0, Reg8: 2>
            r0 = 0
            // CODE → addr: 62 | <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
            r9 = param1[r0]
            // → r9 = param1[r0]
            if (r9 >= 0) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr: 70 | <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
                r9 = param1[r0]
                // → r9 = param1[r0]
                if (r9 === 0) {
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → addr:117 | <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = console;
                    // CODE → addr:123 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = console.log;
                    // CODE → addr:128 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 5>
                    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue")
                    // CODE → addr:133 | <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = console;
                    // CODE → addr:139 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = console.log;
                    // CODE → addr:144 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 3>
                    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
                } else {
                    // ──────────────── Block 3 ──────────────── 
                    // CODE → addr: 78 | <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r11 = console;
                    // CODE → addr: 84 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r10 = console.log;
                    // CODE → addr: 89 | <GetByVal>: <Reg8: 9, Reg8: 8, Reg8: 0>
                    // USED → r9 = param1[r0];
                    // CODE → addr: 93 | <Call3>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 4, Reg8: 9>
                    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item", r9)
                    // CODE → addr: 99 | <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r10 = console;
                    // CODE → addr:105 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r9 = console.log;
                    // CODE → addr:110 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 3>
                    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
                }
                // ──────────────── Block 5 ──────────────── 
                // CODE → addr:153 | <GetByIdShort>: <Reg8: 0, Reg8: 8, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
                r0 = r8.length
            }
        }
        // LOOP → END
        // ──────────────── Block 6 ──────────────── 
        // CODE → addr:162 | <Jmp>: <Addr8: 38>  # Address: 000000c8
        goto label_200;
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:164 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr:170 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:175 | <LoadConstString>: <Reg8: 0, string_id: 4823>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break";
        // CODE → addr:179 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break")
        // CODE → addr:184 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r2 = console;
        // CODE → addr:190 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r0 = console.log;
        // CODE → addr:195 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 3>
        console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:200 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:206 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:211 | <LoadConstString>: <Reg8: 0, string_id: 4825>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end";
    // CODE → addr:215 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end")
    // CODE → addr:220 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:222 | <Ret>: <Reg8: 0>
    return undefined;
    // CODE → addr:224 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr:226 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:232 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:237 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // CODE → addr:242 | <Throw>: <Reg8: 0>
    throw caughtException;
}