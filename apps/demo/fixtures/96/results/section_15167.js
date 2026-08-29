async function* anon_15167(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → addr:  4 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → addr:  4 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → addr:120 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:121 | <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr: 23 | <LoadConstString>: <Reg8: 2, string_id: 4786>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/start' (String)
        // USED → r2 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/start";
        // CODE → addr: 27 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start")
        // CODE → addr: 34 | <Less>: <Reg8: 6, Reg8: 4, Reg8: 5>
        // USED → r6 = 0 < param1;
        // CODE → addr: 38 | <LoadConstString>: <Reg8: 3, string_id: 4783>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/skip' (String)
        // USED → r3 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/skip";
        // CODE → addr: 42 | <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
        // USED → r2 = 2;
        if (0 < param1) {
            // LOOP → START (for)
            for (r4 = 0; r4 < param1; r4 = r4 + 1) {
                // ──────────────── Block 2 ──────────────── 
                if (r4 === 2) {
                    // ──────────────── Block 7 ──────────────── 
                    // CODE → addr: 72 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r8 = console;
                    // CODE → addr: 78 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr: 83 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
                    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip")
                } else {
                    // ──────────────── Block 3 ──────────────── 
                    // CODE → addr: 55 | <Mul>: <Reg8: 7, Reg8: 6, Reg8: 6>
                    r7 = 0 * 0
                    // CODE → addr: 59 | <SaveGenerator>: <Addr8: 4>  # Address: 0000003f
                    goto label_63;
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → addr: 63 | <ResumeGenerator>: <Reg8: 7, Reg8: 8>
                    // USED → r7 = await yield;
                    // CODE → addr: 63 | <ResumeGenerator>: <Reg8: 7, Reg8: 8>
                    // USED → r8 = __resumeIsReturn;
                    if (__resumeIsReturn) {
                        // ──────────────── Block 6 ──────────────── 
                        // CODE → addr: 69 | <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → addr: 70 | <Ret>: <Reg8: 7>
                        return await yield;
                    }
                }
                // ──────────────── Block 8 ──────────────── 
            }
            // LOOP → END
            // ──────────────── Block 4 ──────────────── 
            // CODE → addr: 61 | <Ret>: <Reg8: 7>
            return r7;
        }
        // ──────────────── Block 9 ──────────────── 
        // CODE → addr: 95 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr:101 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr:106 | <LoadConstString>: <Reg8: 1, string_id: 4782>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/end' (String)
        // USED → r1 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/end";
        // CODE → addr:110 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end")
        // CODE → addr:115 | <LoadConstUndefined>: <Reg8: 1>
        // USED → r1 = undefined;
        // CODE → addr:117 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:118 | <Ret>: <Reg8: 1>
        return undefined;
    }
}