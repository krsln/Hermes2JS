function function_15074(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15087>  # Function: [#15087 mayThrow of 52 bytes]: 2 params @ offset 0x0026902a
    // USED → r2 = mayThrow(param1);
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 2>
    r0[0] = mayThrow(param1)
    // CODE → addr: 14 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 16 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = Object;
    // CODE → addr: 22 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = Object.defineProperty;
    // CODE → addr: 27 | <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → addr: 29 | <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → addr: 31 | <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → addr: 35 | <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → addr: 39 | <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = Object.defineProperty(param6, "__esModule", r3)
    // CODE → addr: 46 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15075>  # Function: [#15075 tryCatchTest of 220 bytes]: 1 params @ offset 0x0026886e
    // USED → r2 = tryCatchTest();
    // CODE → addr: 51 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 11096>  # String: 'tryCatchTest' (Identifier)
    param6.tryCatchTest = tryCatchTest()
    // CODE → addr: 57 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15076>  # Function: [#15076 tryCatchNoFinallyTest of 136 bytes]: 1 params @ offset 0x0026894a
    // USED → r2 = tryCatchNoFinallyTest();
    // CODE → addr: 62 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11065>  # String: 'tryCatchNoFinallyTest' (Identifier)
    param6.tryCatchNoFinallyTest = tryCatchNoFinallyTest()
    // CODE → addr: 68 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15077>  # Function: [#15077 tryFinallyNoCatchTest of 98 bytes]: 1 params @ offset 0x002689d2
    // USED → r2 = tryFinallyNoCatchTest();
    // CODE → addr: 73 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 11122>  # String: 'tryFinallyNoCatchTest' (Identifier)
    param6.tryFinallyNoCatchTest = tryFinallyNoCatchTest()
    // CODE → addr: 79 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15078>  # Function: [#15078 tryFinallyNormalCompletionTest of 110 bytes]: 1 params @ offset 0x00268a34
    // USED → r2 = tryFinallyNormalCompletionTest();
    // CODE → addr: 84 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 11126>  # String: 'tryFinallyNormalCompletionTest' (Identifier)
    param6.tryFinallyNormalCompletionTest = tryFinallyNormalCompletionTest()
    // CODE → addr: 90 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15079>  # Function: [#15079 tryCatchRethrowDifferentTest of 156 bytes]: 1 params @ offset 0x00268aa2
    // USED → r2 = tryCatchRethrowDifferentTest();
    // CODE → addr: 95 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 11088>  # String: 'tryCatchRethrowDifferentTest' (Identifier)
    param6.tryCatchRethrowDifferentTest = tryCatchRethrowDifferentTest()
    // CODE → addr:101 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15080>  # Function: [#15080 tryLoopMultiReturnTest of 152 bytes]: 2 params @ offset 0x00268b3e
    // USED → r2 = tryLoopMultiReturnTest(param1);
    // CODE → addr:106 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 10295>  # String: 'tryLoopMultiReturnTest' (Identifier)
    param6.tryLoopMultiReturnTest = tryLoopMultiReturnTest(param1)
    // CODE → addr:112 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15081>  # Function: [#15081 nestedTryCatchTest of 214 bytes]: 1 params @ offset 0x00268bd6
    // USED → r2 = nestedTryCatchTest();
    // CODE → addr:117 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 7, string_id: 11002>  # String: 'nestedTryCatchTest' (Identifier)
    param6.nestedTryCatchTest = nestedTryCatchTest()
    // CODE → addr:123 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15082>  # Function: [#15082 nestedTryCatchFinallyTest of 252 bytes]: 1 params @ offset 0x00268cac
    // USED → r2 = nestedTryCatchFinallyTest();
    // CODE → addr:128 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 10992>  # String: 'nestedTryCatchFinallyTest' (Identifier)
    param6.nestedTryCatchFinallyTest = nestedTryCatchFinallyTest()
    // CODE → addr:134 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15083>  # Function: [#15083 tryCatchFinallyEarlyReturnTest of 108 bytes]: 1 params @ offset 0x00268da8
    // USED → r2 = tryCatchFinallyEarlyReturnTest();
    // CODE → addr:139 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 9, string_id: 11030>  # String: 'tryCatchFinallyEarlyReturnTest' (Identifier)
    param6.tryCatchFinallyEarlyReturnTest = tryCatchFinallyEarlyReturnTest()
    // CODE → addr:145 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15084>  # Function: [#15084 tryFinallyLoopBreakTest of 171 bytes]: 2 params @ offset 0x00268e14
    // USED → r2 = tryFinallyLoopBreakTest(param1);
    // CODE → addr:150 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 10, string_id: 11112>  # String: 'tryFinallyLoopBreakTest' (Identifier)
    param6.tryFinallyLoopBreakTest = tryFinallyLoopBreakTest(param1)
    // CODE → addr:156 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15085>  # Function: [#15085 tryCatchInsideLoopTest of 201 bytes]: 2 params @ offset 0x00268ebf
    // USED → r2 = tryCatchInsideLoopTest(param1);
    // CODE → addr:161 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 11, string_id: 8691>  # String: 'tryCatchInsideLoopTest' (Identifier)
    param6.tryCatchInsideLoopTest = tryCatchInsideLoopTest(param1)
    // CODE → addr:167 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15086>  # Function: [#15086 tryCatchFinallyBranchInFinallyTest of 162 bytes]: 2 params @ offset 0x00268f88
    // USED → r2 = tryCatchFinallyBranchInFinallyTest(param1);
    // CODE → addr:172 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 12, string_id: 8711>  # String: 'tryCatchFinallyBranchInFinallyTest' (Identifier)
    param6.tryCatchFinallyBranchInFinallyTest = tryCatchFinallyBranchInFinallyTest(param1)
    // CODE → addr:178 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15088>  # Function: [#15088 tryCatchFinallyImplicitThrowTest of 159 bytes]: 2 params @ offset 0x0026905e
    // USED → r2 = tryCatchFinallyImplicitThrowTest(param1);
    // CODE → addr:183 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 13, string_id: 11038>  # String: 'tryCatchFinallyImplicitThrowTest' (Identifier)
    param6.tryCatchFinallyImplicitThrowTest = tryCatchFinallyImplicitThrowTest(param1)
    // CODE → addr:189 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15089>  # Function: [#15089 loopBreakCrossesTryBoundaryTest of 266 bytes]: 2 params @ offset 0x002690fd
    // USED → r2 = loopBreakCrossesTryBoundaryTest(param1);
    // CODE → addr:194 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 14, string_id: 10975>  # String: 'loopBreakCrossesTryBoundaryTest' (Identifier)
    param6.loopBreakCrossesTryBoundaryTest = loopBreakCrossesTryBoundaryTest(param1)
    // CODE → addr:200 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15090>  # Function: [#15090 switchInsideTryTest of 207 bytes]: 2 params @ offset 0x00269207
    // USED → r0 = switchInsideTryTest(param1);
    // CODE → addr:205 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 15, string_id: 8763>  # String: 'switchInsideTryTest' (Identifier)
    param6.switchInsideTryTest = switchInsideTryTest(param1)
    // CODE → addr:211 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:213 | <Ret>: <Reg8: 0>
    return r0;
}