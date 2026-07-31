function nestedArrayDestructureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4967>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    r1 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 2, UInt16: 3>
    // USED → r2 = [];
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 42665>  # Array: [1, 2]
    // USED → r1 = [1, 2];
    // CODE → <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 0>
    [][0] = [1, 2]
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 48477>  # Array: [3, 4]
    // USED → r1 = [3, 4];
    // CODE → <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 1>
    [][1] = [3, 4]
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 15101>  # Array: [5, 6]
    // USED → r1 = [5, 6];
    // CODE → <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 2>
    [][2] = [5, 6]
    // CODE → <Mov>: <Reg8: 6, Reg8: 2>
    // USED → r6 = [];
    // CODE → <IteratorBegin>: <Reg8: 1, Reg8: 6>
    // USED → r1 = GetIterator([]);
    // CODE → <Mov>: <Reg8: 2, Reg8: 6>
    r2 = []
    // CODE → <IteratorNext>: <Reg8: 2, Reg8: 1, Reg8: 2>
    // USED → r2 = GetIterator([]).next();
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = GetIterator([]);
    // CODE → <StrictEq>: <Reg8: 4, Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator([]) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    if (GetIterator([]) !== undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        // USED → r5 = GetIterator([]).next();
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 11, Reg8: 5>
    // USED → r11 = GetIterator([]).next();
    // CODE → <IteratorBegin>: <Reg8: 2, Reg8: 11>
    // USED → r2 = GetIterator(GetIterator([]).next());
    // CODE → <Mov>: <Reg8: 5, Reg8: 11>
    r5 = GetIterator([]).next()
    // CODE → <IteratorNext>: <Reg8: 12, Reg8: 2, Reg8: 5>
    // USED → r12 = GetIterator(GetIterator([]).next()).next();
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = GetIterator(GetIterator([]).next());
    // CODE → <StrictEq>: <Reg8: 5, Reg8: 5, Reg8: 3>
    // USED → r5 = GetIterator(GetIterator([]).next()) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    if (GetIterator(GetIterator([]).next()) !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 9, Reg8: 12>
        // USED → r9 = GetIterator(GetIterator([]).next()).next();
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 9>
    // USED → r8 = GetIterator(GetIterator([]).next()).next();
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    if (GetIterator(GetIterator([]).next()) !== undefined) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <IteratorNext>: <Reg8: 12, Reg8: 2, Reg8: 11>
        // USED → r12 = GetIterator(GetIterator([]).next()).next();
        // CODE → <Mov>: <Reg8: 11, Reg8: 2>
        // USED → r11 = GetIterator(GetIterator([]).next());
        // CODE → <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 3>
        // USED → r11 = GetIterator(GetIterator([]).next()) === undefined;
        // CODE → <LoadConstUndefined>: <Reg8: 9>
        r9 = undefined
        // CODE → <Mov>: <Reg8: 5, Reg8: 11>
        r5 = GetIterator(GetIterator([]).next()) === undefined
        if (GetIterator(GetIterator([]).next()) !== undefined) {
            // ──────────────── Block 6 ──────────────── 
            // CODE → <Mov>: <Reg8: 9, Reg8: 12>
            // USED → r9 = GetIterator(GetIterator([]).next()).next();
            // CODE → <Mov>: <Reg8: 5, Reg8: 11>
            // USED → r5 = GetIterator(GetIterator([]).next()) === undefined;
        }
    }
    // ──────────────── Block 7 ──────────────── 
    // CODE → <Mov>: <Reg8: 7, Reg8: 9>
    // USED → r7 = GetIterator(GetIterator([]).next()).next();
    if (GetIterator(GetIterator([]).next()) !== undefined) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 2, UInt8: 0>
        GetIterator(GetIterator([]).next()).return()
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <Mov>: <Reg8: 5, Reg8: 4>
    r5 = GetIterator([]) === undefined
    if (GetIterator([]) !== undefined) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → <Mov>: <Reg8: 2, Reg8: 6>
        r2 = []
        // CODE → <IteratorNext>: <Reg8: 2, Reg8: 1, Reg8: 2>
        r2 = GetIterator([]).next()
        // CODE → <Mov>: <Reg8: 2, Reg8: 1>
        // USED → r2 = GetIterator([]);
        // CODE → <StrictEq>: <Reg8: 5, Reg8: 2, Reg8: 3>
        // USED → r5 = GetIterator([]) === undefined;
    }
    // ──────────────── Block 11 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → <Mov>: <Reg8: 2, Reg8: 5>
    r2 = GetIterator([]) === undefined
    if (GetIterator([]) !== undefined) {
        // ──────────────── Block 12 ──────────────── 
        // CODE → <IteratorNext>: <Reg8: 11, Reg8: 1, Reg8: 6>
        // USED → r11 = GetIterator([]).next();
        // CODE → <Mov>: <Reg8: 6, Reg8: 1>
        // USED → r6 = GetIterator([]);
        // CODE → <StrictEq>: <Reg8: 6, Reg8: 6, Reg8: 3>
        // USED → r6 = GetIterator([]) === undefined;
        // CODE → <LoadConstUndefined>: <Reg8: 9>
        r9 = undefined
        // CODE → <Mov>: <Reg8: 2, Reg8: 6>
        r2 = GetIterator([]) === undefined
        if (GetIterator([]) !== undefined) {
            // ──────────────── Block 13 ──────────────── 
            // CODE → <Mov>: <Reg8: 9, Reg8: 11>
            // USED → r9 = GetIterator([]).next();
            // CODE → <Mov>: <Reg8: 2, Reg8: 6>
            // USED → r2 = GetIterator([]) === undefined;
        }
    }
    // ──────────────── Block 14 ──────────────── 
    // CODE → <Mov>: <Reg8: 12, Reg8: 9>
    // USED → r12 = GetIterator([]).next();
    // CODE → <IteratorBegin>: <Reg8: 6, Reg8: 12>
    // USED → r6 = GetIterator(GetIterator([]).next());
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    r9 = GetIterator([]).next()
    // CODE → <IteratorNext>: <Reg8: 9, Reg8: 6, Reg8: 9>
    r9 = GetIterator(GetIterator([]).next()).next()
    // CODE → <Mov>: <Reg8: 9, Reg8: 6>
    // USED → r9 = GetIterator(GetIterator([]).next());
    // CODE → <StrictEq>: <Reg8: 9, Reg8: 9, Reg8: 3>
    // USED → r9 = GetIterator(GetIterator([]).next()) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 11>
    r11 = undefined
    if (GetIterator(GetIterator([]).next()) !== undefined) {
        // ──────────────── Block 15 ──────────────── 
        // CODE → <IteratorNext>: <Reg8: 13, Reg8: 6, Reg8: 12>
        // USED → r13 = GetIterator(GetIterator([]).next()).next();
        // CODE → <Mov>: <Reg8: 12, Reg8: 6>
        // USED → r12 = GetIterator(GetIterator([]).next());
        // CODE → <StrictEq>: <Reg8: 12, Reg8: 12, Reg8: 3>
        // USED → r12 = GetIterator(GetIterator([]).next()) === undefined;
        // CODE → <LoadConstUndefined>: <Reg8: 11>
        r11 = undefined
        // CODE → <Mov>: <Reg8: 9, Reg8: 12>
        r9 = GetIterator(GetIterator([]).next()) === undefined
        if (GetIterator(GetIterator([]).next()) !== undefined) {
            // ──────────────── Block 16 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 13>
            // USED → r11 = GetIterator(GetIterator([]).next()).next();
            // CODE → <Mov>: <Reg8: 9, Reg8: 12>
            // USED → r9 = GetIterator(GetIterator([]).next()) === undefined;
        }
    }
    // ──────────────── Block 17 ──────────────── 
    // CODE → <Mov>: <Reg8: 0, Reg8: 11>
    // USED → r0 = GetIterator(GetIterator([]).next()).next();
    if (GetIterator(GetIterator([]).next()) !== undefined) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → <Mov>: <Reg8: 9, Reg8: 6>
        // USED → r9 = GetIterator(GetIterator([]).next());
        // CODE → <IteratorClose>: <Reg8: 9, UInt8: 0>
        GetIterator(GetIterator([]).next()).return()
    }
    if (GetIterator([]) !== undefined) {
        // ──────────────── Block 20 ──────────────── 
        // CODE → <Mov>: <Reg8: 9, Reg8: 1>
        // USED → r9 = GetIterator([]);
        // CODE → <IteratorClose>: <Reg8: 9, UInt8: 0>
        GetIterator([]).return()
    }
    // ──────────────── Block 21 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 0, Reg8: 9, Reg8: 11, Reg8: 8, Reg8: 7, Reg8: 0>
    r0 = globalThis.console.log(GetIterator(GetIterator([]).next()).next(), GetIterator(GetIterator([]).next()).next(), GetIterator(GetIterator([]).next()).next())
    // CODE → <NewArrayWithBuffer>: <Reg8: 17, UInt16: 1, UInt16: 1, UInt16: 20024>  # Array: [10]
    // USED → r17 = [10];
    // CODE → <IteratorBegin>: <Reg8: 7, Reg8: 17>
    // USED → r7 = GetIterator([10]);
    // CODE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → <Mov>: <Reg8: 0, Reg8: 17>
    r0 = [10]
    // CODE → <IteratorNext>: <Reg8: 0, Reg8: 7, Reg8: 0>
    // USED → r0 = GetIterator([10]).next();
    // CODE → <Mov>: <Reg8: 8, Reg8: 7>
    // USED → r8 = GetIterator([10]);
    // CODE → <StrictEq>: <Reg8: 9, Reg8: 8, Reg8: 3>
    // USED → r9 = GetIterator([10]) === undefined;
    if (GetIterator([10]) === undefined) {
        // ──────────────── Block 23 ──────────────── 
        // CODE → <LoadConstZero>: <Reg8: 12>
        // USED → r12 = 0;
    } else {
        // ──────────────── Block 22 ──────────────── 
        // CODE → <Mov>: <Reg8: 12, Reg8: 0>
        r12 = GetIterator([10]).next()
        // CODE → <JStrictNotEqual>: <Addr8: 6, Reg8: 0, Reg8: 3>  # Address: 0000015d
        if (GetIterator([10]).next() !== undefined) goto label_349;
    }
    // ──────────────── Block 24 ──────────────── 
    // CODE → <Mov>: <Reg8: 15, Reg8: 12>
    // USED → r15 = 0;
    // CODE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → <Mov>: <Reg8: 11, Reg8: 9>
    r11 = GetIterator([10]) === undefined
    // CODE → <JmpTrue>: <Addr8: 29, Reg8: 9>  # Address: 00000182
    if (GetIterator([10]) === undefined) goto label_386;
    // ──────────────── Block 25 ──────────────── 
    // CODE → <Mov>: <Reg8: 0, Reg8: 17>
    r0 = [10]
    // CODE → <IteratorNext>: <Reg8: 13, Reg8: 7, Reg8: 0>
    // USED → r13 = GetIterator([10]).next();
    // CODE → <Mov>: <Reg8: 0, Reg8: 7>
    // USED → r0 = GetIterator([10]);
    // CODE → <StrictEq>: <Reg8: 0, Reg8: 0, Reg8: 3>
    // USED → r0 = GetIterator([10]) === undefined;
    // CODE → <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = GetIterator([10]) === undefined;
    // CODE → <JmpTrue>: <Addr8: 22, Reg8: 8>  # Address: 0000018f
    if (GetIterator([10]) === undefined) goto label_399;
    // ──────────────── Block 26 ──────────────── 
    // CODE → <Mov>: <Reg8: 12, Reg8: 13>
    // USED → r12 = GetIterator([10]).next();
    // CODE → <Mov>: <Reg8: 11, Reg8: 0>
    // USED → r11 = GetIterator([10]) === undefined;
    // ──────────────── Block 27 ──────────────── 
    // CODE → <Mov>: <Reg8: 0, Reg8: 12>
    // USED → r0 = GetIterator([10]).next();
    // CODE → <Mov>: <Reg8: 8, Reg8: 11>
    // USED → r8 = GetIterator([10]) === undefined;
    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
    r11 = GetIterator([10]) === undefined
    if (GetIterator([10]).next() === undefined) {
        // ──────────────── Block 28 ──────────────── 
        // CODE → <LoadConstZero>: <Reg8: 12>
        // USED → r12 = 0;
        // CODE → <Mov>: <Reg8: 11, Reg8: 8>
        // USED → r11 = GetIterator([10]) === undefined;
        // CODE → <Jmp>: <Addr8: 6>  # Address: 0000019a
        goto label_410;
    }
    // ──────────────── Block 30 ──────────────── 
    // CODE → <Mov>: <Reg8: 14, Reg8: 12>
    // USED → r14 = 0;
    // CODE → <NewArray>: <Reg8: 13, UInt16: 0>
    // USED → r13 = [];
    // CODE → <LoadConstUInt8>: <Reg8: 12, UInt8: 1>
    // USED → r12 = 1;
    // CODE → <LoadConstZero>: <Reg8: 16>
    // USED → r16 = 0;
    if (GetIterator([10]) !== undefined) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 31 ──────────────── 
            // CODE → <Mov>: <Reg8: 11, Reg8: 17>
            r11 = [10]
            // CODE → <IteratorNext>: <Reg8: 19, Reg8: 7, Reg8: 11>
            // USED → r19 = GetIterator([10]).next();
            // CODE → <Mov>: <Reg8: 11, Reg8: 7>
            // USED → r11 = GetIterator([10]);
            // CODE → <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 3>
            // USED → r11 = GetIterator([10]) === undefined;
            // CODE → <Mov>: <Reg8: 18, Reg8: 16>
            // USED → r18 = 0;
            // CODE → <JmpTrue>: <Addr8: 20, Reg8: 11>  # Address: 000001ce
            if (GetIterator([10]) === undefined) goto label_462;
            // ──────────────── Block 32 ──────────────── 
            // CODE → <PutByValStrict>: <Reg8: 13, Reg8: 18, Reg8: 19>
            [][0] = GetIterator([10]).next()
            // CODE → <AddN>: <Reg8: 16, Reg8: 18, Reg8: 12>
            r16 = 0 + 1
            // CODE → <Jmp>: <Addr8: -28>  # Address: 000001a9
            goto label_425;
        }
        // LOOP → END
    }
    // ──────────────── Block 34 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 15, Reg8: 14, Reg8: 13>
    r11 = globalThis.console.log(0, 0, [])
    // CODE → <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 4966>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end' (String)
    // USED → r10 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end";
    // CODE → <Call2>: <Reg8: 10, Reg8: 11, Reg8: 12, Reg8: 10>
    r10 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end")
    // CODE → <Ret>: <Reg8: 3>
    return undefined;
    // CODE → <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → <Mov>: <Reg8: 8, Reg8: 9>
    // USED → r8 = GetIterator([10]) === undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 37 ──────────────── 
        // CODE → <Throw>: <Reg8: 0>
        throw caughtException;
        // CODE → <Catch>: <Reg8: 0>
        // USED → r0 = caughtException;
        // CODE → <IteratorClose>: <Reg8: 6, UInt8: 1>
        GetIterator(GetIterator([]).next()).return()
        // CODE → <Throw>: <Reg8: 0>
        throw caughtException;
        // CODE → <Catch>: <Reg8: 0>
        r0 = caughtException
        // CODE → <Jmp>: <Addr8: 20>  # Address: 00000220
        goto label_544;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 36 ──────────────── 
            // CODE → <IteratorClose>: <Reg8: 7, UInt8: 1>
            GetIterator([10]).return()
            // LOOP → START (while)
            while (GetIterator([10]) === undefined) {
                // ──────────────── Block 35 ──────────────── 
                // CODE → <JmpTrue>: <Addr8: 6, Reg8: 8>  # Address: 00000201
                if (GetIterator([10]) === undefined) goto label_513;
                // ──────────────── Block 29 ──────────────── 
                // CODE → <Catch>: <Reg8: 0>
                r0 = caughtException
                // CODE → <Jmp>: <Addr8: 99>  # Address: 000001fb
                goto label_507;
                // ──────────────── Block 33 ──────────────── 
                // CODE → <Catch>: <Reg8: 0>
                r0 = caughtException
                // CODE → <Mov>: <Reg8: 8, Reg8: 11>
                r8 = GetIterator([10]) === undefined
                // CODE → <Jmp>: <Addr8: 47>  # Address: 000001fb
                goto label_507;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // LOOP → END
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 43 ──────────────── 
        // CODE → <Throw>: <Reg8: 0>
        throw caughtException;
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 42 ──────────────── 
            // CODE → <IteratorClose>: <Reg8: 1, UInt8: 1>
            GetIterator([]).return()
            // LOOP → START (while)
            while (undefined) {
                // ──────────────── Block 41 ──────────────── 
                // CODE → <JmpTrue>: <Addr8: 6, Reg8: 2>  # Address: 00000226
                if (undefined) goto label_550;
                // ──────────────── Block 38 ──────────────── 
                // CODE → <Catch>: <Reg8: 0>
                r0 = caughtException
                // CODE → <Mov>: <Reg8: 2, Reg8: 5>
                r2 = GetIterator([]) === undefined
                // CODE → <Jmp>: <Addr8: 13>  # Address: 00000220
                goto label_544;
                // ──────────────── Block 39 ──────────────── 
                // CODE → <Catch>: <Reg8: 0>
                r0 = caughtException
                // CODE → <Mov>: <Reg8: 2, Reg8: 4>
                r2 = GetIterator([]) === undefined
                // CODE → <Jmp>: <Addr8: 6>  # Address: 00000220
                goto label_544;
                // ──────────────── Block 40 ──────────────── 
                // CODE → <Catch>: <Reg8: 0>
                // USED → r0 = caughtException;
                // CODE → <LoadConstUndefined>: <Reg8: 2>
                // USED → r2 = undefined;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // LOOP → END
}