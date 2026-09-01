function restAfterRequiredTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 2, string_id: 4797>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/start")
    // CODE → addr: 26 | <GetArgumentsLength>: <Reg8: 4, Reg8: 5>
    // USED → r4 = arguments.length;
    // CODE → addr: 29 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r7 = Array;
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → addr: 38 | <Greater>: <Reg8: 6, Reg8: 4, Reg8: 3>
    // USED → r6 = arguments.length > 2;
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 2>
    r2 = 0
    // CODE → addr: 44 | <JmpFalse>: <Addr8: 7, Reg8: 6>  # Address: 00000033
    if (!(arguments.length > 2)) goto label_51;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 47 | <Sub>: <Reg8: 2, Reg8: 4, Reg8: 3>
    // USED → r2 = arguments.length - 2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 51 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r6 = Array.prototype;
    // CODE → addr: 56 | <CreateThis>: <Reg8: 6, Reg8: 6, Reg8: 7>
    // USED → r6 = CreateThis(r6);
    // CODE → addr: 60 | <Mov>: <Reg8: 12, Reg8: 6>
    // USED → r12 = CreateThis(r6);
    // CODE → addr: 63 | <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = arguments.length - 2;
    // CODE → addr: 66 | <Construct>: <Reg8: 2, Reg8: 7, UInt8: 2>
    // USED → r2 = new Array(arguments.length - 2);
    // CODE → addr: 70 | <SelectObject>: <Reg8: 6, Reg8: 6, Reg8: 2>
    // USED → r6 = new Array(arguments.length - 2);
    // CODE → addr: 74 | <Less>: <Reg8: 7, Reg8: 3, Reg8: 4>
    // USED → r7 = 2 < arguments.length;
    // CODE → addr: 78 | <Mov>: <Reg8: 2, Reg8: 3>
    // USED → r2 = 2;
    // CODE → addr: 81 | <JmpFalse>: <Addr8: 22, Reg8: 7>  # Address: 00000067
    if (!(2 < arguments.length)) goto label_103;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 84 | <Sub>: <Reg8: 8, Reg8: 2, Reg8: 3>
    // USED → r8 = 2 - 2;
    // CODE → addr: 88 | <GetArgumentsPropByVal>: <Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r7 = arguments[2];
    // CODE → addr: 92 | <PutByVal>: <Reg8: 6, Reg8: 8, Reg8: 7>
    new Array(arguments.length - 2)[2 - 2] = arguments[2]
    // CODE → addr: 96 | <Inc>: <Reg8: 2, Reg8: 2>
    r2 = r2 + 1
    // CODE → addr: 99 | <JLess>: <Addr8: -15, Reg8: 2, Reg8: 4>  # Address: 00000054
    // → r2 = r2 + 1
    if (r2 < r4) goto label_84;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:103 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:109 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:114 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:117 | <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → addr:120 | <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2, Reg8: 6>
    console.log(param1, param2, r6)
    // CODE → addr:127 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:133 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:138 | <LoadConstString>: <Reg8: 1, string_id: 4796>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/end";
    // CODE → addr:142 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/end")
    // CODE → addr:147 | <Ret>: <Reg8: 0>
    return r0;
}