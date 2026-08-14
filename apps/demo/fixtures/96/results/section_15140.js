function arrowFunctionTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4750>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/start' (String)
    // USED → r2 = "__BC:Functions/ArrowTests/arrowFunctionTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 5>
    // USED → r5 = 5;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
    console.log(r5)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 16>
    // USED → r2 = 16;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <NewArrayWithBuffer>: <Reg8: 4, UInt16: 4, UInt16: 4, UInt16: 20817>  # Array: [1, 2, 3, 4]
    r4 = [1, 2, 3, 4]
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 170>  # String: 'map' (Identifier)
    // USED → r3 = r4.map;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15141>  # Function: [#15141  of 12 bytes]: 2 params @ offset 0x00269c4e
    // USED → r2 = function_15141;
    // CODE → <Call2>: <Reg8: 4, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r4 = r4.map(r2);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15142>  # Function: [#15142 makeMultiplier of 16 bytes]: 2 params @ offset 0x0026a8a3
    // USED → r3 = makeMultiplier;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2>
    // USED → r2 = makeMultiplier.call(undefined, r2);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 5>
    // USED → r2 = makeMultiplier.call(undefined, r2).call(undefined, r5);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4749>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/end' (String)
    // USED → r1 = "__BC:Functions/ArrowTests/arrowFunctionTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}