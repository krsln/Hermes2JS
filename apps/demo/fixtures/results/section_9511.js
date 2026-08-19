function defaultParameterTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED → r6 = (param2 !== undefined) ? param2 : 10;
    // CODE → addr:  3 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 12 | <LoadParam>: <Reg8: 5, UInt8: 3>
    // USED → r5 = (param3 !== undefined) ? param3 : "result";
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 23 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr: 26 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr: 28 | <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr: 34 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 39 | <LoadConstString>: <Reg8: 4, string_id: 4935>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r4 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → addr: 43 | <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → addr: 48 | <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 54 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 59 | <Add>: <Reg8: 2, Reg8: 2, Reg8: 6>
    // USED → r2 = param1 + ((param2 !== undefined) ? param2 : 10);
    // CODE → addr: 63 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 2>
    console.log((param3 !== undefined) ? param3 : "result", r2)
    // CODE → addr: 69 | <Ret>: <Reg8: 1>
    return undefined;
}