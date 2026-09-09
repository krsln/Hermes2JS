function spreadArrayTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4718>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadArrayTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    r3 = [1, 2, 3]
    // CODE → addr: 30 | <NewArray>: <Reg8: 0, UInt16: 0>
    r0 = []
    // CODE → addr: 34 | <Mov>: <Reg8: 13, Reg8: 0>
    r13 = r0
    // CODE → addr: 37 | <Mov>: <Reg8: 12, Reg8: 3>
    r12 = r3
    // CODE → addr: 40 | <LoadConstZero>: <Reg8: 11>
    r11 = 0
    // CODE → addr: 42 | <CallBuiltin>: <Reg8: 11, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r11 = arraySpread(r13, r12, r11, r10)
    // CODE → addr: 46 | <NewArrayWithBuffer>: <Reg8: 12, UInt16: 3, UInt16: 3, UInt16: 11325>  # Array: [4, 5, 6]
    r12 = [4, 5, 6]
    // CODE → addr: 54 | <Mov>: <Reg8: 13, Reg8: 0>
    r13 = r0
    // CODE → addr: 57 | <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r4 = arraySpread(r13, r12, r11, r10)
    // CODE → addr: 61 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 72 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 0>
    console.log(r0)
    // CODE → addr: 77 | <NewArrayWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 1, UInt16: 17298>  # Array: [0]
    r5 = [0]
    // CODE → addr: 85 | <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    // USED → r8 = 1;
    // CODE → addr: 88 | <Mov>: <Reg8: 13, Reg8: 5>
    r13 = r5
    // CODE → addr: 91 | <Mov>: <Reg8: 12, Reg8: 3>
    r12 = r3
    // CODE → addr: 94 | <Mov>: <Reg8: 11, Reg8: 8>
    r11 = 1
    // CODE → addr: 97 | <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r4 = arraySpread(r13, r12, r11, r10)
    // CODE → addr:101 | <LoadConstUInt8>: <Reg8: 3, UInt8: 99>
    // USED → r3 = 99;
    // CODE → addr:104 | <DefineOwnByVal>: <Reg8: 5, Reg8: 3, Reg8: 4, UInt8: 1>
    r5[r4] = 99
    // CODE → addr:109 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:120 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → addr:125 | <Mov>: <Reg8: 7, Reg8: 0>
    r7 = r0
    // CODE → addr:128 | <IteratorBegin>: <Reg8: 3, Reg8: 7>
    r3 = GetIterator(r7)
    // CODE → addr:134 | <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 0>
    r4 = r3.next()
    // CODE → addr:141 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:143 | <StrictEq>: <Reg8: 6, Reg8: 5, Reg8: 0>
    // USED → r6 = r3 === undefined;
    // CODE → addr:147 | <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // → r3 = GetIterator(r7)
    if (r3 !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:152 | <Mov>: <Reg8: 5, Reg8: 4>
        r5 = r4
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:155 | <NewArray>: <Reg8: 4, UInt16: 0>
    r4 = []
    // CODE → addr:159 | <LoadConstZero>: <Reg8: 2>
    r2 = 0
    if (r3 !== undefined) {
        // LOOP → START (while)
        // → r6 = r6 === undefined
        while (!r6) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr:167 | <IteratorNext>: <Reg8: 10, Reg8: 3, Reg8: 6>
            r10 = r3.next()
            // CODE → addr:171 | <Mov>: <Reg8: 6, Reg8: 3>
            r6 = r3
            // CODE → addr:174 | <StrictEq>: <Reg8: 6, Reg8: 6, Reg8: 0>
            r6 = r6 === undefined
            // CODE → addr:178 | <Mov>: <Reg8: 9, Reg8: 2>
            r9 = r2
            // ──────────────── Block 4 ──────────────── 
            // CODE → addr:184 | <PutByValStrict>: <Reg8: 4, Reg8: 9, Reg8: 10>
            r4[r9] = r10
            // CODE → addr:188 | <AddN>: <Reg8: 2, Reg8: 9, Reg8: 8>
            r2 = r9 + 1
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 7 ──────────────── 
            // CODE → addr:202 | <Throw>: <Reg8: 2>
            throw caughtException;
            // LOOP → START (for)
            for (; !(r6 === undefined); ) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → addr:199 | <IteratorClose>: <Reg8: 3, UInt8: 1>
                r3.return()
                // ──────────────── Block 5 ──────────────── 
                // CODE → addr:194 | <Catch>: <Reg8: 2>
                // USED → r2 = caughtException;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:204 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:210 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:215 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r5, r4)
    // CODE → addr:221 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:227 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:232 | <LoadConstString>: <Reg8: 1, string_id: 4717>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadArrayTest/end";
    // CODE → addr:236 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end")
    // CODE → addr:241 | <Ret>: <Reg8: 0>
    return undefined;
}