async function* anon_15167(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    if (r1) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 1>
        // USED → r1 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4786>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/start' (String)
        // USED → r2 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/start";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        r2 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start")
        // CODE → <LoadConstZero>: <Reg8: 4>
        // USED → r4 = 0;
        // CODE → <Less>: <Reg8: 6, Reg8: 4, Reg8: 5>
        // USED → r6 = 0 < param1;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 4783>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/skip' (String)
        // USED → r3 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/skip";
        // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
        // USED → r2 = 2;
        if (!(0 < param1)) {
            // ──────────────── Block 9 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r3 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r2 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 1, string_id: 4782>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/end' (String)
            // USED → r1 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/end";
            // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
            r1 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end")
            // CODE → <LoadConstUndefined>: <Reg8: 1>
            // USED → r1 = undefined;
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return undefined;
        } else {
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <Mov>: <Reg8: 6, Reg8: 4>
                // USED → r6 = 0;
                if (0 !== 2) {
                    // ──────────────── Block 3 ──────────────── 
                    // CODE → <Mul>: <Reg8: 7, Reg8: 6, Reg8: 6>
                    // USED → r7 = 0 * 0;
                    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003f
                    goto label_63;
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <ResumeGenerator>: <Reg8: 7, Reg8: 8>
                    // USED → r7 = await yield;
                    if (!r8) {
                        // ──────────────── Block 8 ──────────────── 
                        // CODE → <Inc>: <Reg8: 4, Reg8: 6>
                        // USED → r4 = 0 + 1;
                        // CODE → <JLess>: <Addr8: -43, Reg8: 4, Reg8: 5>  # Address: 00000030
                        if (0 + 1 < param1) goto label_48;
                    } else {
                        // ──────────────── Block 7 ──────────────── 
                        // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r8 = globalThis.console;
                        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r7 = globalThis.console.log;
                        // CODE → <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
                        r7 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip")
                    }
                }
            }
            // LOOP → END
            // ──────────────── Block 4 ──────────────── 
            // CODE → <Ret>: <Reg8: 7>
            return 0 * 0;
            // ──────────────── Block 6 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 7>
            return await yield;
        }
    }
}