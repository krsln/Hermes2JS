function forEachTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4538>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 4, UInt16: 4, UInt16: 23471>  # Array: [10, 20, 30, 40]
    // USED → r3 = [10, 20, 30, 40];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 144>  # String: 'forEach' (Identifier)
    // USED → r2 = [10, 20, 30, 40].forEach;
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15051>  # Function: [#15051  of 78 bytes]: 3 params @ offset 0x00264552
    // USED → r1 = function_15051;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = [10, 20, 30, 40].forEach(function_15051)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4536>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ForEachTests/forEachTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}