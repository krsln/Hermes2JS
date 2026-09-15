function basicTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 5009>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/start' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r2 = HermesInternal;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 7, Reg8: 2, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r7 = HermesInternal.concat;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 8, string_id: 950>  # String: ' years old.' (String)
    r8 = " years old."
    // CODE → addr: 37 | <LoadConstString>: <Reg8: 10, string_id: 1148>  # String: '! You are ' (String)
    r10 = "! You are "
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 12, string_id: 1294>  # String: 'Hello, ' (String)
    r12 = "Hello, "
    // CODE → addr: 45 | <LoadParam>: <Reg8: 9, UInt8: 2>
    r9 = param2
    // CODE → addr: 48 | <LoadParam>: <Reg8: 11, UInt8: 1>
    r11 = param1
    // CODE → addr: 51 | <Call>: <Reg8: 4, Reg8: 7, UInt8: 5>
    r4 = HermesInternal.concat(r12, param1, r10, param2, r8)
    // CODE → addr: 55 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 61 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 66 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr: 71 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 2, string_id: 4707>  # String: 'line one\nline two' (String)
    // USED → r2 = "line one\\nline two";
    // CODE → addr: 86 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("line one\\nline two")
    // CODE → addr: 91 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:102 | <LoadConstString>: <Reg8: 1, string_id: 5008>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/end' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/end";
    // CODE → addr:106 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/end")
    // CODE → addr:111 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:113 | <Ret>: <Reg8: 0>
    return r0;
}