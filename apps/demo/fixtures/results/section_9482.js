function propertyAccessTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4997>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/start' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/propertyAccessTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/start")
    // CODE → addr: 22 | <NewObjectWithBuffer>: <Reg8: 4, UInt16: 61, UInt16: 42665>  # Object: {'x': 1, 'y': 2}
    r4 = { "x": 1, "y": 2 }
    // CODE → addr: 28 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr: 31 | <PutByIdStrict>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 6711>  # String: 'z' (Identifier)
    r4.z = 3
    // CODE → addr: 37 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 43 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 30>  # String: 'x' (Identifier)
    // USED → r3 = r4.x;
    // CODE → addr: 53 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 4>  # String: 'y' (Identifier)
    // USED → r2 = r4.y;
    // CODE → addr: 58 | <GetById>: <Reg8: 0, Reg8: 4, UInt8: 4, string_id: 6711>  # String: 'z' (Identifier)
    // USED → r0 = r4.z;
    // CODE → addr: 64 | <Call4>: <Reg8: 0, Reg8: 5, Reg8: 6, Reg8: 3, Reg8: 2, Reg8: 0>
    console.log(r4.x, r4.y, r4.z)
    // CODE → addr: 71 | <LoadConstString>: <Reg8: 0, string_id: 30>  # String: 'x' (Identifier)
    // USED → r0 = "x";
    // CODE → addr: 75 | <DelByVal>: <Reg8: 2, Reg8: 4, Reg8: 0, UInt8: 1>
    r2 = delete r4["x"]
    // CODE → addr: 80 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 86 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 91 | <IsIn>: <Reg8: 0, Reg8: 0, Reg8: 4>
    r0 = "x" in r4
    // CODE → addr: 95 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log(r0)
    // CODE → addr:100 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 5, string_id: 23>  # String: 'Object' (Identifier)
    // USED → r2 = Object;
    // CODE → addr:106 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 6, string_id: 173>  # String: 'keys' (Identifier)
    // USED → r0 = Object.keys;
    // CODE → addr:111 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    r0 = Object.keys(r4)
    // CODE → addr:116 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = r0
    // CODE → addr:119 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // CODE → addr:122 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (!(r5 === undefined)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:127 | <IteratorNext>: <Reg8: 8, Reg8: 3, Reg8: 5>
        r8 = r3.next()
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:138 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r7 = console;
        // CODE → addr:144 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r6 = console.log;
        // CODE → addr:149 | <GetByVal>: <Reg8: 5, Reg8: 4, Reg8: 8>
        r5 = r4[r8]
        // CODE → addr:153 | <Call3>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5>
        console.log(r8, r5)
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:161 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr:163 | <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → addr:166 | <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:168 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:174 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:179 | <LoadConstString>: <Reg8: 1, string_id: 4996>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/propertyAccessTest/end";
    // CODE → addr:183 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/end")
    // CODE → addr:188 | <Ret>: <Reg8: 0>
    return undefined;
}