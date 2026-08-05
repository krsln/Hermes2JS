function doWhileTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4755>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/start' (String)
    // USED → r6 = "__BC:ControlFlow/DoWhileTests/doWhileTest/start";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 5>
    r2 = 5
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 0>
    r6 = globalThis.console.log(0)
    // CODE → <AddN>: <Reg8: 0, Reg8: 0, Reg8: 1>
    r0 = 0 + 1
    if (r0 >= r2) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r7 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r6 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 4281>  # String: '__BC:ControlFlow/DoWhileTests/doWhileTest/end' (String)
        // USED → r5 = "__BC:ControlFlow/DoWhileTests/doWhileTest/end";
        // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
        r5 = globalThis.console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/end")
        // CODE → <LoadConstUndefined>: <Reg8: 4>
        // USED → r4 = undefined;
        // CODE → <Ret>: <Reg8: 4>
        return undefined;
    }
}