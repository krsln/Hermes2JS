function objectLiteralTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4827>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 1, UInt16: 3, UInt16: 2, UInt16: 12803, UInt16: 23466>  # Object: {'name': 'Ada', 'age': 30}
    r1 = { "name": "Ada", "age": 30 }
    // CODE → <CreateEnvironment>: <Reg8: 2>
    createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 15096>  # Function: [#15096 greet of 35 bytes]: 1 params @ offset 0x002694da
    // USED → r2 = greet();
    // CODE → <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 17737>  # String: 'greet' (Identifier)
    r1.greet = greet()
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 7743>  # String: 'age' (Identifier)
    // USED → r2 = r1.age;
    // CODE → <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
    console.log(r3, r2)
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 17737>  # String: 'greet' (Identifier)
    // USED → r2 = r1.greet;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    r1.greet()
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r4 = r1.name;
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 7743>  # String: 'age' (Identifier)
    // USED → r3 = r1.age;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log(r4, r3)
    // CODE → <NewObject>: <Reg8: 1>
    r1 = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 7189>  # String: 'a' (Identifier)
    r1.a = 1
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7241>  # String: 'c' (Identifier)
    r2.c = 2
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    // USED → r4 = 3;
    // CODE → <PutNewOwnById>: <Reg8: 3, Reg8: 4, string_id: 7180>  # String: 'e' (Identifier)
    r3.e = 3
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7181>  # String: 'd' (Identifier)
    r2.d = r3
    // CODE → <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 38>  # String: 'b' (Identifier)
    r1.b = r2
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 38>  # String: 'b' (Identifier)
    // USED → r1 = r1.b;
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 7181>  # String: 'd' (Identifier)
    // USED → r1 = r1.b.d;
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 7180>  # String: 'e' (Identifier)
    // USED → r1 = r1.b.d.e;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4826>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r0 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}