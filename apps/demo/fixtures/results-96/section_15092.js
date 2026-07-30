function closureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4593>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r0 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15093>  # Function: [#15093 makeCounter of 41 bytes]: 1 params @ offset 0x00265529
    // USED → r2 = makeCounter;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    // USED → r5 = makeCounter.call(undefined);
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 8421>  # String: 'increment' (Identifier)
    // USED → r2 = makeCounter.call(undefined).increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = makeCounter.call(undefined).increment()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 8421>  # String: 'increment' (Identifier)
    // USED → r2 = makeCounter.call(undefined).increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = makeCounter.call(undefined).increment()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 14314>  # String: 'decrement' (Identifier)
    // USED → r2 = makeCounter.call(undefined).decrement;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = makeCounter.call(undefined).decrement()
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 206>  # String: 'value' (Identifier)
    // USED → r2 = makeCounter.call(undefined).value;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = makeCounter.call(undefined).value();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(makeCounter.call(undefined).value())
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3433>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}