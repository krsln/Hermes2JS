function switchTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 4808>  # String: '__BC:ControlFlow/SwitchTests/switchTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/start")
    // CODE → addr: 22 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 27 | <JStrictEqualLong>: <Addr32: 139, Reg8: 0, Reg8: 2>  # Address: 000000a6
    if (0 === param1) goto label_166;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 34 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr: 37 | <JStrictEqual>: <Addr8: 103, Reg8: 0, Reg8: 2>  # Address: 0000008c
    if (1 === param1) goto label_140;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr: 44 | <JStrictEqual>: <Addr8: 70, Reg8: 0, Reg8: 2>  # Address: 00000072
    if (2 === param1) goto label_114;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 48 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr: 51 | <JStrictEqual>: <Addr8: 37, Reg8: 0, Reg8: 2>  # Address: 00000058
    if (3 === param1) goto label_88;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 55 | <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → addr: 58 | <JStrictEqual>: <Addr8: 30, Reg8: 0, Reg8: 2>  # Address: 00000058
    if (4 === param1) goto label_88;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 62 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 68 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 73 | <LoadConstString>: <Reg8: 2, string_id: 3462>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-default' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-default";
    // CODE → addr: 77 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default")
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 2, string_id: 1861>  # String: 'other' (String)
    r2 = "other"
    // CODE → addr: 86 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 88 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 94 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 99 | <LoadConstString>: <Reg8: 2, string_id: 1730>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-3-4' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-3-4";
    // CODE → addr:103 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4")
    // CODE → addr:108 | <LoadConstString>: <Reg8: 2, string_id: 3949>  # String: 'three-four' (String)
    r2 = "three-four"
    // CODE → addr:112 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:114 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:120 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:125 | <LoadConstString>: <Reg8: 2, string_id: 919>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-2' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-2";
    // CODE → addr:129 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2")
    // CODE → addr:134 | <LoadConstString>: <Reg8: 2, string_id: 9241>  # String: 'two' (Identifier)
    r2 = "two"
    // CODE → addr:138 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:140 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:146 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:151 | <LoadConstString>: <Reg8: 2, string_id: 2021>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-1' (String)
    // USED → r2 = "__BC:ControlFlow/SwitchTests/switchTest/case-1";
    // CODE → addr:155 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1")
    // CODE → addr:160 | <LoadConstString>: <Reg8: 2, string_id: 6956>  # String: 'one' (Identifier)
    r2 = "one"
    // CODE → addr:164 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:166 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:172 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:177 | <LoadConstString>: <Reg8: 1, string_id: 4807>  # String: '__BC:ControlFlow/SwitchTests/switchTest/case-0' (String)
    // USED → r1 = "__BC:ControlFlow/SwitchTests/switchTest/case-0";
    // CODE → addr:181 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0")
    // CODE → addr:186 | <LoadConstString>: <Reg8: 1, string_id: 597>  # String: 'zero' (String)
    r1 = "zero"
    // CODE → addr:190 | <Ret>: <Reg8: 1>
    return r1;
}