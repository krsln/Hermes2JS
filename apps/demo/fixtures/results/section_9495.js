function mapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4740>  # String: '__BC:Collections/MapSetTests/mapTest/start' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/mapTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/mapTest/start")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 18>  # String: 'Map' (Identifier)
    // USED → r2 = Map;
    // CODE → <CreateThisForNew>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = CreateThisForNew(r2);
    // CODE → <Mov>: <Reg8: 15, Reg8: 3>
    // USED → r15 = CreateThisForNew(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new Map();
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    r2 = new Map()
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 90>
    // USED → r4 = 90;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5119>  # String: 'alice' (String)
    // USED → r3 = "alice";
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 2, Reg8: 3, Reg8: 4>
    r3 = r2.set("alice", 90)
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r5 = r2.set;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 75>
    // USED → r3 = 75;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4356>  # String: 'bob' (String)
    // USED → r4 = "bob";
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 2, Reg8: 4, Reg8: 3>
    r3 = r2.set("bob", 75)
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 2, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r8 = r2.set;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 88>
    // USED → r5 = 88;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 666>  # String: 'carol' (String)
    // USED → r3 = "carol";
    // CODE → <Call3>: <Reg8: 3, Reg8: 8, Reg8: 2, Reg8: 3, Reg8: 5>
    r3 = r2.set("carol", 88)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 5, string_id: 49>  # String: 'get' (Identifier)
    // USED → r3 = r2.get;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    // USED → r3 = r2.get("bob");
    // CODE → <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 2, UInt8: 6, string_id: 11>  # String: 'has' (Identifier)
    // USED → r9 = r2.has;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5331>  # String: 'dave' (String)
    // USED → r3 = "dave";
    // CODE → <Call2>: <Reg8: 3, Reg8: 9, Reg8: 2, Reg8: 3>
    // USED → r3 = r2.has("dave");
    // CODE → <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 7, string_id: 69>  # String: 'size' (Identifier)
    // USED → r3 = r2.size;
    // CODE → <Call2>: <Reg8: 3, Reg8: 5, Reg8: 8, Reg8: 3>
    console.log(r3)
    // CODE → <Mov>: <Reg8: 3, Reg8: 2>
    r3 = new Map()
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 3>
    r5 = GetIterator(r3)
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 8, Reg8: 3>
        r8 = new Map()
        // CODE → <IteratorNext>: <Reg8: 9, Reg8: 5, Reg8: 8>
        r9 = r5.next()
        // CODE → <Mov>: <Reg8: 8, Reg8: 5>
        r8 = r5
        // → r8 = r5
        if (r8 !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 9>
            r11 = r9
            // CODE → <IteratorBegin>: <Reg8: 8, Reg8: 11>
            r8 = GetIterator(r11)
            // CODE → <Mov>: <Reg8: 9, Reg8: 11>
            r9 = r9
            // CODE → <IteratorNext>: <Reg8: 12, Reg8: 8, Reg8: 9>
            r12 = r8.next()
            // CODE → <Mov>: <Reg8: 9, Reg8: 8>
            // USED → r9 = r8;
            // CODE → <StrictEq>: <Reg8: 9, Reg8: 9, Reg8: 0>
            // USED → r9 = r8 === undefined;
            // CODE → <LoadConstUndefined>: <Reg8: 10>
            r10 = (r8 === undefined) ? undefined : r12
            // ──────────────── Block 4 ──────────────── 
            // CODE → <Mov>: <Reg8: 7, Reg8: 10>
            // USED → r7 = (r8 === undefined) ? undefined : r12;
            // CODE → <LoadConstUndefined>: <Reg8: 10>
            r10 = undefined
            if (r8 !== undefined) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <IteratorNext>: <Reg8: 12, Reg8: 8, Reg8: 11>
                r12 = r8.next()
                // CODE → <Mov>: <Reg8: 11, Reg8: 8>
                // USED → r11 = r8;
                // CODE → <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 0>
                // USED → r11 = r8 === undefined;
                // CODE → <LoadConstUndefined>: <Reg8: 10>
                r10 = undefined
                // CODE → <Mov>: <Reg8: 9, Reg8: 11>
                r9 = r8 === undefined || r8 === undefined
            }
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Mov>: <Reg8: 6, Reg8: 10>
            // USED → r6 = r12;
            if (r8 !== undefined) {
                // ──────────────── Block 8 ──────────────── 
                // CODE → <IteratorClose>: <Reg8: 8, UInt8: 0>
                r8.return()
            }
            // ──────────────── Block 9 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 11, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r11 = console;
            // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r10 = console.log;
            // CODE → <Mov>: <Reg8: 9, Reg8: 7>
            // USED → r9 = (r8 === undefined) ? undefined : r12;
            // CODE → <Mov>: <Reg8: 8, Reg8: 6>
            // USED → r8 = r12;
            // CODE → <Call3>: <Reg8: 8, Reg8: 10, Reg8: 11, Reg8: 9, Reg8: 8>
            console.log(r9, r8)
            // CODE → <Jmp>: <Addr8: -107>  # Address: 000000ba
            goto label_186;
        }
    }
    // LOOP → END
    // ──────────────── Block 10 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 5, UInt8: 1>
    r5.return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 8, string_id: 118>  # String: 'delete' (Identifier)
    // USED → r3 = r2.delete;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 2, Reg8: 4>
    r3 = r2.delete("bob")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 7, string_id: 69>  # String: 'size' (Identifier)
    // USED → r2 = r2.size;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4737>  # String: '__BC:Collections/MapSetTests/mapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/mapTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/mapTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}