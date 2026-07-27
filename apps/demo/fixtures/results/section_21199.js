function function_21199(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r4 = globalThis.Object;
    // CODE → <GetById>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 12599>  # String: 'values' (Identifier)
    // USED → r3 = globalThis.Object.values;
    // CODE → <GetById>: <Reg8: 0, Reg8: 2, UInt8: 3, string_id: 12621>  # String: 'stats' (Identifier)
    // USED → r0 = param1.stats;
    // CODE → <Call2>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 0>
    // USED → r0 = globalThis.Object.values(param1.stats);
    // CODE → <Mov>: <Reg8: 4, Reg8: 0>
    // USED → r4 = globalThis.Object.values(param1.stats);
    // CODE → <IteratorBegin>: <Reg8: 3, Reg8: 4>
    // USED → r3 = GetIterator(globalThis.Object.values(param1.stats));
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 652>  # String: 'BODYWEIGHT' (String)
    // USED → r0 = "BODYWEIGHT";
    try {
        try {
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 1 ──────────────── 
                // CODE → <IteratorNext>: <Reg8: 10, Reg8: 3, Reg8: 4>
                // USED → r10 = GetIterator(globalThis.Object.values(param1.stats)).next();
                // CODE → <Mov>: <Reg8: 8, Reg8: 3>
                // USED → r8 = GetIterator(globalThis.Object.values(param1.stats));
                // CODE → <JStrictEqualLong>: <Addr32: 186, Reg8: 8, Reg8: 6>  # Address: 000000ed
                if (GetIterator(globalThis.Object.values(param1.stats)) === undefined) goto label_237;
                // ──────────────── Block 2 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
                // USED → r9 = globalThis.Object;
                // CODE → <GetById>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 12599>  # String: 'values' (Identifier)
                // USED → r8 = globalThis.Object.values;
                // CODE → <Call2>: <Reg8: 10, Reg8: 8, Reg8: 9, Reg8: 10>
                // USED → r10 = globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next());
                // CODE → <Mov>: <Reg8: 8, Reg8: 10>
                // USED → r8 = globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next());
                // CODE → <IteratorBegin>: <Reg8: 9, Reg8: 8>
                // USED → r9 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next()));
                // ──────────────── Block 13 ──────────────── 
                // CODE → <JmpLong>: <Addr32: -181>  # Address: 0000002c
                goto label_44;
                // LOOP → START (while)
                while (true) {
                    // ──────────────── Block 3 ──────────────── 
                    // CODE → <IteratorNext>: <Reg8: 10, Reg8: 9, Reg8: 8>
                    // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                    // CODE → <Mov>: <Reg8: 11, Reg8: 9>
                    // USED → r11 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next()));
                    // CODE → <JStrictEqualLong>: <Addr32: 137, Reg8: 11, Reg8: 6>  # Address: 000000e1
                    if (GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())) === undefined) goto label_225;
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <Mov>: <Reg8: 7, Reg8: 10>
                    // USED → r7 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                    // CODE → <GetById>: <Reg8: 10, Reg8: 10, UInt8: 4, string_id: 11997>  # String: 'weight' (Identifier)
                    // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight;
                    if (GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight) {
                        // ──────────────── Block 5 ──────────────── 
                        // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                        // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                        // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 5, string_id: 207>  # String: 'reps' (Identifier)
                        // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps;
                        if (GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps) {
                            // ──────────────── Block 6 ──────────────── 
                            // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                            // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                            // CODE → <GetById>: <Reg8: 10, Reg8: 10, UInt8: 6, string_id: 11855>  # String: 'logTime' (Identifier)
                            // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().logTime;
                            if (GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().logTime) {
                                // ──────────────── Block 7 ──────────────── 
                                // CODE → <TryGetById>: <Reg8: 11, Reg8: 5, UInt8: 7, string_id: 18858>  # String: 'isNaN' (Identifier)
                                // USED → r11 = globalThis.isNaN;
                                // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                                // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                                // CODE → <GetById>: <Reg8: 10, Reg8: 10, UInt8: 4, string_id: 11997>  # String: 'weight' (Identifier)
                                // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight;
                                // CODE → <Call2>: <Reg8: 10, Reg8: 11, Reg8: 6, Reg8: 10>
                                // USED → r10 = globalThis.isNaN.call(undefined, GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight);
                                if (!globalThis.isNaN.call(undefined, GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight)) {
                                    // ──────────────── Block 8 ──────────────── 
                                    // CODE → <TryGetById>: <Reg8: 11, Reg8: 5, UInt8: 7, string_id: 18858>  # String: 'isNaN' (Identifier)
                                    // USED → r11 = globalThis.isNaN;
                                    // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                                    // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                                    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 5, string_id: 207>  # String: 'reps' (Identifier)
                                    // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps;
                                    // CODE → <Call2>: <Reg8: 10, Reg8: 11, Reg8: 6, Reg8: 10>
                                    // USED → r10 = globalThis.isNaN.call(undefined, GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps);
                                    if (!globalThis.isNaN.call(undefined, GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps)) {
                                        // ──────────────── Block 9 ──────────────── 
                                        // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                                        // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                                        // CODE → <GetById>: <Reg8: 10, Reg8: 10, UInt8: 4, string_id: 11997>  # String: 'weight' (Identifier)
                                        // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight;
                                        if (GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight !== "BODYWEIGHT") {
                                            // ──────────────── Block 10 ──────────────── 
                                            // CODE → <Mov>: <Reg8: 11, Reg8: 1>
                                            // USED → r11 = 0;
                                            // CODE → <Mov>: <Reg8: 10, Reg8: 7>
                                            // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next();
                                            // CODE → <GetById>: <Reg8: 12, Reg8: 10, UInt8: 4, string_id: 11997>  # String: 'weight' (Identifier)
                                            // USED → r12 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight;
                                            // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 5, string_id: 207>  # String: 'reps' (Identifier)
                                            // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps;
                                            // CODE → <Mul>: <Reg8: 10, Reg8: 12, Reg8: 10>
                                            // USED → r10 = GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight * GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps;
                                            // CODE → <Add>: <Reg8: 1, Reg8: 11, Reg8: 10>
                                            // USED → r1 = 0 + GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight * GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    // ──────────────── Block 11 ──────────────── 
                    // CODE → <JmpLong>: <Addr32: -132>  # Address: 00000051
                    goto label_81;
                }
                // LOOP → END
            }
            // LOOP → END
        }
        catch (caughtException) {
            // ──────────────── Block 12 ──────────────── 
            // CODE → <IteratorClose>: <Reg8: 9, UInt8: 1>
            // Error: IteratorClose at address 220: Invalid arguments: Reg8: 9, UInt8: 1;
            // CODE → <Throw>: <Reg8: 8>
            throw caughtException;
        }
    }
    catch (caughtException) {
        // ──────────────── Block 14 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 3, UInt8: 1>
        // Error: IteratorClose at address 232: Invalid arguments: Reg8: 3, UInt8: 1;
        // CODE → <Throw>: <Reg8: 0>
        throw caughtException;
    }
    // ──────────────── Block 15 ──────────────── 
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 19019>  # String: 'createdAt' (Identifier)
    // USED → r2 = param1.createdAt;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 2, string_id: 109>  # String: 'date' (Identifier)
    // USED → r0 = { date: param1.createdAt };
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 1, string_id: 21499>  # String: 'totalWeight' (Identifier)
    // USED → r0 = { date: param1.createdAt, totalWeight: 0 + GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight * GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps };
    // CODE → <Ret>: <Reg8: 0>
    return { date: param1.createdAt, totalWeight: 0 + GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().weight * GetIterator(globalThis.Object.values(GetIterator(globalThis.Object.values(param1.stats)).next())).next().reps };
}