function nestedTemplateTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 705>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start' (String)
    // USED → r5 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start")
    // CODE → <Add>: <Reg8: 5, Reg8: 4, Reg8: 3>
    // USED → r5 = param1 + param2;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    if (param1 + param2 > 10) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Add>: <Reg8: 7, Reg8: 4, Reg8: 3>
        // USED → r7 = param1 + param2;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
        // USED → r3 = globalThis.HermesInternal;
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
        // USED → r6 = globalThis.HermesInternal.concat;
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 870>  # String: ')' (String)
        // USED → r4 = ")";
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 1926>  # String: 'big (' (String)
        // USED → r3 = "big (";
        // CODE → <Call3>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 7, Reg8: 4>
        // USED → r5 = globalThis.HermesInternal.concat.call("big (", param1 + param2, ")");
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Add>: <Reg8: 8, Reg8: 4, Reg8: 3>
        // USED → r8 = param1 + param2;
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
        // USED → r5 = globalThis.HermesInternal;
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
        // USED → r7 = globalThis.HermesInternal.concat;
        // CODE → <LoadConstString>: <Reg8: 6, string_id: 870>  # String: ')' (String)
        // USED → r6 = ")";
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 1947>  # String: 'small (' (String)
        // USED → r5 = "small (";
        // CODE → <Call3>: <Reg8: 5, Reg8: 7, Reg8: 5, Reg8: 8, Reg8: 6>
        r5 = globalThis.HermesInternal.concat.call("small (", param1 + param2, ")")
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r3 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r4 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1298>  # String: 'sum is ' (String)
    // USED → r3 = "sum is ";
    // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 3, Reg8: 5>
    // USED → r5 = globalThis.HermesInternal.concat.call("sum is ", globalThis.HermesInternal.concat.call("big (", param1 + param2, ")"));
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    r3 = globalThis.console.log(globalThis.HermesInternal.concat.call("sum is ", globalThis.HermesInternal.concat.call("big (", param1 + param2, ")")))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5011>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}