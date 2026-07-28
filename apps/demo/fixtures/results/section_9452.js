function propertyAccessTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4780>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/start' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/propertyAccessTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Objects/PropertyTests/propertyAccessTest/start");
    // CODE → <NewObjectWithBuffer>: <Reg8: 4, UInt16: 61, UInt16: 42586>  # Object: {'x': 1, 'y': 2}
    // Error: NewObjectWithBuffer at address 22: Invalid arguments: Reg8: 4, UInt16: 61, UInt16: 42586;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → <PutByIdStrict>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 6488>  # String: 'z' (Identifier)
    r4.z = 3;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 28>  # String: 'x' (Identifier)
    // USED → r3 = r4.x;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 4>  # String: 'y' (Identifier)
    // USED → r2 = r4.y;
    // CODE → <GetById>: <Reg8: 0, Reg8: 4, UInt8: 4, string_id: 6488>  # String: 'z' (Identifier)
    // USED → r0 = r4.z;
    // CODE → <Call4>: <Reg8: 0, Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log(r4.x, r4.y, r4.z);
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 28>  # String: 'x' (Identifier)
    // USED → r0 = "x";
    // CODE → <DelByVal>: <Reg8: 2, Reg8: 4, Reg8: 0, UInt8: 1>
    // Error: DelByVal at address 75: Expected three Reg8 arguments: Reg8: 2, Reg8: 4, Reg8: 0, UInt8: 1;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <IsIn>: <Reg8: 0, Reg8: 0, Reg8: 4>
    // USED → r0 = "x" in r4;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("x" in r4);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 21>  # String: 'Object' (Identifier)
    // USED → r2 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 6, string_id: 172>  # String: 'keys' (Identifier)
    // USED → r0 = globalThis.Object.keys;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    // USED → r0 = globalThis.Object.keys(r4);
    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = globalThis.Object.keys(r4);
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator(globalThis.Object.keys(r4));
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        r5 = globalThis.Object.keys(r4);
        // CODE → <IteratorNext>: <Reg8: 8, Reg8: 3, Reg8: 5>
        // USED → r8 = GetIterator(globalThis.Object.keys(r4)).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = GetIterator(globalThis.Object.keys(r4));
        // CODE → <JStrictEqual>: <Addr8: 34, Reg8: 5, Reg8: 0>  # Address: 000000a8
        if (GetIterator(globalThis.Object.keys(r4)) === undefined) goto label_168;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
        // USED → r7 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
        // USED → r6 = globalThis.console.log;
        // CODE → <GetByVal>: <Reg8: 5, Reg8: 4, Reg8: 8>
        // USED → r5 = r4[GetIterator(globalThis.Object.keys(r4)).next()];
        // CODE → <Call3>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5>
        r5 = globalThis.console.log(GetIterator(globalThis.Object.keys(r4)).next(), r4[GetIterator(globalThis.Object.keys(r4)).next()]);
        // CODE → <Jmp>: <Addr8: -35>  # Address: 0000007c
        goto label_124;
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
    GetIterator(globalThis.Object.keys(r4)).return();
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4455>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/propertyAccessTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/PropertyTests/propertyAccessTest/end");
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}