function forEachTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4716>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/ForEachTests/forEachTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 4, UInt16: 4, UInt16: 4, UInt16: 48382>  # Array: [10, 20, 30, 40]
    // USED → r4 = [10, 20, 30, 40];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 147>  # String: 'forEach' (Identifier)
    // USED → r3 = [10, 20, 30, 40].forEach;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 12396>  # Function: [#12396  of 78 bytes]: 3 params @ offset 0x0023e336
    // USED → r2 = function_12396;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = [10, 20, 30, 40].forEach(function_12396)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4711>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}