function defaultWithRestTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = (r6 !== undefined) ? param1 : 1;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 1>
    r9 = 1
    // CODE → <CallBuiltin>: <Reg8: 5, UInt8: 47, UInt8: 2>  # Built-in function: [#47 apply]
    // USED → r5 = apply(r3, r4);
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4936>  # String: '__BC:Functions/DefaultParameterTests/defaultWithRestTest/start' (String)
    // USED → r3 = "__BC:Functions/DefaultParameterTests/defaultWithRestTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    console.log("__BC:Functions/DefaultParameterTests/defaultWithRestTest/start")
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 213>  # String: 'reduce' (Identifier)
    // USED → r4 = apply(r3, r4).reduce;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 12481>  # Function: [#12481  of 12 bytes]: 3 params @ offset 0x00243e24
    // USED → r3 = function_12481;
    // CODE → <Call3>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 6>
    // USED → r4 = apply(r3, r4).reduce(r3, (r6 !== undefined) ? param1 : 1);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}