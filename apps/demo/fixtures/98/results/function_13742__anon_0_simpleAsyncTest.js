function ?anon_0_simpleAsyncTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 2>
    // USED → r0 = r1[2];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[2];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    if (r0 === 2) {
        // ──────────────── Block 19 ──────────────── 
        // CODE → addr:327 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:330 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:333 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
        r1[2] = 3
        // CODE → addr:337 | <LoadConstString>: <Reg8: 12, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r12 = "Generator functions may not be called on executing generators"
        // CODE → addr:341 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r12, r11)
    } else if (r5 === 3) {
        // ──────────────── Block 14 ──────────────── 
        // CODE → addr:294 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // Switch → START
        switch (param1) {
            case 1:
                // ──────────────── Block 18 ──────────────── 
                // CODE → addr:325 | <Throw>: <Reg8: 0>
                throw param2;
            case 2:
                // ──────────────── Block 17 ──────────────── 
                // CODE → addr:313 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:319 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                r3.slot_0 = param2
                // CODE → addr:323 | <Ret>: <Reg8: 3>
                return r3;
            default:
                // ──────────────── Block 16 ──────────────── 
                // CODE → addr:305 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:311 | <Ret>: <Reg8: 3>
                return r3;
        }
        // Switch → END
    } else {
        try {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
            r2 = 2
            // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 4>
            r1[2] = 2
            // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 1>
            r5 = r1[1]
            // CODE → addr: 50 | <LoadConstZero>: <Reg8: 9>
            // USED → r9 = 0;
            if (0 === r5) {
                // ──────────────── Block 8 ──────────────── 
                // CODE → addr:168 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
                // USED → r5 = 1;
                // Switch → START
                switch (param1) {
                    case 1:
                        // ──────────────── Block 12 ──────────────── 
                        // CODE → addr:281 | <Throw>: <Reg8: 0>
                        throw param2;
                    case 2:
                        // ──────────────── Block 11 ──────────────── 
                        // CODE → addr:262 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r5 = { "value": null, "done": true }
                        // CODE → addr:268 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                        r5.slot_0 = param2
                        // CODE → addr:272 | <Ret>: <Reg8: 5>
                        return r5;
                    default:
                        // ──────────────── Block 10 ──────────────── 
                        // CODE → addr:179 | <CreateTopLevelEnvironment>: <Reg8: 8, UInt32: 1>
                        // USED → r8 = __environment__;
                        // CODE → addr:185 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 8>
                        r1[0] = __environment__
                        // CODE → addr:189 | <LoadConstUndefined>: <Reg8: 7>
                        // USED → r7 = undefined;
                        // CODE → addr:191 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 7>
                        __environment__[0] = undefined
                        // CODE → addr:195 | <GetGlobalObject>: <Reg8: 7>
                        // USED → r7 = globalThis;
                        // CODE → addr:197 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r10 = console;
                        // CODE → addr:203 | <GetByIdShort>: <Reg8: 8, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r8 = console.log;
                        // CODE → addr:208 | <LoadConstString>: <Reg8: 7, string_id: 568>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/start' (String)
                        // USED → r7 = "__BC:Functions/AsyncTests/simpleAsyncTest/start";
                        // CODE → addr:212 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 10, Reg8: 7>
                        console.log("__BC:Functions/AsyncTests/simpleAsyncTest/start")
                        // CODE → addr:217 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
                        r7 = getParentEnvironment(1)
                        // CODE → addr:220 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 0>
                        // USED → r8 = r7[0];
                        // CODE → addr:224 | <LoadConstUInt8>: <Reg8: 7, UInt8: 42>
                        // USED → r7 = 42;
                        // CODE → addr:227 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
                        r7 = r7[0].call(r9, 42)
                        // CODE → addr:232 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
                        r1[1] = 1
                        // CODE → addr:236 | <Mov>: <Reg8: 2, Reg8: 5>
                        r2 = 1
                        // CODE → addr:239 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
                        r1[2] = 1
                        // CODE → addr:243 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                        r5 = { "value": null, "done": false }
                        // CODE → addr:249 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
                        r5.slot_0 = r7
                        // CODE → addr:253 | <Ret>: <Reg8: 5>
                        return r5;
                }
                // Switch → END
            } else {
                // ──────────────── Block 3 ──────────────── 
                // CODE → addr: 56 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
                // USED → r5 = 1;
                // Switch → START
                switch (param1) {
                    case 1:
                        // ──────────────── Block 7 ──────────────── 
                        // CODE → addr:166 | <Throw>: <Reg8: 0>
                        throw param2;
                    case 2:
                        // ──────────────── Block 6 ──────────────── 
                        // CODE → addr:147 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r5 = { "value": null, "done": true }
                        // CODE → addr:153 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                        r5.slot_0 = param2
                        // CODE → addr:157 | <Ret>: <Reg8: 5>
                        return r5;
                    default:
                        // ──────────────── Block 5 ──────────────── 
                        // CODE → addr: 67 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 0>
                        // USED → r5 = r1[0];
                        // CODE → addr: 71 | <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 0>
                        r1[0][0] = param2
                        // CODE → addr: 75 | <GetGlobalObject>: <Reg8: 7>
                        // USED → r7 = globalThis;
                        // CODE → addr: 77 | <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r11 = console;
                        // CODE → addr: 83 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r10 = console.log;
                        // CODE → addr: 88 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 0>
                        r8 = r1[0][0]
                        // CODE → addr: 92 | <Call2>: <Reg8: 8, Reg8: 10, Reg8: 11, Reg8: 8>
                        console.log(r8)
                        // CODE → addr: 97 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r10 = console;
                        // CODE → addr:103 | <GetByIdShort>: <Reg8: 8, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r8 = console.log;
                        // CODE → addr:108 | <LoadConstString>: <Reg8: 7, string_id: 4923>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/end' (String)
                        // USED → r7 = "__BC:Functions/AsyncTests/simpleAsyncTest/end";
                        // CODE → addr:112 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 10, Reg8: 7>
                        console.log("__BC:Functions/AsyncTests/simpleAsyncTest/end")
                        // CODE → addr:117 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 0>
                        // USED → r7 = r1[0][0];
                        // CODE → addr:128 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r5 = { "value": null, "done": true }
                        // CODE → addr:134 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
                        r5.slot_0 = r1[0][0]
                        // CODE → addr:138 | <Ret>: <Reg8: 5>
                        return r5;
                }
                // Switch → END
            }
        } finally {
            // ──────────────── Block 13 ──────────────── 
            // CODE → addr:285 | <Mov>: <Reg8: 2, Reg8: 6>
            r2 = 3
            // CODE → addr:288 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
            r1[2] = 3
        }
    }
}