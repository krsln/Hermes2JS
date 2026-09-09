function whileTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 8, string_id: 4822>  # String: '__BC:ControlFlow/WhileTests/whileTest/start' (String)
    // USED → r8 = "__BC:ControlFlow/WhileTests/whileTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:ControlFlow/WhileTests/whileTest/start")
    // CODE → addr: 22 | <LoadConstUInt8>: <Reg8: 4, UInt8: 5>
    // USED → r4 = 5;
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 9, string_id: 4821>  # String: '__BC:ControlFlow/WhileTests/whileTest/if-continue' (String)
    // USED → r9 = "__BC:ControlFlow/WhileTests/whileTest/if-continue";
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 8, string_id: 2495>  # String: 'while' (String)
    // USED → r8 = "while";
    // CODE → addr: 36 | <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
    // USED → r5 = 2;
    // CODE → addr: 39 | <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 41 | <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr: 47 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 52 | <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 1>
    console.log("while", r1)
    // CODE → addr: 58 | <Mov>: <Reg8: 2, Reg8: 1>
    r2 = r1
    // CODE → addr: 61 | <JStrictEqual>: <Addr8: 10, Reg8: 2, Reg8: 5>  # Address: 00000047
    // → r2 = r1
    if (r2 === 2) goto label_71;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 65 | <AddN>: <Reg8: 0, Reg8: 2, Reg8: 3>
    r0 = r2 + 1
    // CODE → addr: 69 | <Jmp>: <Addr8: 22>  # Address: 0000005b
    goto label_91;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 71 | <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 82 | <Call2>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:ControlFlow/WhileTests/whileTest/if-continue")
    // CODE → addr: 87 | <AddN>: <Reg8: 0, Reg8: 2, Reg8: 3>
    r0 = r2 + 1
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 91 | <Mov>: <Reg8: 1, Reg8: 0>
    r1 = r0
    // CODE → addr: 94 | <JLessN>: <Addr8: -53, Reg8: 1, Reg8: 4>  # Address: 00000029
    // → r1 = r0
    if (r1 < 5) goto label_41;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 98 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr:104 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:109 | <LoadConstString>: <Reg8: 7, string_id: 4819>  # String: '__BC:ControlFlow/WhileTests/whileTest/end' (String)
    // USED → r7 = "__BC:ControlFlow/WhileTests/whileTest/end";
    // CODE → addr:113 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:ControlFlow/WhileTests/whileTest/end")
    // CODE → addr:118 | <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → addr:120 | <Ret>: <Reg8: 6>
    return r6;
}