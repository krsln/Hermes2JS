function objectLiteralTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4772>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r2 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r2 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start");
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1913, UInt16: 48399>  # Object: {'name': 'Ada', 'age': 30, 'greet': null}
    // Error: NewObjectWithBuffer at address 22: Invalid arguments: Reg8: 2, UInt16: 1913, UInt16: 48399;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 12397>  # Function: [#12397 greet of 35 bytes]: 1 params @ offset 0x0023e384
    // USED → r3 = greet;
    // CODE → <PutOwnBySlotIdx>: <Reg8: 2, Reg8: 3, UInt8: 2>
    globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").slot_2 = greet;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 2, string_id: 186>  # String: 'name' (Identifier)
    // USED → r4 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name;
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 6914>  # String: 'age' (Identifier)
    // USED → r3 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age;
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 3>
    r3 = globalThis.console.log(globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name, globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age);
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 16987>  # String: 'greet' (Identifier)
    // USED → r3 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").greet;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").greet();
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 186>  # String: 'name' (Identifier)
    // USED → r5 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name;
    // CODE → <GetById>: <Reg8: 4, Reg8: 2, UInt8: 3, string_id: 6914>  # String: 'age' (Identifier)
    // USED → r4 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    // USED → r2 = globalThis.console.log(globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name, globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 1914, UInt16: 17735>  # Object: {'e': 3}
    // Error: NewObjectWithBuffer at address 116: Invalid arguments: Reg8: 2, UInt16: 1914, UInt16: 17735;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 6313>  # String: 'e' (Identifier)
    // USED → r2 = globalThis.console.log(globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name, globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age).e;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(globalThis.console.log(globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").name, globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start").age).e);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2712>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end");
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}