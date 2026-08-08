function spreadArrayTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4718>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadArrayTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    r3 = [1, 2, 3]
    // CODE → <NewArray>: <Reg8: 0, UInt16: 0>
    r0 = []
    // CODE → <Mov>: <Reg8: 13, Reg8: 0>
    r13 = r0
    // CODE → <Mov>: <Reg8: 12, Reg8: 3>
    r12 = r3
    // CODE → <LoadConstZero>: <Reg8: 11>
    r11 = 0
    // CODE → <CallBuiltin>: <Reg8: 11, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r11 = applyArguments(r7, r8, r9, r10)
    // CODE → <NewArrayWithBuffer>: <Reg8: 12, UInt16: 3, UInt16: 3, UInt16: 11325>  # Array: [4, 5, 6]
    r12 = [4, 5, 6]
    // CODE → <Mov>: <Reg8: 13, Reg8: 0>
    r13 = r0
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r4 = applyArguments(r0, r1, r2, r3)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 0>
    r4 = globalThis.console.log(r0)
    // CODE → <NewArrayWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 1, UInt16: 17298>  # Array: [0]
    r5 = [0]
    // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    // USED → r8 = 1;
    // CODE → <Mov>: <Reg8: 13, Reg8: 5>
    r13 = r5
    // CODE → <Mov>: <Reg8: 12, Reg8: 3>
    r12 = r3
    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
    r11 = 1
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    // USED → r4 = applyArguments(r0, r1, r2, r3);
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 99>
    // USED → r3 = 99;
    // CODE → <DefineOwnByVal>: <Reg8: 5, Reg8: 3, Reg8: 4, UInt8: 1>
    r5[applyArguments(r0, r1, r2, r3)] = 99
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    r3 = globalThis.console.log(r5)
    // CODE → <Mov>: <Reg8: 7, Reg8: 0>
    // USED → r7 = r0;
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 7>
    // USED → r3 = GetIterator(r7);
    // CODE → <Mov>: <Reg8: 0, Reg8: 7>
    r0 = r0
    // CODE → <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 0>
    // USED → r4 = GetIterator(r7).next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = GetIterator(r7);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <StrictEq>: <Reg8: 6, Reg8: 5, Reg8: 0>
    // USED → r6 = GetIterator(r7) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = (GetIterator(r7) === undefined) ? undefined : GetIterator(r7).next()
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewArray>: <Reg8: 4, UInt16: 0>
    r4 = []
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    if (GetIterator(r7) !== undefined) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → <Mov>: <Reg8: 6, Reg8: 7>
            r6 = r0
            // CODE → <IteratorNext>: <Reg8: 10, Reg8: 3, Reg8: 6>
            // USED → r10 = (GetIterator(r7) === undefined) ? undefined : GetIterator(r7).next();
            // CODE → <Mov>: <Reg8: 6, Reg8: 3>
            // USED → r6 = GetIterator(r7);
            // CODE → <StrictEq>: <Reg8: 6, Reg8: 6, Reg8: 0>
            // USED → r6 = GetIterator(r7) === undefined;
            // CODE → <Mov>: <Reg8: 9, Reg8: 2>
            // USED → r9 = 0;
            if (GetIterator(r7) !== undefined) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <PutByValStrict>: <Reg8: 4, Reg8: 9, Reg8: 10>
                r4[0] = (GetIterator(r7) === undefined) ? undefined : GetIterator(r7).next()
                // CODE → <AddN>: <Reg8: 2, Reg8: 9, Reg8: 8>
                r2 = 0 + 1
                // CODE → <Jmp>: <Addr8: -28>  # Address: 000000a4
                goto label_164;
            }
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Throw>: <Reg8: 2>
            throw caughtException;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
                GetIterator(r7).return()
                // ──────────────── Block 5 ──────────────── 
                // CODE → <Catch>: <Reg8: 2>
                // USED → r2 = caughtException;
                // CODE → <JmpTrue>: <Addr8: 6, Reg8: 6>  # Address: 000000ca
                if (GetIterator(r7) === undefined) goto label_202;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log((GetIterator(r7) === undefined) ? undefined : GetIterator(r7).next(), r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4717>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadArrayTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}