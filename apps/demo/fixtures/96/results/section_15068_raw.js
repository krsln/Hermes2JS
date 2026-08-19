function tripleNestedLabeledTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4622>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
    // USED → r5 = 2;
    // CODE → addr: 28 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 31 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → addr: 33 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 35 | <Mov>: <Reg8: 10, Reg8: 2>
    // USED → r10 = 0;
    // CODE → addr: 38 | <Mov>: <Reg8: 8, Reg8: 1>
    r8 = 0
    // CODE → addr: 41 | <LoadConstZero>: <Reg8: 9>
    // USED → r9 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 43 | <Mov>: <Reg8: 13, Reg8: 10>
    r13 = 0
    // CODE → addr: 46 | <Mov>: <Reg8: 11, Reg8: 9>
    r11 = 0
    // CODE → addr: 49 | <LoadConstZero>: <Reg8: 12>
    // USED → r12 = 0;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 51 | <Inc>: <Reg8: 4, Reg8: 13>
    // USED → r4 = r13 + 1;
    // CODE → addr: 54 | <Mov>: <Reg8: 14, Reg8: 12>
    r14 = 0
    // CODE → addr: 57 | <JStrictEqual>: <Addr8: 22, Reg8: 14, Reg8: 3>  # Address: 0000004f
    // → r14 = 0
    if (r14 === 1) goto label_79;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 61 | <JStrictNotEqual>: <Addr8: 8, Reg8: 8, Reg8: 5>  # Address: 00000045
    if (r8 !== 2) goto label_69;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 65 | <JStrictEqual>: <Addr8: 34, Reg8: 11, Reg8: 5>  # Address: 00000063
    if (r11 === 2) goto label_99;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 69 | <Inc>: <Reg8: 12, Reg8: 14>
    r12 = r14 + 1
    // CODE → addr: 72 | <Mov>: <Reg8: 13, Reg8: 4>
    r13 = r13 + 1
    // CODE → addr: 75 | <JLess>: <Addr8: -24, Reg8: 12, Reg8: 6>  # Address: 00000033
    // → r12 = r14 + 1
    if (r12 < 3) goto label_51;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 79 | <Inc>: <Reg8: 9, Reg8: 11>
    r9 = r11 + 1
    // CODE → addr: 82 | <Mov>: <Reg8: 10, Reg8: 4>
    r10 = r13 + 1
    // CODE → addr: 85 | <JLess>: <Addr8: -42, Reg8: 9, Reg8: 6>  # Address: 0000002b
    // → r9 = r11 + 1
    if (r9 < 3) goto label_43;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 89 | <Inc>: <Reg8: 1, Reg8: 8>
    r1 = r8 + 1
    // CODE → addr: 92 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r13 + 1
    // CODE → addr: 95 | <JLess>: <Addr8: -60, Reg8: 1, Reg8: 6>  # Address: 00000023
    // → r1 = r8 + 1
    if (r1 < 3) goto label_35;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr: 99 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:110 | <LoadConstString>: <Reg8: 1, string_id: 4620>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits' (String)
    // USED → r1 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits";
    // CODE → addr:114 | <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 4>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", r4)
    // CODE → addr:120 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:126 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:131 | <LoadConstString>: <Reg8: 0, string_id: 4284>  # String: '__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end";
    // CODE → addr:135 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end")
    // CODE → addr:140 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:142 | <Ret>: <Reg8: 0>
    return undefined;
}