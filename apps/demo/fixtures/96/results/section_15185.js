async function* anon_15185(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r2 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstUndefined>: <Reg8: 7>
        // USED → r7 = undefined;
        // CODE → <LoadConstUndefined>: <Reg8: 1>
        r1 = undefined
        // CODE → <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r5 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r4 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 4754>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/start' (String)
        // USED → r3 = "__BC:Functions/AsyncTests/asyncLoopTest/start";
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/start")
        // CODE → <LoadConstZero>: <Reg8: 1>
        // USED → r1 = 0;
        // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
        r6 = param1
        // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 6>
        // USED → r4 = GetIterator(r6);
        // CODE → <GetEnvironment>: <Reg8: 5, UInt8: 2>
        // USED → r5 = getEnvironment(2);
        // LOOP → START (for_of)
        for (const r9 of r6) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 3, Reg8: 4>
            r3 = GetIterator(r6)
            if (r3 !== r7) {
                // ──────────────── Block 3 ──────────────── 
                // CODE → <Mov>: <Reg8: 8, Reg8: 1>
                // USED → r8 = 0;
                // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 5, UInt8: 2>
                // USED → r3 = getEnvironment(2)[2];
                // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 9>
                // USED → r3 = await getEnvironment(2)[2].call(undefined, GetIterator(r6).next());
                // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000004a
                goto label_74;
                // ──────────────── Block 5 ──────────────── 
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 9>
                // USED → r3 = await yield;
                // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 9>
                // USED → r9 = __resumeIsReturn;
                // CODE → <JmpTrue>: <Addr8: 9, Reg8: 9>  # Address: 00000056
                if (__resumeIsReturn) goto label_86;
                // ──────────────── Block 6 ──────────────── 
                // CODE → <Add>: <Reg8: 1, Reg8: 8, Reg8: 3>
                // USED → r1 = 0 + await yield;
                // CODE → <Jmp>: <Addr8: -37>  # Address: 0000002f
                goto label_47;
            }
        }
        // LOOP → END
        // ──────────────── Block 9 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 1>
        console.log(0 + await yield)
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 4751>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/end' (String)
        // USED → r2 = "__BC:Functions/AsyncTests/asyncLoopTest/end";
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/end")
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 1>
        return 0 + await yield;
    }
}