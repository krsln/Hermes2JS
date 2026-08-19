async function* anon_15189() {
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
        // CODE → <GetGlobalObject>: <Reg8: 3>
        // USED → r3 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4761>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
        // USED → r1 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
        console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start")
        // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 3, string_id: 27>  # String: 'Promise' (Identifier)
        // USED → r8 = Promise;
        // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 4, string_id: 7443>  # String: 'all' (Identifier)
        // USED → r7 = Promise.all;
        // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
        r4 = getEnvironment(2)
        // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 4, UInt8: 2>
        // USED → r9 = r4[2];
        // CODE → <LoadConstUndefined>: <Reg8: 2>
        r2 = undefined
        // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // CODE → <Call2>: <Reg8: 6, Reg8: 9, Reg8: 2, Reg8: 5>
        r6 = r4[2].call(r2, 1)
        // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
        r1 = []
        // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 6, UInt8: 0>
        // USED → r1 = r1[0] = r6;
        // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 2>
        // USED → r6 = 2;
        // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 2, Reg8: 6>
        r9 = r4[2].call(r2, 2)
        // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 9, UInt8: 1>
        // USED → r1 = (r1[0] = r6)[1] = r9;
        // CODE → <Call2>: <Reg8: 1, Reg8: 7, Reg8: 8, Reg8: 1>
        // USED → r1 = await Promise.all(r1);
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000005a
        goto label_90;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return await Promise.all(r1);
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 7>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 7>
        // USED → r7 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 0>
            r4 = r4[0]
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 107>  # String: 'default' (Identifier)
            // USED → r4 = r4.default;
            // CODE → <Call3>: <Reg8: 4, Reg8: 4, Reg8: 2, Reg8: 1, Reg8: 6>
            r4 = r4.default.call(r2, r1, 2)
            // CODE → <LoadConstZero>: <Reg8: 6>
            r6 = 0
            // CODE → <GetByVal>: <Reg8: 7, Reg8: 4, Reg8: 6>
            // USED → r7 = r4[r6];
            // CODE → <GetByVal>: <Reg8: 6, Reg8: 4, Reg8: 5>
            // USED → r6 = r4[r5];
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = console.log;
            // CODE → <Call3>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 6>
            console.log(r7, r6)
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = console.log;
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 4760>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
            // USED → r3 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
            // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end")
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 2>
            return undefined;
        }
    }
}