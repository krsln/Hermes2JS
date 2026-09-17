async function* ?anon_0_runAllTests() {
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 67 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 0>
    // USED → r5 = r1[0];
    // CODE → addr: 71 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 26>
    r7 = r1[0][26]
    // CODE → addr: 75 | <GetById>: <Reg8: 8, Reg8: 7, UInt8: 0, string_id: 10699>  # String: 'classTest' (Identifier)
    // USED → r8 = r7.classTest;
    // CODE → addr: 81 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr: 83 | <Call1>: <Reg8: 8, Reg8: 8, Reg8: 7>
    r8 = r7.classTest()
    // CODE → addr: 87 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 27>
    r5 = r1[0][27]
    // CODE → addr: 91 | <GetById>: <Reg8: 5, Reg8: 5, UInt8: 1, string_id: 11131>  # String: 'privateStaticTest' (Identifier)
    // USED → r5 = r5.privateStaticTest;
    // CODE → addr: 97 | <Call1>: <Reg8: 5, Reg8: 5, Reg8: 7>
    r5 = r5.privateStaticTest.call(r7)
    // CODE → addr:101 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:103 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:109 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:114 | <LoadConstString>: <Reg8: 5, string_id: 5016>  # String: '__BC:index/runAllTests/end' (String)
    // USED → r5 = "__BC:index/runAllTests/end";
    // CODE → addr:118 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log("__BC:index/runAllTests/end")
    // CODE → addr:123 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:126 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:130 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:136 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:183 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1)
    // CODE → addr:186 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = r7
    // CODE → addr:190 | <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → addr:192 | <TryGetById>: <Reg8: 11, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:198 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr:203 | <LoadConstString>: <Reg8: 8, string_id: 5019>  # String: '__BC:index/runAllTests/start' (String)
    // USED → r8 = "__BC:index/runAllTests/start";
    // CODE → addr:207 | <Call2>: <Reg8: 8, Reg8: 10, Reg8: 11, Reg8: 8>
    console.log("__BC:index/runAllTests/start")
    // CODE → addr:212 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 0>
    r8 = r7[0]
    // CODE → addr:216 | <GetById>: <Reg8: 10, Reg8: 8, UInt8: 4, string_id: 11270>  # String: 'whileTest' (Identifier)
    // USED → r10 = r8.whileTest;
    // CODE → addr:222 | <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → addr:224 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r8.whileTest()
    // CODE → addr:228 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 1>
    r10 = r7[1]
    // CODE → addr:232 | <GetById>: <Reg8: 10, Reg8: 10, UInt8: 5, string_id: 10741>  # String: 'doWhileTest' (Identifier)
    // USED → r10 = r10.doWhileTest;
    // CODE → addr:238 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r10.doWhileTest.call(r8)
    // CODE → addr:242 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 2>
    r10 = r7[2]
    // CODE → addr:246 | <GetById>: <Reg8: 10, Reg8: 10, UInt8: 6, string_id: 11162>  # String: 'forTest' (Identifier)
    // USED → r10 = r10.forTest;
    // CODE → addr:252 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r10.forTest.call(r8)
    // CODE → addr:256 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 3>
    r10 = r7[3]
    // CODE → addr:260 | <GetById>: <Reg8: 10, Reg8: 10, UInt8: 7, string_id: 11154>  # String: 'forEachTest' (Identifier)
    // USED → r10 = r10.forEachTest;
    // CODE → addr:266 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r10.forEachTest.call(r8)
    // CODE → addr:270 | <TryGetById>: <Reg8: 11, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:276 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 3, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr:281 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 4>
    r9 = r7[4]
    // CODE → addr:285 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 8, string_id: 11250>  # String: 'switchTest' (Identifier)
    // USED → r9 = r9.switchTest;
    // CODE → addr:291 | <LoadConstUInt8>: <Reg8: 12, UInt8: 4>
    // USED → r12 = 4;
    // CODE → addr:294 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 8, Reg8: 12>
    r9 = r9.switchTest.call(r8, 4)
    // CODE → addr:299 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log(r9)
    // CODE → addr:304 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 5>
    r9 = r7[5]
    // CODE → addr:308 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 9, string_id: 8686>  # String: 'nestedLoopTest' (Identifier)
    // USED → r9 = r9.nestedLoopTest;
    // CODE → addr:314 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.nestedLoopTest.call(r8)
    // CODE → addr:318 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 6>
    r9 = r7[6]
    // CODE → addr:322 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 10, string_id: 7943>  # String: 'complexTest' (Identifier)
    // USED → r9 = r9.complexTest;
    // CODE → addr:328 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.complexTest.call(r8)
    // CODE → addr:332 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 7>
    r9 = r7[7]
    // CODE → addr:336 | <GetById>: <Reg8: 11, Reg8: 9, UInt8: 11, string_id: 8063>  # String: 'ifTest' (Identifier)
    // USED → r11 = r9.ifTest;
    // CODE → addr:342 | <LoadConstUInt8>: <Reg8: 10, UInt8: 7>
    // USED → r10 = 7;
    // CODE → addr:345 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 10>
    r10 = r9.ifTest.call(r8, 7)
    // CODE → addr:350 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 12, string_id: 11176>  # String: 'ifElseChainTest' (Identifier)
    // USED → r9 = r9.ifElseChainTest;
    // CODE → addr:356 | <LoadConstFalse>: <Reg8: 10>
    r10 = false
    // CODE → addr:358 | <LoadConstTrue>: <Reg8: 11>
    r11 = true
    // CODE → addr:360 | <Call3>: <Reg8: 9, Reg8: 9, Reg8: 8, Reg8: 11, Reg8: 10>
    r9 = r9.ifElseChainTest.call(r8, r11, r10)
    // CODE → addr:366 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 8>
    r9 = r7[8]
    // CODE → addr:370 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 13, string_id: 11200>  # String: 'labeledBreakTest' (Identifier)
    // USED → r13 = r9.labeledBreakTest;
    // CODE → addr:376 | <Call1>: <Reg8: 13, Reg8: 13, Reg8: 8>
    r13 = r9.labeledBreakTest.call(r8)
    // CODE → addr:380 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 14, string_id: 11217>  # String: 'labeledContinueTest' (Identifier)
    // USED → r13 = r9.labeledContinueTest;
    // CODE → addr:386 | <Call1>: <Reg8: 13, Reg8: 13, Reg8: 8>
    r13 = r9.labeledContinueTest.call(r8)
    // CODE → addr:390 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 15, string_id: 9830>  # String: 'labeledBlockBreakTest' (Identifier)
    // USED → r13 = r9.labeledBlockBreakTest;
    // CODE → addr:396 | <Call1>: <Reg8: 13, Reg8: 13, Reg8: 8>
    r13 = r9.labeledBlockBreakTest.call(r8)
    // CODE → addr:400 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 16, string_id: 11239>  # String: 'tripleNestedLabeledTest' (Identifier)
    // USED → r9 = r9.tripleNestedLabeledTest;
    // CODE → addr:406 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.tripleNestedLabeledTest.call(r8)
    // CODE → addr:410 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 9>
    r9 = r7[9]
    // CODE → addr:414 | <GetById>: <Reg8: 14, Reg8: 9, UInt8: 17, string_id: 11266>  # String: 'ternaryTest' (Identifier)
    // USED → r14 = r9.ternaryTest;
    // CODE → addr:420 | <LoadConstInt>: <Reg8: 13, Imm32: -3>
    r13 = -3
    // CODE → addr:426 | <Call2>: <Reg8: 13, Reg8: 14, Reg8: 8, Reg8: 13>
    r13 = r9.ternaryTest.call(r8, r13)
    // CODE → addr:431 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 18, string_id: 11259>  # String: 'shortCircuitAssignTest' (Identifier)
    // USED → r13 = r9.shortCircuitAssignTest;
    // CODE → addr:437 | <Call1>: <Reg8: 13, Reg8: 13, Reg8: 8>
    r13 = r9.shortCircuitAssignTest.call(r8)
    // CODE → addr:441 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 19, string_id: 11252>  # String: 'logicalShortCircuitTest' (Identifier)
    // USED → r9 = r9.logicalShortCircuitTest;
    // CODE → addr:447 | <Call3>: <Reg8: 9, Reg8: 9, Reg8: 8, Reg8: 11, Reg8: 10>
    r9 = r9.logicalShortCircuitTest.call(r8, r11, r10)
    // CODE → addr:453 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 10>
    r9 = r7[10]
    // CODE → addr:457 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 20, string_id: 11383>  # String: 'tryCatchTest' (Identifier)
    // USED → r10 = r9.tryCatchTest;
    // CODE → addr:463 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryCatchTest.call(r8)
    // CODE → addr:467 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 21, string_id: 11371>  # String: 'tryCatchNoFinallyTest' (Identifier)
    // USED → r10 = r9.tryCatchNoFinallyTest;
    // CODE → addr:473 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryCatchNoFinallyTest.call(r8)
    // CODE → addr:477 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 22, string_id: 11406>  # String: 'tryFinallyNoCatchTest' (Identifier)
    // USED → r10 = r9.tryFinallyNoCatchTest;
    // CODE → addr:483 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryFinallyNoCatchTest.call(r8)
    // CODE → addr:487 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 23, string_id: 9141>  # String: 'tryFinallyNormalCompletionTest' (Identifier)
    // USED → r10 = r9.tryFinallyNormalCompletionTest;
    // CODE → addr:493 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryFinallyNormalCompletionTest.call(r8)
    // CODE → addr:497 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 24, string_id: 11376>  # String: 'tryCatchRethrowDifferentTest' (Identifier)
    // USED → r10 = r9.tryCatchRethrowDifferentTest;
    // CODE → addr:503 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryCatchRethrowDifferentTest.call(r8)
    // CODE → addr:507 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 25, string_id: 11423>  # String: 'tryLoopMultiReturnTest' (Identifier)
    // USED → r13 = r9.tryLoopMultiReturnTest;
    // CODE → addr:513 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 4, UInt16: 4, UInt16: 48899>  # Array: [1, 0, 4294967295, 2]
    r10 = [1, 0, 4294967295, 2]
    // CODE → addr:521 | <Call2>: <Reg8: 10, Reg8: 13, Reg8: 8, Reg8: 10>
    r10 = r9.tryLoopMultiReturnTest.call(r8, r10)
    // CODE → addr:526 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 26, string_id: 11316>  # String: 'nestedTryCatchTest' (Identifier)
    // USED → r10 = r9.nestedTryCatchTest;
    // CODE → addr:532 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.nestedTryCatchTest.call(r8)
    // CODE → addr:536 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 27, string_id: 11297>  # String: 'nestedTryCatchFinallyTest' (Identifier)
    // USED → r10 = r9.nestedTryCatchFinallyTest;
    // CODE → addr:542 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.nestedTryCatchFinallyTest.call(r8)
    // CODE → addr:546 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 28, string_id: 11342>  # String: 'tryCatchFinallyEarlyReturnTest' (Identifier)
    // USED → r10 = r9.tryCatchFinallyEarlyReturnTest;
    // CODE → addr:552 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.tryCatchFinallyEarlyReturnTest.call(r8)
    // CODE → addr:556 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 29, string_id: 11396>  # String: 'tryFinallyLoopBreakTest' (Identifier)
    // USED → r13 = r9.tryFinallyLoopBreakTest;
    // CODE → addr:562 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 4, UInt16: 4, UInt16: 48916>  # Array: [1, 2, 0, 3]
    r10 = [1, 2, 0, 3]
    // CODE → addr:570 | <Call2>: <Reg8: 10, Reg8: 13, Reg8: 8, Reg8: 10>
    r10 = r9.tryFinallyLoopBreakTest.call(r8, r10)
    // CODE → addr:575 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 30, string_id: 11363>  # String: 'tryCatchInsideLoopTest' (Identifier)
    // USED → r13 = r9.tryCatchInsideLoopTest;
    // CODE → addr:581 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 3, UInt16: 3, UInt16: 48933>  # Array: [1, 4294967294, 3]
    r10 = [1, 4294967294, 3]
    // CODE → addr:589 | <Call2>: <Reg8: 10, Reg8: 13, Reg8: 8, Reg8: 10>
    r10 = r9.tryCatchInsideLoopTest.call(r8, r10)
    // CODE → addr:594 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 31, string_id: 8220>  # String: 'tryCatchFinallyBranchInFinallyTest' (Identifier)
    // USED → r10 = r9.tryCatchFinallyBranchInFinallyTest;
    // CODE → addr:600 | <Call2>: <Reg8: 10, Reg8: 10, Reg8: 8, Reg8: 11>
    r10 = r9.tryCatchFinallyBranchInFinallyTest.call(r8, r11)
    // CODE → addr:605 | <GetById>: <Reg8: 11, Reg8: 9, UInt8: 32, string_id: 11354>  # String: 'tryCatchFinallyImplicitThrowTest' (Identifier)
    // USED → r11 = r9.tryCatchFinallyImplicitThrowTest;
    // CODE → addr:611 | <LoadConstUInt8>: <Reg8: 10, UInt8: 5>
    // USED → r10 = 5;
    // CODE → addr:614 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 10>
    r10 = r9.tryCatchFinallyImplicitThrowTest.call(r8, 5)
    // CODE → addr:619 | <GetById>: <Reg8: 11, Reg8: 9, UInt8: 33, string_id: 11279>  # String: 'loopBreakCrossesTryBoundaryTest' (Identifier)
    // USED → r11 = r9.loopBreakCrossesTryBoundaryTest;
    // CODE → addr:625 | <NewArrayWithBuffer>: <Reg8: 10, UInt16: 5, UInt16: 5, UInt16: 48946>  # Array: [1, 0, 2, 4294967295, 3]
    r10 = [1, 0, 2, 4294967295, 3]
    // CODE → addr:633 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 10>
    r10 = r9.loopBreakCrossesTryBoundaryTest.call(r8, r10)
    // CODE → addr:638 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 34, string_id: 11326>  # String: 'switchInsideTryTest' (Identifier)
    // USED → r9 = r9.switchInsideTryTest;
    // CODE → addr:644 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 8, Reg8: 5>
    r9 = r9.switchInsideTryTest.call(r8, 1)
    // CODE → addr:649 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 11>
    r9 = r7[11]
    // CODE → addr:653 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 35, string_id: 11516>  # String: 'forOfTest' (Identifier)
    // USED → r10 = r9.forOfTest;
    // CODE → addr:659 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.forOfTest.call(r8)
    // CODE → addr:663 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 36, string_id: 11511>  # String: 'forInTest' (Identifier)
    // USED → r9 = r9.forInTest;
    // CODE → addr:669 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.forInTest.call(r8)
    // CODE → addr:673 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 12>
    r9 = r7[12]
    // CODE → addr:677 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 37, string_id: 11564>  # String: 'objectLiteralTest' (Identifier)
    // USED → r9 = r9.objectLiteralTest;
    // CODE → addr:683 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.objectLiteralTest.call(r8)
    // CODE → addr:687 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 13>
    r9 = r7[13]
    // CODE → addr:691 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 38, string_id: 11582>  # String: 'propertyAccessTest' (Identifier)
    // USED → r10 = r9.propertyAccessTest;
    // CODE → addr:697 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.propertyAccessTest.call(r8)
    // CODE → addr:701 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 39, string_id: 11572>  # String: 'computedPropertyTest' (Identifier)
    // USED → r10 = r9.computedPropertyTest;
    // CODE → addr:707 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.computedPropertyTest.call(r8)
    // CODE → addr:711 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 40, string_id: 11578>  # String: 'optionalChainingTest' (Identifier)
    // USED → r9 = r9.optionalChainingTest;
    // CODE → addr:717 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.optionalChainingTest.call(r8)
    // CODE → addr:721 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 14>
    r9 = r7[14]
    // CODE → addr:725 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 41, string_id: 11521>  # String: 'callDestructuringTests' (Identifier)
    // USED → r9 = r9.callDestructuringTests;
    // CODE → addr:731 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callDestructuringTests.call(r8)
    // CODE → addr:735 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 15>
    r9 = r7[15]
    // CODE → addr:739 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 42, string_id: 11084>  # String: 'arrayTest' (Identifier)
    // USED → r9 = r9.arrayTest;
    // CODE → addr:745 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.arrayTest.call(r8)
    // CODE → addr:749 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 16>
    r9 = r7[16]
    // CODE → addr:753 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 43, string_id: 11094>  # String: 'spreadArrayTest' (Identifier)
    // USED → r10 = r9.spreadArrayTest;
    // CODE → addr:759 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.spreadArrayTest.call(r8)
    // CODE → addr:763 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 44, string_id: 11109>  # String: 'spreadObjectTest' (Identifier)
    // USED → r10 = r9.spreadObjectTest;
    // CODE → addr:769 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.spreadObjectTest.call(r8)
    // CODE → addr:773 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 45, string_id: 11102>  # String: 'spreadFunctionArgsTest' (Identifier)
    // USED → r9 = r9.spreadFunctionArgsTest;
    // CODE → addr:779 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.spreadFunctionArgsTest.call(r8)
    // CODE → addr:783 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 17>
    r9 = r7[17]
    // CODE → addr:787 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 46, string_id: 6539>  # String: 'callMapSetTests' (Identifier)
    // USED → r9 = r9.callMapSetTests;
    // CODE → addr:793 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callMapSetTests.call(r8)
    // CODE → addr:797 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 18>
    r9 = r7[18]
    // CODE → addr:801 | <GetById>: <Reg8: 13, Reg8: 9, UInt8: 47, string_id: 11614>  # String: 'basicTemplateTest' (Identifier)
    // USED → r13 = r9.basicTemplateTest;
    // CODE → addr:807 | <LoadConstUInt8>: <Reg8: 11, UInt8: 30>
    // USED → r11 = 30;
    // CODE → addr:810 | <LoadConstString>: <Reg8: 10, string_id: 2521>  # String: 'Ada' (String)
    // USED → r10 = "Ada";
    // CODE → addr:814 | <Call3>: <Reg8: 10, Reg8: 13, Reg8: 8, Reg8: 10, Reg8: 11>
    r10 = r9.basicTemplateTest.call(r8, "Ada", 30)
    // CODE → addr:820 | <GetById>: <Reg8: 11, Reg8: 9, UInt8: 48, string_id: 11621>  # String: 'nestedTemplateTest' (Identifier)
    // USED → r11 = r9.nestedTemplateTest;
    // CODE → addr:826 | <LoadConstUInt8>: <Reg8: 10, UInt8: 9>
    // USED → r10 = 9;
    // CODE → addr:829 | <Call3>: <Reg8: 10, Reg8: 11, Reg8: 8, Reg8: 12, Reg8: 10>
    r10 = r9.nestedTemplateTest.call(r8, 4, 9)
    // CODE → addr:835 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 49, string_id: 7693>  # String: 'taggedTemplateTest' (Identifier)
    // USED → r10 = r9.taggedTemplateTest;
    // CODE → addr:841 | <LoadConstUInt8>: <Reg8: 9, UInt8: 6>
    // USED → r9 = 6;
    // CODE → addr:844 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 8, Reg8: 9>
    r9 = r9.taggedTemplateTest.call(r8, 6)
    // CODE → addr:849 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 19>
    r9 = r7[19]
    // CODE → addr:853 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 50, string_id: 10554>  # String: 'callRegExpTests' (Identifier)
    // USED → r9 = r9.callRegExpTests;
    // CODE → addr:859 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callRegExpTests.call(r8)
    // CODE → addr:863 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 20>
    r9 = r7[20]
    // CODE → addr:867 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 51, string_id: 11426>  # String: 'arrowFunctionTest' (Identifier)
    // USED → r9 = r9.arrowFunctionTest;
    // CODE → addr:873 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.arrowFunctionTest.call(r8)
    // CODE → addr:877 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 21>
    r9 = r7[21]
    // CODE → addr:881 | <GetById>: <Reg8: 10, Reg8: 9, UInt8: 52, string_id: 11462>  # String: 'closureTest' (Identifier)
    // USED → r10 = r9.closureTest;
    // CODE → addr:887 | <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
    r10 = r9.closureTest.call(r8)
    // CODE → addr:891 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 53, string_id: 11454>  # String: 'closureLoopTest' (Identifier)
    // USED → r9 = r9.closureLoopTest;
    // CODE → addr:897 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.closureLoopTest.call(r8)
    // CODE → addr:901 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 22>
    r9 = r7[22]
    // CODE → addr:905 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 54, string_id: 11465>  # String: 'callDefaultParameterTests' (Identifier)
    // USED → r9 = r9.callDefaultParameterTests;
    // CODE → addr:911 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callDefaultParameterTests.call(r8)
    // CODE → addr:915 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 23>
    r9 = r7[23]
    // CODE → addr:919 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 55, string_id: 11498>  # String: 'callRestParameterTests' (Identifier)
    // USED → r9 = r9.callRestParameterTests;
    // CODE → addr:925 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callRestParameterTests.call(r8)
    // CODE → addr:929 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 24>
    r9 = r7[24]
    // CODE → addr:933 | <GetById>: <Reg8: 9, Reg8: 9, UInt8: 56, string_id: 11473>  # String: 'callGeneratorTests' (Identifier)
    // USED → r9 = r9.callGeneratorTests;
    // CODE → addr:939 | <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
    r9 = r9.callGeneratorTests.call(r8)
    // CODE → addr:943 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 7, UInt8: 25>
    r7 = r7[25]
    // CODE → addr:947 | <GetById>: <Reg8: 7, Reg8: 7, UInt8: 57, string_id: 8316>  # String: 'callAsyncTests' (Identifier)
    // USED → r7 = r7.callAsyncTests;
    // CODE → addr:953 | <Call1>: <Reg8: 7, Reg8: 7, Reg8: 8>
    await r7.callAsyncTests.call(r8)
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:1008 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:1010 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:1013 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:1017 | <Throw>: <Reg8: 5>
    throw r5;
}