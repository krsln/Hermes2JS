function propertyAccessTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4997>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/start' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/propertyAccessTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 4, UInt16: 61, UInt16: 42665>  # Object: {'x': 1, 'y': 2}
    // USED → r4 = { "x": 1, "y": 2 };
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → <PutByIdStrict>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 6711>  # String: 'z' (Identifier)
    r4.z = 3
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 30>  # String: 'x' (Identifier)
    // USED → r3 = r4.x;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 4>  # String: 'y' (Identifier)
    // USED → r2 = r4.y;
    // CODE → <GetById>: <Reg8: 0, Reg8: 4, UInt8: 4, string_id: 6711>  # String: 'z' (Identifier)
    // USED → r0 = r4.z;
    // CODE → <Call4>: <Reg8: 0, Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 2, Reg8: 0>
    console.log(r3, r2, r0)
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 30>  # String: 'x' (Identifier)
    // USED → r0 = "x";
    // CODE → <DelByVal>: <Reg8: 2, Reg8: 4, Reg8: 0, UInt8: 1>
    r2 = delete r4["x"]
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <IsIn>: <Reg8: 0, Reg8: 0, Reg8: 4>
    // USED → r0 = "x" in r4;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log(r0)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 23>  # String: 'Object' (Identifier)
    // USED → r2 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 6, string_id: 173>  # String: 'keys' (Identifier)
    // USED → r0 = globalThis.Object.keys;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    // USED → r0 = globalThis.Object.keys(r4);
    // CODE → <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = globalThis.Object.keys(r4);
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    // USED → r3 = GetIterator(r2);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        r5 = globalThis.Object.keys(r4)
        // CODE → <IteratorNext>: <Reg8: 8, Reg8: 3, Reg8: 5>
        // USED → r8 = GetIterator(r2).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 3>
        // USED → r5 = GetIterator(r2);
        // → r5 = GetIterator(r2)
        if (r5 !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r7 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r6 = globalThis.console.log;
            // CODE → <GetByVal>: <Reg8: 5, Reg8: 4, Reg8: 8>
            // USED → r5 = r4[r8];
            // CODE → <Call3>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5>
            console.log(r8, r5)
            // CODE → <Jmp>: <Addr8: -35>  # Address: 0000007c
            goto label_124;
        }
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
    GetIterator(r2).return()
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4996>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/propertyAccessTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}