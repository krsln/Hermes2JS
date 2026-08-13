function regExpSingleQuotePatternTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4853>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r5 = param1.replace;
    // CODE → <CreateRegExp>: <Reg8: 4, string_id: 819, string_id: 35, UInt32: 1>  # String: "'" (String)  # String: 'g' (Identifier)
    // USED → r4 = /'/g;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 7151>  # String: '’' (String)
    // USED → r1 = "\u2019";
    // CODE → <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
    // USED → r1 = param1.replace(r4, "\u2019");
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r5 = param1.replace;
    // CODE → <CreateRegExp>: <Reg8: 4, string_id: 2429, string_id: 35, UInt32: 194>  # String: "['-]" (String)  # String: 'g' (Identifier)
    // USED → r4 = /['-]/g;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 389>  # String: '_' (String)
    // USED → r1 = "_";
    // CODE → <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
    // USED → r1 = param1.replace(r4, "_");
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4852>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}