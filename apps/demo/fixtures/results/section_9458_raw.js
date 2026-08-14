function labeledBlockBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4780>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3618>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 2, string_id: 19>  # String: 'Math' (Identifier)
    // USED → r4 = globalThis.Math;
    // CODE → <GetById>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 7174>  # String: 'random' (Identifier)
    // USED → r3 = globalThis.Math.random;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = globalThis.Math.random();
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <JLess>: <Addr8: 24, Reg8: 3, Reg8: 0>  # Address: 00000055
    // → r3 = globalThis.Math.random()
    if (r3 < 2) goto label_85;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3146>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable' (String)
    // USED → r3 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable")
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4778>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}