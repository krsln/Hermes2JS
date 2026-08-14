function nestedTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4860>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start' (String)
    // USED → r3 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start")
    // CODE → <Add>: <Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r4 = param1 + param2;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 10>
    // USED → r3 = 10;
    // → r4 = param1 + param2
    if (r4 > 10) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Add>: <Reg8: 5, Reg8: 2, Reg8: 1>
        // USED → r5 = param1 + param2;
        // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
        // USED → r1 = globalThis.HermesInternal;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
        // USED → r4 = globalThis.HermesInternal.concat;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 1940>  # String: 'big (' (String)
        // USED → r2 = "big (";
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 876>  # String: ')' (String)
        // USED → r1 = ")";
        // CODE → <Call3>: <Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5, Reg8: 1>
        // USED → r3 = globalThis.HermesInternal.concat.call("big (", r5, ")");
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Add>: <Reg8: 6, Reg8: 2, Reg8: 1>
        // USED → r6 = param1 + param2;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
        // USED → r3 = globalThis.HermesInternal;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
        // USED → r5 = globalThis.HermesInternal.concat;
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 524>  # String: 'small (' (String)
        // USED → r4 = "small (";
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 876>  # String: ')' (String)
        // USED → r3 = ")";
        // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 6, Reg8: 3>
        r3 = globalThis.HermesInternal.concat.call("small (", r6, ")")
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r2 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1321>  # String: 'sum is ' (String)
    // USED → r1 = "sum is ";
    // CODE → <Call2>: <Reg8: 3, Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r3 = globalThis.HermesInternal.concat.call("sum is ", r3);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4857>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end' (String)
    // USED → r0 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}