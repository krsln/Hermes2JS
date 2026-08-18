async function* anon_15193() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 6>
        // USED → r6 = globalThis;
        // CODE → <TryGetById>: <Reg8: 3, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r3 = console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4759>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
        // USED → r1 = "__BC:Functions/AsyncTests/callAsyncTests/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
        // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
        r4 = getEnvironment(2)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
        // USED → r1 = r4[3];
        // CODE → <LoadConstUndefined>: <Reg8: 5>
        // USED → r5 = undefined;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 5>
        // USED → r1 = await r4[3].call(r5);
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000031
        goto label_49;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return await r4[3].call(r5);
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r2 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 17 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 5>
            // USED → r2 = r4[5];
            // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
            // USED → r2 = await r4[5].call(r5);
            // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000043
            goto label_67;
            // ──────────────── Block 5 ──────────────── 
            // CODE → <Ret>: <Reg8: 2>
            return await r4[5].call(r5);
            // ──────────────── Block 6 ──────────────── 
            // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r2 = await yield;
            // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            // USED → r3 = __resumeIsReturn;
            if (__resumeIsReturn) {
                // ──────────────── Block 16 ──────────────── 
                // CODE → <CompleteGenerator>: <>
                // CompleteGenerator
                // CODE → <Ret>: <Reg8: 2>
                return await yield;
            } else {
                // ──────────────── Block 7 ──────────────── 
                // CODE → <LoadFromEnvironment>: <Reg8: 7, Reg8: 4, UInt8: 7>
                // USED → r7 = r4[7];
                // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
                // USED → r3 = [1, 2, 3];
                // CODE → <Call2>: <Reg8: 3, Reg8: 7, Reg8: 5, Reg8: 3>
                // USED → r3 = await r4[7].call(r5, r3);
                // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000005e
                goto label_94;
                // ──────────────── Block 8 ──────────────── 
                // CODE → <Ret>: <Reg8: 3>
                return await r4[7].call(r5, r3);
                // ──────────────── Block 9 ──────────────── 
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 7>
                // USED → r3 = await yield;
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 7>
                // USED → r7 = __resumeIsReturn;
                if (__resumeIsReturn) {
                    // ──────────────── Block 15 ──────────────── 
                    // CODE → <CompleteGenerator>: <>
                    // CompleteGenerator
                    // CODE → <Ret>: <Reg8: 3>
                    return await yield;
                } else {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 9>
                    // USED → r4 = r4[9];
                    // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 5>
                    // USED → r4 = await r4[9].call(r5);
                    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000070
                    goto label_112;
                    // ──────────────── Block 11 ──────────────── 
                    // CODE → <Ret>: <Reg8: 4>
                    return await r4[9].call(r5);
                    // ──────────────── Block 12 ──────────────── 
                    // CODE → <ResumeGenerator>: <Reg8: 4, Reg8: 7>
                    // USED → r4 = await yield;
                    // CODE → <ResumeGenerator>: <Reg8: 4, Reg8: 7>
                    // USED → r7 = __resumeIsReturn;
                    if (__resumeIsReturn) {
                        // ──────────────── Block 14 ──────────────── 
                        // CODE → <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → <Ret>: <Reg8: 4>
                        return await yield;
                    } else {
                        // ──────────────── Block 13 ──────────────── 
                        // CODE → <TryGetById>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r8 = console;
                        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r7 = console.log;
                        // CODE → <LoadConstString>: <Reg8: 6, string_id: 2895>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
                        // USED → r6 = "__BC:Functions/AsyncTests/callAsyncTests/end";
                        // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
                        console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
                        // CODE → <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → <Ret>: <Reg8: 5>
                        return undefined;
                    }
                }
            }
        }
    }
}