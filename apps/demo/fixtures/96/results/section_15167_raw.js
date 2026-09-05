function* anon_15167(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → addr:  4 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → addr:  4 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → addr:  7 | <JmpTrue>: <Addr8: 113, Reg8: 1>  # Address: 00000078
    if (__resumeIsReturn) goto label_120;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 2, string_id: 4786>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/start' (String)
    // USED → r2 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start")
    // CODE → addr: 32 | <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → addr: 34 | <Less>: <Reg8: 6, Reg8: 4, Reg8: 5>
    // USED → r6 = 0 < param1;
    // CODE → addr: 38 | <LoadConstString>: <Reg8: 3, string_id: 4783>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/skip' (String)
    // USED → r3 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/skip";
    // CODE → addr: 42 | <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
    // USED → r2 = 2;
    // CODE → addr: 45 | <JmpFalse>: <Addr8: 50, Reg8: 6>  # Address: 0000005f
    if (!(0 < param1)) goto label_95;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 48 | <Mov>: <Reg8: 6, Reg8: 4>
    r6 = r4
    // CODE → addr: 51 | <JStrictEqual>: <Addr8: 21, Reg8: 6, Reg8: 2>  # Address: 00000048
    // → r6 = r4
    if (r6 === 2) goto label_72;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 55 | <Mul>: <Reg8: 7, Reg8: 6, Reg8: 6>
    r7 = r6 * r6
    // CODE → addr: 59 | <SaveGenerator>: <Addr8: 4>  # Address: 0000003f
    goto label_63;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 61 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 63 | <ResumeGenerator>: <Reg8: 7, Reg8: 8>
    r7 = await yield
    // CODE → addr: 63 | <ResumeGenerator>: <Reg8: 7, Reg8: 8>
    // USED → r8 = __resumeIsReturn;
    // CODE → addr: 66 | <JmpFalse>: <Addr8: 22, Reg8: 8>  # Address: 00000058
    if (!__resumeIsReturn) goto label_88;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 69 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr: 70 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 72 | <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr: 78 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 83 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip")
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 88 | <Inc>: <Reg8: 4, Reg8: 6>
    r4 = r6 + 1
    // CODE → addr: 91 | <JLess>: <Addr8: -43, Reg8: 4, Reg8: 5>  # Address: 00000030
    // → r4 = r6 + 1
    if (r4 < param1) goto label_48;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr: 95 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:106 | <LoadConstString>: <Reg8: 1, string_id: 4782>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/end";
    // CODE → addr:110 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end")
    // CODE → addr:115 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr:117 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:118 | <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:120 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:121 | <Ret>: <Reg8: 0>
    return r0;
}