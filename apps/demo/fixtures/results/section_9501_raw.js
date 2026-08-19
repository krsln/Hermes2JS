function tag(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 1>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 4, UInt8: 1>
    r4 = param1
    // CODE → addr:  6 | <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
    r7 = 1
    // CODE → addr:  9 | <CallBuiltin>: <Reg8: 2, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    r2 = copyRestArgs(r0, r1)
    // CODE → addr: 13 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 2>
    __environment__[0] = r2
    // CODE → addr: 17 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 19 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 25 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 30 | <LoadConstString>: <Reg8: 2, string_id: 5013>  # String: '__BC:Strings/TemplateLiteralTests/tag/invoked' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/tag/invoked";
    // CODE → addr: 34 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/tag/invoked")
    // CODE → addr: 39 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 213>  # String: 'reduce' (Identifier)
    // USED → r3 = r4.reduce;
    // CODE → addr: 44 | <LoadConstString>: <Reg8: 2, string_id: 6457>  # String: '' (Identifier)
    // USED → r2 = "";
    // CODE → addr: 48 | <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 12478>  # Function: [#12478  of 57 bytes]: 4 params @ offset 0x00243e4f
    // USED → r1 = function_12478(param1, param2, param3);
    // CODE → addr: 53 | <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 2>
    r1 = r4.reduce(function_12478(param1, param2, param3), "")
    // CODE → addr: 59 | <Ret>: <Reg8: 1>
    return r1;
}