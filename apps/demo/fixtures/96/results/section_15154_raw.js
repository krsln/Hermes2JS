function defaultParameterTest(param1) {
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
    // CODE → <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000026
    if (!(arguments.length > 1)) goto label_38;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
    // USED → r3 = arguments[1];
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = 10
    // CODE → <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000026
    // → r3 = arguments[1]
    if (r3 === undefined) goto label_38;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
    // USED → r5 = arguments[1];
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
    // CODE → <JmpFalse>: <Addr8: 18, Reg8: 3>  # Address: 00000049
    if (!(arguments.length > 2)) goto label_73;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetArgumentsPropByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
    // USED → r3 = arguments[2];
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    r4 = "result"
    // CODE → <JStrictEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000049
    // → r3 = arguments[2]
    if (r3 === undefined) goto label_73;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetArgumentsPropByVal>: <Reg8: 4, Reg8: 1, Reg8: 2>
    // USED → r4 = arguments[2];
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r2 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <Add>: <Reg8: 1, Reg8: 1, Reg8: 5>
    // USED → r1 = param1 + arguments[1];
    // CODE → <Call3>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log(r4, r1)
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}