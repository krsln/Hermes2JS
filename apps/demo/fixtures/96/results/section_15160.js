function restAfterRequiredTest(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4797>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/start")
    // CODE → <GetArgumentsLength>: <Reg8: 4, Reg8: 5>
    r4 = arguments.length
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r7 = globalThis.Array;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → <Greater>: <Reg8: 6, Reg8: 4, Reg8: 3>
    // USED → r6 = r4 > r3;
    // CODE → <LoadConstZero>: <Reg8: 2>
    r2 = 0
    if (r4 > r3) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Sub>: <Reg8: 2, Reg8: 4, Reg8: 3>
        // USED → r2 = r4 - r3;
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r6 = globalThis.Array.prototype;
    // CODE → <CreateThis>: <Reg8: 6, Reg8: 6, Reg8: 7>
    // USED → r6 = createThis(globalThis.Array.prototype, globalThis.Array);
    // CODE → <Mov>: <Reg8: 12, Reg8: 6>
    r12 = createThis(globalThis.Array.prototype, globalThis.Array)
    // CODE → <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = r4 - r3;
    // CODE → <Construct>: <Reg8: 2, Reg8: 7, UInt8: 2>
    // USED → r2 = new globalThis.Array(r4 - r3);
    // CODE → <SelectObject>: <Reg8: 6, Reg8: 6, Reg8: 2>
    // USED → r6 = new globalThis.Array(r4 - r3);
    // CODE → <Less>: <Reg8: 7, Reg8: 3, Reg8: 4>
    // USED → r7 = r3 < r4;
    // CODE → <Mov>: <Reg8: 2, Reg8: 3>
    // USED → r2 = 2;
    if (r3 < r4) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Sub>: <Reg8: 8, Reg8: 2, Reg8: 3>
        // USED → r8 = r2 - r3;
        // CODE → <GetArgumentsPropByVal>: <Reg8: 7, Reg8: 2, Reg8: 5>
        // USED → r7 = arguments[2];
        // CODE → <PutByVal>: <Reg8: 6, Reg8: 8, Reg8: 7>
        new globalThis.Array(r4 - r3)[r2 - r3] = arguments[2]
        // CODE → <Inc>: <Reg8: 2, Reg8: 2>
        r2 = r2 + 1
        // CODE → <JLess>: <Addr8: -15, Reg8: 2, Reg8: 4>  # Address: 00000054
        if (r2 < r4) goto label_84;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2, Reg8: 6>
    r2 = globalThis.console.log(param1, param2, new globalThis.Array(r4 - r3))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4796>  # String: '__BC:Functions/RestParameterTests/restAfterRequiredTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/restAfterRequiredTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}