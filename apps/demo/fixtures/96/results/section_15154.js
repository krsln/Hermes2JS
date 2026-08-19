function defaultParameterTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → addr:  4 | <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
    // USED → r3 = arguments.length;
    // CODE → addr:  7 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → addr: 10 | <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
    // USED → r3 = arguments.length > 1;
    // CODE → addr: 14 | <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
    // USED → r4 = 10;
    // CODE → addr: 17 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = !(arguments.length > 1 && r3 !== undefined) ? 10 : arguments[1]
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 38 | <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
    // USED → r3 = arguments.length;
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → addr: 44 | <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
    // USED → r3 = arguments.length > 2;
    // CODE → addr: 48 | <LoadConstString>: <Reg8: 6, string_id: 7363>  # String: 'result' (Identifier)
    // USED → r6 = "result";
    // CODE → addr: 52 | <Mov>: <Reg8: 4, Reg8: 6>
    r4 = !(arguments.length > 2 && r3 !== undefined) ? "result" : arguments[2]
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 73 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 75 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 86 | <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r2 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → addr: 90 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → addr: 95 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:106 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:109 | <Add>: <Reg8: 1, Reg8: 1, Reg8: 5>
    // USED → r1 = param1 + (!(arguments.length > 1 && r3 !== undefined) ? 10 : arguments[1]);
    // CODE → addr:113 | <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log(r4, r1)
    // CODE → addr:119 | <Ret>: <Reg8: 0>
    return undefined;
}