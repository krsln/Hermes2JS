function labeledBlockBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4606>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 1, string_id: 2099>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break";
    // CODE → addr: 37 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 21>  # String: 'Math' (Identifier)
    // USED → r2 = Math;
    // CODE → addr: 48 | <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 9292>  # String: 'random' (Identifier)
    // USED → r1 = Math.random;
    // CODE → addr: 54 | <Call1>: <Reg8: 2, Reg8: 1, Reg8: 2>
    r2 = Math.random()
    // CODE → addr: 58 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // → r2 = Math.random()
    if (r2 >= 2) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 65 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 71 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 76 | <LoadConstString>: <Reg8: 1, string_id: 4607>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable' (String)
        // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable";
        // CODE → addr: 80 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable")
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 85 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 96 | <LoadConstString>: <Reg8: 0, string_id: 4604>  # String: '__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end";
    // CODE → addr:100 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end")
    // CODE → addr:105 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:107 | <Ret>: <Reg8: 0>
    return undefined;
}