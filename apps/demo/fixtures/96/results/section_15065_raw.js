function labeledBreakTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4615>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 28 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 30 | <Mov>: <Reg8: 5, Reg8: 1>
    // USED → r5 = 0;
    // CODE → addr: 33 | <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 35 | <Mov>: <Reg8: 7, Reg8: 6>
    // USED → r7 = 0;
    // CODE → addr: 38 | <JStrictNotEqual>: <Addr8: 8, Reg8: 5, Reg8: 2>  # Address: 0000002e
    if (r5 !== 1) goto label_46;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 42 | <JStrictEqual>: <Addr8: 37, Reg8: 7, Reg8: 2>  # Address: 0000004f
    if (r7 === 1) goto label_79;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 46 | <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 52 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 57 | <Call3>: <Reg8: 8, Reg8: 8, Reg8: 9, Reg8: 5, Reg8: 7>
    console.log(r5, r7)
    // CODE → addr: 63 | <Inc>: <Reg8: 6, Reg8: 7>
    r6 = r7 + 1
    // CODE → addr: 66 | <JLess>: <Addr8: -31, Reg8: 6, Reg8: 3>  # Address: 00000023
    // → r6 = r7 + 1
    if (r6 < 3) goto label_35;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 70 | <Inc>: <Reg8: 1, Reg8: 5>
    r1 = r5 + 1
    // CODE → addr: 73 | <JLess>: <Addr8: -43, Reg8: 1, Reg8: 3>  # Address: 0000001e
    // → r1 = r5 + 1
    if (r1 < 3) goto label_30;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 77 | <Jmp>: <Addr8: 22>  # Address: 00000063
    goto label_99;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 79 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 90 | <LoadConstString>: <Reg8: 1, string_id: 4608>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer";
    // CODE → addr: 94 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer")
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 0, string_id: 4610>  # String: '__BC:ControlFlow/LabeledTests/labeledBreakTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/labeledBreakTest/end";
    // CODE → addr:114 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end")
    // CODE → addr:119 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:121 | <Ret>: <Reg8: 0>
    return undefined;
}