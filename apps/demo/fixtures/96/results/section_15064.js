function function_15064(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  7 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = Object;
    // CODE → addr: 13 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = Object.defineProperty;
    // CODE → addr: 18 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr: 20 | <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → addr: 22 | <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → addr: 26 | <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → addr: 30 | <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = Object.defineProperty(param6, "__esModule", r3)
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15065>  # Function: [#15065 labeledBreakTest of 123 bytes]: 1 params @ offset 0x00268359
    // USED → r2 = labeledBreakTest();
    // CODE → addr: 42 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 10933>  # String: 'labeledBreakTest' (Identifier)
    param6.labeledBreakTest = labeledBreakTest()
    // CODE → addr: 48 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15066>  # Function: [#15066 labeledContinueTest of 139 bytes]: 1 params @ offset 0x002683d4
    // USED → r2 = labeledContinueTest();
    // CODE → addr: 53 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 10940>  # String: 'labeledContinueTest' (Identifier)
    param6.labeledContinueTest = labeledContinueTest()
    // CODE → addr: 59 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15067>  # Function: [#15067 labeledBlockBreakTest of 109 bytes]: 1 params @ offset 0x0026845f
    // USED → r2 = labeledBlockBreakTest();
    // CODE → addr: 64 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 8658>  # String: 'labeledBlockBreakTest' (Identifier)
    param6.labeledBlockBreakTest = labeledBlockBreakTest()
    // CODE → addr: 70 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15068>  # Function: [#15068 tripleNestedLabeledTest of 144 bytes]: 1 params @ offset 0x002684cc
    // USED → r0 = tripleNestedLabeledTest();
    // CODE → addr: 75 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 10646>  # String: 'tripleNestedLabeledTest' (Identifier)
    param6.tripleNestedLabeledTest = tripleNestedLabeledTest()
    // CODE → addr: 81 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 83 | <Ret>: <Reg8: 0>
    return undefined;
}