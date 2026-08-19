async function* anon_15045() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    // CODE → <JmpTrueLong>: <Addr32: 997, Reg8: 1>  # Address: 000003e9
    if (__resumeIsReturn) goto label_1001;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4866>  # String: '__BC:index/runAllTests/start' (String)
    // USED → r1 = "__BC:index/runAllTests/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:index/runAllTests/start")
    // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
    r4 = getEnvironment(2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 1>
    r1 = r4[1]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 10971>  # String: 'whileTest' (Identifier)
    // USED → r1 = r1.whileTest;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.whileTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 2>
    r1 = r4[2]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 4, string_id: 10882>  # String: 'doWhileTest' (Identifier)
    // USED → r1 = r1.doWhileTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.doWhileTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
    r1 = r4[3]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 10341>  # String: 'forTest' (Identifier)
    // USED → r1 = r1.forTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.forTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 4>
    r1 = r4[4]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 10885>  # String: 'forEachTest' (Identifier)
    // USED → r1 = r1.forEachTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.forEachTest.call(r2)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 5>
    r1 = r4[5]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 8729>  # String: 'switchTest' (Identifier)
    // USED → r1 = r1.switchTest;
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 4>
    // USED → r6 = 4;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 6>
    // USED → r1 = r1.switchTest.call(r2, 4);
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 7, Reg8: 1>
    console.log(r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 6>
    r1 = r4[6]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 10944>  # String: 'nestedLoopTest' (Identifier)
    // USED → r1 = r1.nestedLoopTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.nestedLoopTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 7>
    r1 = r4[7]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 9, string_id: 7792>  # String: 'complexTest' (Identifier)
    // USED → r1 = r1.complexTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.complexTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
    r1 = r4[8]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 10, string_id: 8596>  # String: 'ifTest' (Identifier)
    // USED → r5 = r1.ifTest;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 7>
    // USED → r1 = 7;
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
    r1 = r1.ifTest.call(r2, 7)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
    r1 = r4[8]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 11, string_id: 10899>  # String: 'ifElseChainTest' (Identifier)
    // USED → r1 = r1.ifElseChainTest;
    // CODE → <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → <LoadConstFalse>: <Reg8: 7>
    // USED → r7 = false;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
    r1 = r1.ifElseChainTest.call(r2, r5, r7)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
    r1 = r4[9]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 12, string_id: 10933>  # String: 'labeledBreakTest' (Identifier)
    // USED → r1 = r1.labeledBreakTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.labeledBreakTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
    r1 = r4[9]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 13, string_id: 10940>  # String: 'labeledContinueTest' (Identifier)
    // USED → r1 = r1.labeledContinueTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.labeledContinueTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
    r1 = r4[9]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 14, string_id: 8658>  # String: 'labeledBlockBreakTest' (Identifier)
    // USED → r1 = r1.labeledBlockBreakTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.labeledBlockBreakTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
    r1 = r4[9]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 15, string_id: 10646>  # String: 'tripleNestedLabeledTest' (Identifier)
    // USED → r1 = r1.tripleNestedLabeledTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tripleNestedLabeledTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
    r1 = r4[10]
    // CODE → <GetById>: <Reg8: 8, Reg8: 1, UInt8: 16, string_id: 9849>  # String: 'ternaryTest' (Identifier)
    // USED → r8 = r1.ternaryTest;
    // CODE → <LoadConstInt>: <Reg8: 1, Imm32: -3>
    // USED → r1 = -3;
    // CODE → <Call2>: <Reg8: 1, Reg8: 8, Reg8: 2, Reg8: 1>
    r1 = r1.ternaryTest.call(r2, r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
    r1 = r4[10]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 17, string_id: 10963>  # String: 'shortCircuitAssignTest' (Identifier)
    // USED → r1 = r1.shortCircuitAssignTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.shortCircuitAssignTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
    r1 = r4[10]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 18, string_id: 10952>  # String: 'logicalShortCircuitTest' (Identifier)
    // USED → r1 = r1.logicalShortCircuitTest;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
    r1 = r1.logicalShortCircuitTest.call(r2, r5, r7)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 19, string_id: 11096>  # String: 'tryCatchTest' (Identifier)
    // USED → r1 = r1.tryCatchTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryCatchTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 20, string_id: 11065>  # String: 'tryCatchNoFinallyTest' (Identifier)
    // USED → r1 = r1.tryCatchNoFinallyTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryCatchNoFinallyTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 21, string_id: 11122>  # String: 'tryFinallyNoCatchTest' (Identifier)
    // USED → r1 = r1.tryFinallyNoCatchTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryFinallyNoCatchTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 22, string_id: 11126>  # String: 'tryFinallyNormalCompletionTest' (Identifier)
    // USED → r1 = r1.tryFinallyNormalCompletionTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryFinallyNormalCompletionTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 23, string_id: 11088>  # String: 'tryCatchRethrowDifferentTest' (Identifier)
    // USED → r1 = r1.tryCatchRethrowDifferentTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryCatchRethrowDifferentTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 24, string_id: 10295>  # String: 'tryLoopMultiReturnTest' (Identifier)
    // USED → r7 = r1.tryLoopMultiReturnTest;
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 4, UInt16: 2, UInt16: 23560>  # Array: [1, 0]
    r1 = [1, 0]
    // CODE → <LoadConstInt>: <Reg8: 8, Imm32: -1>
    // USED → r8 = -1;
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 8, UInt8: 2>
    // USED → r1 = r1[2] = -1;
    // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 2>
    // USED → r9 = 2;
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 9, UInt8: 3>
    // USED → r1 = (r1[2] = -1)[3] = 2;
    // CODE → <Call2>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 1>
    r1 = r1.tryLoopMultiReturnTest.call(r2, r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 11002>  # String: 'nestedTryCatchTest' (Identifier)
    // USED → r1 = r1.nestedTryCatchTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.nestedTryCatchTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 26, string_id: 10992>  # String: 'nestedTryCatchFinallyTest' (Identifier)
    // USED → r1 = r1.nestedTryCatchFinallyTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.nestedTryCatchFinallyTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 27, string_id: 11030>  # String: 'tryCatchFinallyEarlyReturnTest' (Identifier)
    // USED → r1 = r1.tryCatchFinallyEarlyReturnTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.tryCatchFinallyEarlyReturnTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 28, string_id: 11112>  # String: 'tryFinallyLoopBreakTest' (Identifier)
    // USED → r7 = r1.tryFinallyLoopBreakTest;
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 4, UInt16: 4, UInt16: 23569>  # Array: [1, 2, 0, 3]
    // USED → r1 = [1, 2, 0, 3];
    // CODE → <Call2>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 1>
    r1 = r1.tryFinallyLoopBreakTest.call(r2, r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 9, Reg8: 1, UInt8: 29, string_id: 8691>  # String: 'tryCatchInsideLoopTest' (Identifier)
    // USED → r9 = r1.tryCatchInsideLoopTest;
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 3, UInt16: 1, UInt16: 3>  # Array: [1]
    r1 = [1]
    // CODE → <LoadConstInt>: <Reg8: 7, Imm32: -2>
    // USED → r7 = -2;
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 1>
    // USED → r1 = r1[1] = -2;
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
    // USED → r7 = 3;
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 2>
    // USED → r1 = (r1[1] = -2)[2] = 3;
    // CODE → <Call2>: <Reg8: 1, Reg8: 9, Reg8: 2, Reg8: 1>
    r1 = r1.tryCatchInsideLoopTest.call(r2, r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 30, string_id: 8711>  # String: 'tryCatchFinallyBranchInFinallyTest' (Identifier)
    // USED → r1 = r1.tryCatchFinallyBranchInFinallyTest;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5>
    r1 = r1.tryCatchFinallyBranchInFinallyTest.call(r2, r5)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 31, string_id: 11038>  # String: 'tryCatchFinallyImplicitThrowTest' (Identifier)
    // USED → r5 = r1.tryCatchFinallyImplicitThrowTest;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
    r1 = r1.tryCatchFinallyImplicitThrowTest.call(r2, 5)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 32, string_id: 10975>  # String: 'loopBreakCrossesTryBoundaryTest' (Identifier)
    // USED → r5 = r1.loopBreakCrossesTryBoundaryTest;
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 5, UInt16: 3, UInt16: 23586>  # Array: [1, 0, 2]
    r1 = [1, 0, 2]
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 8, UInt8: 3>
    // USED → r1 = r1[3] = -1;
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 4>
    // USED → r1 = (r1[3] = -1)[4] = 3;
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
    r1 = r1.loopBreakCrossesTryBoundaryTest.call(r2, r1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
    r1 = r4[11]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 33, string_id: 8763>  # String: 'switchInsideTryTest' (Identifier)
    // USED → r5 = r1.switchInsideTryTest;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
    r1 = r1.switchInsideTryTest.call(r2, 1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
    r1 = r4[12]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 34, string_id: 11254>  # String: 'forOfTest' (Identifier)
    // USED → r1 = r1.forOfTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.forOfTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
    r1 = r4[12]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 35, string_id: 11239>  # String: 'forInTest' (Identifier)
    // USED → r1 = r1.forInTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.forInTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 13>
    r1 = r4[13]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 36, string_id: 11286>  # String: 'objectLiteralTest' (Identifier)
    // USED → r1 = r1.objectLiteralTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.objectLiteralTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
    r1 = r4[14]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 37, string_id: 11307>  # String: 'propertyAccessTest' (Identifier)
    // USED → r1 = r1.propertyAccessTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.propertyAccessTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
    r1 = r4[14]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 38, string_id: 11290>  # String: 'computedPropertyTest' (Identifier)
    // USED → r1 = r1.computedPropertyTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.computedPropertyTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
    r1 = r4[14]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 39, string_id: 11295>  # String: 'optionalChainingTest' (Identifier)
    // USED → r1 = r1.optionalChainingTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.optionalChainingTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 15>
    r1 = r4[15]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 40, string_id: 10657>  # String: 'callDestructuringTests' (Identifier)
    // USED → r1 = r1.callDestructuringTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callDestructuringTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 16>
    r1 = r4[16]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 41, string_id: 7969>  # String: 'arrayTest' (Identifier)
    // USED → r1 = r1.arrayTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.arrayTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
    r1 = r4[17]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 42, string_id: 10787>  # String: 'spreadArrayTest' (Identifier)
    // USED → r1 = r1.spreadArrayTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.spreadArrayTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
    r1 = r4[17]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 43, string_id: 10795>  # String: 'spreadObjectTest' (Identifier)
    // USED → r1 = r1.spreadObjectTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.spreadObjectTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
    r1 = r4[17]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 44, string_id: 10792>  # String: 'spreadFunctionArgsTest' (Identifier)
    // USED → r1 = r1.spreadFunctionArgsTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.spreadFunctionArgsTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 18>
    r1 = r4[18]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 45, string_id: 7228>  # String: 'callMapSetTests' (Identifier)
    // USED → r1 = r1.callMapSetTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callMapSetTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
    r1 = r4[19]
    // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 46, string_id: 11328>  # String: 'basicTemplateTest' (Identifier)
    // USED → r7 = r1.basicTemplateTest;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 2445>  # String: 'Ada' (String)
    // USED → r5 = "Ada";
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 30>
    // USED → r1 = 30;
    // CODE → <Call3>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 5, Reg8: 1>
    r1 = r1.basicTemplateTest.call(r2, "Ada", 30)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
    r1 = r4[19]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 47, string_id: 11332>  # String: 'nestedTemplateTest' (Identifier)
    // USED → r5 = r1.nestedTemplateTest;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 9>
    // USED → r1 = 9;
    // CODE → <Call3>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 6, Reg8: 1>
    r1 = r1.nestedTemplateTest.call(r2, 4, 9)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
    r1 = r4[19]
    // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 48, string_id: 11337>  # String: 'taggedTemplateTest' (Identifier)
    // USED → r5 = r1.taggedTemplateTest;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 6>
    // USED → r1 = 6;
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
    r1 = r1.taggedTemplateTest.call(r2, 6)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 20>
    r1 = r4[20]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 49, string_id: 11311>  # String: 'callRegExpTests' (Identifier)
    // USED → r1 = r1.callRegExpTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callRegExpTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 21>
    r1 = r4[21]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 50, string_id: 11139>  # String: 'arrowFunctionTest' (Identifier)
    // USED → r1 = r1.arrowFunctionTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.arrowFunctionTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
    r1 = r4[22]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 51, string_id: 10113>  # String: 'closureTest' (Identifier)
    // USED → r1 = r1.closureTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.closureTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
    r1 = r4[22]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 52, string_id: 11176>  # String: 'closureLoopTest' (Identifier)
    // USED → r1 = r1.closureLoopTest;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.closureLoopTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 23>
    r1 = r4[23]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 53, string_id: 11182>  # String: 'callDefaultParameterTests' (Identifier)
    // USED → r1 = r1.callDefaultParameterTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callDefaultParameterTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 24>
    r1 = r4[24]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 54, string_id: 11222>  # String: 'callRestParameterTests' (Identifier)
    // USED → r1 = r1.callRestParameterTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callRestParameterTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 25>
    r1 = r4[25]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 55, string_id: 11199>  # String: 'callGeneratorTests' (Identifier)
    // USED → r1 = r1.callGeneratorTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r1.callGeneratorTests.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 26>
    r1 = r4[26]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 56, string_id: 9338>  # String: 'callAsyncTests' (Identifier)
    // USED → r1 = r1.callAsyncTests;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    // USED → r1 = await r1.callAsyncTests.call(r2);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 000003ad
    goto label_941;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return await r1.callAsyncTests.call(r2);
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 5>
    // USED → r1 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 5>
    // USED → r5 = __resumeIsReturn;
    // CODE → <JmpTrue>: <Addr8: 54, Reg8: 5>  # Address: 000003e6
    if (__resumeIsReturn) goto label_998;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 4, UInt8: 27>
    r5 = r4[27]
    // CODE → <GetById>: <Reg8: 5, Reg8: 5, UInt8: 57, string_id: 10812>  # String: 'classTest' (Identifier)
    // USED → r5 = r5.classTest;
    // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 2>
    r5 = r5.classTest.call(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 28>
    r4 = r4[28]
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 58, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
    // USED → r4 = r4.privateStaticTest;
    // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 2>
    r4 = r4.privateStaticTest.call(r2)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4865>  # String: '__BC:index/runAllTests/end' (String)
    // USED → r3 = "__BC:index/runAllTests/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:index/runAllTests/end")
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