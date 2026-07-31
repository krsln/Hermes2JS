function basicRegExpTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4999>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → <CreateRegExp>: <Reg8: 5, string_id: 4696, string_id: 6457, UInt32: 155>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    // USED → r5 = /^\\d+$/;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /^\\d+$/.test;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    // USED → r2 = /^\\d+$/.test(param1);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(/^\\d+$/.test(param1))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = param1.match;
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 6471, string_id: 6578, UInt32: 156>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    // USED → r2 = /a/g;
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    // USED → r2 = param1.match(/a/g);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(param1.match(/a/g))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4998>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}