function forEachTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4582>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 3, UInt16: 4, UInt16: 4, UInt16: 23599>  # Array: [10, 20, 30, 40]
    r3 = [10, 20, 30, 40]
    // CODE → addr: 30 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 144>  # String: 'forEach' (Identifier)
    // USED → r2 = r3.forEach;
    // CODE → addr: 35 | <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15054>  # Function: [#15054  of 78 bytes]: 3 params @ offset 0x00267dd1
    // USED → r1 = function_15054(param1, param2);
    // CODE → addr: 42 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = r3.forEach(function_15054(param1, param2))
    // CODE → addr: 47 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 53 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr: 58 | <LoadConstString>: <Reg8: 0, string_id: 4578>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ForEachTests/forEachTest/end";
    // CODE → addr: 62 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/end")
    // CODE → addr: 67 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 69 | <Ret>: <Reg8: 0>
    return r0;
}