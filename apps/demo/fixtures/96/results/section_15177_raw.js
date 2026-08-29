async function* anon_15177() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → addr:  4 | <JmpTrue>: <Addr8: 94, Reg8: 1>  # Address: 00000062
    if (__resumeIsReturn) goto label_98;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:  7 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  9 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 15 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 20 | <LoadConstString>: <Reg8: 1, string_id: 4765>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/simpleAsyncTest/start";
    // CODE → addr: 24 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/start")
    // CODE → addr: 29 | <GetEnvironment>: <Reg8: 1, UInt8: 2>
    r1 = getEnvironment(2)
    // CODE → addr: 32 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
    // USED → r4 = r1[2];
    // CODE → addr: 36 | <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // CODE → addr: 38 | <LoadConstUInt8>: <Reg8: 1, UInt8: 42>
    // USED → r1 = 42;
    // CODE → addr: 41 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 3, Reg8: 1>
    r1 = await r1[2].call(r3, 42)
    // CODE → addr: 46 | <SaveGenerator>: <Addr8: 4>  # Address: 00000032
    goto label_50;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 48 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 50 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield;
    // CODE → addr: 50 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r3 = __resumeIsReturn;
    // CODE → addr: 53 | <JmpTrue>: <Addr8: 42, Reg8: 3>  # Address: 0000005f
    if (__resumeIsReturn) goto label_95;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 56 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 62 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 67 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log(r1)
    // CODE → addr: 72 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 78 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 83 | <LoadConstString>: <Reg8: 2, string_id: 4764>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/end' (String)
    // USED → r2 = "__BC:Functions/AsyncTests/simpleAsyncTest/end";
    // CODE → addr: 87 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/end")
    // CODE → addr: 92 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 93 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 95 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 96 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 98 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 99 | <Ret>: <Reg8: 0>
    return r0;
}