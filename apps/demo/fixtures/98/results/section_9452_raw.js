function nestedLoopTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 11, string_id: 4806>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/start' (String)
    // USED → r11 = "__BC:ControlFlow/NestedTests/nestedLoopTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 11, Reg8: 12, Reg8: 13, Reg8: 11>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 28 | <LoadConstUInt8>: <Reg8: 7, UInt8: 4>
    // USED → r7 = 4;
    // CODE → addr: 31 | <LoadConstString>: <Reg8: 12, string_id: 2611>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if' (String)
    // USED → r12 = "__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if";
    // CODE → addr: 35 | <LoadConstString>: <Reg8: 11, string_id: 1491>  # String: 'nested' (String)
    // USED → r11 = "nested";
    // CODE → addr: 39 | <LoadConstUInt8>: <Reg8: 8, UInt8: 2>
    // USED → r8 = 2;
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 44 | <Mov>: <Reg8: 4, Reg8: 3>
    r4 = 0
    // CODE → addr: 47 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <Mov>: <Reg8: 1, Reg8: 0>
    r1 = 0
    // CODE → addr: 52 | <JStrictNotEqual>: <Addr8: 40, Reg8: 4, Reg8: 2>  # Address: 0000005c
    if (r4 !== 1) goto label_92;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 56 | <JStrictNotEqual>: <Addr8: 36, Reg8: 1, Reg8: 8>  # Address: 0000005c
    if (r1 !== 2) goto label_92;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 60 | <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = console.log;
    // CODE → addr: 71 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 12>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if")
    // CODE → addr: 76 | <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = console;
    // CODE → addr: 82 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = console.log;
    // CODE → addr: 87 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 11>
    console.log("nested")
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 92 | <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
    r0 = r1 + 1
    // CODE → addr: 96 | <JLessN>: <Addr8: -47, Reg8: 0, Reg8: 7>  # Address: 00000031
    // → r0 = r1 + 1
    if (r0 < 4) goto label_49;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:100 | <AddN>: <Reg8: 3, Reg8: 4, Reg8: 2>
    r3 = r4 + 1
    // CODE → addr:104 | <JLessN>: <Addr8: -60, Reg8: 3, Reg8: 6>  # Address: 0000002c
    // → r3 = r4 + 1
    if (r3 < 3) goto label_44;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:108 | <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = console;
    // CODE → addr:114 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = console.log;
    // CODE → addr:119 | <LoadConstString>: <Reg8: 10, string_id: 4805>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/end' (String)
    // USED → r10 = "__BC:ControlFlow/NestedTests/nestedLoopTest/end";
    // CODE → addr:123 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 12, Reg8: 10>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/end")
    // CODE → addr:128 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:130 | <Ret>: <Reg8: 9>
    return r9;
}