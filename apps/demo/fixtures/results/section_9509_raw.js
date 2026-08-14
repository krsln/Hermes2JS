function closureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4932>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r3 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → <CreateFunctionEnvironment>: <Reg8: 3, UInt8: 1>
    // USED → r3 = __environment__;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 1921, UInt16: 17424>  # Object: {'increment': null, 'decrement': null, 'value': null}
    r6 = { "increment": null, "decrement": null, "value": null }
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13738>  # Function: [#13738 increment of 20 bytes]: 1 params @ offset 0x00261027
    // USED → r4 = increment(param0);
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 0>
    r6.slot_0 = increment(param0)
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13739>  # Function: [#13739 decrement of 20 bytes]: 1 params @ offset 0x0026103b
    // USED → r4 = decrement(param0);
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 1>
    r6.slot_1 = decrement(param0)
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 3, function_id: 13740>  # Function: [#13740 value of 9 bytes]: 1 params @ offset 0x00193d54
    // USED → r3 = value(param0);
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 3, UInt8: 2>
    r6.slot_2 = value(param0)
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r3 = r6.increment;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.increment()
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r3 = r6.increment;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.increment()
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 3, string_id: 9910>  # String: 'decrement' (Identifier)
    // USED → r3 = r6.decrement;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.decrement()
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 4, string_id: 211>  # String: 'value' (Identifier)
    // USED → r3 = r6.value;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    // USED → r3 = r6.value();
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4931>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r2 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}