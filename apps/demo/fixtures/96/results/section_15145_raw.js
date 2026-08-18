function closureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4768>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r0 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15146>  # Function: [#15146 makeCounter of 41 bytes]: 1 params @ offset 0x0026a962
    // USED → r2 = makeCounter();
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 5, Reg8: 2, Reg8: 0>
    r5 = makeCounter().call(undefined)
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10333>  # String: 'decrement' (Identifier)
    // USED → r2 = r5.decrement;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.decrement()
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 205>  # String: 'value' (Identifier)
    // USED → r2 = r5.value;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.value();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3716>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r1 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}