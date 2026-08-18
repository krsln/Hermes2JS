async function* anon_15185(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 2>
    // USED → r2 = __resumeIsReturn;
    // CODE → <JmpTrueLong>: <Addr32: 134, Reg8: 2>  # Address: 0000008a
    if (__resumeIsReturn) goto label_138;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4754>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/start' (String)
    // USED → r3 = "__BC:Functions/AsyncTests/asyncLoopTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/AsyncTests/asyncLoopTest/start")
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    r6 = param1
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 6>
    r4 = GetIterator(r6)
    // CODE → <GetEnvironment>: <Reg8: 5, UInt8: 2>
    r5 = getEnvironment(2)
    // ──────────────── Block 2 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 9, Reg8: 4, Reg8: 6>
    // USED → r9 = r4.next();
    // CODE → <Mov>: <Reg8: 3, Reg8: 4>
    r3 = r4
    // CODE → <JStrictEqual>: <Addr8: 45, Reg8: 3, Reg8: 7>  # Address: 00000063
    // → r3 = r4
    if (r3 === undefined) goto label_99;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 1>
    // USED → r8 = 0;
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 5, UInt8: 2>
    // USED → r3 = r5[2];
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 9>
    // USED → r3 = await r5[2].call(r7, r9);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000004a
    goto label_74;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <Ret>: <Reg8: 3>
    return await r5[2].call(r7, r9);
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
    // ──────────────── Block 7 ──────────────── 
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 0>
    r4.return()
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    return await yield;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <Catch>: <Reg8: 3>
    // USED → r3 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    r4.return()
    // CODE → <Throw>: <Reg8: 3>
    throw caughtException;
    // ──────────────── Block 9 ──────────────── 
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
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4751>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/end' (String)
    // USED → r2 = "__BC:Functions/AsyncTests/asyncLoopTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/AsyncTests/asyncLoopTest/end")
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return 0 + await yield;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}