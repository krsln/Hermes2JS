async function* anon_15193(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __generatorReturn;
    // CODE → <JmpTrueLong>: <Addr32: 149, Reg8: 1>  # Address: 00000099
    if (__generatorReturn) goto label_153;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 6>
    // USED → r6 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4759>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/callAsyncTests/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
    // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
    // USED → r4 = getEnvironment(2);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
    // USED → r1 = getEnvironment(2)[3];
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 5>
    // USED → r1 = await getEnvironment(2)[3].call(undefined);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000031
    goto label_49;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return await getEnvironment(2)[3].call(undefined);
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
    // USED → r1 = await yield;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
    // USED → r2 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 98, Reg8: 2>  # Address: 00000096
    if (__generatorReturn) goto label_150;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 5>
    // USED → r2 = getEnvironment(2)[5];
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = await getEnvironment(2)[5].call(undefined);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000043
    goto label_67;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Ret>: <Reg8: 2>
    return await getEnvironment(2)[5].call(undefined);
    // ──────────────── Block 7 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    // USED → r2 = await yield;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    // USED → r3 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 77, Reg8: 3>  # Address: 00000093
    if (__generatorReturn) goto label_147;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 7, Reg8: 4, UInt8: 7>
    // USED → r7 = getEnvironment(2)[7];
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
    // USED → r3 = [1, 2, 3];
    // CODE → <Call2>: <Reg8: 3, Reg8: 7, Reg8: 5, Reg8: 3>
    // USED → r3 = await getEnvironment(2)[7].call(undefined, [1, 2, 3]);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000005e
    goto label_94;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <Ret>: <Reg8: 3>
    return await getEnvironment(2)[7].call(undefined, [1, 2, 3]);
    // ──────────────── Block 11 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 7>
    // USED → r3 = await yield;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 7>
    // USED → r7 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 47, Reg8: 7>  # Address: 00000090
    if (__generatorReturn) goto label_144;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 9>
    // USED → r4 = getEnvironment(2)[9];
    // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 5>
    // USED → r4 = await getEnvironment(2)[9].call(undefined);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000070
    goto label_112;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <Ret>: <Reg8: 4>
    return await getEnvironment(2)[9].call(undefined);
    // ──────────────── Block 15 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 4, Reg8: 7>
    // USED → r4 = await yield;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 4, Reg8: 7>
    // USED → r7 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 26, Reg8: 7>  # Address: 0000008d
    if (__generatorReturn) goto label_141;
    // ──────────────── Block 17 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 2895>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
    // USED → r6 = "__BC:Functions/AsyncTests/callAsyncTests/end";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 5>
    return undefined;
    // ──────────────── Block 18 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 4>
    return await yield;
    // ──────────────── Block 19 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    return await yield;
    // ──────────────── Block 20 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    return await yield;
    // ──────────────── Block 21 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 22 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}