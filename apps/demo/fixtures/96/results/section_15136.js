function regExpSingleQuotePatternTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 1>
    r6 = param1
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4853>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → addr: 25 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r5 = r6.replace;
    // CODE → addr: 41 | <CreateRegExp>: <Reg8: 4, string_id: 819, string_id: 35, UInt32: 1>  # String: "'" (String)  # String: 'g' (Identifier)
    r4 = /'/g
    // CODE → addr: 55 | <LoadConstString>: <Reg8: 1, string_id: 7151>  # String: '’' (String)
    // USED → r1 = "\u2019";
    // CODE → addr: 59 | <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
    r1 = r6.replace(r4, "\u2019")
    // CODE → addr: 65 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr: 70 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r5 = r6.replace;
    // CODE → addr: 86 | <CreateRegExp>: <Reg8: 4, string_id: 2429, string_id: 35, UInt32: 194>  # String: "['-]" (String)  # String: 'g' (Identifier)
    r4 = /['-]/g
    // CODE → addr:100 | <LoadConstString>: <Reg8: 1, string_id: 389>  # String: '_' (String)
    // USED → r1 = "_";
    // CODE → addr:104 | <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
    r1 = r6.replace(r4, "_")
    // CODE → addr:110 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr:115 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 0, string_id: 4852>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → addr:130 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → addr:135 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:137 | <Ret>: <Reg8: 0>
    return undefined;
}