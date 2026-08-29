function closureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4932>  # String: '__BC:Functions/ClosureTests/closureTest/start' (String)
    // USED → r3 = "__BC:Functions/ClosureTests/closureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/ClosureTests/closureTest/start")
    // CODE → addr: 22 | <CreateFunctionEnvironment>: <Reg8: 3, UInt8: 1>
    // USED → r3 = __environment__;
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 27 | <StoreNPToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → addr: 31 | <NewObjectWithBuffer>: <Reg8: 6, UInt16: 1921, UInt16: 17424>  # Object: {'increment': null, 'decrement': null, 'value': null}
    r6 = { "increment": null, "decrement": null, "value": null }
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13738>  # Function: [#13738 increment of 20 bytes]: 1 params @ offset 0x00261027
    // USED → r4 = increment();
    // CODE → addr: 42 | <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 0>
    r6.slot_0 = increment()
    // CODE → addr: 46 | <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 13739>  # Function: [#13739 decrement of 20 bytes]: 1 params @ offset 0x0026103b
    // USED → r4 = decrement();
    // CODE → addr: 51 | <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 4, UInt8: 1>
    r6.slot_1 = decrement()
    // CODE → addr: 55 | <CreateClosure>: <Reg8: 3, Reg8: 3, function_id: 13740>  # Function: [#13740 value of 9 bytes]: 1 params @ offset 0x00193d54
    // USED → r3 = value();
    // CODE → addr: 60 | <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 3, UInt8: 2>
    r6.slot_2 = value()
    // CODE → addr: 64 | <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r3 = r6.increment;
    // CODE → addr: 70 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.increment()
    // CODE → addr: 74 | <GetById>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r3 = r6.increment;
    // CODE → addr: 80 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.increment()
    // CODE → addr: 84 | <GetById>: <Reg8: 3, Reg8: 6, UInt8: 3, string_id: 9910>  # String: 'decrement' (Identifier)
    // USED → r3 = r6.decrement;
    // CODE → addr: 90 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    r3 = r6.decrement()
    // CODE → addr: 94 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:100 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:105 | <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 4, string_id: 211>  # String: 'value' (Identifier)
    // USED → r3 = r6.value;
    // CODE → addr:110 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 6>
    // USED → r3 = r6.value();
    // CODE → addr:114 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → addr:119 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:125 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:130 | <LoadConstString>: <Reg8: 2, string_id: 4931>  # String: '__BC:Functions/ClosureTests/closureTest/end' (String)
    // USED → r2 = "__BC:Functions/ClosureTests/closureTest/end";
    // CODE → addr:134 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ClosureTests/closureTest/end")
    // CODE → addr:139 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr:141 | <Ret>: <Reg8: 1>
    return r1;
}