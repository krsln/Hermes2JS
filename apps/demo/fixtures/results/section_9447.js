function whileTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4822>  # String: '__BC:ControlFlow/WhileTests/whileTest/start' (String)
    // USED → r8 = "__BC:ControlFlow/WhileTests/whileTest/start";
    // CODE → <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    r8 = globalThis.console.log("__BC:ControlFlow/WhileTests/whileTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 5>
    // USED → r4 = 5;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4821>  # String: '__BC:ControlFlow/WhileTests/whileTest/if-continue' (String)
    // USED → r9 = "__BC:ControlFlow/WhileTests/whileTest/if-continue";
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 2495>  # String: 'while' (String)
    // USED → r8 = "while";
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
    // USED → r5 = 2;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // LOOP → START (while)
    while (0 === 2) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r11 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r10 = globalThis.console.log;
        // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 1>
        r10 = globalThis.console.log("while", 0)
        // CODE → <Mov>: <Reg8: 2, Reg8: 1>
        // USED → r2 = 0;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <AddN>: <Reg8: 0, Reg8: 2, Reg8: 3>
        r0 = 0 + 1
        // CODE → <Jmp>: <Addr8: 22>  # Address: 0000005b
        goto label_91;
        // ──────────────── Block 3 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r11 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r10 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 9>
        r10 = globalThis.console.log("__BC:ControlFlow/WhileTests/whileTest/if-continue")
        // CODE → <AddN>: <Reg8: 0, Reg8: 2, Reg8: 3>
        // USED → r0 = 0 + 1;
        // ──────────────── Block 4 ──────────────── 
        // CODE → <Mov>: <Reg8: 1, Reg8: 0>
        // USED → r1 = 0 + 1;
        // CODE → <JLessN>: <Addr8: -53, Reg8: 1, Reg8: 4>  # Address: 00000029
        if (0 + 1 < 5) goto label_41;
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4819>  # String: '__BC:ControlFlow/WhileTests/whileTest/end' (String)
    // USED → r7 = "__BC:ControlFlow/WhileTests/whileTest/end";
    // CODE → <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    r7 = globalThis.console.log("__BC:ControlFlow/WhileTests/whileTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined;
    // CODE → <Ret>: <Reg8: 6>
    return undefined;
}