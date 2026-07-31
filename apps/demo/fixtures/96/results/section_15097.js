function function_15097(param0, param1, param2, param3, param4, param5, param6, param7) {
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
    // USED → r3 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15098>  # Function: [#15098 propertyAccessTest of 199 bytes]: 1 params @ offset 0x00269547
    // USED → r2 = propertyAccessTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 11307>  # String: 'propertyAccessTest' (Identifier)
    param6.propertyAccessTest = propertyAccessTest
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15099>  # Function: [#15099 computedPropertyTest of 89 bytes]: 1 params @ offset 0x0026960e
    // USED → r2 = computedPropertyTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11290>  # String: 'computedPropertyTest' (Identifier)
    param6.computedPropertyTest = computedPropertyTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15100>  # Function: [#15100 optionalChainingTest of 133 bytes]: 1 params @ offset 0x00269667
    // USED → r0 = optionalChainingTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 11295>  # String: 'optionalChainingTest' (Identifier)
    param6.optionalChainingTest = optionalChainingTest
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}