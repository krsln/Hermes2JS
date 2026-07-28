function runAllTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    // USED → r5 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4781>  # String: '__BC:index/runAllTests/start' (String)
    // USED → r6 = "__BC:index/runAllTests/start";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log("__BC:index/runAllTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 0>
    // USED → r6 = getParentEnvironment(0)[0];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 2, string_id: 11062>  # String: 'whileTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[0].whileTest;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[0].whileTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 1>
    // USED → r6 = getParentEnvironment(0)[1];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 3, string_id: 11004>  # String: 'doWhileTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[1].doWhileTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[1].doWhileTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 2>
    // USED → r6 = getParentEnvironment(0)[2];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 4, string_id: 11016>  # String: 'forTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[2].forTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[2].forTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 3>
    // USED → r6 = getParentEnvironment(0)[3];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 5, string_id: 11007>  # String: 'forEachTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[3].forEachTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[3].forEachTest.call(undefined)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 4>
    // USED → r6 = getParentEnvironment(0)[4];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 6, string_id: 11053>  # String: 'switchTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[4].switchTest;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 1, Reg8: 0>
    // USED → r6 = getParentEnvironment(0)[4].switchTest.call(undefined, 4);
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log(getParentEnvironment(0)[4].switchTest.call(undefined, 4))
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 5>
    // USED → r6 = getParentEnvironment(0)[5];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 7, string_id: 8434>  # String: 'nestedLoopTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[5].nestedLoopTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[5].nestedLoopTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 6>
    // USED → r6 = getParentEnvironment(0)[6];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 8, string_id: 7759>  # String: 'complexTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[6].complexTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[6].complexTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 7>
    // USED → r6 = getParentEnvironment(0)[7];
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 9, string_id: 9384>  # String: 'ifTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[7].ifTest;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 7>
    // USED → r0 = 7;
    // CODE → <Call2>: <Reg8: 7, Reg8: 7, Reg8: 1, Reg8: 0>
    r7 = getParentEnvironment(0)[7].ifTest.call(undefined, 7)
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 10, string_id: 11028>  # String: 'ifElseChainTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[7].ifElseChainTest;
    // CODE → <LoadConstFalse>: <Reg8: 2>
    // USED → r2 = false;
    // CODE → <LoadConstTrue>: <Reg8: 3>
    // USED → r3 = true;
    // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 1, Reg8: 3, Reg8: 2>
    r6 = getParentEnvironment(0)[7].ifElseChainTest.call(undefined, true, false)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 8>
    // USED → r6 = getParentEnvironment(0)[8];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 11, string_id: 11072>  # String: 'tryCatchTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[8].tryCatchTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[8].tryCatchTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 9>
    // USED → r6 = getParentEnvironment(0)[9];
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 12, string_id: 11102>  # String: 'forOfTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[9].forOfTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[9].forOfTest.call(undefined)
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 13, string_id: 11099>  # String: 'forInTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[9].forInTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[9].forInTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 10>
    // USED → r6 = getParentEnvironment(0)[10];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 14, string_id: 8593>  # String: 'objectLiteralTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[10].objectLiteralTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[10].objectLiteralTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 11>
    // USED → r6 = getParentEnvironment(0)[11];
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 15, string_id: 10831>  # String: 'propertyAccessTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[11].propertyAccessTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[11].propertyAccessTest.call(undefined)
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 16, string_id: 11108>  # String: 'computedPropertyTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[11].computedPropertyTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[11].computedPropertyTest.call(undefined)
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 17, string_id: 11119>  # String: 'optionalChainingTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[11].optionalChainingTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[11].optionalChainingTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 12>
    // USED → r6 = getParentEnvironment(0)[12];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 18, string_id: 10961>  # String: 'arrayTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[12].arrayTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[12].arrayTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 13>
    // USED → r6 = getParentEnvironment(0)[13];
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 19, string_id: 10973>  # String: 'spreadArrayTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[13].spreadArrayTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[13].spreadArrayTest.call(undefined)
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 20, string_id: 10986>  # String: 'spreadObjectTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[13].spreadObjectTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[13].spreadObjectTest.call(undefined)
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 21, string_id: 10979>  # String: 'spreadFunctionArgsTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[13].spreadFunctionArgsTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[13].spreadFunctionArgsTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 14>
    // USED → r6 = getParentEnvironment(0)[14];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 22, string_id: 7917>  # String: 'arrowFunctionTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[14].arrowFunctionTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[14].arrowFunctionTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 15>
    // USED → r6 = getParentEnvironment(0)[15];
    // CODE → <GetById>: <Reg8: 7, Reg8: 6, UInt8: 23, string_id: 8902>  # String: 'closureTest' (Identifier)
    // USED → r7 = getParentEnvironment(0)[15].closureTest;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 1>
    r7 = getParentEnvironment(0)[15].closureTest.call(undefined)
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 24, string_id: 11088>  # String: 'closureLoopTest' (Identifier)
    // USED → r6 = getParentEnvironment(0)[15].closureLoopTest;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[15].closureLoopTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 5, UInt8: 16>
    // USED → r6 = getParentEnvironment(0)[16];
    // CODE → <GetById>: <Reg8: 6, Reg8: 6, UInt8: 25, string_id: 8313>  # String: 'callDefaultParameterTests' (Identifier)
    // USED → r6 = getParentEnvironment(0)[16].callDefaultParameterTests;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 1>
    r6 = getParentEnvironment(0)[16].callDefaultParameterTests.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 17>
    // USED → r5 = getParentEnvironment(0)[17];
    // CODE → <GetById>: <Reg8: 5, Reg8: 5, UInt8: 26, string_id: 11000>  # String: 'classTest' (Identifier)
    // USED → r5 = getParentEnvironment(0)[17].classTest;
    // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 1>
    r5 = getParentEnvironment(0)[17].classTest.call(undefined)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 3446>  # String: '__BC:index/runAllTests/end' (String)
    // USED → r4 = "__BC:index/runAllTests/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:index/runAllTests/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}