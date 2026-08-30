function setTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4559>  # String: '__BC:Collections/MapSetTests/setTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/setTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/setTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 32>  # String: 'Set' (Identifier)
    // USED → r3 = Set;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = Set.prototype;
    // CODE → addr: 33 | <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = CreateThis(r0);
    // CODE → addr: 37 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 6, UInt16: 6, UInt16: 23684>  # Array: [1, 2, 2, 3, 3, 3]
    // USED → r10 = [1, 2, 2, 3, 3, 3];
    // CODE → addr: 45 | <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = CreateThis(r0);
    // CODE → addr: 48 | <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new Set([1, 2, 2, 3, 3, 3]);
    // CODE → addr: 52 | <SelectObject>: <Reg8: 3, Reg8: 2, Reg8: 0>
    r3 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr: 56 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 62 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 5, string_id: 226>  # String: 'size' (Identifier)
    // USED → r0 = r3.size;
    // CODE → addr: 72 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(r3.size)
    // CODE → addr: 77 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 6, string_id: 59>  # String: 'add' (Identifier)
    // USED → r2 = r3.add;
    // CODE → addr: 82 | <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → addr: 85 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = r3.add(4)
    // CODE → addr: 90 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 7, string_id: 153>  # String: 'has' (Identifier)
    // USED → r5 = r3.has;
    // CODE → addr:106 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:109 | <Call2>: <Reg8: 0, Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r0 = r3.has(2);
    // CODE → addr:114 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(r0)
    // CODE → addr:119 | <Mov>: <Reg8: 2, Reg8: 3>
    r2 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr:122 | <IteratorBegin>: <Reg8: 4, Reg8: 2>
    r4 = GetIterator(r2)
    // CODE → addr:125 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (for_of)
    for (const r7 of r2) {
        // ──────────────── Block 1 ──────────────── 
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:138 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r6 = console;
        // CODE → addr:144 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr:149 | <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
        console.log(r7)
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:163 | <NewArray>: <Reg8: 4, UInt16: 0>
    // USED → r4 = [];
    // CODE → addr:167 | <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → addr:169 | <Mov>: <Reg8: 10, Reg8: 4>
    r10 = r4
    // CODE → addr:172 | <Mov>: <Reg8: 9, Reg8: 3>
    r9 = new Set([1, 2, 2, 3, 3, 3])
    // CODE → addr:175 | <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = arraySpread(r-2, r-1, r0, r1)
    // CODE → addr:179 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:185 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:190 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr:195 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:201 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:206 | <LoadConstString>: <Reg8: 1, string_id: 4558>  # String: '__BC:Collections/MapSetTests/setTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/setTest/end";
    // CODE → addr:210 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/setTest/end")
    // CODE → addr:215 | <Ret>: <Reg8: 0>
    return undefined;
}