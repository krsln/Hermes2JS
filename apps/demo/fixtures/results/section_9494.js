function spreadFunctionArgsTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4720>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start' (String)
    // USED → r3 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 33 | <NewArray>: <Reg8: 6, UInt16: 0>
    r6 = []
    // CODE → addr: 37 | <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → addr: 39 | <NewArrayWithBuffer>: <Reg8: 8, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    r8 = [1, 2, 3]
    // CODE → addr: 50 | <CallBuiltin>: <Reg8: 0, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r0 = arraySpread(r-4, r-3, r-2, r-1)
    // CODE → addr: 54 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 56 | <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 12477>  # Function: [#12477 sum of 19 bytes]: 4 params @ offset 0x00243e3c
    r9 = sum(param1, param2, param3)
    // CODE → addr: 61 | <Mov>: <Reg8: 8, Reg8: 6>
    r8 = r6
    // CODE → addr: 64 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr: 66 | <CallBuiltin>: <Reg8: 3, UInt8: 49, UInt8: 4>  # Built-in function: [#49 apply]
    // USED → r3 = apply(r-1, r0, r1, r2);
    // CODE → addr: 70 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → addr: 75 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 86 | <LoadConstString>: <Reg8: 2, string_id: 4719>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end' (String)
    // USED → r2 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end";
    // CODE → addr: 90 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end")
    // CODE → addr: 95 | <Ret>: <Reg8: 1>
    return undefined;
}