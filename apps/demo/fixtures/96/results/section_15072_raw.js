function logicalShortCircuitTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → addr:  6 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  8 | <CreateClosure>: <Reg8: 7, Reg8: 0, function_id: 15073>  # Function: [#15073 sideEffect of 31 bytes]: 3 params @ offset 0x00268778
    // USED → r7 = sideEffect(param1, param2);
    // CODE → addr: 13 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 15 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 21 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 26 | <LoadConstString>: <Reg8: 0, string_id: 4635>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start' (String)
    // USED → r0 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start";
    // CODE → addr: 30 | <Call2>: <Reg8: 0, Reg8: 4, Reg8: 5, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start")
    // CODE → addr: 35 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 37 | <LoadConstString>: <Reg8: 4, string_id: 5116>  # String: 'and-left' (String)
    // USED → r4 = "and-left";
    // CODE → addr: 41 | <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 3>
    r4 = sideEffect(param1, param2).call(undefined, "and-left", param1)
    // CODE → addr: 47 | <Mov>: <Reg8: 6, Reg8: 3>
    r6 = param1
    // CODE → addr: 50 | <JmpFalse>: <Addr8: 16, Reg8: 3>  # Address: 00000042
    if (!param1) goto label_66;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 4, string_id: 5117>  # String: 'and-right' (String)
    // USED → r4 = "and-right";
    // CODE → addr: 57 | <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 2>
    r4 = sideEffect(param1, param2).call(undefined, "and-right", param2)
    // CODE → addr: 63 | <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = param2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 66 | <LoadConstString>: <Reg8: 4, string_id: 1184>  # String: 'or-left' (String)
    // USED → r4 = "or-left";
    // CODE → addr: 70 | <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 3>
    r4 = sideEffect(param1, param2).call(undefined, "or-left", param1)
    // CODE → addr: 76 | <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = param1;
    // CODE → addr: 79 | <JmpTrue>: <Addr8: 16, Reg8: 5>  # Address: 0000005f
    if (param1) goto label_95;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 4, string_id: 1951>  # String: 'or-right' (String)
    // USED → r4 = "or-right";
    // CODE → addr: 86 | <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 2>
    r4 = sideEffect(param1, param2).call(undefined, "or-right", param2)
    // CODE → addr: 92 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = param2;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 95 | <LoadConstString>: <Reg8: 4, string_id: 74>  # String: 'left' (Identifier)
    r4 = "left"
    // CODE → addr: 99 | <JmpFalse>: <Addr8: 5, Reg8: 3>  # Address: 00000068
    if (!param1) goto label_104;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:102 | <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:104 | <LoadConstNull>: <Reg8: 3>
    // USED → r3 = null;
    // CODE → addr:106 | <JNotEqual>: <Addr8: 17, Reg8: 4, Reg8: 3>  # Address: 0000007b
    if (null != null) goto label_123;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:110 | <LoadConstString>: <Reg8: 3, string_id: 3574>  # String: 'nullish-right' (String)
    // USED → r3 = "nullish-right";
    // CODE → addr:114 | <Call3>: <Reg8: 3, Reg8: 7, Reg8: 0, Reg8: 3, Reg8: 2>
    r3 = sideEffect(param1, param2).call(undefined, "nullish-right", param2)
    // CODE → addr:120 | <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = param2;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:123 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:129 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:134 | <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 4>
    console.log(r6, r5, r4)
    // CODE → addr:141 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:147 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:152 | <LoadConstString>: <Reg8: 1, string_id: 4632>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end";
    // CODE → addr:156 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end")
    // CODE → addr:161 | <Ret>: <Reg8: 0>
    return undefined;
}