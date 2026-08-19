function taggedTemplateTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4116>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
    r9 = 1
    // CODE → <LoadConstTrue>: <Reg8: 8>
    r8 = true
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 1327>  # String: 'x squared is ' (String)
    r7 = "x squared is "
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 7163>  # String: '' (Identifier)
    r6 = ""
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 39, UInt8: 5>  # Built-in function: [#39 getTemplateObject]
    // USED → r4 = getTemplateObject(r-1, r0, r1, r2, r3);
    // CODE → <Mul>: <Reg8: 3, Reg8: 0, Reg8: 0>
    // USED → r3 = param1 * param1;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r0[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <Call3>: <Reg8: 4, Reg8: 2, Reg8: 0, Reg8: 4, Reg8: 3>
    // USED → r4 = r0[0](r4, r3);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4864>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}