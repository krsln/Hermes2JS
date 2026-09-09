function basicRegExpTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 4999>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 5, string_id: 4696, string_id: 6457, UInt32: 155>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    r5 = /^\d+$/
    // CODE → addr: 39 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r5.test;
    // CODE → addr: 55 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    r2 = r5.test(param1)
    // CODE → addr: 60 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 65 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = param1.match;
    // CODE → addr: 81 | <CreateRegExp>: <Reg8: 2, string_id: 6471, string_id: 6578, UInt32: 156>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    r2 = /a/g
    // CODE → addr: 95 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    r2 = param1.match(r2)
    // CODE → addr:100 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:105 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:116 | <LoadConstString>: <Reg8: 1, string_id: 4998>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → addr:120 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → addr:125 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:127 | <Ret>: <Reg8: 0>
    return r0;
}