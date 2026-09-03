function tag(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  5 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  7 | <GetArgumentsLength>: <Reg8: 6, Reg8: 7>
    // USED → r6 = arguments.length;
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r8 = Array;
    // CODE → addr: 18 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 21 | <Greater>: <Reg8: 4, Reg8: 6, Reg8: 5>
    // USED → r4 = arguments.length > 1;
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 2>
    r2 = 0
    // CODE → addr: 27 | <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000022
    if (!(arguments.length > 1)) goto label_34;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 30 | <Sub>: <Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = arguments.length - 1;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 34 | <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 2, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r4 = Array.prototype;
    // CODE → addr: 39 | <CreateThis>: <Reg8: 4, Reg8: 4, Reg8: 8>
    // USED → r4 = CreateThis(r4);
    // CODE → addr: 43 | <Mov>: <Reg8: 12, Reg8: 4>
    // USED → r12 = CreateThis(r4);
    // CODE → addr: 46 | <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = arguments.length - 1;
    // CODE → addr: 49 | <Construct>: <Reg8: 2, Reg8: 8, UInt8: 2>
    // USED → r2 = new Array(arguments.length - 1);
    // CODE → addr: 53 | <SelectObject>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = new Array(arguments.length - 1);
    // CODE → addr: 57 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    r0[0] = new Array(arguments.length - 1)
    // CODE → addr: 61 | <Less>: <Reg8: 8, Reg8: 5, Reg8: 6>
    // USED → r8 = 1 < arguments.length;
    // CODE → addr: 65 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr: 68 | <JmpFalse>: <Addr8: 22, Reg8: 8>  # Address: 0000005a
    if (!(1 < arguments.length)) goto label_90;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 71 | <Sub>: <Reg8: 9, Reg8: 2, Reg8: 5>
    r9 = r2 - 1
    // CODE → addr: 75 | <GetArgumentsPropByVal>: <Reg8: 8, Reg8: 2, Reg8: 7>
    // USED → r8 = arguments[r2];
    // CODE → addr: 79 | <PutByVal>: <Reg8: 4, Reg8: 9, Reg8: 8>
    new Array(arguments.length - 1)[r9] = arguments[r2]
    // CODE → addr: 83 | <Inc>: <Reg8: 2, Reg8: 2>
    r2 = r2 + 1
    // CODE → addr: 86 | <JLess>: <Addr8: -15, Reg8: 2, Reg8: 6>  # Address: 00000047
    // → r2 = r2 + 1
    if (r2 < r6) goto label_71;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 90 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 4, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:101 | <LoadConstString>: <Reg8: 1, string_id: 4861>  # String: '__BC:Strings/TemplateLiteralTests/tag/invoked' (String)
    // USED → r1 = "__BC:Strings/TemplateLiteralTests/tag/invoked";
    // CODE → addr:105 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Strings/TemplateLiteralTests/tag/invoked")
    // CODE → addr:110 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r2 = param1.reduce;
    // CODE → addr:115 | <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 15131>  # Function: [#15131  of 61 bytes]: 4 params @ offset 0x0026a42e
    // USED → r1 = function_15131(param1, param2, param3);
    // CODE → addr:120 | <LoadConstString>: <Reg8: 0, string_id: 7163>  # String: '' (Identifier)
    // USED → r0 = "";
    // CODE → addr:124 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
    r0 = param1.reduce(function_15131(param1, param2, param3), "")
    // CODE → addr:130 | <Ret>: <Reg8: 0>
    return r0;
}