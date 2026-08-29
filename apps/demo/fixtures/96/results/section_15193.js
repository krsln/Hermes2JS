async function* anon_15193() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → addr:153 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:154 | <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 6>
        // USED → r6 = globalThis;
        // CODE → addr: 12 | <TryGetById>: <Reg8: 3, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4759>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
        // USED → r1 = "__BC:Functions/AsyncTests/callAsyncTests/start";
        // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
        // CODE → addr: 32 | <GetEnvironment>: <Reg8: 4, UInt8: 2>
        r4 = getEnvironment(2)
        // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
        // USED → r1 = r4[3];
        // CODE → addr: 39 | <LoadConstUndefined>: <Reg8: 5>
        // USED → r5 = undefined;
        // CODE → addr: 41 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 5>
        r1 = await r4[3].call(r5)
        // CODE → addr: 45 | <SaveGenerator>: <Addr8: 4>  # Address: 00000031
        goto label_49;
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr: 47 | <Ret>: <Reg8: 1>
        return r1;
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr: 49 | <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r1 = await yield;
        // CODE → addr: 49 | <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r2 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 17 ──────────────── 
            // CODE → addr:150 | <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → addr:151 | <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → addr: 55 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 5>
            // USED → r2 = r4[5];
            // CODE → addr: 59 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
            r2 = await r4[5].call(r5)
            // CODE → addr: 63 | <SaveGenerator>: <Addr8: 4>  # Address: 00000043
            goto label_67;
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr: 65 | <Ret>: <Reg8: 2>
            return r2;
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr: 67 | <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r2 = await yield;
            // CODE → addr: 67 | <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r3 = __resumeIsReturn;
            if (__resumeIsReturn) {
                // ──────────────── Block 16 ──────────────── 
                // CODE → addr:147 | <CompleteGenerator>: <>
                // CompleteGenerator
                // CODE → addr:148 | <Ret>: <Reg8: 2>
                return await yield;
            } else {
                // ──────────────── Block 7 ──────────────── 
                // CODE → addr: 73 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 4, UInt8: 7>
                // USED → r7 = r4[7];
                // CODE → addr: 77 | <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
                // USED → r3 = [1, 2, 3];
                // CODE → addr: 85 | <Call2>: <Reg8: 3, Reg8: 7, Reg8: 5, Reg8: 3>
                r3 = await r4[7].call(r5, r3)
                // CODE → addr: 90 | <SaveGenerator>: <Addr8: 4>  # Address: 0000005e
                goto label_94;
                // ──────────────── Block 8 ──────────────── 
                // CODE → addr: 92 | <Ret>: <Reg8: 3>
                return r3;
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr: 94 | <ResumeGenerator>: <Reg8: 3, Reg8: 7>
                // USED → r3 = await yield;
                // CODE → addr: 94 | <ResumeGenerator>: <Reg8: 3, Reg8: 7>
                // USED → r7 = __resumeIsReturn;
                if (__resumeIsReturn) {
                    // ──────────────── Block 15 ──────────────── 
                    // CODE → addr:144 | <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → addr:145 | <Ret>: <Reg8: 3>
                    return await yield;
                } else {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → addr:100 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 9>
                    // USED → r4 = r4[9];
                    // CODE → addr:104 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 5>
                    r4 = await r4[9].call(r5)
                    // CODE → addr:108 | <SaveGenerator>: <Addr8: 4>  # Address: 00000070
                    goto label_112;
                    // ──────────────── Block 11 ──────────────── 
                    // CODE → addr:110 | <Ret>: <Reg8: 4>
                    return r4;
                    // ──────────────── Block 12 ──────────────── 
                    // CODE → addr:112 | <ResumeGenerator>: <Reg8: 4, Reg8: 7>
                    // USED → r4 = await yield;
                    // CODE → addr:112 | <ResumeGenerator>: <Reg8: 4, Reg8: 7>
                    // USED → r7 = __resumeIsReturn;
                    if (__resumeIsReturn) {
                        // ──────────────── Block 14 ──────────────── 
                        // CODE → addr:141 | <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → addr:142 | <Ret>: <Reg8: 4>
                        return await yield;
                    } else {
                        // ──────────────── Block 13 ──────────────── 
                        // CODE → addr:118 | <TryGetById>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r8 = console;
                        // CODE → addr:124 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r7 = console.log;
                        // CODE → addr:129 | <LoadConstString>: <Reg8: 6, string_id: 2895>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
                        // USED → r6 = "__BC:Functions/AsyncTests/callAsyncTests/end";
                        // CODE → addr:133 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
                        console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
                        // CODE → addr:138 | <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → addr:139 | <Ret>: <Reg8: 5>
                        return undefined;
                    }
                }
            }
        }
    }
}