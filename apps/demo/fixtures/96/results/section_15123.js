function mapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4557>  # String: '__BC:Collections/MapSetTests/mapTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/mapTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/mapTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 0, Reg8: 1, UInt8: 3, string_id: 20>  # String: 'Map' (Identifier)
    // USED → r0 = Map;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = Map.prototype;
    // CODE → addr: 33 | <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 0>
    // USED → r2 = CreateThis(r2);
    // CODE → addr: 37 | <Mov>: <Reg8: 16, Reg8: 2>
    // USED → r16 = CreateThis(r2);
    // CODE → addr: 40 | <Construct>: <Reg8: 0, Reg8: 0, UInt8: 1>
    // USED → r0 = new Map();
    // CODE → addr: 44 | <SelectObject>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = new Map()
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r4 = r2.set;
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 3, string_id: 5105>  # String: 'alice' (String)
    // USED → r3 = "alice";
    // CODE → addr: 57 | <LoadConstUInt8>: <Reg8: 0, UInt8: 90>
    // USED → r0 = 90;
    // CODE → addr: 60 | <Call3>: <Reg8: 0, Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r2.set("alice", 90)
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r3 = r2.set;
    // CODE → addr: 71 | <LoadConstString>: <Reg8: 4, string_id: 2540>  # String: 'bob' (String)
    // USED → r4 = "bob";
    // CODE → addr: 75 | <LoadConstUInt8>: <Reg8: 0, UInt8: 75>
    // USED → r0 = 75;
    // CODE → addr: 78 | <Call3>: <Reg8: 0, Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 0>
    r0 = r2.set("bob", 75)
    // CODE → addr: 84 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → addr: 89 | <LoadConstString>: <Reg8: 3, string_id: 677>  # String: 'carol' (String)
    // USED → r3 = "carol";
    // CODE → addr: 93 | <LoadConstUInt8>: <Reg8: 0, UInt8: 88>
    // USED → r0 = 88;
    // CODE → addr: 96 | <Call3>: <Reg8: 0, Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r2.set("carol", 88)
    // CODE → addr:102 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:108 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:113 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 6, string_id: 50>  # String: 'get' (Identifier)
    // USED → r0 = r2.get;
    // CODE → addr:118 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    // USED → r0 = r2.get("bob");
    // CODE → addr:123 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → addr:128 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:134 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:139 | <GetByIdShort>: <Reg8: 6, Reg8: 2, UInt8: 7, string_id: 153>  # String: 'has' (Identifier)
    // USED → r6 = r2.has;
    // CODE → addr:144 | <LoadConstString>: <Reg8: 0, string_id: 903>  # String: 'dave' (String)
    // USED → r0 = "dave";
    // CODE → addr:148 | <Call2>: <Reg8: 0, Reg8: 6, Reg8: 2, Reg8: 0>
    // USED → r0 = r2.has("dave");
    // CODE → addr:153 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → addr:158 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:164 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:169 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 8, string_id: 226>  # String: 'size' (Identifier)
    // USED → r0 = r2.size;
    // CODE → addr:174 | <Call2>: <Reg8: 0, Reg8: 3, Reg8: 5, Reg8: 0>
    console.log(r2.size)
    // CODE → addr:179 | <Mov>: <Reg8: 9, Reg8: 2>
    r9 = new Map()
    // CODE → addr:182 | <IteratorBegin>: <Reg8: 5, Reg8: 9>
    r5 = GetIterator(r9)
    // CODE → addr:185 | <GetEnvironment>: <Reg8: 8, UInt8: 0>
    r8 = getEnvironment(0)
    // CODE → addr:188 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:190 | <LoadConstUInt8>: <Reg8: 7, UInt8: 2>
    // USED → r7 = 2;
    // CODE → addr:193 | <LoadConstZero>: <Reg8: 6>
    r6 = 0
    // CODE → addr:195 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    r3 = 1
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr:198 | <IteratorNext>: <Reg8: 11, Reg8: 5, Reg8: 9>
            // USED → r11 = r5.next();
            // CODE → addr:202 | <Mov>: <Reg8: 10, Reg8: 5>
            r10 = r5
            // → r10 = r5
            if (r10 !== undefined) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr:209 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 8, UInt8: 0>
                r10 = r8[0]
                // CODE → addr:213 | <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 9, string_id: 107>  # String: 'default' (Identifier)
                // USED → r10 = r10.default;
                // CODE → addr:218 | <Call3>: <Reg8: 10, Reg8: 10, Reg8: 0, Reg8: 11, Reg8: 7>
                r10 = r10.default.call(r0, r11, 2)
                // CODE → addr:224 | <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 6>
                // USED → r13 = r10[r6];
                // CODE → addr:228 | <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 3>
                // USED → r12 = r10[r3];
                // CODE → addr:232 | <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r11 = console;
                // CODE → addr:238 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r10 = console.log;
                // CODE → addr:243 | <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 13, Reg8: 12>
                console.log(r13, r12)
                // CODE → addr:249 | <Jmp>: <Addr8: -51>  # Address: 000000c6
                goto label_198;
            }
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr:253 | <IteratorClose>: <Reg8: 5, UInt8: 1>
        r5.return()
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:258 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 10, string_id: 114>  # String: 'delete' (Identifier)
    // USED → r3 = r2.delete;
    // CODE → addr:263 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    r3 = r2.delete("bob")
    // CODE → addr:268 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:274 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:279 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 226>  # String: 'size' (Identifier)
    // USED → r2 = r2.size;
    // CODE → addr:284 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.size)
    // CODE → addr:289 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:295 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:300 | <LoadConstString>: <Reg8: 1, string_id: 4556>  # String: '__BC:Collections/MapSetTests/mapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/mapTest/end";
    // CODE → addr:304 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/mapTest/end")
    // CODE → addr:309 | <Ret>: <Reg8: 0>
    return undefined;
}