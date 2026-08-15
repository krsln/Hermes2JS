function basicTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5009>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/start' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/start")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r2 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 2, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r7 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 950>  # String: ' years old.' (String)
    r8 = " years old."
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 1148>  # String: '! You are ' (String)
    r10 = "! You are "
    // CODE → <LoadConstString>: <Reg8: 12, string_id: 1294>  # String: 'Hello, ' (String)
    r12 = "Hello, "
    // CODE → <LoadParam>: <Reg8: 9, UInt8: 2>
    r9 = param2
    // CODE → <LoadParam>: <Reg8: 11, UInt8: 1>
    r11 = param1
    // CODE → <Call>: <Reg8: 4, Reg8: 7, UInt8: 5>
    // USED → r4 = globalThis.HermesInternal.concat(r12, r11, r10, r9, r8);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4707>  # String: 'line one\nline two' (String)
    // USED → r2 = "line one\\nline two";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("line one\\nline two")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 5008>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/end' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}