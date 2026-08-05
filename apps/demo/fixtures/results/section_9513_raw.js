function callDefaultParameterTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4934>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start' (String)
    // USED → r6 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4935>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r8 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    r6 = globalThis.console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 15>
    // USED → r0 = 15;
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 7900>  # String: 'result' (Identifier)
    // USED → r9 = "result";
    // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 0>
    r6 = globalThis.console.log("result", 15)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    r6 = globalThis.console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 25>
    // USED → r0 = 25;
    // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 0>
    r6 = globalThis.console.log("result", 25)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    r6 = globalThis.console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 1414>  # String: 'sum' (String)
    // USED → r6 = "sum";
    // CODE → <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 0>
    r6 = globalThis.console.log("sum", 25)
    // CODE → <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
    // USED → r6 = getParentEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 0>
    // USED → r6 = getParentEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <Call1>: <Reg8: 4, Reg8: 6, Reg8: 3>
    r4 = getParentEnvironment(0)[0].call(undefined)
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    // USED → r1 = 4;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <Call4>: <Reg8: 4, Reg8: 6, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r4 = getParentEnvironment(0)[0].call(undefined, 2, 3, 4)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4933>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end' (String)
    // USED → r5 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end")
    // CODE → <Ret>: <Reg8: 3>
    return undefined;
}