async function* anon_15169() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 11 ──────────────── 
        // CODE → addr:155 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:156 | <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 12 ──────────────── 
        // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4779>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/start' (String)
        // USED → r1 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/start";
        // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start")
        try {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 32 | <LoadConstString>: <Reg8: 1, string_id: 7189>  # String: 'a' (Identifier)
            r1 = "a"
            // CODE → addr: 36 | <SaveGenerator>: <Addr8: 4>  # Address: 00000028
            goto label_40;
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 38 | <Ret>: <Reg8: 1>
            return r1;
            // ──────────────── Block 3 ──────────────── 
            // CODE → addr: 40 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
            // USED → r1 = await yield;
            // CODE → addr: 40 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
            // USED → r3 = __resumeIsReturn;
            if (__resumeIsReturn) {
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr:128 | <CompleteGenerator>: <>
                // CompleteGenerator
                // CODE → addr:129 | <Ret>: <Reg8: 1>
                return await yield;
            } else {
                // ──────────────── Block 4 ──────────────── 
                // CODE → addr: 46 | <LoadConstString>: <Reg8: 3, string_id: 38>  # String: 'b' (Identifier)
                r3 = "b"
                // CODE → addr: 50 | <SaveGenerator>: <Addr8: 4>  # Address: 00000036
                goto label_54;
                // ──────────────── Block 5 ──────────────── 
                // CODE → addr: 52 | <Ret>: <Reg8: 3>
                return r3;
                // ──────────────── Block 6 ──────────────── 
                // CODE → addr: 54 | <ResumeGenerator>: <Reg8: 3, Reg8: 4>
                // USED → r3 = await yield;
                // CODE → addr: 54 | <ResumeGenerator>: <Reg8: 3, Reg8: 4>
                // USED → r4 = __resumeIsReturn;
                if (__resumeIsReturn) {
                    // ──────────────── Block 8 ──────────────── 
                    // CODE → addr:105 | <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → addr:106 | <Ret>: <Reg8: 3>
                    return await yield;
                } else {
                    // ──────────────── Block 7 ──────────────── 
                    // CODE → addr: 80 | <LoadConstUndefined>: <Reg8: 4>
                    // USED → r4 = undefined;
                    // CODE → addr: 82 | <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → addr: 83 | <Ret>: <Reg8: 4>
                    return undefined;
                }
            }
        } finally {
            // ──────────────── Block 10 ──────────────── 
            // CODE → addr:133 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → addr:139 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → addr:144 | <LoadConstString>: <Reg8: 2, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
            // USED → r2 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
            // CODE → addr:148 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
        }
    }
}