function switchInsideTryTest(param1) {
    try {
        // ──────────────── Block 0 ──────────────── 
        // CODE → addr:  0 | <LoadParam>: <Reg8: 0, UInt8: 1>
        // USED → r0 = param1;
        // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4684>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/start' (String)
        // USED → r2 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/start";
        // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/start")
        // CODE → addr: 25 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = param1
        // CODE → addr: 28 | <LoadConstZero>: <Reg8: 0>
        // USED → r0 = 0;
        // Switch → START
        switch (r2) {
            case 0:
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 95 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = console;
                // CODE → addr:101 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r2 = console.log;
                // CODE → addr:106 | <LoadConstString>: <Reg8: 0, string_id: 2266>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0";
                // CODE → addr:110 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
                console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0")
                break;
            case 1:
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr: 63 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
                // USED → r3 = Error;
                // CODE → addr: 69 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
                // USED → r0 = Error.prototype;
                // CODE → addr: 74 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
                // USED → r2 = CreateThis(r0);
                // CODE → addr: 78 | <LoadConstString>: <Reg8: 5, string_id: 5270>  # String: 'case 1 throws' (String)
                // USED → r5 = "case 1 throws";
                // CODE → addr: 82 | <Mov>: <Reg8: 6, Reg8: 2>
                // USED → r6 = CreateThis(r0);
                // CODE → addr: 85 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
                // USED → r0 = new Error("case 1 throws");
                // CODE → addr: 89 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
                // USED → r0 = new Error("case 1 throws");
                // CODE → addr: 93 | <Throw>: <Reg8: 0>
                throw new Error("case 1 throws");
            default:
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr: 41 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r3 = console;
                // CODE → addr: 47 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r2 = console.log;
                // CODE → addr: 52 | <LoadConstString>: <Reg8: 0, string_id: 4678>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default' (String)
                // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default";
                // CODE → addr: 56 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
                console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default")
                // CODE → addr: 61 | <Jmp>: <Addr8: 54>  # Address: 00000073
                goto label_115;
                break;
        }
        // Switch → END
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr:115 | <Jmp>: <Addr8: 24>  # Address: 0000008b
        goto label_139;
    } catch (caughtException) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → addr:119 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:125 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:130 | <LoadConstString>: <Reg8: 0, string_id: 4680>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block";
        // CODE → addr:134 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block")
    } finally {
        // ──────────────── Block 8 ──────────────── 
        // CODE → addr:185 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:191 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:196 | <LoadConstString>: <Reg8: 1, string_id: 4683>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
        // CODE → addr:200 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
    }
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:159 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:165 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:170 | <LoadConstString>: <Reg8: 0, string_id: 4682>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/end' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/end";
    // CODE → addr:174 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/end")
    // CODE → addr:179 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:181 | <Ret>: <Reg8: 0>
    return undefined;
}