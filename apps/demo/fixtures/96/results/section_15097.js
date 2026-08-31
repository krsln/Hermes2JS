function function_15097(param1, param2, param3, param4, param5, param6, param7) {
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
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15098>  # Function: [#15098 propertyAccessTest of 199 bytes]: 1 params @ offset 0x00269547
    // USED → r2 = propertyAccessTest();
    // CODE → addr: 42 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 11307>  # String: 'propertyAccessTest' (Identifier)
    param6.propertyAccessTest = propertyAccessTest()
    // CODE → addr: 48 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15099>  # Function: [#15099 computedPropertyTest of 89 bytes]: 1 params @ offset 0x0026960e
    // USED → r2 = computedPropertyTest();
    // CODE → addr: 53 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11290>  # String: 'computedPropertyTest' (Identifier)
    param6.computedPropertyTest = computedPropertyTest()
    // CODE → addr: 59 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15100>  # Function: [#15100 optionalChainingTest of 133 bytes]: 1 params @ offset 0x00269667
    // USED → r0 = optionalChainingTest();
    // CODE → addr: 64 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 11295>  # String: 'optionalChainingTest' (Identifier)
    param6.optionalChainingTest = optionalChainingTest()
    // CODE → addr: 70 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 72 | <Ret>: <Reg8: 0>
    return undefined;
}