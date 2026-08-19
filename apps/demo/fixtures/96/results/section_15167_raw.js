async function* anon_15167(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 1>
    // USED → r5 = param1;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → <JmpTrue>: <Addr8: 113, Reg8: 1>  # Address: 00000078
    if (__resumeIsReturn) goto label_120;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4786>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/start' (String)
    // USED → r2 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start")
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <Less>: <Reg8: 6, Reg8: 4, Reg8: 5>
    // USED → r6 = 0 < param1;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4783>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/skip' (String)
    // USED → r3 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/skip";
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 2>
    // USED → r2 = 2;
    // CODE → <JmpFalse>: <Addr8: 50, Reg8: 6>  # Address: 0000005f
    if (!(0 < param1)) goto label_95;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 4>
    r6 = 0
    // CODE → <JStrictEqual>: <Addr8: 21, Reg8: 6, Reg8: 2>  # Address: 00000048
    // → r6 = 0
    if (r6 === 2) goto label_72;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Mul>: <Reg8: 7, Reg8: 6, Reg8: 6>
    // USED → r7 = 0 * 0;
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003f
    goto label_63;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Ret>: <Reg8: 7>
    return 0 * 0;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 7, Reg8: 8>
    // USED → r7 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 7, Reg8: 8>
    // USED → r8 = __resumeIsReturn;
    // CODE → <JmpFalse>: <Addr8: 22, Reg8: 8>  # Address: 00000058
    if (!__resumeIsReturn) goto label_88;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 7>
    return await yield;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip")
    // ──────────────── Block 8 ──────────────── 
    // CODE → <Inc>: <Reg8: 4, Reg8: 6>
    r4 = r6 + 1
    // CODE → <JLess>: <Addr8: -43, Reg8: 4, Reg8: 5>  # Address: 00000030
    // → r4 = r6 + 1
    if (r4 < param1) goto label_48;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4782>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/end' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}