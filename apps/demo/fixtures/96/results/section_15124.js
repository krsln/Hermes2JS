function setTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4559>  # String: '__BC:Collections/MapSetTests/setTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/setTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Collections/MapSetTests/setTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 32>  # String: 'Set' (Identifier)
    // USED → r3 = globalThis.Set;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r0 = globalThis.Set.prototype;
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 0, Reg8: 3>
    // USED → r2 = createThis(globalThis.Set.prototype, globalThis.Set);
    // CODE → <NewArrayWithBuffer>: <Reg8: 10, UInt16: 6, UInt16: 6, UInt16: 23684>  # Array: [1, 2, 2, 3, 3, 3]
    // USED → r10 = [1, 2, 2, 3, 3, 3];
    // CODE → <Mov>: <Reg8: 11, Reg8: 2>
    r11 = createThis(globalThis.Set.prototype, globalThis.Set)
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3]);
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 2, Reg8: 0>
    // USED → r3 = new globalThis.Set([1, 2, 2, 3, 3, 3]);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 5, string_id: 226>  # String: 'size' (Identifier)
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3]).size;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    r0 = globalThis.console.log(new globalThis.Set([1, 2, 2, 3, 3, 3]).size)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 6, string_id: 59>  # String: 'add' (Identifier)
    // USED → r2 = new globalThis.Set([1, 2, 2, 3, 3, 3]).add;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = new globalThis.Set([1, 2, 2, 3, 3, 3]).add(4)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 7, string_id: 153>  # String: 'has' (Identifier)
    // USED → r5 = new globalThis.Set([1, 2, 2, 3, 3, 3]).has;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <Call2>: <Reg8: 0, Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3]).has(2);
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    r0 = globalThis.console.log(new globalThis.Set([1, 2, 2, 3, 3, 3]).has(2))
    // CODE → <Mov>: <Reg8: 2, Reg8: 3>
    // USED → r2 = new globalThis.Set([1, 2, 2, 3, 3, 3]);
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 2>
    // USED → r4 = GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3]));
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 2>
            // USED → r7 = GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3])).next();
            // CODE → <Mov>: <Reg8: 5, Reg8: 4>
            // USED → r5 = GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3]));
            // CODE → <JStrictEqual>: <Addr8: 29, Reg8: 5, Reg8: 0>  # Address: 000000a3
            if (GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3])) === undefined) goto label_163;
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
            r5 = globalThis.console.log(GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3])).next())
            // CODE → <Jmp>: <Addr8: -27>  # Address: 0000007f
            goto label_127;
        }
        // LOOP → END
    } finally {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
        GetIterator(new globalThis.Set([1, 2, 2, 3, 3, 3])).return()
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <NewArray>: <Reg8: 4, UInt16: 0>
    // USED → r4 = [];
    // CODE → <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    r10 = []
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = new globalThis.Set([1, 2, 2, 3, 3, 3])
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = arraySpread(r-2, r-1, r0, r1)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    r2 = globalThis.console.log([])
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4558>  # String: '__BC:Collections/MapSetTests/setTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/setTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Collections/MapSetTests/setTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}