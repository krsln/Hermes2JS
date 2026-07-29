function closureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3585>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r3 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → <CreateFunctionEnvironment>: <Reg8: 3, UInt8: 1>
    // USED → r3 = __environment__;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 1917, UInt16: 17338>  # Object: {'increment': null, 'decrement': null, 'value': null}
    // USED → r6 = { "increment": null, "decrement": null, "value": null };
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13654>  # Function: [#13654 increment of 20 bytes]: 1 params @ offset 0x0025ac17
    // USED → r4 = increment;
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 0>
    { "increment": null, "decrement": null, "value": null }.slot_0 = increment
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13655>  # Function: [#13655 decrement of 20 bytes]: 1 params @ offset 0x0025ac2b
    // USED → r4 = decrement;
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 1>
    { "increment": null, "decrement": null, "value": null }.slot_1 = decrement
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 3, function_id: 13656>  # Function: [#13656 value of 9 bytes]: 1 params @ offset 0x001905c0
    // USED → r3 = value;
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 3, UInt8: 2>
    { "increment": null, "decrement": null, "value": null }.slot_2 = value
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 13091>  # String: 'increment' (Identifier)
    // USED → r3 = { "increment": null, "decrement": null, "value": null }.increment;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = { "increment": null, "decrement": null, "value": null }.increment()
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 13091>  # String: 'increment' (Identifier)
    // USED → r3 = { "increment": null, "decrement": null, "value": null }.increment;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = { "increment": null, "decrement": null, "value": null }.increment()
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 3, string_id: 16228>  # String: 'decrement' (Identifier)
    // USED → r3 = { "increment": null, "decrement": null, "value": null }.decrement;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = { "increment": null, "decrement": null, "value": null }.decrement()
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 4, string_id: 212>  # String: 'value' (Identifier)
    // USED → r3 = { "increment": null, "decrement": null, "value": null }.value;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    // USED → r3 = { "increment": null, "decrement": null, "value": null }.value();
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log({ "increment": null, "decrement": null, "value": null }.value())
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2988>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r2 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}