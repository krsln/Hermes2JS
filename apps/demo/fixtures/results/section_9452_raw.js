function nestedLoopTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 11, string_id: 4806>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/start' (String)
    // USED → r11 = "__BC:ControlFlow/NestedTests/nestedLoopTest/start";
    // CODE → <Call2>: <Reg8: 11, Reg8: 12, Reg8: 13, Reg8: 11>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 4>
    // USED → r7 = 4;
    // CODE → <LoadConstString>: <Reg8: 12, string_id: 2611>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if' (String)
    // USED → r12 = "__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if";
    // CODE → <LoadConstString>: <Reg8: 11, string_id: 1491>  # String: 'nested' (String)
    // USED → r11 = "nested";
    // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 2>
    // USED → r8 = 2;
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 4, Reg8: 3>
    // USED → r4 = 0;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = 0;
    // CODE → <JStrictNotEqual>: <Addr8: 40, Reg8: 4, Reg8: 2>  # Address: 0000005c
    if (0 !== 1) goto label_92;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <JStrictNotEqual>: <Addr8: 36, Reg8: 1, Reg8: 8>  # Address: 0000005c
    if (0 !== 2) goto label_92;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 12>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if")
    // CODE → <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 11>
    console.log("nested")
    // ──────────────── Block 5 ──────────────── 
    // CODE → <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
    // USED → r0 = 0 + 1;
    // CODE → <JLessN>: <Addr8: -47, Reg8: 0, Reg8: 7>  # Address: 00000031
    if (0 + 1 < 4) goto label_49;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <AddN>: <Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r3 = 0 + 1;
    // CODE → <JLessN>: <Addr8: -60, Reg8: 3, Reg8: 6>  # Address: 0000002c
    if (0 + 1 < 3) goto label_44;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 4805>  # String: '__BC:ControlFlow/NestedTests/nestedLoopTest/end' (String)
    // USED → r10 = "__BC:ControlFlow/NestedTests/nestedLoopTest/end";
    // CODE → <Call2>: <Reg8: 10, Reg8: 11, Reg8: 12, Reg8: 10>
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    // USED → r9 = undefined;
    // CODE → <Ret>: <Reg8: 9>
    return undefined;
}