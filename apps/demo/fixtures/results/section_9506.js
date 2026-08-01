function regExpGroupsAndReplaceTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5005>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → <CreateRegExp>: <Reg8: 4, string_id: 1955, string_id: 6457, UInt32: 162>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    // USED → r4 = /(\\d{4})-(\\d{2})-(\\d{2})/;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 180>  # String: 'match' (Identifier)
    // USED → r2 = param1.match;
    // CODE → <Call2>: <Reg8: 6, Reg8: 2, Reg8: 5, Reg8: 4>
    // USED → r6 = param1.match(/(\\d{4})-(\\d{2})-(\\d{2})/);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    r2 = globalThis.console.log(param1.match(/(\\d{4})-(\\d{2})-(\\d{2})/))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 3, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r3 = param1.replace;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1684>  # String: '$3/$2/$1' (String)
    // USED → r2 = "$3/$2/$1";
    // CODE → <Call3>: <Reg8: 4, Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 2>
    // USED → r4 = param1.replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1");
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    r2 = globalThis.console.log(param1.replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1"))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 5004>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}