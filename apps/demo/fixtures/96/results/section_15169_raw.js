async function* anon_15169() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → addr:  4 | <JmpTrueLong>: <Addr32: 151, Reg8: 1>  # Address: 0000009b
    if (__resumeIsReturn) goto label_155;
    // ──────────────── Block 1 ──────────────── 
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
    // CODE → addr: 32 | <LoadConstString>: <Reg8: 1, string_id: 7189>  # String: 'a' (Identifier)
    r1 = "a"
    // CODE → addr: 36 | <SaveGenerator>: <Addr8: 4>  # Address: 00000028
    goto label_40;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 38 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 40 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    r1 = await yield
    // CODE → addr: 40 | <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r3 = __resumeIsReturn;
    // CODE → addr: 43 | <JmpTrue>: <Addr8: 65, Reg8: 3>  # Address: 0000006c
    if (__resumeIsReturn) goto label_108;
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
    r3 = await yield
    // CODE → addr: 54 | <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r4 = __resumeIsReturn;
    // CODE → addr: 57 | <JmpTrue>: <Addr8: 28, Reg8: 4>  # Address: 00000055
    if (__resumeIsReturn) goto label_85;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 60 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 71 | <LoadConstString>: <Reg8: 4, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → addr: 75 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr: 80 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr: 82 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 83 | <Ret>: <Reg8: 4>
    return r4;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 85 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 96 | <LoadConstString>: <Reg8: 4, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → addr:100 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:105 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:106 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:108 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:114 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:119 | <LoadConstString>: <Reg8: 3, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r3 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → addr:123 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:128 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:129 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:131 | <Catch>: <Reg8: 1>
    r1 = caughtException
    // CODE → addr:133 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:139 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:144 | <LoadConstString>: <Reg8: 2, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r2 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → addr:148 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:153 | <Throw>: <Reg8: 1>
    throw r1;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:155 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:156 | <Ret>: <Reg8: 0>
    return r0;
}