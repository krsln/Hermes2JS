function taggedTemplateTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4116>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start")
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
    r9 = 1
    // CODE → addr: 28 | <LoadConstTrue>: <Reg8: 8>
    r8 = true
    // CODE → addr: 30 | <LoadConstString>: <Reg8: 7, string_id: 1327>  # String: 'x squared is ' (String)
    r7 = "x squared is "
    // CODE → addr: 34 | <LoadConstString>: <Reg8: 6, string_id: 7163>  # String: '' (Identifier)
    r6 = ""
    // CODE → addr: 38 | <CallBuiltin>: <Reg8: 4, UInt8: 39, UInt8: 5>  # Built-in function: [#39 getTemplateObject]
    // USED → r4 = getTemplateObject(r9, r8, r7, r6, r5);
    // CODE → addr: 42 | <Mul>: <Reg8: 3, Reg8: 0, Reg8: 0>
    // USED → r3 = param1 * param1;
    // CODE → addr: 46 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 49 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r0[0];
    // CODE → addr: 53 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 55 | <Call3>: <Reg8: 4, Reg8: 2, Reg8: 0, Reg8: 4, Reg8: 3>
    // USED → r4 = r0[0](r4, r3);
    // CODE → addr: 61 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 72 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr: 77 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 83 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 88 | <LoadConstString>: <Reg8: 1, string_id: 4864>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end";
    // CODE → addr: 92 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end")
    // CODE → addr: 97 | <Ret>: <Reg8: 0>
    return undefined;
}