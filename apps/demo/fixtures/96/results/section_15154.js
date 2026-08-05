function defaultParameterTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
    // USED → r3 = arguments.length;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
    // USED → r3 = arguments.length > 1;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
    // USED → r4 = 10;
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 10
    if (arguments.length > 1 && r3 !== r0) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
        // USED → r5 = arguments[1];
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetArgumentsLength>: <Reg8: 3, Reg8: 2>
    // USED → r3 = arguments.length;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <Greater>: <Reg8: 3, Reg8: 3, Reg8: 1>
    // USED → r3 = arguments.length > 2;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 7363>  # String: 'result' (Identifier)
    // USED → r6 = "result";
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    r4 = "result"
    if (arguments.length > 2 && r3 !== r0) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <GetArgumentsPropByVal>: <Reg8: 4, Reg8: 1, Reg8: 2>
        // USED → r4 = arguments[2];
    }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r2 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <Add>: <Reg8: 1, Reg8: 1, Reg8: 5>
    // USED → r1 = param1 + arguments[1];
    // CODE → <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1>
    r1 = globalThis.console.log(arguments[2], param1 + arguments[1])
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}