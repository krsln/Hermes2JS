function defaultParameterTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED → r6 = param2;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <JStrictNotEqual>: <Addr8: 7, Reg8: 6, Reg8: 1>  # Address: 0000000c
    if (param2 !== undefined) goto label_12;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 10>
    // USED → r6 = 10;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 3>
    // USED → r5 = param3;
    // CODE → <JStrictNotEqual>: <Addr8: 8, Reg8: 5, Reg8: 1>  # Address: 00000017
    if (param3 !== undefined) goto label_23;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 7900>  # String: 'result' (Identifier)
    // USED → r5 = "result";
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4935>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r4 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 6>
    // USED → r2 = param1 + 10;
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 2>
    console.log("result", param1 + 10)
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}