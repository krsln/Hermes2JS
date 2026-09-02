function regExpFlagsTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 5003>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 7, string_id: 6140, string_id: 280, UInt32: 157>  # String: 'hello' (String)  # String: 'i' (String)
    r7 = /hello/i
    // CODE → addr: 39 | <CreateRegExp>: <Reg8: 5, string_id: 4706, string_id: 6516, UInt32: 158>  # String: '^line' (String)  # String: 'm' (Identifier)
    r5 = /^line/m
    // CODE → addr: 53 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 64 | <GetByIdShort>: <Reg8: 2, Reg8: 7, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r7.test;
    // CODE → addr: 69 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 7, Reg8: 6>
    r2 = r7.test(param1)
    // CODE → addr: 74 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 79 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 90 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r5.test;
    // CODE → addr: 95 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    r2 = r5.test(param1)
    // CODE → addr:100 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:105 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:116 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = param1.match;
    // CODE → addr:121 | <CreateRegExp>: <Reg8: 2, string_id: 1961, string_id: 2193, UInt32: 159>  # String: '\\w+' (String)  # String: 'gu' (String)
    r2 = /\w+/gu
    // CODE → addr:135 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    r2 = param1.match(r2)
    // CODE → addr:140 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:145 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:151 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:156 | <LoadConstString>: <Reg8: 1, string_id: 5001>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → addr:160 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → addr:165 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:167 | <Ret>: <Reg8: 0>
    return undefined;
}