function restOnlyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 2, string_id: 4799>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restOnlyTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/start")
    // CODE → addr: 26 | <GetArgumentsLength>: <Reg8: 3, Reg8: 4>
    // USED → r3 = arguments.length;
    // CODE → addr: 29 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r2 = Array;
    // CODE → addr: 35 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r5 = Array.prototype;
    // CODE → addr: 40 | <CreateThis>: <Reg8: 5, Reg8: 5, Reg8: 2>
    // USED → r5 = CreateThis(r5);
    // CODE → addr: 44 | <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = CreateThis(r5);
    // CODE → addr: 47 | <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = arguments.length;
    // CODE → addr: 50 | <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = new Array(arguments.length);
    // CODE → addr: 54 | <SelectObject>: <Reg8: 5, Reg8: 5, Reg8: 2>
    // USED → r5 = new Array(arguments.length);
    // CODE → addr: 58 | <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → addr: 60 | <Less>: <Reg8: 6, Reg8: 2, Reg8: 3>
    // USED → r6 = 0 < arguments.length;
    // CODE → addr: 64 | <JmpFalse>: <Addr8: 18, Reg8: 6>  # Address: 00000052
    if (!(0 < arguments.length)) goto label_82;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 67 | <GetArgumentsPropByVal>: <Reg8: 6, Reg8: 2, Reg8: 4>
    // USED → r6 = arguments[0];
    // CODE → addr: 71 | <PutByVal>: <Reg8: 5, Reg8: 2, Reg8: 6>
    new Array(arguments.length)[0] = arguments[0]
    // CODE → addr: 75 | <Inc>: <Reg8: 2, Reg8: 2>
    r2 = r2 + 1
    // CODE → addr: 78 | <JLess>: <Addr8: -11, Reg8: 2, Reg8: 3>  # Address: 00000043
    // → r2 = r2 + 1
    if (r2 < r3) goto label_67;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 82 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 88 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 93 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = r5.length;
    // CODE → addr: 98 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    console.log(r5.length, r5)
    // CODE → addr:104 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:110 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:115 | <LoadConstString>: <Reg8: 1, string_id: 4798>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/restOnlyTest/end";
    // CODE → addr:119 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/end")
    // CODE → addr:124 | <Ret>: <Reg8: 0>
    return r0;
}