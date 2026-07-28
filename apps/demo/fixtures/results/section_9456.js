function spreadArrayTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4696>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadArrayTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start");
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    // USED → r3 = [1, 2, 3];
    // CODE → <NewArray>: <Reg8: 0, UInt16: 0>
    // USED → r0 = [];
    // CODE → <Mov>: <Reg8: 13, Reg8: 0>
    r13 = [];
    // CODE → <Mov>: <Reg8: 12, Reg8: 3>
    r12 = [1, 2, 3];
    // CODE → <LoadConstZero>: <Reg8: 11>
    r11 = 0;
    // CODE → <CallBuiltin>: <Reg8: 11, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r11 = builtin_48(r7, r8, r9, r10);
    // CODE → <NewArrayWithBuffer>: <Reg8: 12, UInt16: 3, UInt16: 3, UInt16: 12638>  # Array: [4, 5, 6]
    r12 = [4, 5, 6];
    // CODE → <Mov>: <Reg8: 13, Reg8: 0>
    r13 = [];
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r4 = builtin_48(r0, r1, r2, r3);
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 0>
    r4 = globalThis.console.log([]);
    // CODE → <NewArrayWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 1, UInt16: 17242>  # Array: [0]
    // USED → r5 = [0];
    // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    // USED → r8 = 1;
    // CODE → <Mov>: <Reg8: 13, Reg8: 5>
    r13 = [0];
    // CODE → <Mov>: <Reg8: 12, Reg8: 3>
    r12 = [1, 2, 3];
    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
    r11 = 1;
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    // USED → r4 = builtin_48(r0, r1, r2, r3);
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 99>
    // USED → r3 = 99;
    // CODE → <DefineOwnByVal>: <Reg8: 5, Reg8: 3, Reg8: 4, UInt8: 1>
    [0][builtin_48(r0, r1, r2, r3)] = 99;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    r3 = globalThis.console.log([0]);
    // CODE → <Mov>: <Reg8: 7, Reg8: 0>
    // USED → r7 = [];
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 7>
    // USED → r3 = GetIterator([]);
    // CODE → <Mov>: <Reg8: 0, Reg8: 7>
    r0 = [];
    // CODE → <IteratorNext>: <Reg8: 4, Reg8: 3, Reg8: 0>
    // USED → r4 = GetIterator([]).next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = GetIterator([]);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <StrictEq>: <Reg8: 6, Reg8: 5, Reg8: 0>
    // USED → r6 = GetIterator([]) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined;
    if (GetIterator([]) !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator([]).next();
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewArray>: <Reg8: 4, UInt16: 0>
    // USED → r4 = [];
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    if (GetIterator([]) !== undefined) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → <Mov>: <Reg8: 6, Reg8: 7>
            r6 = [];
            // CODE → <IteratorNext>: <Reg8: 10, Reg8: 3, Reg8: 6>
            // USED → r10 = GetIterator([]).next();
            // CODE → <Mov>: <Reg8: 6, Reg8: 3>
            // USED → r6 = GetIterator([]);
            // CODE → <StrictEq>: <Reg8: 6, Reg8: 6, Reg8: 0>
            // USED → r6 = GetIterator([]) === undefined;
            // CODE → <Mov>: <Reg8: 9, Reg8: 2>
            // USED → r9 = 0;
            // CODE → <JmpTrue>: <Addr8: 23, Reg8: 6>  # Address: 000000cc
            if (GetIterator([]) === undefined) goto label_204;
            // ──────────────── Block 4 ──────────────── 
            // CODE → <PutByValStrict>: <Reg8: 4, Reg8: 9, Reg8: 10>
            [][0] = GetIterator([]).next();
            // CODE → <AddN>: <Reg8: 2, Reg8: 9, Reg8: 8>
            r2 = 0 + 1;
            // CODE → <Jmp>: <Addr8: -28>  # Address: 000000a4
            goto label_164;
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
                GetIterator([]).return();
                // ──────────────── Block 5 ──────────────── 
                // CODE → <Catch>: <Reg8: 2>
                // USED → r2 = caughtException;
                // CODE → <JmpTrue>: <Addr8: 6, Reg8: 6>  # Address: 000000ca
                if (GetIterator([]) === undefined) goto label_202;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log(GetIterator([]).next(), []);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4695>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadArrayTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end");
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}