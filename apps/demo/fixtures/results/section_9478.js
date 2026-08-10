function switchInsideTryTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4124>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/start")
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // Switch → START
    switch (param1) {
        case 0:
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4852>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0")
            break;
        case 1:
            // ──────────────── Block 3 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
            // USED → r3 = globalThis.Error;
            // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
            // USED → r2 = __uninitialized_this_for_new__;
            // CODE → <LoadConstString>: <Reg8: 4, string_id: 5232>  # String: 'case 1 throws' (String)
            // USED → r4 = "case 1 throws";
            // CODE → <Mov>: <Reg8: 5, Reg8: 2>
            // USED → r5 = __uninitialized_this_for_new__;
            // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
            // USED → r0 = new globalThis.Error("case 1 throws", __uninitialized_this_for_new__);
            // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
            // USED → r0 = new globalThis.Error("case 1 throws", __uninitialized_this_for_new__);
            // CODE → <Throw>: <Reg8: 0>
            throw new globalThis.Error("case 1 throws", __uninitialized_this_for_new__);
        default:
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4853>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default' (String)
            // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default";
            // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
            console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default")
            // CODE → <Jmp>: <Addr8: 49>  # Address: 0000006b
            goto label_107;
            break;
    }
    // Switch → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Jmp>: <Addr8: 24>  # Address: 00000083
    goto label_131;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4857>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4855>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/end' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/end";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/end")
        // CODE → <LoadConstUndefined>: <Reg8: 0>
        // USED → r0 = undefined;
        // CODE → <Ret>: <Reg8: 0>
        return undefined;
        // CODE → <Catch>: <Reg8: 0>
        // USED → r0 = caughtException;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4857>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block' (String)
        // USED → r1 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block")
        // CODE → <Throw>: <Reg8: 0>
        throw caughtException;
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Catch>: <Reg8: 0>
        r0 = caughtException
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 3688>  # String: '__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block' (String)
        // USED → r0 = "__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block";
        // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block")
    }
    // LOOP → END
}