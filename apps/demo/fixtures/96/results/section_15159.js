function restOnlyTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4799>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/start' (String)
    // USED → r2 = "__BC:Functions/RestParameterTests/restOnlyTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/RestParameterTests/restOnlyTest/start")
    // CODE → <GetArgumentsLength>: <Reg8: 3, Reg8: 4>
    // USED → r3 = arguments.length;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r2 = globalThis.Array;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r5 = globalThis.Array.prototype;
    // CODE → <CreateThis>: <Reg8: 5, Reg8: 5, Reg8: 2>
    // USED → r5 = createThis(globalThis.Array.prototype, globalThis.Array);
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    r9 = createThis(globalThis.Array.prototype, globalThis.Array)
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = arguments.length;
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = new globalThis.Array(arguments.length);
    // CODE → <SelectObject>: <Reg8: 5, Reg8: 5, Reg8: 2>
    // USED → r5 = new globalThis.Array(arguments.length);
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <Less>: <Reg8: 6, Reg8: 2, Reg8: 3>
    // USED → r6 = 0 < arguments.length;
    if (0 < arguments.length) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetArgumentsPropByVal>: <Reg8: 6, Reg8: 2, Reg8: 4>
        // USED → r6 = arguments[0];
        // CODE → <PutByVal>: <Reg8: 5, Reg8: 2, Reg8: 6>
        new globalThis.Array(arguments.length)[0] = arguments[0]
        // CODE → <Inc>: <Reg8: 2, Reg8: 2>
        r2 = r2 + 1
        // CODE → <JLess>: <Addr8: -11, Reg8: 2, Reg8: 3>  # Address: 00000043
        if (r2 < r3) goto label_67;
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = new globalThis.Array(arguments.length).length;
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    r2 = globalThis.console.log(new globalThis.Array(arguments.length).length, new globalThis.Array(arguments.length))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4798>  # String: '__BC:Functions/RestParameterTests/restOnlyTest/end' (String)
    // USED → r1 = "__BC:Functions/RestParameterTests/restOnlyTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/RestParameterTests/restOnlyTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}