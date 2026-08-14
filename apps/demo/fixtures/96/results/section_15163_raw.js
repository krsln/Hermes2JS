function function_15163(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateGeneratorClosure>: <Reg8: 4, Reg8: 0, function_id: 15164>  # Function: [#15164 simpleGeneratorTest of 9 bytes]: 1 params @ offset 0x0026aee0
    // USED → r4 = simpleGeneratorTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = simpleGeneratorTest
    // CODE → <CreateGeneratorClosure>: <Reg8: 3, Reg8: 0, function_id: 15166>  # Function: [#15166 generatorWithLoopTest of 9 bytes]: 2 params @ offset 0x0026af52
    // USED → r3 = generatorWithLoopTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 3>
    createEnvironment()[1] = generatorWithLoopTest
    // CODE → <CreateGeneratorClosure>: <Reg8: 2, Reg8: 0, function_id: 15168>  # Function: [#15168 generatorTryFinallyTest of 9 bytes]: 1 params @ offset 0x0026afd6
    // USED → r2 = generatorTryFinallyTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 2, Reg8: 2>
    createEnvironment()[2] = generatorTryFinallyTest
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r5 = "__esModule";
    // CODE → <Call4>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 5, Reg8: 6>
    r5 = globalThis.Object.defineProperty(r1, "__esModule", r6)
    // CODE → <PutById>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 8828>  # String: 'simpleGeneratorTest' (Identifier)
    param6.simpleGeneratorTest = simpleGeneratorTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 3, UInt8: 2, string_id: 8827>  # String: 'generatorWithLoopTest' (Identifier)
    param6.generatorWithLoopTest = generatorWithLoopTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 8821>  # String: 'generatorTryFinallyTest' (Identifier)
    param6.generatorTryFinallyTest = generatorTryFinallyTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15170>  # Function: [#15170 callGeneratorTests of 212 bytes]: 1 params @ offset 0x0026b07d
    // USED → r0 = callGeneratorTests(param0);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11199>  # String: 'callGeneratorTests' (Identifier)
    param6.callGeneratorTests = callGeneratorTests(param0)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}