function switchTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4808>  # String: '__BC:ControlFlow/SwitchTests/switchTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/start")
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    r2 = param1
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <JStrictEqualLong>: <Addr32: 139, Reg8: 0, Reg8: 2>  # Address: 000000a6
    if (0 === r2) goto label_166;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <JStrictEqual>: <Addr8: 103, Reg8: 0, Reg8: 2>  # Address: 0000008c
    if (1 === r2) goto label_140;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <JStrictEqual>: <Addr8: 70, Reg8: 0, Reg8: 2>  # Address: 00000072
    if (2 === r2) goto label_114;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → <JStrictEqual>: <Addr8: 37, Reg8: 0, Reg8: 2>  # Address: 00000058
    if (3 === r2) goto label_88;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → <JStrictEqual>: <Addr8: 30, Reg8: 0, Reg8: 2>  # Address: 00000058
    if (4 === r2) goto label_88;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 3462>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-default' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-default";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default")
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1861>  # String: 'other' (String)
    // USED → r2 = "other";
    // CODE → <Ret>: <Reg8: 2>
    return "other";
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1730>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-3-4' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-3-4";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4")
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 3949>  # String: 'three-four' (String)
    // USED → r2 = "three-four";
    // CODE → <Ret>: <Reg8: 2>
    return "three-four";
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 919>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-2' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-2";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2")
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 9241>  # String: 'two' (Identifier)
    // USED → r2 = "two";
    // CODE → <Ret>: <Reg8: 2>
    return "two";
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2021>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-1' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-1";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1")
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 6956>  # String: 'one' (Identifier)
    // USED → r2 = "one";
    // CODE → <Ret>: <Reg8: 2>
    return "one";
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4807>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-0' (String)
    // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-0";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0")
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 597>  # String: 'zero' (String)
    // USED → r1 = "zero";
    // CODE → <Ret>: <Reg8: 1>
    return "zero";
}