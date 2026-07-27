function mapObject(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 1>
    // USED → r8 = param1;
    // CODE → <LoadParam>: <Reg8: 9, UInt8: 2>
    // USED → r9 = param2;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 10>
    r10 = undefined;
    // CODE → <NewArray>: <Reg8: 1, UInt16: 0>
    // USED → r1 = [];
    // CODE → <LoadConstTrue>: <Reg8: 4>
    r4 = true;
    // CODE → <LoadConstFalse>: <Reg8: 2>
    r2 = false;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined;
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 13, Reg8: 5, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r13 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 167>  # String: 'keys' (Identifier)
    // USED → r12 = globalThis.Object.keys;
    // CODE → <Mov>: <Reg8: 11, Reg8: 8>
    // USED → r11 = param1;
    // CODE → <Call2>: <Reg8: 11, Reg8: 12, Reg8: 13, Reg8: 11>
    // USED → r11 = globalThis.Object.keys(param1);
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 52>  # String: 'Symbol' (Identifier)
    // USED → r5 = globalThis.Symbol;
    // CODE → <GetById>: <Reg8: 5, Reg8: 5, UInt8: 4, string_id: 13658>  # String: 'iterator' (Identifier)
    // USED → r5 = globalThis.Symbol.iterator;
    // CODE → <GetByVal>: <Reg8: 5, Reg8: 11, Reg8: 5>
    // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator];
    // CODE → <Call1>: <Reg8: 11, Reg8: 5, Reg8: 11>
    // USED → r11 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
    // CODE → <Mov>: <Reg8: 3, Reg8: 11>
    // USED → r3 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 11, UInt8: 5, string_id: 184>  # String: 'next' (Identifier)
    // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next;
    // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 11>
    // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next();
    // CODE → <Mov>: <Reg8: 10, Reg8: 5>
    // USED → r10 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next();
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 6, string_id: 118>  # String: 'done' (Identifier)
    // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done;
    // CODE → <Mov>: <Reg8: 4, Reg8: 5>
    r4 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done;
    try {
        if (!globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <Mov>: <Reg8: 5, Reg8: 10>
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next();
            // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 5, UInt8: 7, string_id: 249>  # String: 'value' (Identifier)
            // USED → r14 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value;
            // CODE → <Mov>: <Reg8: 5, Reg8: 8>
            // USED → r5 = param1;
            // CODE → <GetByVal>: <Reg8: 13, Reg8: 5, Reg8: 14>
            // USED → r13 = param1[globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value];
            // CODE → <Mov>: <Reg8: 12, Reg8: 1>
            // USED → r12 = [];
            // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 8, string_id: 201>  # String: 'push' (Identifier)
            // USED → r11 = [].push;
            // CODE → <Mov>: <Reg8: 5, Reg8: 9>
            // USED → r5 = param2;
            // CODE → <Call3>: <Reg8: 5, Reg8: 5, Reg8: 7, Reg8: 14, Reg8: 13>
            // USED → r5 = param2.call(undefined, globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value, param1[globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value]);
            // CODE → <Call2>: <Reg8: 5, Reg8: 11, Reg8: 12, Reg8: 5>
            r5 = [].push(param2.call(undefined, globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value, param1[globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().value]));
            // CODE → <LoadConstTrue>: <Reg8: 4>
            r4 = true;
            // CODE → <Mov>: <Reg8: 11, Reg8: 3>
            // USED → r11 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 11, UInt8: 5, string_id: 184>  # String: 'next' (Identifier)
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next;
            // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 11>
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next();
            // CODE → <Mov>: <Reg8: 10, Reg8: 5>
            r10 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next();
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 6, string_id: 118>  # String: 'done' (Identifier)
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done;
            // CODE → <Mov>: <Reg8: 4, Reg8: 5>
            // USED → r4 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done;
            // CODE → <JmpFalse>: <Addr8: -62, Reg8: 5>  # Address: 00000059
            if (!globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done) goto label_89;
        }
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Jmp>: <Addr8: 6>  # Address: 000000a0
        goto label_160;
    }
    catch (caughtException) {
        try {
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <Mov>: <Reg8: 5, Reg8: 4>
                // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done;
                // CODE → <JmpTrue>: <Addr8: 26, Reg8: 5>  # Address: 000000bd
                if (globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done) goto label_189;
                // ──────────────── Block 3 ──────────────── 
                // CODE → <LoadConstTrue>: <Reg8: 2>
                // USED → r2 = true;
            }
            // LOOP → END
            // ──────────────── Block 5 ──────────────── 
            // CODE → <Mov>: <Reg8: 5, Reg8: 3>
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 5, UInt8: 9, string_id: 209>  # String: 'return' (Identifier)
            // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return;
            if (globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → <Mov>: <Reg8: 6, Reg8: 3>
                // USED → r6 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
                // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 9, string_id: 209>  # String: 'return' (Identifier)
                // USED → r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return;
                // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 6>
                r5 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return();
            }
            // ──────────────── Block 7 ──────────────── 
            // CODE → <Mov>: <Reg8: 5, Reg8: 2>
            // USED → r5 = true;
        }
        catch (caughtException) {
            if (true) {
                // ──────────────── Block 9 ──────────────── 
                // CODE → <Mov>: <Reg8: 1, Reg8: 0>
                // USED → r1 = caughtException;
                // CODE → <Throw>: <Reg8: 1>
                throw caughtException;
                // LOOP → START (while)
                while (true) {
                    // ──────────────── Block 11 ──────────────── 
                    // CODE → <Throw>: <Reg8: 1>
                    throw caughtException;
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
                    // USED → r5 = true;
                    // CODE → <JmpTrue>: <Addr8: 5, Reg8: 5>  # Address: 000000d4
                    if (true) goto label_212;
                }
                // LOOP → END
                // LOOP → START (while)
                while (true) {
                    // ──────────────── Block 12 ──────────────── 
                    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
                    // USED → r1 = caughtException;
                    // CODE → <Throw>: <Reg8: 1>
                    throw caughtException;
                }
                // LOOP → END
                try {
                    // LOOP → START (while)
                    while (true) {
                        // ──────────────── Block 17 ──────────────── 
                        // CODE → <Throw>: <Reg8: 1>
                        throw caughtException;
                        // ──────────────── Block 13 ──────────────── 
                        // CODE → <Catch>: <Reg8: 1>
                        // USED → r1 = caughtException;
                        if (!globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().next().done) {
                            // ──────────────── Block 14 ──────────────── 
                            // CODE → <Mov>: <Reg8: 4, Reg8: 3>
                            // USED → r4 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
                            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 9, string_id: 209>  # String: 'return' (Identifier)
                            // USED → r4 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return;
                            if (globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return) {
                                // ──────────────── Block 15 ──────────────── 
                                // CODE → <Mov>: <Reg8: 4, Reg8: 3>
                                // USED → r4 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]();
                                // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 9, string_id: 209>  # String: 'return' (Identifier)
                                // USED → r3 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return;
                                // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 4>
                                r3 = globalThis.Object.keys(param1)[globalThis.Symbol.iterator]().return();
                            }
                        }
                        // ──────────────── Block 16 ──────────────── 
                        // CODE → <Mov>: <Reg8: 3, Reg8: 2>
                        // USED → r3 = true;
                        // CODE → <JmpTrue>: <Addr8: 5, Reg8: 3>  # Address: 000000fd
                        if (true) goto label_253;
                    }
                    // LOOP → END
                    // LOOP → START (while)
                    while (true) {
                        // ──────────────── Block 18 ──────────────── 
                        // CODE → <Mov>: <Reg8: 1, Reg8: 0>
                        // USED → r1 = caughtException;
                        // CODE → <Throw>: <Reg8: 1>
                        throw caughtException;
                        // LOOP → START (while)
                        while (true) {
                            // LOOP → START (while)
                            while (true) {
                                // LOOP → START (while)
                                while (true) {
                                }
                                // LOOP → END
                            }
                            // LOOP → END
                        }
                        // LOOP → END
                    }
                    // LOOP → END
                }
                catch (caughtException) {
                    // LOOP → START (while)
                    while (true) {
                        // ──────────────── Block 20 ──────────────── 
                        // CODE → <Throw>: <Reg8: 1>
                        throw caughtException;
                        // ──────────────── Block 19 ──────────────── 
                        // CODE → <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 00000109
                        if (true) goto label_265;
                    }
                    // LOOP → END
                    // LOOP → START (while)
                    while (true) {
                        // ──────────────── Block 21 ──────────────── 
                        // CODE → <Throw>: <Reg8: 0>
                        throw caughtException;
                    }
                    // LOOP → END
                }
            } else {
                // ──────────────── Block 8 ──────────────── 
                // CODE → <Ret>: <Reg8: 1>
                return [];
            }
        }
    }
}