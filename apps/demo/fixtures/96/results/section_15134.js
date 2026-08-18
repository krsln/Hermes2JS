function basicRegExpTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4840>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → <CreateRegExp>: <Reg8: 4, string_id: 4503, string_id: 7163, UInt32: 3>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    // USED → r4 = /^\\d+$/;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = /^\\d+$/.test;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 4, Reg8: 5>
    // USED → r1 = /^\\d+$/.test(param1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 171>  # String: 'match' (Identifier)
    // USED → r4 = param1.match;
    // CODE → <CreateRegExp>: <Reg8: 1, string_id: 7189, string_id: 35, UInt32: 190>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    // USED → r1 = /a/g;
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    // USED → r1 = param1.match(r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 724>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}