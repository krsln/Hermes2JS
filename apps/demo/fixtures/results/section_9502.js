function taggedTemplateTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5015>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start' (String)
    // USED → r4 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start")
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 6457>  # String: '' (Identifier)
    r7 = ""
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 1303>  # String: 'x squared is ' (String)
    r8 = "x squared is "
    // CODE → <LoadConstTrue>: <Reg8: 9>
    r9 = true
    // CODE → <LoadConstUInt8>: <Reg8: 10, UInt8: 1>
    r10 = 1
    // CODE → <CallBuiltin>: <Reg8: 5, UInt8: 41, UInt8: 5>  # Built-in function: [#41 getTemplateObject]
    // USED → r5 = getTemplateObject(r0, r1, r2, r3, r4);
    // CODE → <Mul>: <Reg8: 4, Reg8: 3, Reg8: 3>
    // USED → r4 = param1 * param1;
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call3>: <Reg8: 5, Reg8: 3, Reg8: 1, Reg8: 5, Reg8: 4>
    // USED → r5 = getParentEnvironment(0)[0].call(undefined, r5, r4);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1383>  # String: '__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}