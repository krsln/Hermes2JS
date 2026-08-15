function tag(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 6, Reg8: 7>
    // USED → r6 = arguments.length;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r8 = globalThis.Array;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → <Greater>: <Reg8: 4, Reg8: 6, Reg8: 5>
    // USED → r4 = arguments.length > 1;
    // CODE → <LoadConstZero>: <Reg8: 2>
    r2 = 0
    // CODE → <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000022
    if (!(arguments.length > 1)) goto label_34;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Sub>: <Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = arguments.length - 1;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
    r4 = globalThis.Array.prototype
    // CODE → <CreateThis>: <Reg8: 4, Reg8: 4, Reg8: 8>
    // USED → r4 = CreateThis(r4);
    // CODE → <Mov>: <Reg8: 12, Reg8: 4>
    // USED → r12 = CreateThis(r4);
    // CODE → <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = arguments.length - 1;
    // CODE → <Construct>: <Reg8: 2, Reg8: 8, UInt8: 2>
    // USED → r2 = new globalThis.Array(arguments.length - 1);
    // CODE → <SelectObject>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = new globalThis.Array(arguments.length - 1);
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = new globalThis.Array(arguments.length - 1)
    // CODE → <Less>: <Reg8: 8, Reg8: 5, Reg8: 6>
    // USED → r8 = 1 < arguments.length;
    // CODE → <Mov>: <Reg8: 2, Reg8: 5>
    // USED → r2 = 1;
    // CODE → <JmpFalse>: <Addr8: 22, Reg8: 8>  # Address: 0000005a
    if (!(1 < arguments.length)) goto label_90;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Sub>: <Reg8: 9, Reg8: 2, Reg8: 5>
    // USED → r9 = 1 - 1;
    // CODE → <GetArgumentsPropByVal>: <Reg8: 8, Reg8: 2, Reg8: 7>
    // USED → r8 = arguments[1];
    // CODE → <PutByVal>: <Reg8: 4, Reg8: 9, Reg8: 8>
    new globalThis.Array(arguments.length - 1)[1 - 1] = arguments[1]
    // CODE → <Inc>: <Reg8: 2, Reg8: 2>
    // USED → r2 = r2 + 1;
    // CODE → <JLess>: <Addr8: -15, Reg8: 2, Reg8: 6>  # Address: 00000047
    // → r2 = r2 + 1
    if (r2 < r6) goto label_71;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 4, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4861>  # String: '__BC:Strings/TemplateLiteralTests/tag/invoked' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/tag/invoked";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/tag/invoked")
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r2 = param1.reduce;
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 15131>  # Function: [#15131  of 61 bytes]: 4 params @ offset 0x0026a42e
    // USED → r1 = function_15131(param1, param2, param3);
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 7163>  # String: '' (Identifier)
    // USED → r0 = "";
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
    // USED → r0 = param1.reduce(function_15131(param1, param2, param3), "");
    // CODE → <Ret>: <Reg8: 0>
    return param1.reduce(function_15131(param1, param2, param3), "");
}