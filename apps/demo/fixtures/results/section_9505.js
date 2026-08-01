function regExpSingleQuotePatternTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5007>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = param1.replace;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 6445>  # String: '’' (String)
    // USED → r5 = "\u2019";
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 833, string_id: 6578, UInt32: 160>  # String: "'" (String)  # String: 'g' (Identifier)
    // USED → r2 = /'/g;
    // CODE → <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = param1.replace(/'/g, "\u2019");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(param1.replace(/'/g, "\u2019"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = param1.replace;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 362>  # String: '_' (String)
    // USED → r5 = "_";
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 2515, string_id: 6578, UInt32: 161>  # String: "['-]" (String)  # String: 'g' (Identifier)
    // USED → r2 = /['-]/g;
    // CODE → <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = param1.replace(/['-]/g, "_");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(param1.replace(/['-]/g, "_"))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 5006>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}