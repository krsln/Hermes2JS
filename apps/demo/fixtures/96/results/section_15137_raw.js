function regExpGroupsAndReplaceTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 4, UInt8: 1>
    r4 = param1
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4851>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → addr: 25 | <CreateRegExp>: <Reg8: 3, string_id: 1977, string_id: 7163, UInt32: 195>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    // USED → r3 = /(\\d{4})-(\\d{2})-(\\d{2})/;
    // CODE → addr: 39 | <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 3, string_id: 171>  # String: 'match' (Identifier)
    // USED → r1 = r4.match;
    // CODE → addr: 44 | <Call2>: <Reg8: 5, Reg8: 1, Reg8: 4, Reg8: 3>
    // USED → r5 = r4.match(r3);
    // CODE → addr: 49 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 55 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 60 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5>
    console.log(r5)
    // CODE → addr: 65 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 4, string_id: 213>  # String: 'replace' (Identifier)
    // USED → r2 = r4.replace;
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 1, string_id: 1716>  # String: '$3/$2/$1' (String)
    // USED → r1 = "$3/$2/$1";
    // CODE → addr: 74 | <Call3>: <Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 1>
    // USED → r3 = r4.replace(r3, "$3/$2/$1");
    // CODE → addr: 80 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 86 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 91 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr: 96 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:107 | <LoadConstString>: <Reg8: 0, string_id: 4850>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → addr:111 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → addr:116 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:118 | <Ret>: <Reg8: 0>
    return r0;
}