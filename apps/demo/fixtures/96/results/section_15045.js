async function* anon_15045() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        return await yield;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetGlobalObject>: <Reg8: 3>
        // USED → r3 = globalThis;
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 1, string_id: 4866>  # String: '__BC:index/runAllTests/start' (String)
        // USED → r1 = "__BC:index/runAllTests/start";
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
        console.log("__BC:index/runAllTests/start")
        // CODE → <GetEnvironment>: <Reg8: 4, UInt8: 2>
        // USED → r4 = getEnvironment(2);
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 1>
        // USED → r1 = getEnvironment(2)[1];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 10971>  # String: 'whileTest' (Identifier)
        // USED → r1 = getEnvironment(2)[1].whileTest;
        // CODE → <LoadConstUndefined>: <Reg8: 2>
        // USED → r2 = undefined;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[1].whileTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 2>
        // USED → r1 = getEnvironment(2)[2];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 4, string_id: 10882>  # String: 'doWhileTest' (Identifier)
        // USED → r1 = getEnvironment(2)[2].doWhileTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[2].doWhileTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
        // USED → r1 = getEnvironment(2)[3];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 10341>  # String: 'forTest' (Identifier)
        // USED → r1 = getEnvironment(2)[3].forTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[3].forTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 4>
        // USED → r1 = getEnvironment(2)[4];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 10885>  # String: 'forEachTest' (Identifier)
        // USED → r1 = getEnvironment(2)[4].forEachTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[4].forEachTest.call(undefined)
        // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r7 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = globalThis.console.log;
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 5>
        // USED → r1 = getEnvironment(2)[5];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 8729>  # String: 'switchTest' (Identifier)
        // USED → r1 = getEnvironment(2)[5].switchTest;
        // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 4>
        // USED → r6 = 4;
        // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 6>
        // USED → r1 = getEnvironment(2)[5].switchTest.call(undefined, r6);
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 7, Reg8: 1>
        console.log(r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 6>
        // USED → r1 = getEnvironment(2)[6];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 10944>  # String: 'nestedLoopTest' (Identifier)
        // USED → r1 = getEnvironment(2)[6].nestedLoopTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[6].nestedLoopTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 7>
        // USED → r1 = getEnvironment(2)[7];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 9, string_id: 7792>  # String: 'complexTest' (Identifier)
        // USED → r1 = getEnvironment(2)[7].complexTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[7].complexTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
        // USED → r1 = getEnvironment(2)[8];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 10, string_id: 8596>  # String: 'ifTest' (Identifier)
        // USED → r5 = getEnvironment(2)[8].ifTest;
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 7>
        // USED → r1 = 7;
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[8].ifTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
        // USED → r1 = getEnvironment(2)[8];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 11, string_id: 10899>  # String: 'ifElseChainTest' (Identifier)
        // USED → r1 = getEnvironment(2)[8].ifElseChainTest;
        // CODE → <LoadConstTrue>: <Reg8: 5>
        // USED → r5 = true;
        // CODE → <LoadConstFalse>: <Reg8: 7>
        // USED → r7 = false;
        // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
        r1 = getEnvironment(2)[8].ifElseChainTest.call(undefined, r5, r7)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        // USED → r1 = getEnvironment(2)[9];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 12, string_id: 10933>  # String: 'labeledBreakTest' (Identifier)
        // USED → r1 = getEnvironment(2)[9].labeledBreakTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[9].labeledBreakTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        // USED → r1 = getEnvironment(2)[9];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 13, string_id: 10940>  # String: 'labeledContinueTest' (Identifier)
        // USED → r1 = getEnvironment(2)[9].labeledContinueTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[9].labeledContinueTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        // USED → r1 = getEnvironment(2)[9];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 14, string_id: 8658>  # String: 'labeledBlockBreakTest' (Identifier)
        // USED → r1 = getEnvironment(2)[9].labeledBlockBreakTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[9].labeledBlockBreakTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        // USED → r1 = getEnvironment(2)[9];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 15, string_id: 10646>  # String: 'tripleNestedLabeledTest' (Identifier)
        // USED → r1 = getEnvironment(2)[9].tripleNestedLabeledTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[9].tripleNestedLabeledTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        // USED → r1 = getEnvironment(2)[10];
        // CODE → <GetById>: <Reg8: 8, Reg8: 1, UInt8: 16, string_id: 9849>  # String: 'ternaryTest' (Identifier)
        // USED → r8 = getEnvironment(2)[10].ternaryTest;
        // CODE → <LoadConstInt>: <Reg8: 1, Imm32: -3>
        // USED → r1 = -3;
        // CODE → <Call2>: <Reg8: 1, Reg8: 8, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[10].ternaryTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        // USED → r1 = getEnvironment(2)[10];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 17, string_id: 10963>  # String: 'shortCircuitAssignTest' (Identifier)
        // USED → r1 = getEnvironment(2)[10].shortCircuitAssignTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[10].shortCircuitAssignTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        // USED → r1 = getEnvironment(2)[10];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 18, string_id: 10952>  # String: 'logicalShortCircuitTest' (Identifier)
        // USED → r1 = getEnvironment(2)[10].logicalShortCircuitTest;
        // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
        r1 = getEnvironment(2)[10].logicalShortCircuitTest.call(undefined, r5, r7)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 19, string_id: 11096>  # String: 'tryCatchTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryCatchTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryCatchTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 20, string_id: 11065>  # String: 'tryCatchNoFinallyTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryCatchNoFinallyTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryCatchNoFinallyTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 21, string_id: 11122>  # String: 'tryFinallyNoCatchTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryFinallyNoCatchTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryFinallyNoCatchTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 22, string_id: 11126>  # String: 'tryFinallyNormalCompletionTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryFinallyNormalCompletionTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryFinallyNormalCompletionTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 23, string_id: 11088>  # String: 'tryCatchRethrowDifferentTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryCatchRethrowDifferentTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryCatchRethrowDifferentTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 24, string_id: 10295>  # String: 'tryLoopMultiReturnTest' (Identifier)
        // USED → r7 = getEnvironment(2)[11].tryLoopMultiReturnTest;
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
        r1 = getEnvironment(2)[11].tryLoopMultiReturnTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 11002>  # String: 'nestedTryCatchTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].nestedTryCatchTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].nestedTryCatchTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 26, string_id: 10992>  # String: 'nestedTryCatchFinallyTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].nestedTryCatchFinallyTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].nestedTryCatchFinallyTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 27, string_id: 11030>  # String: 'tryCatchFinallyEarlyReturnTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryCatchFinallyEarlyReturnTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[11].tryCatchFinallyEarlyReturnTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 28, string_id: 11112>  # String: 'tryFinallyLoopBreakTest' (Identifier)
        // USED → r7 = getEnvironment(2)[11].tryFinallyLoopBreakTest;
        // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 4, UInt16: 4, UInt16: 23569>  # Array: [1, 2, 0, 3]
        // USED → r1 = [1, 2, 0, 3];
        // CODE → <Call2>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[11].tryFinallyLoopBreakTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 9, Reg8: 1, UInt8: 29, string_id: 8691>  # String: 'tryCatchInsideLoopTest' (Identifier)
        // USED → r9 = getEnvironment(2)[11].tryCatchInsideLoopTest;
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
        r1 = getEnvironment(2)[11].tryCatchInsideLoopTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 30, string_id: 8711>  # String: 'tryCatchFinallyBranchInFinallyTest' (Identifier)
        // USED → r1 = getEnvironment(2)[11].tryCatchFinallyBranchInFinallyTest;
        // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5>
        r1 = getEnvironment(2)[11].tryCatchFinallyBranchInFinallyTest.call(undefined, r5)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 31, string_id: 11038>  # String: 'tryCatchFinallyImplicitThrowTest' (Identifier)
        // USED → r5 = getEnvironment(2)[11].tryCatchFinallyImplicitThrowTest;
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
        // USED → r1 = 5;
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[11].tryCatchFinallyImplicitThrowTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 32, string_id: 10975>  # String: 'loopBreakCrossesTryBoundaryTest' (Identifier)
        // USED → r5 = getEnvironment(2)[11].loopBreakCrossesTryBoundaryTest;
        // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 5, UInt16: 3, UInt16: 23586>  # Array: [1, 0, 2]
        r1 = [1, 0, 2]
        // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 8, UInt8: 3>
        // USED → r1 = r1[3] = -1;
        // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 4>
        // USED → r1 = (r1[3] = -1)[4] = 3;
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[11].loopBreakCrossesTryBoundaryTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        // USED → r1 = getEnvironment(2)[11];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 33, string_id: 8763>  # String: 'switchInsideTryTest' (Identifier)
        // USED → r5 = getEnvironment(2)[11].switchInsideTryTest;
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
        // USED → r1 = 1;
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[11].switchInsideTryTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
        // USED → r1 = getEnvironment(2)[12];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 34, string_id: 11254>  # String: 'forOfTest' (Identifier)
        // USED → r1 = getEnvironment(2)[12].forOfTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[12].forOfTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
        // USED → r1 = getEnvironment(2)[12];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 35, string_id: 11239>  # String: 'forInTest' (Identifier)
        // USED → r1 = getEnvironment(2)[12].forInTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[12].forInTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 13>
        // USED → r1 = getEnvironment(2)[13];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 36, string_id: 11286>  # String: 'objectLiteralTest' (Identifier)
        // USED → r1 = getEnvironment(2)[13].objectLiteralTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[13].objectLiteralTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        // USED → r1 = getEnvironment(2)[14];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 37, string_id: 11307>  # String: 'propertyAccessTest' (Identifier)
        // USED → r1 = getEnvironment(2)[14].propertyAccessTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[14].propertyAccessTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        // USED → r1 = getEnvironment(2)[14];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 38, string_id: 11290>  # String: 'computedPropertyTest' (Identifier)
        // USED → r1 = getEnvironment(2)[14].computedPropertyTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[14].computedPropertyTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        // USED → r1 = getEnvironment(2)[14];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 39, string_id: 11295>  # String: 'optionalChainingTest' (Identifier)
        // USED → r1 = getEnvironment(2)[14].optionalChainingTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[14].optionalChainingTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 15>
        // USED → r1 = getEnvironment(2)[15];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 40, string_id: 10657>  # String: 'callDestructuringTests' (Identifier)
        // USED → r1 = getEnvironment(2)[15].callDestructuringTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[15].callDestructuringTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 16>
        // USED → r1 = getEnvironment(2)[16];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 41, string_id: 7969>  # String: 'arrayTest' (Identifier)
        // USED → r1 = getEnvironment(2)[16].arrayTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[16].arrayTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        // USED → r1 = getEnvironment(2)[17];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 42, string_id: 10787>  # String: 'spreadArrayTest' (Identifier)
        // USED → r1 = getEnvironment(2)[17].spreadArrayTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[17].spreadArrayTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        // USED → r1 = getEnvironment(2)[17];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 43, string_id: 10795>  # String: 'spreadObjectTest' (Identifier)
        // USED → r1 = getEnvironment(2)[17].spreadObjectTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[17].spreadObjectTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        // USED → r1 = getEnvironment(2)[17];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 44, string_id: 10792>  # String: 'spreadFunctionArgsTest' (Identifier)
        // USED → r1 = getEnvironment(2)[17].spreadFunctionArgsTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[17].spreadFunctionArgsTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 18>
        // USED → r1 = getEnvironment(2)[18];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 45, string_id: 7228>  # String: 'callMapSetTests' (Identifier)
        // USED → r1 = getEnvironment(2)[18].callMapSetTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[18].callMapSetTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        // USED → r1 = getEnvironment(2)[19];
        // CODE → <GetById>: <Reg8: 7, Reg8: 1, UInt8: 46, string_id: 11328>  # String: 'basicTemplateTest' (Identifier)
        // USED → r7 = getEnvironment(2)[19].basicTemplateTest;
        // CODE → <LoadConstString>: <Reg8: 5, string_id: 2445>  # String: 'Ada' (String)
        // USED → r5 = "Ada";
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 30>
        // USED → r1 = 30;
        // CODE → <Call3>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 5, Reg8: 1>
        r1 = getEnvironment(2)[19].basicTemplateTest.call(undefined, "Ada", r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        // USED → r1 = getEnvironment(2)[19];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 47, string_id: 11332>  # String: 'nestedTemplateTest' (Identifier)
        // USED → r5 = getEnvironment(2)[19].nestedTemplateTest;
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 9>
        // USED → r1 = 9;
        // CODE → <Call3>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 6, Reg8: 1>
        r1 = getEnvironment(2)[19].nestedTemplateTest.call(undefined, r6, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        // USED → r1 = getEnvironment(2)[19];
        // CODE → <GetById>: <Reg8: 5, Reg8: 1, UInt8: 48, string_id: 11337>  # String: 'taggedTemplateTest' (Identifier)
        // USED → r5 = getEnvironment(2)[19].taggedTemplateTest;
        // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 6>
        // USED → r1 = 6;
        // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = getEnvironment(2)[19].taggedTemplateTest.call(undefined, r1)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 20>
        // USED → r1 = getEnvironment(2)[20];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 49, string_id: 11311>  # String: 'callRegExpTests' (Identifier)
        // USED → r1 = getEnvironment(2)[20].callRegExpTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[20].callRegExpTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 21>
        // USED → r1 = getEnvironment(2)[21];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 50, string_id: 11139>  # String: 'arrowFunctionTest' (Identifier)
        // USED → r1 = getEnvironment(2)[21].arrowFunctionTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[21].arrowFunctionTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
        // USED → r1 = getEnvironment(2)[22];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 51, string_id: 10113>  # String: 'closureTest' (Identifier)
        // USED → r1 = getEnvironment(2)[22].closureTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[22].closureTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
        // USED → r1 = getEnvironment(2)[22];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 52, string_id: 11176>  # String: 'closureLoopTest' (Identifier)
        // USED → r1 = getEnvironment(2)[22].closureLoopTest;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[22].closureLoopTest.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 23>
        // USED → r1 = getEnvironment(2)[23];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 53, string_id: 11182>  # String: 'callDefaultParameterTests' (Identifier)
        // USED → r1 = getEnvironment(2)[23].callDefaultParameterTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[23].callDefaultParameterTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 24>
        // USED → r1 = getEnvironment(2)[24];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 54, string_id: 11222>  # String: 'callRestParameterTests' (Identifier)
        // USED → r1 = getEnvironment(2)[24].callRestParameterTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[24].callRestParameterTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 25>
        // USED → r1 = getEnvironment(2)[25];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 55, string_id: 11199>  # String: 'callGeneratorTests' (Identifier)
        // USED → r1 = getEnvironment(2)[25].callGeneratorTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = getEnvironment(2)[25].callGeneratorTests.call(undefined)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 26>
        // USED → r1 = getEnvironment(2)[26];
        // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 56, string_id: 9338>  # String: 'callAsyncTests' (Identifier)
        // USED → r1 = getEnvironment(2)[26].callAsyncTests;
        // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        // USED → r1 = await getEnvironment(2)[26].callAsyncTests.call(undefined);
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 000003ad
        goto label_941;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return await getEnvironment(2)[26].callAsyncTests.call(undefined);
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 5>
        // USED → r1 = await yield;
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 5>
        // USED → r5 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 1>
            return await yield;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 4, UInt8: 27>
            // USED → r5 = getEnvironment(2)[27];
            // CODE → <GetById>: <Reg8: 5, Reg8: 5, UInt8: 57, string_id: 10812>  # String: 'classTest' (Identifier)
            // USED → r5 = getEnvironment(2)[27].classTest;
            // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 2>
            r5 = getEnvironment(2)[27].classTest.call(undefined)
            // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 28>
            // USED → r4 = getEnvironment(2)[28];
            // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 58, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
            // USED → r4 = getEnvironment(2)[28].privateStaticTest;
            // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 2>
            r4 = getEnvironment(2)[28].privateStaticTest.call(undefined)
            // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = globalThis.console.log;
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 4865>  # String: '__BC:index/runAllTests/end' (String)
            // USED → r3 = "__BC:index/runAllTests/end";
            // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            console.log("__BC:index/runAllTests/end")
            // CODE → <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → <Ret>: <Reg8: 2>
            return undefined;
        }
    }
}