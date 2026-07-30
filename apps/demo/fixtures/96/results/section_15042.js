function runAllTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4616>  # String: '__BC:index/runAllTests/start' (String)
    // USED → r0 = "__BC:index/runAllTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:index/runAllTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 2, UInt8: 0>
    // USED → r0 = getEnvironment(0)[0];
    // CODE → <GetById>: <Reg8: 3, Reg8: 0, UInt8: 3, string_id: 10754>  # String: 'whileTest' (Identifier)
    // USED → r3 = getEnvironment(0)[0].whileTest;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[0].whileTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 1>
    // USED → r3 = getEnvironment(0)[1];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 10692>  # String: 'doWhileTest' (Identifier)
    // USED → r3 = getEnvironment(0)[1].doWhileTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[1].doWhileTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = getEnvironment(0)[2];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 10710>  # String: 'forTest' (Identifier)
    // USED → r3 = getEnvironment(0)[2].forTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[2].forTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = getEnvironment(0)[3];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 6, string_id: 10704>  # String: 'forEachTest' (Identifier)
    // USED → r3 = getEnvironment(0)[3].forEachTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[3].forEachTest.call(undefined)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 4>
    // USED → r3 = getEnvironment(0)[4];
    // CODE → <GetById>: <Reg8: 6, Reg8: 3, UInt8: 7, string_id: 8540>  # String: 'switchTest' (Identifier)
    // USED → r6 = getEnvironment(0)[4].switchTest;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 4>
    // USED → r3 = 4;
    // CODE → <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 3>
    // USED → r3 = getEnvironment(0)[4].switchTest.call(undefined, 4);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log(getEnvironment(0)[4].switchTest.call(undefined, 4))
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 5>
    // USED → r3 = getEnvironment(0)[5];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 8, string_id: 10744>  # String: 'nestedLoopTest' (Identifier)
    // USED → r3 = getEnvironment(0)[5].nestedLoopTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[5].nestedLoopTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 6>
    // USED → r3 = getEnvironment(0)[6];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 9, string_id: 7572>  # String: 'complexTest' (Identifier)
    // USED → r3 = getEnvironment(0)[6].complexTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[6].complexTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 7>
    // USED → r3 = getEnvironment(0)[7];
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 10, string_id: 10728>  # String: 'ifTest' (Identifier)
    // USED → r4 = getEnvironment(0)[7].ifTest;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 7>
    // USED → r3 = 7;
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = getEnvironment(0)[7].ifTest.call(undefined, 7)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 7>
    // USED → r3 = getEnvironment(0)[7];
    // CODE → <GetById>: <Reg8: 5, Reg8: 3, UInt8: 11, string_id: 10719>  # String: 'ifElseChainTest' (Identifier)
    // USED → r5 = getEnvironment(0)[7].ifElseChainTest;
    // CODE → <LoadConstTrue>: <Reg8: 4>
    // USED → r4 = true;
    // CODE → <LoadConstFalse>: <Reg8: 3>
    // USED → r3 = false;
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 3>
    r3 = getEnvironment(0)[7].ifElseChainTest.call(undefined, true, false)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 8>
    // USED → r3 = getEnvironment(0)[8];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 12, string_id: 10761>  # String: 'tryCatchTest' (Identifier)
    // USED → r3 = getEnvironment(0)[8].tryCatchTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[8].tryCatchTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 9>
    // USED → r3 = getEnvironment(0)[9];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 13, string_id: 10789>  # String: 'forOfTest' (Identifier)
    // USED → r3 = getEnvironment(0)[9].forOfTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[9].forOfTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 9>
    // USED → r3 = getEnvironment(0)[9];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 14, string_id: 8463>  # String: 'forInTest' (Identifier)
    // USED → r3 = getEnvironment(0)[9].forInTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[9].forInTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 10>
    // USED → r3 = getEnvironment(0)[10];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 15, string_id: 10792>  # String: 'objectLiteralTest' (Identifier)
    // USED → r3 = getEnvironment(0)[10].objectLiteralTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[10].objectLiteralTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 11>
    // USED → r3 = getEnvironment(0)[11];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 16, string_id: 10808>  # String: 'propertyAccessTest' (Identifier)
    // USED → r3 = getEnvironment(0)[11].propertyAccessTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[11].propertyAccessTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 11>
    // USED → r3 = getEnvironment(0)[11];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 17, string_id: 10801>  # String: 'computedPropertyTest' (Identifier)
    // USED → r3 = getEnvironment(0)[11].computedPropertyTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[11].computedPropertyTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 11>
    // USED → r3 = getEnvironment(0)[11];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 18, string_id: 9758>  # String: 'optionalChainingTest' (Identifier)
    // USED → r3 = getEnvironment(0)[11].optionalChainingTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[11].optionalChainingTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 12>
    // USED → r3 = getEnvironment(0)[12];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 19, string_id: 7735>  # String: 'arrayTest' (Identifier)
    // USED → r3 = getEnvironment(0)[12].arrayTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[12].arrayTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 13>
    // USED → r3 = getEnvironment(0)[13];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 20, string_id: 10645>  # String: 'spreadArrayTest' (Identifier)
    // USED → r3 = getEnvironment(0)[13].spreadArrayTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[13].spreadArrayTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 13>
    // USED → r3 = getEnvironment(0)[13];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 21, string_id: 10651>  # String: 'spreadObjectTest' (Identifier)
    // USED → r3 = getEnvironment(0)[13].spreadObjectTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[13].spreadObjectTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 13>
    // USED → r3 = getEnvironment(0)[13];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 22, string_id: 10648>  # String: 'spreadFunctionArgsTest' (Identifier)
    // USED → r3 = getEnvironment(0)[13].spreadFunctionArgsTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[13].spreadFunctionArgsTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 14>
    // USED → r3 = getEnvironment(0)[14];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 23, string_id: 10769>  # String: 'arrowFunctionTest' (Identifier)
    // USED → r3 = getEnvironment(0)[14].arrowFunctionTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[14].arrowFunctionTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 15>
    // USED → r3 = getEnvironment(0)[15];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 24, string_id: 9676>  # String: 'closureTest' (Identifier)
    // USED → r3 = getEnvironment(0)[15].closureTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[15].closureTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 15>
    // USED → r3 = getEnvironment(0)[15];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 25, string_id: 10775>  # String: 'closureLoopTest' (Identifier)
    // USED → r3 = getEnvironment(0)[15].closureLoopTest;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[15].closureLoopTest.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 16>
    // USED → r3 = getEnvironment(0)[16];
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 26, string_id: 10781>  # String: 'callDefaultParameterTests' (Identifier)
    // USED → r3 = getEnvironment(0)[16].callDefaultParameterTests;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = getEnvironment(0)[16].callDefaultParameterTests.call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 17>
    // USED → r2 = getEnvironment(0)[17];
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 27, string_id: 10666>  # String: 'classTest' (Identifier)
    // USED → r2 = getEnvironment(0)[17].classTest;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = getEnvironment(0)[17].classTest.call(undefined)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4615>  # String: '__BC:index/runAllTests/end' (String)
    // USED → r1 = "__BC:index/runAllTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:index/runAllTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}