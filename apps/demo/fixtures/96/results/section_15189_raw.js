async function* anon_15189(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <JmpTrueLong>: <Addr32: 160, Reg8: 1>  # Address: 000000a4
    if (r1_undefined) goto label_164;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4761>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start")
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 3, string_id: 27>  # String: 'Promise' (Identifier)
    // USED → r8 = globalThis.Promise;
    // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 4, string_id: 7443>  # String: 'all' (Identifier)
    // USED → r7 = globalThis.Promise.all;
    // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
    // USED → r4 = getEnvironment(2);
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 4, UInt8: 2>
    // USED → r9 = getEnvironment(2)[2];
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → <Call2>: <Reg8: 6, Reg8: 9, Reg8: 2, Reg8: 5>
    // USED → r6 = getEnvironment(2)[2].call(undefined, 1);
    // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
    // USED → r1 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 6, UInt8: 0>
    // USED → r1 = [getEnvironment(2)[2].call(undefined, 1)];
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 2>
    // USED → r6 = 2;
    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 2, Reg8: 6>
    // USED → r9 = getEnvironment(2)[2].call(undefined, 2);
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 9, UInt8: 1>
    // USED → r1 = [getEnvironment(2)[2].call(undefined, 1), getEnvironment(2)[2].call(undefined, 2)];
    // CODE → <Call2>: <Reg8: 1, Reg8: 7, Reg8: 8, Reg8: 1>
    // USED → r1 = await globalThis.Promise.all([getEnvironment(2)[2].call(undefined, 1), getEnvironment(2)[2].call(undefined, 2)]);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000005a
    goto label_90;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return await globalThis.Promise.all([getEnvironment(2)[2].call(undefined, 1), getEnvironment(2)[2].call(undefined, 2)]);
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 7>
    // USED → r1 = await yield;
    // CODE → <JmpTrue>: <Addr8: 68, Reg8: 7>  # Address: 000000a1
    if (globalThis.Promise.all) goto label_161;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 0>
    // USED → r4 = getEnvironment(2)[0];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = getEnvironment(2)[0].default;
    // CODE → <Call3>: <Reg8: 4, Reg8: 4, Reg8: 2, Reg8: 1, Reg8: 6>
    // USED → r4 = getEnvironment(2)[0].default.call(undefined, await yield, 2);
    // CODE → <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → <GetByVal>: <Reg8: 7, Reg8: 4, Reg8: 6>
    // USED → r7 = getEnvironment(2)[0].default.call(undefined, await yield, 2)[0];
    // CODE → <GetByVal>: <Reg8: 6, Reg8: 4, Reg8: 5>
    // USED → r6 = getEnvironment(2)[0].default.call(undefined, await yield, 2)[1];
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 6>
    r4 = globalThis.console.log(getEnvironment(2)[0].default.call(undefined, await yield, 2)[0], getEnvironment(2)[0].default.call(undefined, await yield, 2)[1])
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4760>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
    // USED → r3 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end")
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}