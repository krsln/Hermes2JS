function objectLiteralTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4603>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/start' (String)
    // USED → r1 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 1, UInt16: 3, UInt16: 2, UInt16: 12813, UInt16: 23462>  # Object: {'name': 'Ada', 'age': 30}
    // USED → r1 = { "name": "Ada", "age": 30 };
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 15068>  # Function: [#15068 greet of 35 bytes]: 1 params @ offset 0x00264d99
    // USED → r2 = greet;
    // CODE → <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 17457>  # String: 'greet' (Identifier)
    // USED → r1 = { "name": "Ada", "age": 30, greet: greet };
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r3 = { "name": "Ada", "age": 30, greet: greet }.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 7526>  # String: 'age' (Identifier)
    // USED → r2 = { "name": "Ada", "age": 30, greet: greet }.age;
    // CODE → <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
    r2 = globalThis.console.log({ "name": "Ada", "age": 30, greet: greet }.name, { "name": "Ada", "age": 30, greet: greet }.age)
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 17457>  # String: 'greet' (Identifier)
    // USED → r2 = { "name": "Ada", "age": 30, greet: greet }.greet;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    r2 = { "name": "Ada", "age": 30, greet: greet }.greet()
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r4 = { "name": "Ada", "age": 30, greet: greet }.name;
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 4, string_id: 7526>  # String: 'age' (Identifier)
    // USED → r3 = { "name": "Ada", "age": 30, greet: greet }.age;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 3>
    r1 = globalThis.console.log({ "name": "Ada", "age": 30, greet: greet }.name, { "name": "Ada", "age": 30, greet: greet }.age)
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <PutNewOwnById>: <Reg8: 1, Reg8: 2, string_id: 6974>  # String: 'a' (Identifier)
    // USED → r1 = { a: 1 };
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7026>  # String: 'c' (Identifier)
    // USED → r2 = { c: 2 };
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    // USED → r4 = 3;
    // CODE → <PutNewOwnById>: <Reg8: 3, Reg8: 4, string_id: 6965>  # String: 'e' (Identifier)
    // USED → r3 = { e: 3 };
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 6966>  # String: 'd' (Identifier)
    // USED → r2 = { c: 2, d: { e: 3 } };
    // CODE → <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 39>  # String: 'b' (Identifier)
    // USED → r1 = { a: 1, b: { c: 2, d: { e: 3 } } };
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 39>  # String: 'b' (Identifier)
    // USED → r1 = { a: 1, b: { c: 2, d: { e: 3 } } }.b;
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 6966>  # String: 'd' (Identifier)
    // USED → r1 = { a: 1, b: { c: 2, d: { e: 3 } } }.b.d;
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 6965>  # String: 'e' (Identifier)
    // USED → r1 = { a: 1, b: { c: 2, d: { e: 3 } } }.b.d.e;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log({ a: 1, b: { c: 2, d: { e: 3 } } }.b.d.e)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4601>  # String: '__BC:Objects/ObjectLiteralTests/objectLiteralTest/end' (String)
    // USED → r0 = "__BC:Objects/ObjectLiteralTests/objectLiteralTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Objects/ObjectLiteralTests/objectLiteralTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}