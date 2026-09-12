function arrowFunctionTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  4 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 15 | <LoadConstString>: <Reg8: 2, string_id: 4750>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/start' (String)
    // USED → r2 = "__BC:Functions/ArrowTests/arrowFunctionTest/start";
    // CODE → addr: 19 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/start")
    // CODE → addr: 24 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 30 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 5, UInt8: 5>
    // USED → r5 = 5;
    // CODE → addr: 38 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
    console.log(5)
    // CODE → addr: 43 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 54 | <LoadConstUInt8>: <Reg8: 2, UInt8: 16>
    // USED → r2 = 16;
    // CODE → addr: 57 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(16)
    // CODE → addr: 62 | <NewArrayWithBuffer>: <Reg8: 4, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    r4 = [1, 2, 3, 4]
    // CODE → addr: 70 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 170>  # String: 'map' (Identifier)
    // USED → r3 = r4.map;
    // CODE → addr: 75 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15141>  # Function: [#15141  of 12 bytes]: 2 params @ offset 0x00269c4e
    // USED → r2 = function_15141(param1);
    // CODE → addr: 80 | <Call2>: <Reg8: 4, Reg8: 3, Reg8: 4, Reg8: 2>
    r4 = r4.map(function_15141(param1))
    // CODE → addr: 85 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 96 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr:101 | <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15142>  # Function: [#15142 makeMultiplier of 16 bytes]: 2 params @ offset 0x0026a8a3
    // USED → r3 = makeMultiplier(param1);
    // CODE → addr:106 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:108 | <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → addr:111 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2>
    r2 = makeMultiplier(param1).call(undefined, 3)
    // CODE → addr:116 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:122 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:127 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 5>
    r2 = r2.call(undefined, 5)
    // CODE → addr:132 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:137 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:143 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:148 | <LoadConstString>: <Reg8: 1, string_id: 4749>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/end' (String)
    // USED → r1 = "__BC:Functions/ArrowTests/arrowFunctionTest/end";
    // CODE → addr:152 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/end")
    // CODE → addr:157 | <Ret>: <Reg8: 0>
    return r0;
}