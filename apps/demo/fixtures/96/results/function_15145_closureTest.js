function closureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4768>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r0 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → addr: 22 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr: 24 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15146>  # Function: [#15146 makeCounter of 41 bytes]: 1 params @ offset 0x0026a962
    // USED → r2 = makeCounter();
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 31 | <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    r5 = makeCounter().call(undefined)
    // CODE → addr: 35 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → addr: 41 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → addr: 45 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → addr: 51 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → addr: 55 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10333>  # String: 'decrement' (Identifier)
    // USED → r2 = r5.decrement;
    // CODE → addr: 61 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.decrement()
    // CODE → addr: 65 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 205>  # String: 'value' (Identifier)
    // USED → r2 = r5.value;
    // CODE → addr: 81 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.value()
    // CODE → addr: 85 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 90 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:101 | <LoadConstString>: <Reg8: 1, string_id: 3716>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → addr:105 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → addr:110 | <Ret>: <Reg8: 0>
    return undefined;
}