function nestedLoopTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4627>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/NestedTests/nestedLoopTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
    // USED → r7 = 3;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 6, UInt8: 4>
    // USED → r6 = 4;
    // CODE → addr: 28 | <LoadConstString>: <Reg8: 5, string_id: 4623>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if' (String)
    // USED → r5 = "__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if";
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 4, string_id: 1516>  # String: 'nested' (String)
    // USED → r4 = "nested";
    // CODE → addr: 36 | <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → addr: 39 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 44 | <Mov>: <Reg8: 9, Reg8: 1>
    r9 = 0
    // CODE → addr: 47 | <LoadConstZero>: <Reg8: 10>
    // USED → r10 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <Mov>: <Reg8: 11, Reg8: 10>
    r11 = 0
    // CODE → addr: 52 | <JStrictNotEqual>: <Addr8: 40, Reg8: 9, Reg8: 2>  # Address: 0000005c
    if (r9 !== 1) goto label_92;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 56 | <JStrictNotEqual>: <Addr8: 36, Reg8: 11, Reg8: 3>  # Address: 0000005c
    if (r11 !== 2) goto label_92;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 60 | <TryGetById>: <Reg8: 13, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr: 71 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 5>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if")
    // CODE → addr: 76 | <TryGetById>: <Reg8: 13, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr: 82 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr: 87 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 4>
    console.log("nested")
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 92 | <Inc>: <Reg8: 10, Reg8: 11>
    r10 = r11 + 1
    // CODE → addr: 95 | <JLess>: <Addr8: -46, Reg8: 10, Reg8: 6>  # Address: 00000031
    // → r10 = r11 + 1
    if (r10 < 4) goto label_49;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 99 | <Inc>: <Reg8: 1, Reg8: 9>
    r1 = r9 + 1
    // CODE → addr:102 | <JLess>: <Addr8: -58, Reg8: 1, Reg8: 7>  # Address: 0000002c
    // → r1 = r9 + 1
    if (r1 < 3) goto label_44;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:106 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:112 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:117 | <LoadConstString>: <Reg8: 0, string_id: 4625>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/NestedTests/nestedLoopTest/end";
    // CODE → addr:121 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/end")
    // CODE → addr:126 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:128 | <Ret>: <Reg8: 0>
    return r0;
}