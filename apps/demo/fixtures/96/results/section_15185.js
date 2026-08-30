async function* anon_15185(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r0 = await yield;
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r2 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → addr:138 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:139 | <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 10 | <LoadConstUndefined>: <Reg8: 7>
        // USED → r7 = undefined;
        // CODE → addr: 12 | <LoadConstUndefined>: <Reg8: 1>
        r1 = undefined
        // CODE → addr: 14 | <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → addr: 16 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r5 = console;
        // CODE → addr: 22 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r4 = console.log;
        // CODE → addr: 27 | <LoadConstString>: <Reg8: 3, string_id: 4754>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/start' (String)
        // USED → r3 = "__BC:Functions/AsyncTests/asyncLoopTest/start";
        // CODE → addr: 31 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/start")
        // CODE → addr: 36 | <LoadConstZero>: <Reg8: 1>
        // USED → r1 = 0;
        // CODE → addr: 38 | <LoadParam>: <Reg8: 6, UInt8: 1>
        r6 = param1
        // CODE → addr: 41 | <IteratorBegin>: <Reg8: 4, Reg8: 6>
        r4 = GetIterator(r6)
        // CODE → addr: 44 | <GetEnvironment>: <Reg8: 5, UInt8: 2>
        r5 = getEnvironment(2)
        // LOOP → START (for_of)
        for (const r9 of r6) {
            // ──────────────── Block 2 ──────────────── 
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 58 | <Mov>: <Reg8: 8, Reg8: 1>
            // USED → r8 = 0;
            // CODE → addr: 61 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 5, UInt8: 2>
            // USED → r3 = r5[2];
            // CODE → addr: 65 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 9>
            r3 = await r5[2].call(r7, r9)
            // CODE → addr: 70 | <SaveGenerator>: <Addr8: 4>  # Address: 0000004a
            goto label_74;
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr: 74 | <ResumeGenerator>: <Reg8: 3, Reg8: 9>
            // USED → r3 = await yield;
            // CODE → addr: 74 | <ResumeGenerator>: <Reg8: 3, Reg8: 9>
            // USED → r9 = __resumeIsReturn;
            if (__resumeIsReturn) {
                // ──────────────── Block 7 ──────────────── 
                // CODE → addr: 89 | <CompleteGenerator>: <>
                // CompleteGenerator
                // CODE → addr: 90 | <Ret>: <Reg8: 3>
                return await yield;
            }
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr: 80 | <Add>: <Reg8: 1, Reg8: 8, Reg8: 3>
            // USED → r1 = 0 + await yield;
        }
        // LOOP → END
        // ──────────────── Block 9 ──────────────── 
        // CODE → addr: 99 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr:105 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr:110 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 1>
        console.log(r1)
        // CODE → addr:115 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr:121 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr:126 | <LoadConstString>: <Reg8: 2, string_id: 4751>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/end' (String)
        // USED → r2 = "__BC:Functions/AsyncTests/asyncLoopTest/end";
        // CODE → addr:130 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/end")
        // CODE → addr:135 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:136 | <Ret>: <Reg8: 1>
        return r1;
    }
}