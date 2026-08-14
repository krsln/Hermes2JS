function logicalShortCircuitTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 7, Reg8: 0, function_id: 15073>  # Function: [#15073 sideEffect of 31 bytes]: 3 params @ offset 0x00268778
    // USED → r7 = sideEffect(param1, param2);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4635>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start' (String)
    // USED → r0 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 4, Reg8: 5, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5116>  # String: 'and-left' (String)
    // USED → r4 = "and-left";
    // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 3>
    r4 = sideEffect(param1, param2).call(undefined, "and-left", r3)
    // CODE → <Mov>: <Reg8: 6, Reg8: 3>
    r6 = param1
    // CODE → <JmpFalse>: <Addr8: 16, Reg8: 3>  # Address: 00000042
    if (!param1) goto label_66;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5117>  # String: 'and-right' (String)
    // USED → r4 = "and-right";
    // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 2>
    r4 = sideEffect(param1, param2).call(undefined, "and-right", r2)
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = param2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1184>  # String: 'or-left' (String)
    // USED → r4 = "or-left";
    // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 3>
    r4 = sideEffect(param1, param2).call(undefined, "or-left", r3)
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = param1;
    // CODE → <JmpTrue>: <Addr8: 16, Reg8: 5>  # Address: 0000005f
    if (param1) goto label_95;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1951>  # String: 'or-right' (String)
    // USED → r4 = "or-right";
    // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 0, Reg8: 4, Reg8: 2>
    r4 = sideEffect(param1, param2).call(undefined, "or-right", r2)
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = param2;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 74>  # String: 'left' (Identifier)
    r4 = "left"
    // CODE → <JmpFalse>: <Addr8: 5, Reg8: 3>  # Address: 00000068
    if (!param1) goto label_104;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 3>
    // USED → r3 = null;
    // CODE → <JNotEqual>: <Addr8: 17, Reg8: 4, Reg8: 3>  # Address: 0000007b
    if (null != null) goto label_123;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3574>  # String: 'nullish-right' (String)
    // USED → r3 = "nullish-right";
    // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 0, Reg8: 3, Reg8: 2>
    r3 = sideEffect(param1, param2).call(undefined, "nullish-right", r2)
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = param2;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 4>
    console.log(r6, r5, r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4632>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}