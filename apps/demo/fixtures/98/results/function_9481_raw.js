function objectLiteralTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 4989>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r2 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1913, UInt16: 48468>  # Object: {'name': 'Ada', 'age': 30, 'greet': null}
    r2 = { "name": "Ada", "age": 30, "greet": null }
    // CODE → addr: 28 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 30 | <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 12471>  # Function: [#12471 greet of 35 bytes]: 1 params @ offset 0x00243de9
    // USED → r3 = greet();
    // CODE → addr: 35 | <PutOwnBySlotIdx>: <Reg8: 2, Reg8: 3, UInt8: 2>
    r2.slot_2 = greet()
    // CODE → addr: 39 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r4 = r2.name;
    // CODE → addr: 55 | <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 7158>  # String: 'age' (Identifier)
    // USED → r3 = r2.age;
    // CODE → addr: 61 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 3>
    console.log(r2.name, r2.age)
    // CODE → addr: 67 | <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 17251>  # String: 'greet' (Identifier)
    // USED → r3 = r2.greet;
    // CODE → addr: 73 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = r2.greet()
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r5 = r2.name;
    // CODE → addr: 82 | <GetById>: <Reg8: 4, Reg8: 2, UInt8: 3, string_id: 7158>  # String: 'age' (Identifier)
    // USED → r4 = r2.age;
    // CODE → addr: 88 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 94 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 99 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r2.name, r2.age)
    // CODE → addr:105 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:111 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:116 | <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1914, UInt16: 17759>  # Object: {'e': 3}
    r2 = { "e": 3 }
    // CODE → addr:122 | <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 6520>  # String: 'e' (Identifier)
    // USED → r2 = r2.e;
    // CODE → addr:128 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.e)
    // CODE → addr:133 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:139 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:144 | <LoadConstString>: <Reg8: 1, string_id: 4987>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → addr:148 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end")
    // CODE → addr:153 | <Ret>: <Reg8: 0>
    return r0;
}