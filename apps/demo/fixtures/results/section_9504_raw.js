function regExpFlagsTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5003>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → <CreateRegExp>: <Reg8: 7, string_id: 6140, string_id: 280, UInt32: 157>  # String: 'hello' (String)  # String: 'i' (String)
    // USED → r7 = /hello/i;
    // CODE → <CreateRegExp>: <Reg8: 5, string_id: 4706, string_id: 6516, UInt32: 158>  # String: '^line' (String)  # String: 'm' (Identifier)
    // USED → r5 = /^line/m;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 7, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /hello/i.test;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 7, Reg8: 6>
    // USED → r2 = /hello/i.test(param1);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(/hello/i.test(param1))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /^line/m.test;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    // USED → r2 = /^line/m.test(param1);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(/^line/m.test(param1))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = param1.match;
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 1961, string_id: 2193, UInt32: 159>  # String: '\\w+' (String)  # String: 'gu' (String)
    // USED → r2 = /\\w+/gu;
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    // USED → r2 = param1.match(/\\w+/gu);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(param1.match(/\\w+/gu))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 5001>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}