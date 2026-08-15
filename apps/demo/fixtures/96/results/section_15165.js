async function* anon_15165() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 14 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 4>
        // USED → r4 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4789>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
        // USED → r1 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
        // USED → r1 = 1;
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000024
        goto label_36;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return 1;
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r2 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 13 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
            // USED → r2 = 2;
            // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000031
            goto label_49;
            // ──────────────── Block 5 ──────────────── 
            // CODE → <Ret>: <Reg8: 2>
            return 2;
            // ──────────────── Block 6 ──────────────── 
            // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r2 = await yield;
            // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r3 = __resumeIsReturn;
            if (__resumeIsReturn) {
                // ──────────────── Block 12 ──────────────── 
                // CODE → <CompleteGenerator>: <>
                // CompleteGenerator
                // CODE → <Ret>: <Reg8: 2>
                return await yield;
            } else {
                // ──────────────── Block 7 ──────────────── 
                // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
                // USED → r3 = 3;
                // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003e
                goto label_62;
                // ──────────────── Block 8 ──────────────── 
                // CODE → <Ret>: <Reg8: 3>
                return 3;
                // ──────────────── Block 9 ──────────────── 
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 5>
                // USED → r3 = await yield;
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 5>
                // USED → r5 = __resumeIsReturn;
                if (__resumeIsReturn) {
                    // ──────────────── Block 11 ──────────────── 
                    // CODE → <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → <Ret>: <Reg8: 3>
                    return await yield;
                } else {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r6 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r5 = globalThis.console.log;
                    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4197>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
                    // USED → r4 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
                    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
                    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
                    // CODE → <LoadConstUndefined>: <Reg8: 4>
                    // USED → r4 = undefined;
                    // CODE → <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → <Ret>: <Reg8: 4>
                    return undefined;
                }
            }
        }
    }
}