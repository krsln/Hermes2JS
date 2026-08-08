function function_15127(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15130>  # Function: [#15130 tag of 132 bytes]: 2 params @ offset 0x0026a3aa
    // USED → r2 = tag;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 2>
    createEnvironment()[0] = tag
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = globalThis.Object.defineProperty(param6, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15128>  # Function: [#15128 basicTemplateTest of 115 bytes]: 3 params @ offset 0x0026a298
    // USED → r2 = basicTemplateTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 11328>  # String: 'basicTemplateTest' (Identifier)
    param6.basicTemplateTest = basicTemplateTest
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15129>  # Function: [#15129 nestedTemplateTest of 159 bytes]: 3 params @ offset 0x0026a30b
    // USED → r2 = nestedTemplateTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11332>  # String: 'nestedTemplateTest' (Identifier)
    param6.nestedTemplateTest = nestedTemplateTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15132>  # Function: [#15132 taggedTemplateTest of 99 bytes]: 2 params @ offset 0x0026a46b
    // USED → r0 = taggedTemplateTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 11337>  # String: 'taggedTemplateTest' (Identifier)
    param6.taggedTemplateTest = taggedTemplateTest
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}