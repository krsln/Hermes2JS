function defaultWithRestTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  4 | <GetArgumentsLength>: <Reg8: 1, Reg8: 7>
    // USED → r1 = arguments.length;
    // CODE → addr:  7 | <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → addr:  9 | <Greater>: <Reg8: 1, Reg8: 1, Reg8: 8>
    // USED → r1 = arguments.length > 0;
    // CODE → addr: 13 | <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → addr: 16 | <Mov>: <Reg8: 5, Reg8: 6>
    r5 = 1
    // CODE → addr: 19 | <JmpFalse>: <Addr8: 18, Reg8: 1>  # Address: 00000025
    if (!(arguments.length > 0)) goto label_37;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 22 | <GetArgumentsPropByVal>: <Reg8: 1, Reg8: 8, Reg8: 7>
    r1 = arguments[0]
    // CODE → addr: 26 | <Mov>: <Reg8: 5, Reg8: 6>
    r5 = 1
    // CODE → addr: 29 | <JStrictEqual>: <Addr8: 8, Reg8: 1, Reg8: 0>  # Address: 00000025
    // → r1 = arguments[0]
    if (r1 === undefined) goto label_37;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 33 | <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 8, Reg8: 7>
    r5 = arguments[0]
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 37 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 39 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 50 | <LoadConstString>: <Reg8: 2, string_id: 4773>  # String: '__BC:Functions/DefaultParameterTests/defaultWithRestTest/start' (String)
    // USED → r2 = "__BC:Functions/DefaultParameterTests/defaultWithRestTest/start";
    // CODE → addr: 54 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/DefaultParameterTests/defaultWithRestTest/start")
    // CODE → addr: 59 | <GetArgumentsLength>: <Reg8: 3, Reg8: 7>
    // USED → r3 = arguments.length;
    // CODE → addr: 62 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r2 = Array;
    // CODE → addr: 68 | <Greater>: <Reg8: 4, Reg8: 3, Reg8: 6>
    // USED → r4 = arguments.length > 1;
    // CODE → addr: 72 | <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → addr: 74 | <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000051
    if (!(arguments.length > 1)) goto label_81;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 77 | <Sub>: <Reg8: 8, Reg8: 3, Reg8: 6>
    // USED → r8 = arguments.length - 1;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r4 = Array.prototype;
    // CODE → addr: 86 | <CreateThis>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = CreateThis(r4);
    // CODE → addr: 90 | <Mov>: <Reg8: 12, Reg8: 4>
    // USED → r12 = CreateThis(r4);
    // CODE → addr: 93 | <Mov>: <Reg8: 11, Reg8: 8>
    // USED → r11 = arguments.length - 1;
    // CODE → addr: 96 | <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = new Array(arguments.length - 1);
    // CODE → addr:100 | <SelectObject>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = new Array(arguments.length - 1);
    // CODE → addr:104 | <Less>: <Reg8: 8, Reg8: 6, Reg8: 3>
    // USED → r8 = 1 < arguments.length;
    // CODE → addr:108 | <Mov>: <Reg8: 2, Reg8: 6>
    // USED → r2 = 1;
    // CODE → addr:111 | <JmpFalse>: <Addr8: 22, Reg8: 8>  # Address: 00000085
    if (!(1 < arguments.length)) goto label_133;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:114 | <Sub>: <Reg8: 9, Reg8: 2, Reg8: 6>
    // USED → r9 = 1 - 1;
    // CODE → addr:118 | <GetArgumentsPropByVal>: <Reg8: 8, Reg8: 2, Reg8: 7>
    // USED → r8 = arguments[1];
    // CODE → addr:122 | <PutByVal>: <Reg8: 4, Reg8: 9, Reg8: 8>
    new Array(arguments.length - 1)[1 - 1] = arguments[1]
    // CODE → addr:126 | <Inc>: <Reg8: 2, Reg8: 2>
    r2 = r2 + 1
    // CODE → addr:129 | <JLess>: <Addr8: -15, Reg8: 2, Reg8: 3>  # Address: 00000072
    // → r2 = r2 + 1
    if (r2 < r3) goto label_114;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:133 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 5, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r3 = r4.reduce;
    // CODE → addr:138 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:140 | <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 15156>  # Function: [#15156  of 12 bytes]: 3 params @ offset 0x00269c66
    // USED → r2 = function_15156(param1, param2);
    // CODE → addr:145 | <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    r3 = r4.reduce(function_15156(param1, param2), r5)
    // CODE → addr:151 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:157 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:162 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:167 | <Ret>: <Reg8: 0>
    return r0;
}