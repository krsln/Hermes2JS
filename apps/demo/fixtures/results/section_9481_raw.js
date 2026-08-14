function objectLiteralTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4989>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r2 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1913, UInt16: 48468>  # Object: {'name': 'Ada', 'age': 30, 'greet': null}
    r2 = { "name": "Ada", "age": 30, "greet": null }
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 12471>  # Function: [#12471 greet of 35 bytes]: 1 params @ offset 0x00243de9
    // USED → r3 = greet(param0);
    // CODE → <PutOwnBySlotIdx>: <Reg8: 2, Reg8: 3, UInt8: 2>
    r2.slot_2 = greet(param0)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r4 = r2.name;
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 7158>  # String: 'age' (Identifier)
    // USED → r3 = r2.age;
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 3>
    console.log(r4, r3)
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 17251>  # String: 'greet' (Identifier)
    // USED → r3 = r2.greet;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = r2.greet()
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r5 = r2.name;
    // CODE → <GetById>: <Reg8: 4, Reg8: 2, UInt8: 3, string_id: 7158>  # String: 'age' (Identifier)
    // USED → r4 = r2.age;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r5, r4)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1914, UInt16: 17759>  # Object: {'e': 3}
    r2 = { "e": 3 }
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 6520>  # String: 'e' (Identifier)
    // USED → r2 = r2.e;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4987>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}