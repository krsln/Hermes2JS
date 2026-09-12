function nestedTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 3, string_id: 4860>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start' (String)
    // USED → r3 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start")
    // CODE → addr: 28 | <Add>: <Reg8: 4, Reg8: 2, Reg8: 1>
    r4 = param1 + param2
    // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 3, UInt8: 10>
    // USED → r3 = 10;
    // CODE → addr: 35 | <JGreater>: <Addr8: 35, Reg8: 4, Reg8: 3>  # Address: 00000046
    // → r4 = param1 + param2
    if (r4 > 10) goto label_70;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 39 | <Add>: <Reg8: 6, Reg8: 2, Reg8: 1>
    r6 = param1 + param2
    // CODE → addr: 43 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r3 = HermesInternal;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r5 = HermesInternal.concat;
    // CODE → addr: 54 | <LoadConstString>: <Reg8: 4, string_id: 524>  # String: 'small (' (String)
    // USED → r4 = "small (";
    // CODE → addr: 58 | <LoadConstString>: <Reg8: 3, string_id: 876>  # String: ')' (String)
    // USED → r3 = ")";
    // CODE → addr: 62 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 6, Reg8: 3>
    r3 = HermesInternal.concat.call("small (", r6, ")")
    // CODE → addr: 68 | <Jmp>: <Addr8: 31>  # Address: 00000063
    goto label_99;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 70 | <Add>: <Reg8: 5, Reg8: 2, Reg8: 1>
    r5 = param1 + param2
    // CODE → addr: 74 | <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = HermesInternal;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r4 = HermesInternal.concat;
    // CODE → addr: 85 | <LoadConstString>: <Reg8: 2, string_id: 1940>  # String: 'big (' (String)
    // USED → r2 = "big (";
    // CODE → addr: 89 | <LoadConstString>: <Reg8: 1, string_id: 876>  # String: ')' (String)
    // USED → r1 = ")";
    // CODE → addr: 93 | <Call3>: <Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5, Reg8: 1>
    r3 = HermesInternal.concat.call("big (", r5, ")")
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = HermesInternal;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r2 = HermesInternal.concat;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 1, string_id: 1321>  # String: 'sum is ' (String)
    // USED → r1 = "sum is ";
    // CODE → addr:114 | <Call2>: <Reg8: 3, Reg8: 2, Reg8: 1, Reg8: 3>
    r3 = HermesInternal.concat.call("sum is ", r3)
    // CODE → addr:119 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:125 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:130 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:135 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:141 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:146 | <LoadConstString>: <Reg8: 0, string_id: 4857>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end' (String)
    // USED → r0 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end";
    // CODE → addr:150 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end")
    // CODE → addr:155 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:157 | <Ret>: <Reg8: 0>
    return r0;
}