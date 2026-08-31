function spreadFunctionArgsTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 993>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 33 | <NewArray>: <Reg8: 5, UInt16: 0>
    r5 = []
    // CODE → addr: 37 | <NewArrayWithBuffer>: <Reg8: 7, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
    r7 = [1, 2, 3]
    // CODE → addr: 45 | <LoadConstZero>: <Reg8: 6>
    r6 = 0
    // CODE → addr: 47 | <Mov>: <Reg8: 8, Reg8: 5>
    r8 = r5
    // CODE → addr: 50 | <CallBuiltin>: <Reg8: 0, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r0 = arraySpread(r8, r7, r6, r5)
    // CODE → addr: 54 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr: 56 | <CreateClosure>: <Reg8: 8, Reg8: 0, function_id: 15121>  # Function: [#15121 sum of 19 bytes]: 4 params @ offset 0x00269ebf
    r8 = sum(param1, param2, param3)
    // CODE → addr: 61 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 63 | <Mov>: <Reg8: 7, Reg8: 5>
    r7 = r5
    // CODE → addr: 66 | <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → addr: 68 | <CallBuiltin>: <Reg8: 2, UInt8: 47, UInt8: 4>  # Built-in function: [#47 apply]
    // USED → r2 = apply(r8, r7, r6, r5);
    // CODE → addr: 72 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 77 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 83 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 88 | <LoadConstString>: <Reg8: 1, string_id: 4526>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end";
    // CODE → addr: 92 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end")
    // CODE → addr: 97 | <Ret>: <Reg8: 0>
    return undefined;
}