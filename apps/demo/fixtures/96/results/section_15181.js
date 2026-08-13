async function* anon_15181(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 11 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4758>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/start' (String)
        // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/start")
        // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 2>
        // USED → r1 = getEnvironment(2);
        // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
        // USED → r4 = getEnvironment(2)[2];
        // CODE → <LoadConstUndefined>: <Reg8: 1>
        // USED → r1 = undefined;
        // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
        // USED → r3 = 1;
        // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 1, Reg8: 3>
        // USED → r1 = await getEnvironment(2)[2].call(undefined, 1);
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000035
        goto label_53;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return await getEnvironment(2)[2].call(undefined, 1);
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 4>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 4>
        // USED → r4 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 7 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 4757>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
            // USED → r3 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
            // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 4, string_id: 401>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/awaited' (String)
            // USED → r4 = "__BC:Functions/AsyncTests/asyncTryCatchTest/awaited";
            // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
            console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/awaited", r1)
            if (r1 === 1) {
                // ──────────────── Block 6 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
                // USED → r5 = globalThis.Error;
                // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
                // USED → r3 = globalThis.Error.prototype;
                // CODE → <CreateThis>: <Reg8: 4, Reg8: 3, Reg8: 5>
                // USED → r4 = createThis(globalThis.Error.prototype, globalThis.Error);
                // CODE → <LoadConstString>: <Reg8: 8, string_id: 6849>  # String: 'post-await failure' (String)
                // USED → r8 = "post-await failure";
                // CODE → <Mov>: <Reg8: 9, Reg8: 4>
                r9 = createThis(globalThis.Error.prototype, globalThis.Error)
                // CODE → <Construct>: <Reg8: 3, Reg8: 5, UInt8: 2>
                // USED → r3 = new globalThis.Error("post-await failure");
                // CODE → <SelectObject>: <Reg8: 3, Reg8: 4, Reg8: 3>
                // USED → r3 = new globalThis.Error("post-await failure");
                // CODE → <Throw>: <Reg8: 3>
                throw new globalThis.Error("post-await failure");
            } else {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <Jmp>: <Addr8: 79>  # Address: 000000a3
                goto label_163;
                try {
                    // LOOP → START (while)
                    while (true) {
                        // ──────────────── Block 9 ──────────────── 
                        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r4 = globalThis.console;
                        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r3 = globalThis.console.log;
                        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4756>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/end' (String)
                        // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/end";
                        // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
                        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/end")
                        // CODE → <LoadConstUndefined>: <Reg8: 1>
                        // USED → r1 = undefined;
                        // CODE → <CompleteGenerator>: <>
                        // CompleteGenerator
                        // CODE → <Ret>: <Reg8: 1>
                        return undefined;
                        // ──────────────── Block 8 ──────────────── 
                        // CODE → <Catch>: <Reg8: 1>
                        r1 = caughtException
                        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                        // USED → r4 = globalThis.console;
                        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                        // USED → r3 = globalThis.console.log;
                        // CODE → <LoadConstString>: <Reg8: 1, string_id: 2140>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/caught' (String)
                        // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/caught";
                        // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
                        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/caught")
                    }
                    // LOOP → END
                } finally {
                    // ──────────────── Block 10 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r4 = globalThis.console;
                    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r3 = globalThis.console.log;
                    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4757>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
                    // USED → r2 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
                    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
                    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
                }
            }
        }
    }
}