function basicTemplateTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4855>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/start' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/start")
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r6 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 11, string_id: 2020>  # String: 'Hello, ' (String)
    r11 = "Hello, "
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    r10 = param1
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 1194>  # String: '! You are ' (String)
    r9 = "! You are "
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 2>
    r8 = param2
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 979>  # String: ' years old.' (String)
    r7 = " years old."
    // CODE → <Call>: <Reg8: 3, Reg8: 6, UInt8: 5>
    // USED → r3 = globalThis.HermesInternal.concat(r1, r2, r3, r4, r5);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log(globalThis.HermesInternal.concat(r1, r2, r3, r4, r5))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4515>  # String: 'line one\nline two' (String)
    // USED → r1 = "line one\\nline two";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("line one\\nline two")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4854>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/end' (String)
    // USED → r0 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}