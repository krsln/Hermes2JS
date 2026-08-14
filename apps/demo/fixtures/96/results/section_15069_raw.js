function function_15069(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = globalThis.Object.defineProperty(r1, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15070>  # Function: [#15070 ternaryTest of 137 bytes]: 2 params @ offset 0x002685a6
    // USED → r2 = ternaryTest(param0, param1);
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 9849>  # String: 'ternaryTest' (Identifier)
    param6.ternaryTest = ternaryTest(param0, param1)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15071>  # Function: [#15071 shortCircuitAssignTest of 166 bytes]: 1 params @ offset 0x0026862f
    // USED → r2 = shortCircuitAssignTest(param0);
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 10963>  # String: 'shortCircuitAssignTest' (Identifier)
    param6.shortCircuitAssignTest = shortCircuitAssignTest(param0)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15072>  # Function: [#15072 logicalShortCircuitTest of 163 bytes]: 3 params @ offset 0x002686d5
    // USED → r0 = logicalShortCircuitTest(param0, param1, param2);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10952>  # String: 'logicalShortCircuitTest' (Identifier)
    param6.logicalShortCircuitTest = logicalShortCircuitTest(param0, param1, param2)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}