function function_15201(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15202>  # Function: [#15202 Dog of 98 bytes]: 3 params @ offset 0x0026b998
    // USED → r4 = Dog;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = Dog
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 2>
    // USED → r2 = getEnvironment(0)[2];
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = getEnvironment(0)[2].default;
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <Call3>: <Reg8: 2, Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = getEnvironment(0)[2].default.call(undefined, r4, r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 4>
    // USED → r1 = getEnvironment(0)[4];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[4].default;
    // CODE → <NewObject>: <Reg8: 5>
    r5 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r5.key = "makeSound"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 15203>  # Function: [#15203 makeSound of 106 bytes]: 1 params @ offset 0x0026b9fa
    // USED → r1 = makeSound;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r5.value = makeSound
    // CODE → <NewArray>: <Reg8: 1, UInt16: 1>
    r1 = []
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 5, UInt8: 0>
    // USED → r1 = r1[0] = r5;
    // CODE → <NewObject>: <Reg8: 5>
    r5 = {  }
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 103>  # String: 'create' (Identifier)
    // USED → r6 = "create";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 6, string_id: 117>  # String: 'key' (Identifier)
    r5.key = "create"
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15204>  # Function: [#15204 create of 58 bytes]: 2 params @ offset 0x0026ba64
    // USED → r0 = create;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r5.value = create
    // CODE → <NewArray>: <Reg8: 0, UInt16: 1>
    r0 = []
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 0>
    // USED → r0 = r0[0] = r5;
    // CODE → <Call4>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0>
    // USED → r0 = getEnvironment(0)[4].default.call(undefined, r4, r1, r0);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[4].default.call(undefined, r4, r1, r0);
}