function function_15163(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateGeneratorClosure>: <Reg8: 4, Reg8: 0, function_id: 15164>  # Function: [#15164 simpleGeneratorTest of 9 bytes]: 1 params @ offset 0x0026aee0
    // USED → r4 = simpleGeneratorTest;
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    r0[0] = simpleGeneratorTest
    // CODE → addr: 14 | <CreateGeneratorClosure>: <Reg8: 3, Reg8: 0, function_id: 15166>  # Function: [#15166 generatorWithLoopTest of 9 bytes]: 2 params @ offset 0x0026af52
    // USED → r3 = generatorWithLoopTest;
    // CODE → addr: 19 | <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 3>
    r0[1] = generatorWithLoopTest
    // CODE → addr: 23 | <CreateGeneratorClosure>: <Reg8: 2, Reg8: 0, function_id: 15168>  # Function: [#15168 generatorTryFinallyTest of 9 bytes]: 1 params @ offset 0x0026afd6
    // USED → r2 = generatorTryFinallyTest;
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 0, UInt8: 2, Reg8: 2>
    r0[2] = generatorTryFinallyTest
    // CODE → addr: 32 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr: 34 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr: 40 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr: 45 | <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → addr: 47 | <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → addr: 49 | <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r5 = "__esModule";
    // CODE → addr: 57 | <Call4>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 5, Reg8: 6>
    r5 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → addr: 64 | <PutById>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 8828>  # String: 'simpleGeneratorTest' (Identifier)
    param6.simpleGeneratorTest = simpleGeneratorTest
    // CODE → addr: 70 | <PutById>: <Reg8: 1, Reg8: 3, UInt8: 2, string_id: 8827>  # String: 'generatorWithLoopTest' (Identifier)
    param6.generatorWithLoopTest = generatorWithLoopTest
    // CODE → addr: 76 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 8821>  # String: 'generatorTryFinallyTest' (Identifier)
    param6.generatorTryFinallyTest = generatorTryFinallyTest
    // CODE → addr: 82 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15170>  # Function: [#15170 callGeneratorTests of 212 bytes]: 1 params @ offset 0x0026b07d
    // USED → r0 = callGeneratorTests();
    // CODE → addr: 87 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11199>  # String: 'callGeneratorTests' (Identifier)
    param6.callGeneratorTests = callGeneratorTests()
    // CODE → addr: 93 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 95 | <Ret>: <Reg8: 0>
    return undefined;
}