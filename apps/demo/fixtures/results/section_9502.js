function taggedTemplateTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 4, string_id: 5015>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start' (String)
    // USED → r4 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start")
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 7, string_id: 6457>  # String: '' (Identifier)
    r7 = ""
    // CODE → addr: 29 | <LoadConstString>: <Reg8: 8, string_id: 1303>  # String: 'x squared is ' (String)
    r8 = "x squared is "
    // CODE → addr: 33 | <LoadConstTrue>: <Reg8: 9>
    r9 = true
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 10, UInt8: 1>
    r10 = 1
    // CODE → addr: 38 | <CallBuiltin>: <Reg8: 5, UInt8: 41, UInt8: 5>  # Built-in function: [#41 getTemplateObject]
    // USED → r5 = getTemplateObject(r0, r1, r2, r3, r4);
    // CODE → addr: 42 | <Mul>: <Reg8: 4, Reg8: 3, Reg8: 3>
    // USED → r4 = param1 * param1;
    // CODE → addr: 46 | <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → addr: 49 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 0>
    // USED → r3 = r3[0];
    // CODE → addr: 53 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 55 | <Call3>: <Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 5, Reg8: 4>
    // USED → r5 = r3[0].call(r1, r5, r4);
    // CODE → addr: 61 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 72 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → addr: 77 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 83 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 88 | <LoadConstString>: <Reg8: 2, string_id: 1383>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end";
    // CODE → addr: 92 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end")
    // CODE → addr: 97 | <Ret>: <Reg8: 1>
    return undefined;
}