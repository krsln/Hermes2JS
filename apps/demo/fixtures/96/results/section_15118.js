function spreadArrayTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4523>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadArrayTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 2, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
    r2 = [1, 2, 3]
    // CODE → <NewArray>: <Reg8: 3, UInt16: 0>
    r3 = []
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = r3
    // CODE → <Mov>: <Reg8: 8, Reg8: 2>
    r8 = r2
    // CODE → <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → <CallBuiltin>: <Reg8: 7, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r7 = arraySpread(r3, r4, r5, r6)
    // CODE → <NewArrayWithBuffer>: <Reg8: 8, UInt16: 3, UInt16: 3, UInt16: 23671>  # Array: [4, 5, 6]
    r8 = [4, 5, 6]
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = r3
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r4 = arraySpread(r0, r1, r2, r3)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 3>
    r4 = globalThis.console.log(r3)
    // CODE → <NewArrayWithBuffer>: <Reg8: 6, UInt16: 2, UInt16: 1, UInt16: 18648>  # Array: [0]
    r6 = [0]
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
    // USED → r4 = 1;
    // CODE → <Mov>: <Reg8: 9, Reg8: 6>
    r9 = r6
    // CODE → <Mov>: <Reg8: 8, Reg8: 2>
    r8 = r2
    // CODE → <Mov>: <Reg8: 7, Reg8: 4>
    r7 = 1
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    // USED → r2 = arraySpread(r-2, r-1, r0, r1);
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 99>
    // USED → r5 = 99;
    // CODE → <PutOwnByVal>: <Reg8: 6, Reg8: 5, Reg8: 2, UInt8: 1>
    r6[arraySpread(r-2, r-1, r0, r1)] = 99
    // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 4>
    r2 = arraySpread(r-2, r-1, r0, r1) + 1
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    r2 = globalThis.console.log(r6)
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r5 = r3[0];
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 2>
    // USED → r0 = getEnvironment(0)[2];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[2].default;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 3, Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r3 = getEnvironment(0)[2].default.call(undefined, r3);
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r2 = getEnvironment(0)[2].default.call(undefined, r3).slice;
    // CODE → <Call2>: <Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r4 = getEnvironment(0)[2].default.call(undefined, r3).slice(1);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log(r3[0], getEnvironment(0)[2].default.call(undefined, r3).slice(1))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4521>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadArrayTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}