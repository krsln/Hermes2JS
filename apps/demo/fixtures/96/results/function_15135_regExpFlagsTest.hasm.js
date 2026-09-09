function regExpFlagsTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4849>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 6, string_id: 6584, string_id: 268, UInt32: 191>  # String: 'hello' (String)  # String: 'i' (String)
    r6 = /hello/i
    // CODE → addr: 39 | <CreateRegExp>: <Reg8: 4, string_id: 4514, string_id: 7179, UInt32: 192>  # String: '^line' (String)  # String: 'm' (Identifier)
    r4 = /^line/m
    // CODE → addr: 53 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 64 | <GetByIdShort>: <Reg8: 1, Reg8: 6, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = r6.test;
    // CODE → addr: 69 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 6, Reg8: 5>
    r1 = r6.test(param1)
    // CODE → addr: 74 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr: 79 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 90 | <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = r4.test;
    // CODE → addr: 95 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 4, Reg8: 5>
    r1 = r4.test(param1)
    // CODE → addr:100 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr:105 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:116 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 171>  # String: 'match' (Identifier)
    // USED → r4 = param1.match;
    // CODE → addr:121 | <CreateRegExp>: <Reg8: 1, string_id: 4336, string_id: 35, UInt32: 193>  # String: '[0-9A-Z_a-z]+' (String)  # String: 'g' (Identifier)
    r1 = /[0-9A-Z_a-z]+/g
    // CODE → addr:135 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    r1 = param1.match(r1)
    // CODE → addr:140 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr:145 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:151 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:156 | <LoadConstString>: <Reg8: 0, string_id: 4845>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → addr:160 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → addr:165 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:167 | <Ret>: <Reg8: 0>
    return undefined;
}