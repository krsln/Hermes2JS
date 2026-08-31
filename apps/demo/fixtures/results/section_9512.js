function defaultWithRestTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = (param1 !== undefined) ? param1 : 1;
    // CODE → addr:  3 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 12 | <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
    r9 = 1
    // CODE → addr: 15 | <CallBuiltin>: <Reg8: 5, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    r5 = copyRestArgs(r9, r8)
    // CODE → addr: 19 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 21 | <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 27 | <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 3, string_id: 4936>  # String: '__BC:Functions/DefaultParameterTests/defaultWithRestTest/start' (String)
    // USED → r3 = "__BC:Functions/DefaultParameterTests/defaultWithRestTest/start";
    // CODE → addr: 36 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    console.log("__BC:Functions/DefaultParameterTests/defaultWithRestTest/start")
    // CODE → addr: 41 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 213>  # String: 'reduce' (Identifier)
    // USED → r4 = r5.reduce;
    // CODE → addr: 46 | <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 12481>  # Function: [#12481  of 12 bytes]: 3 params @ offset 0x00243e24
    // USED → r3 = function_12481(param1, param2);
    // CODE → addr: 51 | <Call3>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 6>
    // USED → r4 = r5.reduce(function_12481(param1, param2), (param1 !== undefined) ? param1 : 1);
    // CODE → addr: 57 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 63 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 68 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr: 73 | <Ret>: <Reg8: 1>
    return undefined;
}