function propertyAccessTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4839>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/start' (String)
    // USED → r2 = "__BC:Objects/PropertyTests/propertyAccessTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 2, UInt16: 317, UInt16: 19852>  # Object: {'x': 1, 'y': 2}
    // USED → r5 = { "x": 1, "y": 2 };
    // CODE → <Mov>: <Reg8: 4, Reg8: 5>
    // USED → r4 = r5;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → <PutById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 7612>  # String: 'z' (Identifier)
    r5.z = 3
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 3, string_id: 41>  # String: 'x' (Identifier)
    // USED → r6 = r5.x;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 4, string_id: 7>  # String: 'y' (Identifier)
    // USED → r3 = r5.y;
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 7612>  # String: 'z' (Identifier)
    // USED → r2 = r5.z;
    // CODE → <Call4>: <Reg8: 2, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 3, Reg8: 2>
    console.log(r6, r3, r2)
    // CODE → <DelById>: <Reg8: 2, Reg8: 5, string_id: 41>  # String: 'x' (Identifier)
    r2 = delete r5.x
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 41>  # String: 'x' (Identifier)
    // USED → r2 = "x";
    // CODE → <IsIn>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = "x" in r5;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 6, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r3 = Object;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 7, string_id: 118>  # String: 'keys' (Identifier)
    // USED → r2 = Object.keys;
    // CODE → <Call2>: <Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 5>
    r5 = Object.keys(r5)
    // CODE → <Mov>: <Reg8: 2, Reg8: 5>
    r2 = r5
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 2>
    r3 = GetIterator(r2)
    // ──────────────── Block 1 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 8, Reg8: 3, Reg8: 2>
    // USED → r8 = r3.next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    r5 = r3
    // CODE → <JStrictEqual>: <Addr8: 37, Reg8: 5, Reg8: 0>  # Address: 000000b1
    // → r5 = r3
    if (r5 === undefined) goto label_177;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    // USED → r5 = r5;
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 5, Reg8: 8>
    // USED → r5 = r5[r8];
    // CODE → <Call3>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log(r8, r5)
    // CODE → <Jmp>: <Addr8: -35>  # Address: 00000085
    goto label_133;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
    r3.return()
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4838>  # String: '__BC:Objects/PropertyTests/propertyAccessTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/propertyAccessTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/propertyAccessTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}