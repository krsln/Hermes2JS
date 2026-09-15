function objectLiteralTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4827>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 1, UInt16: 3, UInt16: 2, UInt16: 12803, UInt16: 23466>  # Object: {'name': 'Ada', 'age': 30}
    r1 = { "name": "Ada", "age": 30 }
    // CODE → addr: 32 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr: 34 | <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 15096>  # Function: [#15096 greet of 35 bytes]: 1 params @ offset 0x002694da
    // USED → r2 = greet();
    // CODE → addr: 39 | <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 17737>  # String: 'greet' (Identifier)
    r1.greet = greet()
    // CODE → addr: 44 | <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 55 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → addr: 60 | <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 7743>  # String: 'age' (Identifier)
    // USED → r2 = r1.age;
    // CODE → addr: 66 | <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
    console.log(r1.name, r1.age)
    // CODE → addr: 72 | <GetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 17737>  # String: 'greet' (Identifier)
    // USED → r2 = r1.greet;
    // CODE → addr: 78 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    r2 = r1.greet()
    // CODE → addr: 82 | <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r4 = r1.name;
    // CODE → addr: 87 | <GetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 7743>  # String: 'age' (Identifier)
    // USED → r3 = r1.age;
    // CODE → addr: 93 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 99 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:104 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log(r1.name, r1.age)
    // CODE → addr:110 | <NewObject>: <Reg8: 1>
    r1 = {  }
    // CODE → addr:112 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr:115 | <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 7189>  # String: 'a' (Identifier)
    r1.a = 1
    // CODE → addr:120 | <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → addr:122 | <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → addr:125 | <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7241>  # String: 'c' (Identifier)
    r2.c = 2
    // CODE → addr:130 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr:132 | <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    // USED → r4 = 3;
    // CODE → addr:135 | <PutNewOwnById>: <Reg8: 3, Reg8: 4, string_id: 7180>  # String: 'e' (Identifier)
    r3.e = 3
    // CODE → addr:140 | <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7181>  # String: 'd' (Identifier)
    r2.d = r3
    // CODE → addr:145 | <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 38>  # String: 'b' (Identifier)
    r1.b = r2
    // CODE → addr:149 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:155 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:160 | <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 38>  # String: 'b' (Identifier)
    r1 = r1.b
    // CODE → addr:165 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 7181>  # String: 'd' (Identifier)
    r1 = r1.d
    // CODE → addr:171 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 7180>  # String: 'e' (Identifier)
    // USED → r1 = r1.e;
    // CODE → addr:177 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1.e)
    // CODE → addr:182 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:188 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:193 | <LoadConstString>: <Reg8: 0, string_id: 4826>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r0 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → addr:197 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end")
    // CODE → addr:202 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:204 | <Ret>: <Reg8: 0>
    return undefined;
}