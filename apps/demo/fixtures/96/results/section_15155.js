function defaultWithRestTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <GetArgumentsLength>: <Reg8: 1, Reg8: 7>
    r1 = arguments.length
    // CODE → <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → <Greater>: <Reg8: 1, Reg8: 1, Reg8: 8>
    // USED → r1 = r1 > r8;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → <Mov>: <Reg8: 5, Reg8: 6>
    r5 = 1
    if (r1 > r8 && r1 !== r0) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <GetArgumentsPropByVal>: <Reg8: 5, Reg8: 8, Reg8: 7>
        // USED → r5 = arguments[0];
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4773>  # String: '__BC:Functions/DefaultParameterTests/defaultWithRestTest/start' (String)
    // USED → r2 = "__BC:Functions/DefaultParameterTests/defaultWithRestTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/DefaultParameterTests/defaultWithRestTest/start")
    // CODE → <GetArgumentsLength>: <Reg8: 3, Reg8: 7>
    r3 = arguments.length
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 6>  # String: 'Array' (Identifier)
    // USED → r2 = globalThis.Array;
    // CODE → <Greater>: <Reg8: 4, Reg8: 3, Reg8: 6>
    // USED → r4 = r3 > r6;
    // CODE → <LoadConstZero>: <Reg8: 8>
    r8 = 0
    if (r3 > r6) {
        // ──────────────── Block 4 ──────────────── 
        // CODE → <Sub>: <Reg8: 8, Reg8: 3, Reg8: 6>
        // USED → r8 = r3 - r6;
    }
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r4 = globalThis.Array.prototype;
    // CODE → <CreateThis>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = createThis(globalThis.Array.prototype, globalThis.Array);
    // CODE → <Mov>: <Reg8: 12, Reg8: 4>
    r12 = createThis(globalThis.Array.prototype, globalThis.Array)
    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
    // USED → r11 = r3 - r6;
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 2>
    // USED → r2 = new globalThis.Array(r3 - r6);
    // CODE → <SelectObject>: <Reg8: 4, Reg8: 4, Reg8: 2>
    // USED → r4 = new globalThis.Array(r3 - r6);
    // CODE → <Less>: <Reg8: 8, Reg8: 6, Reg8: 3>
    // USED → r8 = r6 < r3;
    // CODE → <Mov>: <Reg8: 2, Reg8: 6>
    // USED → r2 = 1;
    if (r6 < r3) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Sub>: <Reg8: 9, Reg8: 2, Reg8: 6>
        // USED → r9 = r2 - r6;
        // CODE → <GetArgumentsPropByVal>: <Reg8: 8, Reg8: 2, Reg8: 7>
        // USED → r8 = arguments[1];
        // CODE → <PutByVal>: <Reg8: 4, Reg8: 9, Reg8: 8>
        new globalThis.Array(r3 - r6)[r2 - r6] = arguments[1]
        // CODE → <Inc>: <Reg8: 2, Reg8: 2>
        r2 = r2 + 1
        // CODE → <JLess>: <Addr8: -15, Reg8: 2, Reg8: 3>  # Address: 00000072
        if (r2 < r3) goto label_114;
    }
    // ──────────────── Block 7 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 5, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r3 = new globalThis.Array(r3 - r6).reduce;
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 15156>  # Function: [#15156  of 12 bytes]: 3 params @ offset 0x00269c66
    // USED → r2 = function_15156;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    // USED → r3 = new globalThis.Array(r3 - r6).reduce(function_15156, arguments[0]);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log(new globalThis.Array(r3 - r6).reduce(function_15156, arguments[0]))
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}