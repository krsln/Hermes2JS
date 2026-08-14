function labeledBlockBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4606>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2099>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 21>  # String: 'Math' (Identifier)
    // USED → r2 = globalThis.Math;
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 9292>  # String: 'random' (Identifier)
    // USED → r1 = globalThis.Math.random;
    // CODE → <Call1>: <Reg8: 2, Reg8: 1, Reg8: 2>
    // USED → r2 = globalThis.Math.random();
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // → r2 = globalThis.Math.random()
    if (r2 >= 2) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4607>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable' (String)
        // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable")
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4604>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}