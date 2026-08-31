function basicTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4855>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/start' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = HermesInternal;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r6 = HermesInternal.concat;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 11, string_id: 2020>  # String: 'Hello, ' (String)
    r11 = "Hello, "
    // CODE → addr: 37 | <LoadParam>: <Reg8: 10, UInt8: 1>
    r10 = param1
    // CODE → addr: 40 | <LoadConstString>: <Reg8: 9, string_id: 1194>  # String: '! You are ' (String)
    r9 = "! You are "
    // CODE → addr: 44 | <LoadParam>: <Reg8: 8, UInt8: 2>
    r8 = param2
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 7, string_id: 979>  # String: ' years old.' (String)
    r7 = " years old."
    // CODE → addr: 51 | <Call>: <Reg8: 3, Reg8: 6, UInt8: 5>
    r3 = HermesInternal.concat(r11, r10, r9, r8, r7)
    // CODE → addr: 55 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 61 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 66 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr: 71 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 1, string_id: 4515>  # String: 'line one\nline two' (String)
    // USED → r1 = "line one\\nline two";
    // CODE → addr: 86 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("line one\\nline two")
    // CODE → addr: 91 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:102 | <LoadConstString>: <Reg8: 0, string_id: 4854>  # String: '__BC:Strings/TemplateLiteralTests/basicTemplateTest/end' (String)
    // USED → r0 = "__BC:Strings/TemplateLiteralTests/basicTemplateTest/end";
    // CODE → addr:106 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/end")
    // CODE → addr:111 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:113 | <Ret>: <Reg8: 0>
    return r0;
}