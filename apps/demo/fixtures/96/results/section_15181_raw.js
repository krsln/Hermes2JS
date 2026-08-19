async function* anon_15181() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → addr:  4 | <JmpTrueLong>: <Addr32: 228, Reg8: 1>  # Address: 000000e8
    if (__resumeIsReturn) goto label_232;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4758>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/start")
    // CODE → addr: 32 | <GetEnvironment>: <Reg8: 1, UInt8: 2>
    r1 = getEnvironment(2)
    // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 2>
    // USED → r4 = r1[2];
    // CODE → addr: 39 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 3, UInt8: 1>
    // USED → r3 = 1;
    // CODE → addr: 44 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 1, Reg8: 3>
    // USED → r1 = await r1[2](1);
    // CODE → addr: 49 | <SaveGenerator>: <Addr8: 4>  # Address: 00000035
    goto label_53;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 51 | <Ret>: <Reg8: 1>
    return await r1[2](1);
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 53 | <ResumeGenerator>: <Reg8: 1, Reg8: 4>
    // USED → r1 = await yield;
    // CODE → addr: 53 | <ResumeGenerator>: <Reg8: 1, Reg8: 4>
    // USED → r4 = __resumeIsReturn;
    // CODE → addr: 56 | <JmpTrue>: <Addr8: 62, Reg8: 4>  # Address: 00000076
    if (__resumeIsReturn) goto label_118;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 59 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 65 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 4, string_id: 401>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/awaited' (String)
    // USED → r4 = "__BC:Functions/AsyncTests/asyncTryCatchTest/awaited";
    // CODE → addr: 74 | <Call3>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/awaited", r1)
    // CODE → addr: 80 | <JStrictEqual>: <Addr8: 6, Reg8: 1, Reg8: 3>  # Address: 00000056
    if (r1 === 1) goto label_86;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 84 | <Jmp>: <Addr8: 79>  # Address: 000000a3
    goto label_163;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 86 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 3, string_id: 12>  # String: 'Error' (Identifier)
    // USED → r5 = Error;
    // CODE → addr: 92 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r3 = Error.prototype;
    // CODE → addr: 97 | <CreateThis>: <Reg8: 4, Reg8: 3, Reg8: 5>
    // USED → r4 = CreateThis(r3);
    // CODE → addr:101 | <LoadConstString>: <Reg8: 8, string_id: 6849>  # String: 'post-await failure' (String)
    // USED → r8 = "post-await failure";
    // CODE → addr:105 | <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = CreateThis(r3);
    // CODE → addr:108 | <Construct>: <Reg8: 3, Reg8: 5, UInt8: 2>
    // USED → r3 = new Error("post-await failure");
    // CODE → addr:112 | <SelectObject>: <Reg8: 3, Reg8: 4, Reg8: 3>
    // USED → r3 = new Error("post-await failure");
    // CODE → addr:116 | <Throw>: <Reg8: 3>
    throw new Error("post-await failure");
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:118 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:124 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:129 | <LoadConstString>: <Reg8: 3, string_id: 4757>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
    // USED → r3 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
    // CODE → addr:133 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:138 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:139 | <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:141 | <Catch>: <Reg8: 1>
    r1 = caughtException
    // CODE → addr:143 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:149 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:154 | <LoadConstString>: <Reg8: 1, string_id: 2140>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/caught' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/caught";
    // CODE → addr:158 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/caught")
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:163 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:169 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:174 | <LoadConstString>: <Reg8: 1, string_id: 4757>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
    // CODE → addr:178 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:183 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:189 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:194 | <LoadConstString>: <Reg8: 1, string_id: 4756>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/end' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/asyncTryCatchTest/end";
    // CODE → addr:198 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/end")
    // CODE → addr:203 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr:205 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:206 | <Ret>: <Reg8: 1>
    return undefined;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:208 | <Catch>: <Reg8: 1>
    // USED → r1 = caughtException;
    // CODE → addr:210 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:216 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:221 | <LoadConstString>: <Reg8: 2, string_id: 4757>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
    // USED → r2 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
    // CODE → addr:225 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:230 | <Throw>: <Reg8: 1>
    throw caughtException;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:232 | <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → addr:233 | <Ret>: <Reg8: 0>
    return await yield;
}