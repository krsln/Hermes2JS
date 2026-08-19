function mapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4557>  # String: '__BC:Collections/MapSetTests/mapTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/mapTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/mapTest/start")
    // CODE → <TryGetById>: <Reg8: 0, Reg8: 1, UInt8: 3, string_id: 20>  # String: 'Map' (Identifier)
    // USED → r0 = Map;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = Map.prototype;
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 0>
    // USED → r2 = CreateThis(r2);
    // CODE → <Mov>: <Reg8: 16, Reg8: 2>
    // USED → r16 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 0, Reg8: 0, UInt8: 1>
    // USED → r0 = new Map();
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = new Map()
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r4 = r2.set;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5105>  # String: 'alice' (String)
    // USED → r3 = "alice";
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 90>
    // USED → r0 = 90;
    // CODE → <Call3>: <Reg8: 0, Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r2.set("alice", 90)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r3 = r2.set;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 2540>  # String: 'bob' (String)
    // USED → r4 = "bob";
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 75>
    // USED → r0 = 75;
    // CODE → <Call3>: <Reg8: 0, Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 0>
    r0 = r2.set("bob", 75)
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 677>  # String: 'carol' (String)
    // USED → r3 = "carol";
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 88>
    // USED → r0 = 88;
    // CODE → <Call3>: <Reg8: 0, Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r2.set("carol", 88)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 6, string_id: 50>  # String: 'get' (Identifier)
    // USED → r0 = r2.get;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    // USED → r0 = r2.get("bob");
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 2, UInt8: 7, string_id: 153>  # String: 'has' (Identifier)
    // USED → r6 = r2.has;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 903>  # String: 'dave' (String)
    // USED → r0 = "dave";
    // CODE → <Call2>: <Reg8: 0, Reg8: 6, Reg8: 2, Reg8: 0>
    // USED → r0 = r2.has("dave");
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 8, string_id: 226>  # String: 'size' (Identifier)
    // USED → r0 = r2.size;
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → <Mov>: <Reg8: 9, Reg8: 2>
    r9 = new Map()
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 9>
    r5 = GetIterator(r9)
    // CODE → <GetEnvironment>: <Reg8: 8, UInt8: 0>
    r8 = getEnvironment(0)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 2>
    // USED → r7 = 2;
    // CODE → <LoadConstZero>: <Reg8: 6>
    r6 = 0
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    r3 = 1
    // ──────────────── Block 1 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 11, Reg8: 5, Reg8: 9>
    // USED → r11 = r5.next();
    // CODE → <Mov>: <Reg8: 10, Reg8: 5>
    r10 = r5
    // CODE → <JStrictEqual>: <Addr8: 53, Reg8: 10, Reg8: 0>  # Address: 00000102
    // → r10 = r5
    if (r10 === undefined) goto label_258;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 10, Reg8: 8, UInt8: 0>
    r10 = r8[0]
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
    // USED → r10 = r10.default;
    // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 0, Reg8: 11, Reg8: 7>
    r10 = r10.default.call(r0, r11, 2)
    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 6>
    // USED → r13 = r10[r6];
    // CODE → <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 3>
    // USED → r12 = r10[r3];
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 13, Reg8: 12>
    console.log(r13, r12)
    // CODE → <Jmp>: <Addr8: -51>  # Address: 000000c6
    goto label_198;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 5, UInt8: 1>
    r5.return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 10, string_id: 114>  # String: 'delete' (Identifier)
    // USED → r3 = r2.delete;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    r3 = r2.delete("bob")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 226>  # String: 'size' (Identifier)
    // USED → r2 = r2.size;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4556>  # String: '__BC:Collections/MapSetTests/mapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/mapTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/mapTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}