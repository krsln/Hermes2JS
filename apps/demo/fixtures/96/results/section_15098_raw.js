function propertyAccessTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 2, string_id: 4839>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/start' (String)
    // USED → r2 = "__BC:Objects/PropertyTests/propertyAccessTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/start")
    // CODE → addr: 26 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 2, UInt16: 317, UInt16: 19852>  # Object: {'x': 1, 'y': 2}
    // USED → r5 = { "x": 1, "y": 2 };
    // CODE → addr: 36 | <Mov>: <Reg8: 4, Reg8: 5>
    // USED → r4 = r5;
    // CODE → addr: 39 | <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → addr: 42 | <PutById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 7612>  # String: 'z' (Identifier)
    r5.z = 3
    // CODE → addr: 48 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr: 54 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 3, string_id: 41>  # String: 'x' (Identifier)
    // USED → r6 = r5.x;
    // CODE → addr: 64 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 4, string_id: 7>  # String: 'y' (Identifier)
    // USED → r3 = r5.y;
    // CODE → addr: 69 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 7612>  # String: 'z' (Identifier)
    // USED → r2 = r5.z;
    // CODE → addr: 75 | <Call4>: <Reg8: 2, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 3, Reg8: 2>
    console.log(r5.x, r5.y, r5.z)
    // CODE → addr: 82 | <DelById>: <Reg8: 2, Reg8: 5, string_id: 41>  # String: 'x' (Identifier)
    r2 = delete r5.x
    // CODE → addr: 87 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 93 | <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 98 | <LoadConstString>: <Reg8: 2, string_id: 41>  # String: 'x' (Identifier)
    // USED → r2 = "x";
    // CODE → addr:102 | <IsIn>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = "x" in r5;
    // CODE → addr:106 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
    console.log(r2)
    // CODE → addr:111 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 6, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r3 = Object;
    // CODE → addr:117 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 7, string_id: 118>  # String: 'keys' (Identifier)
    // USED → r2 = Object.keys;
    // CODE → addr:122 | <Call2>: <Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 5>
    r5 = Object.keys(r5)
    // CODE → addr:127 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = r5
    // CODE → addr:130 | <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:133 | <IteratorNext>: <Reg8: 8, Reg8: 3, Reg8: 2>
    // USED → r8 = r3.next();
    // CODE → addr:137 | <Mov>: <Reg8: 5, Reg8: 3>
    r5 = r3
    // CODE → addr:140 | <JStrictEqual>: <Addr8: 37, Reg8: 5, Reg8: 0>  # Address: 000000b1
    // → r5 = r3
    if (r5 === undefined) goto label_177;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:144 | <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:150 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:155 | <Mov>: <Reg8: 5, Reg8: 4>
    // USED → r5 = r5;
    // CODE → addr:158 | <GetByVal>: <Reg8: 5, Reg8: 5, Reg8: 8>
    // USED → r5 = r5[r8];
    // CODE → addr:162 | <Call3>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log(r8, r5)
    // CODE → addr:168 | <Jmp>: <Addr8: -35>  # Address: 00000085
    goto label_133;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:170 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr:172 | <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → addr:175 | <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:177 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:183 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:188 | <LoadConstString>: <Reg8: 1, string_id: 4838>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/propertyAccessTest/end";
    // CODE → addr:192 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/end")
    // CODE → addr:197 | <Ret>: <Reg8: 0>
    return undefined;
}