function labeledBlockBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4780>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 3, string_id: 3618>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break";
    // CODE → addr: 37 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 2, string_id: 19>  # String: 'Math' (Identifier)
    // USED → r4 = Math;
    // CODE → addr: 48 | <GetById>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 7174>  # String: 'random' (Identifier)
    // USED → r3 = Math.random;
    // CODE → addr: 54 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 4>
    r3 = Math.random()
    // CODE → addr: 58 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr: 61 | <JLess>: <Addr8: 24, Reg8: 3, Reg8: 0>  # Address: 00000055
    // → r3 = Math.random()
    if (r3 < 2) goto label_85;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 65 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 76 | <LoadConstString>: <Reg8: 3, string_id: 3146>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable";
    // CODE → addr: 80 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable")
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 85 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 96 | <LoadConstString>: <Reg8: 2, string_id: 4778>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end";
    // CODE → addr:100 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end")
    // CODE → addr:105 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr:107 | <Ret>: <Reg8: 1>
    return undefined;
}