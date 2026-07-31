function regExpGroupsAndReplaceTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4851>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → <CreateRegExp>: <Reg8: 3, string_id: 1977, string_id: 7163, UInt32: 195>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    // USED → r3 = /(\\d{4})-(\\d{2})-(\\d{2})/;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 171>  # String: 'match' (Identifier)
    // USED → r1 = param1.match;
    // CODE → <Call2>: <Reg8: 5, Reg8: 1, Reg8: 4, Reg8: 3>
    // USED → r5 = param1.match(/(\\d{4})-(\\d{2})-(\\d{2})/);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5>
    r1 = globalThis.console.log(param1.match(/(\\d{4})-(\\d{2})-(\\d{2})/))
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 4, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r2 = param1.replace;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1716>  # String: '$3/$2/$1' (String)
    // USED → r1 = "$3/$2/$1";
    // CODE → <Call3>: <Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 1>
    // USED → r3 = param1.replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1");
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log(param1.replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1"))
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4850>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}