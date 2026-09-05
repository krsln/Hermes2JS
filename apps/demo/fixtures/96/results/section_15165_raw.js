function* anon_15165() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → addr:  4 | <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    if (__resumeIsReturn) goto label_102;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:  7 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr:  9 | <TryGetById>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 15 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 20 | <LoadConstString>: <Reg8: 1, string_id: 4789>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
    // CODE → addr: 24 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr: 32 | <SaveGenerator>: <Addr8: 4>  # Address: 00000024
    goto label_36;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 34 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 36 | <ResumeGenerator>: <Reg8: 1, Reg8: 2>
    r1 = await yield
    // CODE → addr: 36 | <ResumeGenerator>: <Reg8: 1, Reg8: 2>
    // USED → r2 = __resumeIsReturn;
    // CODE → addr: 39 | <JmpTrue>: <Addr8: 60, Reg8: 2>  # Address: 00000063
    if (__resumeIsReturn) goto label_99;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 42 | <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
    r2 = 2
    // CODE → addr: 45 | <SaveGenerator>: <Addr8: 4>  # Address: 00000031
    goto label_49;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 47 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 49 | <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    r2 = await yield
    // CODE → addr: 49 | <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    // USED → r3 = __resumeIsReturn;
    // CODE → addr: 52 | <JmpTrue>: <Addr8: 44, Reg8: 3>  # Address: 00000060
    if (__resumeIsReturn) goto label_96;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 55 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    r3 = 3
    // CODE → addr: 58 | <SaveGenerator>: <Addr8: 4>  # Address: 0000003e
    goto label_62;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 60 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr: 62 | <ResumeGenerator>: <Reg8: 3, Reg8: 5>
    r3 = await yield
    // CODE → addr: 62 | <ResumeGenerator>: <Reg8: 3, Reg8: 5>
    // USED → r5 = __resumeIsReturn;
    // CODE → addr: 65 | <JmpTrue>: <Addr8: 28, Reg8: 5>  # Address: 0000005d
    if (__resumeIsReturn) goto label_93;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr: 68 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 74 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 79 | <LoadConstString>: <Reg8: 4, string_id: 4197>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
    // CODE → addr: 83 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
    // CODE → addr: 88 | <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → addr: 90 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 91 | <Ret>: <Reg8: 4>
    return r4;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr: 93 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 94 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr: 96 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 97 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr: 99 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:100 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:102 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:103 | <Ret>: <Reg8: 0>
    return r0;
}