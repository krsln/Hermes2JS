function forEachTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 4760>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/start' (String)
    // USED → r2 = "__BC:ControlFlow/ForEachTests/forEachTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 4, UInt16: 4, UInt16: 4, UInt16: 48446>  # Array: [10, 20, 30, 40]
    r4 = [10, 20, 30, 40]
    // CODE → addr: 30 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 148>  # String: 'forEach' (Identifier)
    // USED → r3 = r4.forEach;
    // CODE → addr: 35 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 12470>  # Function: [#12470  of 78 bytes]: 3 params @ offset 0x00243d9b
    // USED → r2 = function_12470(param1, param2);
    // CODE → addr: 42 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r4.forEach(function_12470(param1, param2))
    // CODE → addr: 47 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 53 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 58 | <LoadConstString>: <Reg8: 1, string_id: 4756>  # String: '__BC:ControlFlow/ForEachTests/forEachTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/ForEachTests/forEachTest/end";
    // CODE → addr: 62 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/end")
    // CODE → addr: 67 | <Ret>: <Reg8: 0>
    return r0;
}