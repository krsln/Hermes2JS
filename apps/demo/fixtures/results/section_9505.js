function regExpSingleQuotePatternTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 7, UInt8: 1>
    r7 = param1
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 5007>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → addr: 25 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = r7.replace;
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 5, string_id: 6445>  # String: '’' (String)
    // USED → r5 = "\u2019";
    // CODE → addr: 45 | <CreateRegExp>: <Reg8: 2, string_id: 833, string_id: 6578, UInt32: 160>  # String: "'" (String)  # String: 'g' (Identifier)
    // USED → r2 = /'/g;
    // CODE → addr: 59 | <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = r7.replace(r2, "\u2019");
    // CODE → addr: 65 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 70 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = r7.replace;
    // CODE → addr: 86 | <LoadConstString>: <Reg8: 5, string_id: 362>  # String: '_' (String)
    // USED → r5 = "_";
    // CODE → addr: 90 | <CreateRegExp>: <Reg8: 2, string_id: 2515, string_id: 6578, UInt32: 161>  # String: "['-]" (String)  # String: 'g' (Identifier)
    // USED → r2 = /['-]/g;
    // CODE → addr:104 | <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = r7.replace(r2, "_");
    // CODE → addr:110 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:115 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 1, string_id: 5006>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → addr:130 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → addr:135 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:137 | <Ret>: <Reg8: 0>
    return undefined;
}