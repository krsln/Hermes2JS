function nestedTemplateTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 5, string_id: 705>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start' (String)
    // USED → r5 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start")
    // CODE → addr: 28 | <Add>: <Reg8: 5, Reg8: 4, Reg8: 3>
    r5 = param1 + param2
    // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    // CODE → addr: 35 | <JGreater>: <Addr8: 35, Reg8: 5, Reg8: 0>  # Address: 00000046
    // → r5 = param1 + param2
    if (r5 > 10) goto label_70;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 39 | <Add>: <Reg8: 8, Reg8: 4, Reg8: 3>
    // USED → r8 = param1 + param2;
    // CODE → addr: 43 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r5 = HermesInternal;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r7 = HermesInternal.concat;
    // CODE → addr: 54 | <LoadConstString>: <Reg8: 6, string_id: 870>  # String: ')' (String)
    // USED → r6 = ")";
    // CODE → addr: 58 | <LoadConstString>: <Reg8: 5, string_id: 1947>  # String: 'small (' (String)
    // USED → r5 = "small (";
    // CODE → addr: 62 | <Call3>: <Reg8: 5, Reg8: 7, Reg8: 5, Reg8: 8, Reg8: 6>
    r5 = HermesInternal.concat.call("small (", r8, ")")
    // CODE → addr: 68 | <Jmp>: <Addr8: 31>  # Address: 00000063
    goto label_99;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 70 | <Add>: <Reg8: 7, Reg8: 4, Reg8: 3>
    // USED → r7 = param1 + param2;
    // CODE → addr: 74 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r3 = HermesInternal;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r6 = HermesInternal.concat;
    // CODE → addr: 85 | <LoadConstString>: <Reg8: 4, string_id: 870>  # String: ')' (String)
    // USED → r4 = ")";
    // CODE → addr: 89 | <LoadConstString>: <Reg8: 3, string_id: 1926>  # String: 'big (' (String)
    // USED → r3 = "big (";
    // CODE → addr: 93 | <Call3>: <Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 7, Reg8: 4>
    // USED → r5 = HermesInternal.concat.call("big (", r7, ")");
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r3 = HermesInternal;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r4 = HermesInternal.concat;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 3, string_id: 1298>  # String: 'sum is ' (String)
    // USED → r3 = "sum is ";
    // CODE → addr:114 | <Call2>: <Reg8: 5, Reg8: 4, Reg8: 3, Reg8: 5>
    // USED → r5 = HermesInternal.concat.call("sum is ", r5);
    // CODE → addr:119 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:125 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:130 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → addr:135 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:141 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:146 | <LoadConstString>: <Reg8: 2, string_id: 5011>  # String: '__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end";
    // CODE → addr:150 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end")
    // CODE → addr:155 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr:157 | <Ret>: <Reg8: 1>
    return r1;
}