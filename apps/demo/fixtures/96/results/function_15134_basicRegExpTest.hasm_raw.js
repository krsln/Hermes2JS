function basicRegExpTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4840>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 4, string_id: 4503, string_id: 7163, UInt32: 3>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    r4 = /^\d+$/
    // CODE → addr: 39 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = r4.test;
    // CODE → addr: 55 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 4, Reg8: 5>
    r1 = r4.test(param1)
    // CODE → addr: 60 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr: 65 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 171>  # String: 'match' (Identifier)
    // USED → r4 = param1.match;
    // CODE → addr: 81 | <CreateRegExp>: <Reg8: 1, string_id: 7189, string_id: 35, UInt32: 190>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    r1 = /a/g
    // CODE → addr: 95 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    r1 = param1.match(r1)
    // CODE → addr:100 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr:105 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:116 | <LoadConstString>: <Reg8: 0, string_id: 724>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → addr:120 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → addr:125 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:127 | <Ret>: <Reg8: 0>
    return r0;
}