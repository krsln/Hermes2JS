async function* anon_15045() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <StartGenerator>: <>
    // StartGenerator
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → addr:  1 | <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r1 = __resumeIsReturn;
    if (__resumeIsReturn) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → addr:1001 | <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → addr:1002 | <Ret>: <Reg8: 0>
        return r0;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 3>
        // USED → r3 = globalThis;
        // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r4 = console;
        // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r2 = console.log;
        // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4866>  # String: '__BC:index/runAllTests/start' (String)
        // USED → r1 = "__BC:index/runAllTests/start";
        // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
        console.log("__BC:index/runAllTests/start")
        // CODE → addr: 32 | <GetEnvironment>: <Reg8: 4, UInt8: 2>
        r4 = getEnvironment(2)
        // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 1>
        r1 = r4[1]
        // CODE → addr: 39 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 10971>  # String: 'whileTest' (Identifier)
        // USED → r1 = r1.whileTest;
        // CODE → addr: 45 | <LoadConstUndefined>: <Reg8: 2>
        // USED → r2 = undefined;
        // CODE → addr: 47 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.whileTest.call(r2)
        // CODE → addr: 51 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 2>
        r1 = r4[2]
        // CODE → addr: 55 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 4, string_id: 10882>  # String: 'doWhileTest' (Identifier)
        // USED → r1 = r1.doWhileTest;
        // CODE → addr: 61 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.doWhileTest.call(r2)
        // CODE → addr: 65 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
        r1 = r4[3]
        // CODE → addr: 69 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 10341>  # String: 'forTest' (Identifier)
        // USED → r1 = r1.forTest;
        // CODE → addr: 75 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.forTest.call(r2)
        // CODE → addr: 79 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 4>
        r1 = r4[4]
        // CODE → addr: 83 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 6, string_id: 10885>  # String: 'forEachTest' (Identifier)
        // USED → r1 = r1.forEachTest;
        // CODE → addr: 89 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.forEachTest.call(r2)
        // CODE → addr: 93 | <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
        // USED → r7 = console;
        // CODE → addr: 99 | <GetByIdShort>: <Reg8: 5, Reg8: 7, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
        // USED → r5 = console.log;
        // CODE → addr:104 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 5>
        r1 = r4[5]
        // CODE → addr:108 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 8729>  # String: 'switchTest' (Identifier)
        // USED → r1 = r1.switchTest;
        // CODE → addr:114 | <LoadConstUInt8>: <Reg8: 6, UInt8: 4>
        // USED → r6 = 4;
        // CODE → addr:117 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 6>
        r1 = r1.switchTest.call(r2, 4)
        // CODE → addr:122 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 7, Reg8: 1>
        console.log(r1)
        // CODE → addr:127 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 6>
        r1 = r4[6]
        // CODE → addr:131 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 8, string_id: 10944>  # String: 'nestedLoopTest' (Identifier)
        // USED → r1 = r1.nestedLoopTest;
        // CODE → addr:137 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.nestedLoopTest.call(r2)
        // CODE → addr:141 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 7>
        r1 = r4[7]
        // CODE → addr:145 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 9, string_id: 7792>  # String: 'complexTest' (Identifier)
        // USED → r1 = r1.complexTest;
        // CODE → addr:151 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.complexTest.call(r2)
        // CODE → addr:155 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
        r1 = r4[8]
        // CODE → addr:159 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 10, string_id: 8596>  # String: 'ifTest' (Identifier)
        // USED → r5 = r1.ifTest;
        // CODE → addr:165 | <LoadConstUInt8>: <Reg8: 1, UInt8: 7>
        // USED → r1 = 7;
        // CODE → addr:168 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = r1.ifTest.call(r2, 7)
        // CODE → addr:173 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 8>
        r1 = r4[8]
        // CODE → addr:177 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 11, string_id: 10899>  # String: 'ifElseChainTest' (Identifier)
        // USED → r1 = r1.ifElseChainTest;
        // CODE → addr:183 | <LoadConstTrue>: <Reg8: 5>
        r5 = true
        // CODE → addr:185 | <LoadConstFalse>: <Reg8: 7>
        r7 = false
        // CODE → addr:187 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
        r1 = r1.ifElseChainTest.call(r2, r5, r7)
        // CODE → addr:193 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        r1 = r4[9]
        // CODE → addr:197 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 12, string_id: 10933>  # String: 'labeledBreakTest' (Identifier)
        // USED → r1 = r1.labeledBreakTest;
        // CODE → addr:203 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.labeledBreakTest.call(r2)
        // CODE → addr:207 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        r1 = r4[9]
        // CODE → addr:211 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 13, string_id: 10940>  # String: 'labeledContinueTest' (Identifier)
        // USED → r1 = r1.labeledContinueTest;
        // CODE → addr:217 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.labeledContinueTest.call(r2)
        // CODE → addr:221 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        r1 = r4[9]
        // CODE → addr:225 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 14, string_id: 8658>  # String: 'labeledBlockBreakTest' (Identifier)
        // USED → r1 = r1.labeledBlockBreakTest;
        // CODE → addr:231 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.labeledBlockBreakTest.call(r2)
        // CODE → addr:235 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 9>
        r1 = r4[9]
        // CODE → addr:239 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 15, string_id: 10646>  # String: 'tripleNestedLabeledTest' (Identifier)
        // USED → r1 = r1.tripleNestedLabeledTest;
        // CODE → addr:245 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tripleNestedLabeledTest.call(r2)
        // CODE → addr:249 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        r1 = r4[10]
        // CODE → addr:253 | <GetById>: <Reg8: 8, Reg8: 1, UInt8: 16, string_id: 9849>  # String: 'ternaryTest' (Identifier)
        // USED → r8 = r1.ternaryTest;
        // CODE → addr:259 | <LoadConstInt>: <Reg8: 1, Imm32: -3>
        r1 = -3
        // CODE → addr:265 | <Call2>: <Reg8: 1, Reg8: 8, Reg8: 2, Reg8: 1>
        r1 = r1.ternaryTest.call(r2, r1)
        // CODE → addr:270 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        r1 = r4[10]
        // CODE → addr:274 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 17, string_id: 10963>  # String: 'shortCircuitAssignTest' (Identifier)
        // USED → r1 = r1.shortCircuitAssignTest;
        // CODE → addr:280 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.shortCircuitAssignTest.call(r2)
        // CODE → addr:284 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 10>
        r1 = r4[10]
        // CODE → addr:288 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 18, string_id: 10952>  # String: 'logicalShortCircuitTest' (Identifier)
        // USED → r1 = r1.logicalShortCircuitTest;
        // CODE → addr:294 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 7>
        r1 = r1.logicalShortCircuitTest.call(r2, r5, r7)
        // CODE → addr:300 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:304 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 19, string_id: 11096>  # String: 'tryCatchTest' (Identifier)
        // USED → r1 = r1.tryCatchTest;
        // CODE → addr:310 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryCatchTest.call(r2)
        // CODE → addr:314 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:318 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 20, string_id: 11065>  # String: 'tryCatchNoFinallyTest' (Identifier)
        // USED → r1 = r1.tryCatchNoFinallyTest;
        // CODE → addr:324 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryCatchNoFinallyTest.call(r2)
        // CODE → addr:328 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:332 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 21, string_id: 11122>  # String: 'tryFinallyNoCatchTest' (Identifier)
        // USED → r1 = r1.tryFinallyNoCatchTest;
        // CODE → addr:338 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryFinallyNoCatchTest.call(r2)
        // CODE → addr:342 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:346 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 22, string_id: 11126>  # String: 'tryFinallyNormalCompletionTest' (Identifier)
        // USED → r1 = r1.tryFinallyNormalCompletionTest;
        // CODE → addr:352 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryFinallyNormalCompletionTest.call(r2)
        // CODE → addr:356 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:360 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 23, string_id: 11088>  # String: 'tryCatchRethrowDifferentTest' (Identifier)
        // USED → r1 = r1.tryCatchRethrowDifferentTest;
        // CODE → addr:366 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryCatchRethrowDifferentTest.call(r2)
        // CODE → addr:370 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:374 | <GetById>: <Reg8: 7, Reg8: 1, UInt8: 24, string_id: 10295>  # String: 'tryLoopMultiReturnTest' (Identifier)
        // USED → r7 = r1.tryLoopMultiReturnTest;
        // CODE → addr:380 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 4, UInt16: 2, UInt16: 23560>  # Array: [1, 0]
        r1 = [1, 0]
        // CODE → addr:388 | <LoadConstInt>: <Reg8: 8, Imm32: -1>
        // USED → r8 = -1;
        // CODE → addr:394 | <PutOwnByIndex>: <Reg8: 1, Reg8: 8, UInt8: 2>
        // USED → r1 = r1[2] = -1;
        // CODE → addr:398 | <LoadConstUInt8>: <Reg8: 9, UInt8: 2>
        // USED → r9 = 2;
        // CODE → addr:401 | <PutOwnByIndex>: <Reg8: 1, Reg8: 9, UInt8: 3>
        r1 = (r1[2] = -1)[3] = 2
        // CODE → addr:405 | <Call2>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 1>
        r1 = r1.tryLoopMultiReturnTest.call(r2, r1)
        // CODE → addr:410 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:414 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 11002>  # String: 'nestedTryCatchTest' (Identifier)
        // USED → r1 = r1.nestedTryCatchTest;
        // CODE → addr:420 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.nestedTryCatchTest.call(r2)
        // CODE → addr:424 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:428 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 26, string_id: 10992>  # String: 'nestedTryCatchFinallyTest' (Identifier)
        // USED → r1 = r1.nestedTryCatchFinallyTest;
        // CODE → addr:434 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.nestedTryCatchFinallyTest.call(r2)
        // CODE → addr:438 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:442 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 27, string_id: 11030>  # String: 'tryCatchFinallyEarlyReturnTest' (Identifier)
        // USED → r1 = r1.tryCatchFinallyEarlyReturnTest;
        // CODE → addr:448 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.tryCatchFinallyEarlyReturnTest.call(r2)
        // CODE → addr:452 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:456 | <GetById>: <Reg8: 7, Reg8: 1, UInt8: 28, string_id: 11112>  # String: 'tryFinallyLoopBreakTest' (Identifier)
        // USED → r7 = r1.tryFinallyLoopBreakTest;
        // CODE → addr:462 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 4, UInt16: 4, UInt16: 23569>  # Array: [1, 2, 0, 3]
        r1 = [1, 2, 0, 3]
        // CODE → addr:470 | <Call2>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 1>
        r1 = r1.tryFinallyLoopBreakTest.call(r2, r1)
        // CODE → addr:475 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:479 | <GetById>: <Reg8: 9, Reg8: 1, UInt8: 29, string_id: 8691>  # String: 'tryCatchInsideLoopTest' (Identifier)
        // USED → r9 = r1.tryCatchInsideLoopTest;
        // CODE → addr:485 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 3, UInt16: 1, UInt16: 3>  # Array: [1]
        r1 = [1]
        // CODE → addr:493 | <LoadConstInt>: <Reg8: 7, Imm32: -2>
        // USED → r7 = -2;
        // CODE → addr:499 | <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 1>
        // USED → r1 = r1[1] = -2;
        // CODE → addr:503 | <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
        // USED → r7 = 3;
        // CODE → addr:506 | <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 2>
        r1 = (r1[1] = -2)[2] = 3
        // CODE → addr:510 | <Call2>: <Reg8: 1, Reg8: 9, Reg8: 2, Reg8: 1>
        r1 = r1.tryCatchInsideLoopTest.call(r2, r1)
        // CODE → addr:515 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:519 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 30, string_id: 8711>  # String: 'tryCatchFinallyBranchInFinallyTest' (Identifier)
        // USED → r1 = r1.tryCatchFinallyBranchInFinallyTest;
        // CODE → addr:525 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 5>
        r1 = r1.tryCatchFinallyBranchInFinallyTest.call(r2, r5)
        // CODE → addr:530 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:534 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 31, string_id: 11038>  # String: 'tryCatchFinallyImplicitThrowTest' (Identifier)
        // USED → r5 = r1.tryCatchFinallyImplicitThrowTest;
        // CODE → addr:540 | <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
        // USED → r1 = 5;
        // CODE → addr:543 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = r1.tryCatchFinallyImplicitThrowTest.call(r2, 5)
        // CODE → addr:548 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:552 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 32, string_id: 10975>  # String: 'loopBreakCrossesTryBoundaryTest' (Identifier)
        // USED → r5 = r1.loopBreakCrossesTryBoundaryTest;
        // CODE → addr:558 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 5, UInt16: 3, UInt16: 23586>  # Array: [1, 0, 2]
        r1 = [1, 0, 2]
        // CODE → addr:566 | <PutOwnByIndex>: <Reg8: 1, Reg8: 8, UInt8: 3>
        // USED → r1 = r1[3] = -1;
        // CODE → addr:570 | <PutOwnByIndex>: <Reg8: 1, Reg8: 7, UInt8: 4>
        r1 = (r1[3] = -1)[4] = 3
        // CODE → addr:574 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = r1.loopBreakCrossesTryBoundaryTest.call(r2, r1)
        // CODE → addr:579 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 11>
        r1 = r4[11]
        // CODE → addr:583 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 33, string_id: 8763>  # String: 'switchInsideTryTest' (Identifier)
        // USED → r5 = r1.switchInsideTryTest;
        // CODE → addr:589 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
        // USED → r1 = 1;
        // CODE → addr:592 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = r1.switchInsideTryTest.call(r2, 1)
        // CODE → addr:597 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
        r1 = r4[12]
        // CODE → addr:601 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 34, string_id: 11254>  # String: 'forOfTest' (Identifier)
        // USED → r1 = r1.forOfTest;
        // CODE → addr:607 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.forOfTest.call(r2)
        // CODE → addr:611 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 12>
        r1 = r4[12]
        // CODE → addr:615 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 35, string_id: 11239>  # String: 'forInTest' (Identifier)
        // USED → r1 = r1.forInTest;
        // CODE → addr:621 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.forInTest.call(r2)
        // CODE → addr:625 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 13>
        r1 = r4[13]
        // CODE → addr:629 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 36, string_id: 11286>  # String: 'objectLiteralTest' (Identifier)
        // USED → r1 = r1.objectLiteralTest;
        // CODE → addr:635 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.objectLiteralTest.call(r2)
        // CODE → addr:639 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        r1 = r4[14]
        // CODE → addr:643 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 37, string_id: 11307>  # String: 'propertyAccessTest' (Identifier)
        // USED → r1 = r1.propertyAccessTest;
        // CODE → addr:649 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.propertyAccessTest.call(r2)
        // CODE → addr:653 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        r1 = r4[14]
        // CODE → addr:657 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 38, string_id: 11290>  # String: 'computedPropertyTest' (Identifier)
        // USED → r1 = r1.computedPropertyTest;
        // CODE → addr:663 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.computedPropertyTest.call(r2)
        // CODE → addr:667 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 14>
        r1 = r4[14]
        // CODE → addr:671 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 39, string_id: 11295>  # String: 'optionalChainingTest' (Identifier)
        // USED → r1 = r1.optionalChainingTest;
        // CODE → addr:677 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.optionalChainingTest.call(r2)
        // CODE → addr:681 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 15>
        r1 = r4[15]
        // CODE → addr:685 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 40, string_id: 10657>  # String: 'callDestructuringTests' (Identifier)
        // USED → r1 = r1.callDestructuringTests;
        // CODE → addr:691 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callDestructuringTests.call(r2)
        // CODE → addr:695 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 16>
        r1 = r4[16]
        // CODE → addr:699 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 41, string_id: 7969>  # String: 'arrayTest' (Identifier)
        // USED → r1 = r1.arrayTest;
        // CODE → addr:705 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.arrayTest.call(r2)
        // CODE → addr:709 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        r1 = r4[17]
        // CODE → addr:713 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 42, string_id: 10787>  # String: 'spreadArrayTest' (Identifier)
        // USED → r1 = r1.spreadArrayTest;
        // CODE → addr:719 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.spreadArrayTest.call(r2)
        // CODE → addr:723 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        r1 = r4[17]
        // CODE → addr:727 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 43, string_id: 10795>  # String: 'spreadObjectTest' (Identifier)
        // USED → r1 = r1.spreadObjectTest;
        // CODE → addr:733 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.spreadObjectTest.call(r2)
        // CODE → addr:737 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 17>
        r1 = r4[17]
        // CODE → addr:741 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 44, string_id: 10792>  # String: 'spreadFunctionArgsTest' (Identifier)
        // USED → r1 = r1.spreadFunctionArgsTest;
        // CODE → addr:747 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.spreadFunctionArgsTest.call(r2)
        // CODE → addr:751 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 18>
        r1 = r4[18]
        // CODE → addr:755 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 45, string_id: 7228>  # String: 'callMapSetTests' (Identifier)
        // USED → r1 = r1.callMapSetTests;
        // CODE → addr:761 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callMapSetTests.call(r2)
        // CODE → addr:765 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        r1 = r4[19]
        // CODE → addr:769 | <GetById>: <Reg8: 7, Reg8: 1, UInt8: 46, string_id: 11328>  # String: 'basicTemplateTest' (Identifier)
        // USED → r7 = r1.basicTemplateTest;
        // CODE → addr:775 | <LoadConstString>: <Reg8: 5, string_id: 2445>  # String: 'Ada' (String)
        // USED → r5 = "Ada";
        // CODE → addr:779 | <LoadConstUInt8>: <Reg8: 1, UInt8: 30>
        // USED → r1 = 30;
        // CODE → addr:782 | <Call3>: <Reg8: 1, Reg8: 7, Reg8: 2, Reg8: 5, Reg8: 1>
        r1 = r1.basicTemplateTest.call(r2, "Ada", 30)
        // CODE → addr:788 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        r1 = r4[19]
        // CODE → addr:792 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 47, string_id: 11332>  # String: 'nestedTemplateTest' (Identifier)
        // USED → r5 = r1.nestedTemplateTest;
        // CODE → addr:798 | <LoadConstUInt8>: <Reg8: 1, UInt8: 9>
        // USED → r1 = 9;
        // CODE → addr:801 | <Call3>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 6, Reg8: 1>
        r1 = r1.nestedTemplateTest.call(r2, 4, 9)
        // CODE → addr:807 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 19>
        r1 = r4[19]
        // CODE → addr:811 | <GetById>: <Reg8: 5, Reg8: 1, UInt8: 48, string_id: 11337>  # String: 'taggedTemplateTest' (Identifier)
        // USED → r5 = r1.taggedTemplateTest;
        // CODE → addr:817 | <LoadConstUInt8>: <Reg8: 1, UInt8: 6>
        // USED → r1 = 6;
        // CODE → addr:820 | <Call2>: <Reg8: 1, Reg8: 5, Reg8: 2, Reg8: 1>
        r1 = r1.taggedTemplateTest.call(r2, 6)
        // CODE → addr:825 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 20>
        r1 = r4[20]
        // CODE → addr:829 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 49, string_id: 11311>  # String: 'callRegExpTests' (Identifier)
        // USED → r1 = r1.callRegExpTests;
        // CODE → addr:835 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callRegExpTests.call(r2)
        // CODE → addr:839 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 21>
        r1 = r4[21]
        // CODE → addr:843 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 50, string_id: 11139>  # String: 'arrowFunctionTest' (Identifier)
        // USED → r1 = r1.arrowFunctionTest;
        // CODE → addr:849 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.arrowFunctionTest.call(r2)
        // CODE → addr:853 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
        r1 = r4[22]
        // CODE → addr:857 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 51, string_id: 10113>  # String: 'closureTest' (Identifier)
        // USED → r1 = r1.closureTest;
        // CODE → addr:863 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.closureTest.call(r2)
        // CODE → addr:867 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 22>
        r1 = r4[22]
        // CODE → addr:871 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 52, string_id: 11176>  # String: 'closureLoopTest' (Identifier)
        // USED → r1 = r1.closureLoopTest;
        // CODE → addr:877 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.closureLoopTest.call(r2)
        // CODE → addr:881 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 23>
        r1 = r4[23]
        // CODE → addr:885 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 53, string_id: 11182>  # String: 'callDefaultParameterTests' (Identifier)
        // USED → r1 = r1.callDefaultParameterTests;
        // CODE → addr:891 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callDefaultParameterTests.call(r2)
        // CODE → addr:895 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 24>
        r1 = r4[24]
        // CODE → addr:899 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 54, string_id: 11222>  # String: 'callRestParameterTests' (Identifier)
        // USED → r1 = r1.callRestParameterTests;
        // CODE → addr:905 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callRestParameterTests.call(r2)
        // CODE → addr:909 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 25>
        r1 = r4[25]
        // CODE → addr:913 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 55, string_id: 11199>  # String: 'callGeneratorTests' (Identifier)
        // USED → r1 = r1.callGeneratorTests;
        // CODE → addr:919 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r1.callGeneratorTests.call(r2)
        // CODE → addr:923 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 26>
        r1 = r4[26]
        // CODE → addr:927 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 56, string_id: 9338>  # String: 'callAsyncTests' (Identifier)
        // USED → r1 = r1.callAsyncTests;
        // CODE → addr:933 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = await r1.callAsyncTests.call(r2)
        // CODE → addr:937 | <SaveGenerator>: <Addr8: 4>  # Address: 000003ad
        goto label_941;
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:939 | <Ret>: <Reg8: 1>
        return r1;
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr:941 | <ResumeGenerator>: <Reg8: 1, Reg8: 5>
        r1 = await yield
        // CODE → addr:941 | <ResumeGenerator>: <Reg8: 1, Reg8: 5>
        // USED → r5 = __resumeIsReturn;
        if (__resumeIsReturn) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → addr:998 | <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → addr:999 | <Ret>: <Reg8: 1>
            return r1;
        } else {
            // ──────────────── Block 4 ──────────────── 
            // CODE → addr:947 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 4, UInt8: 27>
            r5 = r4[27]
            // CODE → addr:951 | <GetById>: <Reg8: 5, Reg8: 5, UInt8: 57, string_id: 10812>  # String: 'classTest' (Identifier)
            // USED → r5 = r5.classTest;
            // CODE → addr:957 | <Call1>: <Reg8: 5, Reg8: 5, Reg8: 2>
            r5 = r5.classTest.call(r2)
            // CODE → addr:961 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 28>
            r4 = r4[28]
            // CODE → addr:965 | <GetById>: <Reg8: 4, Reg8: 4, UInt8: 58, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
            // USED → r4 = r4.privateStaticTest;
            // CODE → addr:971 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 2>
            r4 = r4.privateStaticTest.call(r2)
            // CODE → addr:975 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
            // USED → r5 = console;
            // CODE → addr:981 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
            // USED → r4 = console.log;
            // CODE → addr:986 | <LoadConstString>: <Reg8: 3, string_id: 4865>  # String: '__BC:index/runAllTests/end' (String)
            // USED → r3 = "__BC:index/runAllTests/end";
            // CODE → addr:990 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
            console.log("__BC:index/runAllTests/end")
            // CODE → addr:995 | <CompleteGenerator>: <>
            // CompleteGenerator
            // CODE → addr:996 | <Ret>: <Reg8: 2>
            return undefined;
        }
    }
}