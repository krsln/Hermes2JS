async function* anon_15177() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 2>
        // USED → r2 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r3 = console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4765>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/start' (String)
        // USED → r1 = "__BC:Functions/AsyncTests/simpleAsyncTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
        console.log("__BC:Functions/AsyncTests/simpleAsyncTest/start")
        // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 2>
        r1 = getEnvironment(2)
        // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
        // USED → r4 = r1[2];
        // CODE → <LoadConstUndefined>: <Reg8: 3>
        r3 = undefined
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 42>
        // USED → r1 = 42;
        // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 3, Reg8: 1>
        // USED → r1 = await r1[2].call(r3, 42);
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000032
        goto label_50;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return await r1[2].call(r3, 42);
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        // USED → r3 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 1>
            console.log(r1)
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r4 = console;
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r3 = console.log;
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 4764>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/end' (String)
            // USED → r2 = "__BC:Functions/AsyncTests/simpleAsyncTest/end";
            // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            console.log("__BC:Functions/AsyncTests/simpleAsyncTest/end")
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        }
    }
}