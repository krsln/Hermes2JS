function function_15064(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = Object.defineProperty(param6, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15065>  # Function: [#15065 labeledBreakTest of 123 bytes]: 1 params @ offset 0x00268359
    // USED → r2 = labeledBreakTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 10933>  # String: 'labeledBreakTest' (Identifier)
    param6.labeledBreakTest = labeledBreakTest()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15066>  # Function: [#15066 labeledContinueTest of 139 bytes]: 1 params @ offset 0x002683d4
    // USED → r2 = labeledContinueTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 10940>  # String: 'labeledContinueTest' (Identifier)
    param6.labeledContinueTest = labeledContinueTest()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15067>  # Function: [#15067 labeledBlockBreakTest of 109 bytes]: 1 params @ offset 0x0026845f
    // USED → r2 = labeledBlockBreakTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 8658>  # String: 'labeledBlockBreakTest' (Identifier)
    param6.labeledBlockBreakTest = labeledBlockBreakTest()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15068>  # Function: [#15068 tripleNestedLabeledTest of 144 bytes]: 1 params @ offset 0x002684cc
    // USED → r0 = tripleNestedLabeledTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 10646>  # String: 'tripleNestedLabeledTest' (Identifier)
    param6.tripleNestedLabeledTest = tripleNestedLabeledTest()
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}