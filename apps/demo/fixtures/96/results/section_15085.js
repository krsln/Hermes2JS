function tryCatchInsideLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <Mov>: <Reg8: 7, Reg8: 2>
    // USED → r7 = param1;
    // CODE → addr:  6 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  8 | <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 3, string_id: 4708>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start")
    // CODE → addr: 32 | <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → addr: 34 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 36 | <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r2 = param1.length
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 5, string_id: 2131>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught";
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 4, string_id: 4701>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok' (String)
    // USED → r4 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok";
    // → r2 = param1.length
    if (0 < r2) {
        // LOOP → START (for)
        // → r2 = param1[r2]; r3 = param1
        for (; r3 < r2; r3 = r2 + 1) {
            try {
                // ──────────────── Block 1 ──────────────── 
                // CODE → addr: 58 | <Mov>: <Reg8: 3, Reg8: 7>
                // USED → r3 = param1;
                // CODE → addr: 61 | <Mov>: <Reg8: 2, Reg8: 8>
                r2 = 0
                // CODE → addr: 64 | <GetByVal>: <Reg8: 2, Reg8: 3, Reg8: 2>
                r2 = param1[r2]
            } catch (caughtException) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr:135 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = console;
                // CODE → addr:141 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r2 = console.log;
                // CODE → addr:146 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 9>
                console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", r9)
                // CODE → addr:152 | <Mov>: <Reg8: 2, Reg8: 0>
                r2 = 0
                // CODE → addr:155 | <Inc>: <Reg8: 0, Reg8: 2>
                r0 = r2 + 1
            }
            if (r2 < 0) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr:101 | <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 4, string_id: 12>  # String: 'Error' (Identifier)
                // USED → r9 = Error;
                // CODE → addr:107 | <GetByIdShort>: <Reg8: 2, Reg8: 9, UInt8: 5, string_id: 206>  # String: 'prototype' (Identifier)
                // USED → r2 = Error.prototype;
                // CODE → addr:112 | <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 9>
                // USED → r3 = CreateThis(r2);
                // CODE → addr:116 | <LoadConstString>: <Reg8: 12, string_id: 839>  # String: 'negative value' (String)
                // USED → r12 = "negative value";
                // CODE → addr:120 | <Mov>: <Reg8: 13, Reg8: 3>
                // USED → r13 = CreateThis(r2);
                // CODE → addr:123 | <Construct>: <Reg8: 2, Reg8: 9, UInt8: 2>
                // USED → r2 = new Error("negative value");
                // CODE → addr:127 | <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
                // USED → r2 = new Error("negative value");
                // CODE → addr:131 | <Throw>: <Reg8: 2>
                throw new Error("negative value");
            }
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 72 | <TryGetById>: <Reg8: 9, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r9 = console;
            // CODE → addr: 78 | <GetByIdShort>: <Reg8: 3, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → addr: 83 | <Mov>: <Reg8: 10, Reg8: 7>
            // USED → r10 = param1;
            // CODE → addr: 86 | <Mov>: <Reg8: 2, Reg8: 8>
            r2 = 0
            // CODE → addr: 89 | <GetByVal>: <Reg8: 2, Reg8: 10, Reg8: 2>
            r2 = param1[r2]
            // CODE → addr: 93 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 9, Reg8: 4, Reg8: 2>
            console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", r2)
            // CODE → addr: 99 | <Jmp>: <Addr8: 59>  # Address: 0000009e
            goto label_158;
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr:158 | <Mov>: <Reg8: 2, Reg8: 8>
            r2 = 0
            // CODE → addr:164 | <Mov>: <Reg8: 8, Reg8: 3>
            r8 = r2 + 1
            // CODE → addr:167 | <Mov>: <Reg8: 2, Reg8: 7>
            r2 = param1
            // CODE → addr:170 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
            r2 = r2.length
        }
        // LOOP → END
    }
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:179 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:185 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:190 | <LoadConstString>: <Reg8: 1, string_id: 4699>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end";
    // CODE → addr:194 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end")
    // CODE → addr:199 | <Ret>: <Reg8: 0>
    return r0;
}