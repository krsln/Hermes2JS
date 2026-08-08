function forEachTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4582>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 4, UInt16: 4, UInt16: 23599>  # Array: [10, 20, 30, 40]
    r3 = [10, 20, 30, 40]
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 144>  # String: 'forEach' (Identifier)
    // USED → r2 = r3.forEach;
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15054>  # Function: [#15054  of 78 bytes]: 3 params @ offset 0x00267dd1
    // USED → r1 = function_15054;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = r3.forEach(function_15054)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4578>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ForEachTests/forEachTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/ForEachTests/forEachTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}