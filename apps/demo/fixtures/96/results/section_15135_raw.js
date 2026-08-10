function regExpFlagsTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4849>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → <CreateRegExp>: <Reg8: 6, string_id: 6584, string_id: 268, UInt32: 191>  # String: 'hello' (String)  # String: 'i' (String)
    // USED → r6 = /hello/i;
    // CODE → <CreateRegExp>: <Reg8: 4, string_id: 4514, string_id: 7179, UInt32: 192>  # String: '^line' (String)  # String: 'm' (Identifier)
    // USED → r4 = /^line/m;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 6, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = /hello/i.test;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 6, Reg8: 5>
    // USED → r1 = /hello/i.test(param1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(/hello/i.test(param1))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 238>  # String: 'test' (Identifier)
    // USED → r1 = /^line/m.test;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 4, Reg8: 5>
    // USED → r1 = /^line/m.test(param1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(/^line/m.test(param1))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 171>  # String: 'match' (Identifier)
    // USED → r4 = param1.match;
    // CODE → <CreateRegExp>: <Reg8: 1, string_id: 4336, string_id: 35, UInt32: 193>  # String: '[0-9A-Z_a-z]+' (String)  # String: 'g' (Identifier)
    // USED → r1 = /[0-9A-Z_a-z]+/g;
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 5, Reg8: 1>
    // USED → r1 = param1.match(/[0-9A-Z_a-z]+/g);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(param1.match(/[0-9A-Z_a-z]+/g))
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4845>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}