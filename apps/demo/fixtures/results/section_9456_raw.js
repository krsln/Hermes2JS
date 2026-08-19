function labeledBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 9, string_id: 4789>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 28 | <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 30 | <Mov>: <Reg8: 2, Reg8: 4>
    // USED → r2 = 0;
    // CODE → addr: 33 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 35 | <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = 0;
    // CODE → addr: 38 | <JStrictNotEqual>: <Addr8: 8, Reg8: 2, Reg8: 3>  # Address: 0000002e
    if (r2 !== 1) goto label_46;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 42 | <JStrictEqual>: <Addr8: 39, Reg8: 1, Reg8: 3>  # Address: 00000051
    if (r1 === 1) goto label_81;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 46 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr: 52 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr: 57 | <Call3>: <Reg8: 9, Reg8: 9, Reg8: 10, Reg8: 2, Reg8: 1>
    console.log(r2, r1)
    // CODE → addr: 63 | <AddN>: <Reg8: 0, Reg8: 1, Reg8: 3>
    r0 = r1 + 1
    // CODE → addr: 67 | <JLessN>: <Addr8: -32, Reg8: 0, Reg8: 6>  # Address: 00000023
    // → r0 = r1 + 1
    if (r0 < 3) goto label_35;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 71 | <AddN>: <Reg8: 4, Reg8: 2, Reg8: 3>
    r4 = r2 + 1
    // CODE → addr: 75 | <JLessN>: <Addr8: -45, Reg8: 4, Reg8: 6>  # Address: 0000001e
    // → r4 = r2 + 1
    if (r4 < 3) goto label_30;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 79 | <Jmp>: <Addr8: 22>  # Address: 00000065
    goto label_101;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 81 | <TryGetById>: <Reg8: 11, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr: 87 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 92 | <LoadConstString>: <Reg8: 9, string_id: 4783>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
    // USED → r9 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
    // CODE → addr: 96 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:101 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:107 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:112 | <LoadConstString>: <Reg8: 8, string_id: 4784>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r8 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → addr:116 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → addr:121 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:123 | <Ret>: <Reg8: 7>
    return undefined;
}