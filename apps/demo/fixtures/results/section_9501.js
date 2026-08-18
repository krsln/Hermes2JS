function tag(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 1>
    // USED → r1 = __environment__;
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
    r7 = 1
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 47, UInt8: 2>  # Built-in function: [#47 copyRestArgs]
    r2 = copyRestArgs(r0, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 2>
    __environment__[0] = r2
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5013>  # String: '__BC:Strings/TemplateLiteralTests/tag/invoked' (String)
    // USED → r2 = "__BC:Strings/TemplateLiteralTests/tag/invoked";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Strings/TemplateLiteralTests/tag/invoked")
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 213>  # String: 'reduce' (Identifier)
    // USED → r3 = param1.reduce;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 6457>  # String: '' (Identifier)
    // USED → r2 = "";
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 12478>  # Function: [#12478  of 57 bytes]: 4 params @ offset 0x00243e4f
    // USED → r1 = function_12478(param1, param2, param3);
    // CODE → <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 2>
    r1 = param1.reduce(function_12478(param1, param2, param3), "")
    // CODE → <Ret>: <Reg8: 1>
    return r1;
}