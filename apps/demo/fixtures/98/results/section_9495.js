function mapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  4 | <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 2, string_id: 4740>  # String: '__BC:Collections/MapSetTests/mapTest/start' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/mapTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/mapTest/start")
    // CODE → addr: 28 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 18>  # String: 'Map' (Identifier)
    // USED → r2 = Map;
    // CODE → addr: 34 | <CreateThisForNew>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = CreateThisForNew(r2);
    // CODE → addr: 38 | <Mov>: <Reg8: 15, Reg8: 3>
    // USED → r15 = CreateThisForNew(r2);
    // CODE → addr: 41 | <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new Map();
    // CODE → addr: 45 | <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    r2 = new Map()
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → addr: 54 | <LoadConstUInt8>: <Reg8: 4, UInt8: 90>
    // USED → r4 = 90;
    // CODE → addr: 57 | <LoadConstString>: <Reg8: 3, string_id: 5119>  # String: 'alice' (String)
    // USED → r3 = "alice";
    // CODE → addr: 61 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 4>
    r3 = r2.set("alice", 90)
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → addr: 72 | <LoadConstUInt8>: <Reg8: 3, UInt8: 75>
    // USED → r3 = 75;
    // CODE → addr: 75 | <LoadConstString>: <Reg8: 4, string_id: 4356>  # String: 'bob' (String)
    // USED → r4 = "bob";
    // CODE → addr: 79 | <Call3>: <Reg8: 3, Reg8: 5, Reg8: 2, Reg8: 4, Reg8: 3>
    r3 = r2.set("bob", 75)
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 8, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r8 = r2.set;
    // CODE → addr: 90 | <LoadConstUInt8>: <Reg8: 5, UInt8: 88>
    // USED → r5 = 88;
    // CODE → addr: 93 | <LoadConstString>: <Reg8: 3, string_id: 666>  # String: 'carol' (String)
    // USED → r3 = "carol";
    // CODE → addr: 97 | <Call3>: <Reg8: 3, Reg8: 8, Reg8: 2, Reg8: 3, Reg8: 5>
    r3 = r2.set("carol", 88)
    // CODE → addr:103 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:109 | <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:114 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 5, string_id: 49>  # String: 'get' (Identifier)
    // USED → r3 = r2.get;
    // CODE → addr:119 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    r3 = r2.get("bob")
    // CODE → addr:124 | <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r3)
    // CODE → addr:129 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:135 | <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:140 | <GetByIdShort>: <Reg8: 9, Reg8: 2, UInt8: 6, string_id: 11>  # String: 'has' (Identifier)
    // USED → r9 = r2.has;
    // CODE → addr:145 | <LoadConstString>: <Reg8: 3, string_id: 5331>  # String: 'dave' (String)
    // USED → r3 = "dave";
    // CODE → addr:149 | <Call2>: <Reg8: 3, Reg8: 9, Reg8: 2, Reg8: 3>
    r3 = r2.has("dave")
    // CODE → addr:154 | <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r3)
    // CODE → addr:159 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:165 | <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:170 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 7, string_id: 69>  # String: 'size' (Identifier)
    // USED → r3 = r2.size;
    // CODE → addr:175 | <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r2.size)
    // CODE → addr:180 | <Mov>: <Reg8: 3, Reg8: 2>
    r3 = new Map()
    // CODE → addr:183 | <IteratorBegin>: <Reg8: 5, Reg8: 3>
    r5 = GetIterator(r3)
    // LOOP → START (while)
    // → r8 = new Map()
    while (!(r8 === undefined)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:186 | <Mov>: <Reg8: 8, Reg8: 3>
        r8 = new Map()
        // CODE → addr:189 | <IteratorNext>: <Reg8: 9, Reg8: 5, Reg8: 8>
        r9 = r5.next()
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:200 | <Mov>: <Reg8: 11, Reg8: 9>
        r11 = r9
        // CODE → addr:203 | <IteratorBegin>: <Reg8: 8, Reg8: 11>
        r8 = GetIterator(r11)
        // CODE → addr:209 | <IteratorNext>: <Reg8: 12, Reg8: 8, Reg8: 9>
        r12 = r8.next()
        // CODE → addr:213 | <Mov>: <Reg8: 9, Reg8: 8>
        r9 = r8
        // CODE → addr:216 | <StrictEq>: <Reg8: 9, Reg8: 9, Reg8: 0>
        r9 = r9 === undefined
        // CODE → addr:220 | <LoadConstUndefined>: <Reg8: 10>
        r10 = undefined
        // → r9 = r9 === undefined
        if (!r9) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr:225 | <Mov>: <Reg8: 10, Reg8: 12>
            r10 = r12
        }
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr:228 | <Mov>: <Reg8: 7, Reg8: 10>
        r7 = r10
        // CODE → addr:231 | <LoadConstUndefined>: <Reg8: 10>
        r10 = undefined
        if (!r9 && !r11) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr:236 | <IteratorNext>: <Reg8: 12, Reg8: 8, Reg8: 11>
            r12 = r8.next()
            // CODE → addr:240 | <Mov>: <Reg8: 11, Reg8: 8>
            r11 = r8
            // CODE → addr:243 | <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 0>
            r11 = r11 === undefined
            // CODE → addr:247 | <LoadConstUndefined>: <Reg8: 10>
            r10 = undefined
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr:255 | <Mov>: <Reg8: 10, Reg8: 12>
            r10 = r12
            // CODE → addr:258 | <Mov>: <Reg8: 9, Reg8: 11>
            r9 = r11
        }
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:261 | <Mov>: <Reg8: 6, Reg8: 10>
        r6 = r10
        if (!r9) {
            // ──────────────── Block 8 ──────────────── 
            // CODE → addr:267 | <IteratorClose>: <Reg8: 8, UInt8: 0>
            r8.return()
        }
        // ──────────────── Block 9 ──────────────── 
        // CODE → addr:270 | <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r11 = console;
        // CODE → addr:276 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r10 = console.log;
        // CODE → addr:281 | <Mov>: <Reg8: 9, Reg8: 7>
        r9 = r7
        // CODE → addr:284 | <Mov>: <Reg8: 8, Reg8: 6>
        r8 = r6
        // CODE → addr:287 | <Call3>: <Reg8: 8, Reg8: 10, Reg8: 11, Reg8: 9, Reg8: 8>
        console.log(r9, r8)
    }
    // LOOP → END
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:295 | <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → addr:297 | <IteratorClose>: <Reg8: 5, UInt8: 1>
    r5.return()
    // CODE → addr:300 | <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:302 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 8, string_id: 118>  # String: 'delete' (Identifier)
    // USED → r3 = r2.delete;
    // CODE → addr:307 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    r3 = r2.delete("bob")
    // CODE → addr:312 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:318 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:323 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 7, string_id: 69>  # String: 'size' (Identifier)
    // USED → r2 = r2.size;
    // CODE → addr:328 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.size)
    // CODE → addr:333 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:339 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:344 | <LoadConstString>: <Reg8: 1, string_id: 4737>  # String: '__BC:Collections/MapSetTests/mapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/mapTest/end";
    // CODE → addr:348 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/mapTest/end")
    // CODE → addr:353 | <Ret>: <Reg8: 0>
    return undefined;
}