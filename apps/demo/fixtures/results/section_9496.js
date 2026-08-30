function setTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4745>  # String: '__BC:Collections/MapSetTests/setTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/setTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/setTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 31>  # String: 'Set' (Identifier)
    // USED → r3 = Set;
    // CODE → addr: 28 | <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = CreateThisForNew(r3);
    // CODE → addr: 32 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 6, UInt16: 6, UInt16: 48500>  # Array: [1, 2, 2, 3, 3, 3]
    // USED → r10 = [1, 2, 2, 3, 3, 3];
    // CODE → addr: 40 | <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = CreateThisForNew(r3);
    // CODE → addr: 43 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Set([1, 2, 2, 3, 3, 3]);
    // CODE → addr: 47 | <SelectObject>: <Reg8: 3, Reg8: 2, Reg8: 0>
    r3 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr: 51 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 57 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 62 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 69>  # String: 'size' (Identifier)
    // USED → r0 = r3.size;
    // CODE → addr: 67 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(r3.size)
    // CODE → addr: 72 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 79>  # String: 'add' (Identifier)
    // USED → r2 = r3.add;
    // CODE → addr: 77 | <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → addr: 80 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r3.add(4)
    // CODE → addr: 85 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 6, string_id: 11>  # String: 'has' (Identifier)
    // USED → r5 = r3.has;
    // CODE → addr:101 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:104 | <Call2>: <Reg8: 0, Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r0 = r3.has(2);
    // CODE → addr:109 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(r0)
    // CODE → addr:114 | <Mov>: <Reg8: 2, Reg8: 3>
    r2 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr:117 | <IteratorBegin>: <Reg8: 4, Reg8: 2>
    r4 = GetIterator(r2)
    // CODE → addr:120 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    // → r5 = r4
    while (!(r5 === undefined)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:122 | <Mov>: <Reg8: 5, Reg8: 2>
        r5 = new Set([1, 2, 2, 3, 3, 3])
        // CODE → addr:125 | <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = r4.next();
        // CODE → addr:129 | <Mov>: <Reg8: 5, Reg8: 4>
        r5 = r4
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:136 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr:142 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr:147 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        console.log(r7)
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:154 | <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → addr:156 | <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → addr:159 | <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:161 | <NewArray>: <Reg8: 4, UInt16: 0>
    // USED → r4 = [];
    // CODE → addr:165 | <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → addr:167 | <Mov>: <Reg8: 10, Reg8: 4>
    r10 = r4
    // CODE → addr:170 | <Mov>: <Reg8: 9, Reg8: 3>
    r9 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr:173 | <CallBuiltin>: <Reg8: 2, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r2 = arraySpread(r-2, r-1, r0, r1)
    // CODE → addr:177 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:183 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:188 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr:193 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:199 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:204 | <LoadConstString>: <Reg8: 1, string_id: 4741>  # String: '__BC:Collections/MapSetTests/setTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/setTest/end";
    // CODE → addr:208 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/setTest/end")
    // CODE → addr:213 | <Ret>: <Reg8: 0>
    return undefined;
}