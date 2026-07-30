function spreadFunctionArgsTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4690>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start' (String)
    // USED → r3 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <NewArray>: <Reg8: 6, UInt16: 0>
    // USED → r6 = [];
    // CODE → <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → <NewArrayWithBuffer>: <Reg8: 8, UInt16: 3, UInt16: 3, UInt16: 19180>  # Array: [1, 2, 3]
    r8 = [1, 2, 3]
    // CODE → <Mov>: <Reg8: 9, Reg8: 6>
    r9 = []
    // CODE → <CallBuiltin>: <Reg8: 0, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r0 = builtin_48(r-4, r-3, r-2, r-1)
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 12401>  # Function: [#12401 sum of 19 bytes]: 4 params @ offset 0x0023e3b8
    r9 = sum
    // CODE → <Mov>: <Reg8: 8, Reg8: 6>
    r8 = []
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <CallBuiltin>: <Reg8: 3, UInt8: 49, UInt8: 4>  # Built-in function: [#49 applyWithNewTarget]
    // USED → r3 = builtin_49(r-1, r0, r1, r2);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log(builtin_49(r-1, r0, r1, r2))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4689>  # String: '__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end' (String)
    // USED → r2 = "__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}