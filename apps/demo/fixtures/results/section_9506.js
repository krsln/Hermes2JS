function regExpGroupsAndReplaceTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 5, UInt8: 1>
    r5 = param1
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 5005>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 4, string_id: 1955, string_id: 6457, UInt32: 162>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    r4 = /(\\d{4})-(\\d{2})-(\\d{2})/
    // CODE → addr: 39 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 180>  # String: 'match' (Identifier)
    // USED → r2 = r5.match;
    // CODE → addr: 44 | <Call2>: <Reg8: 6, Reg8: 2, Reg8: 5, Reg8: 4>
    r6 = r5.match(r4)
    // CODE → addr: 49 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 55 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 60 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → addr: 65 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 3, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r3 = r5.replace;
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 2, string_id: 1684>  # String: '$3/$2/$1' (String)
    // USED → r2 = "$3/$2/$1";
    // CODE → addr: 74 | <Call3>: <Reg8: 4, Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 2>
    r4 = r5.replace(r4, "$3/$2/$1")
    // CODE → addr: 80 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 86 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 91 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr: 96 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:107 | <LoadConstString>: <Reg8: 1, string_id: 5004>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → addr:111 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → addr:116 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:118 | <Ret>: <Reg8: 0>
    return undefined;
}