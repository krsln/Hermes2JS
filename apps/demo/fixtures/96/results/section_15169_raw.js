async function* anon_15169(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __generatorReturn;
    // CODE → <JmpTrueLong>: <Addr32: 151, Reg8: 1>  # Address: 0000009b
    if (__generatorReturn) goto label_155;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4779>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/start' (String)
    // USED → r1 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    r1 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start")
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 7189>  # String: 'a' (Identifier)
    // USED → r1 = "a";
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000028
    goto label_40;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return "a";
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r3 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 65, Reg8: 3>  # Address: 0000006c
    if (__generatorReturn) goto label_108;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 38>  # String: 'b' (Identifier)
    // USED → r3 = "b";
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000036
    goto label_54;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Ret>: <Reg8: 3>
    return "b";
    // ──────────────── Block 7 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r3 = await yield;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r4 = __generatorReturn;
    // CODE → <JmpTrue>: <Addr8: 28, Reg8: 4>  # Address: 00000055
    if (__generatorReturn) goto label_85;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 4>
    return undefined;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r4 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    return await yield;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r3 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <Catch>: <Reg8: 1>
    // USED → r1 = caughtException;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4777>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r2 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → <Throw>: <Reg8: 1>
    throw caughtException;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}