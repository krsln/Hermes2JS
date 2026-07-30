function function_15112(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15113>  # Function: [#15113 Dog of 98 bytes]: 3 params @ offset 0x00265aed
    // USED → r4 = Dog;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = Dog
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 2>
    // USED → r2 = getEnvironment(0)[2];
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 108>  # String: 'default' (Identifier)
    // USED → r5 = getEnvironment(0)[2].default;
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <Call3>: <Reg8: 2, Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = getEnvironment(0)[2].default.call(undefined, Dog, param1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 4>
    // USED → r1 = getEnvironment(0)[4];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 108>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[4].default;
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 118>  # String: 'key' (Identifier)
    // USED → r5 = { key: "makeSound" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 15114>  # Function: [#15114 makeSound of 106 bytes]: 1 params @ offset 0x00265b4f
    // USED → r1 = makeSound;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 206>  # String: 'value' (Identifier)
    // USED → r5 = { key: "makeSound", value: makeSound };
    // CODE → <NewArray>: <Reg8: 1, UInt16: 1>
    // USED → r1 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 5, UInt8: 0>
    // USED → r1 = [{ key: "makeSound", value: makeSound }];
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 104>  # String: 'create' (Identifier)
    // USED → r6 = "create";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 6, string_id: 118>  # String: 'key' (Identifier)
    // USED → r5 = { key: "create" };
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15115>  # Function: [#15115 create of 58 bytes]: 2 params @ offset 0x00265bb9
    // USED → r0 = create;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 0, string_id: 206>  # String: 'value' (Identifier)
    // USED → r5 = { key: "create", value: create };
    // CODE → <NewArray>: <Reg8: 0, UInt16: 1>
    // USED → r0 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 0>
    // USED → r0 = [{ key: "create", value: create }];
    // CODE → <Call4>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0>
    // USED → r0 = getEnvironment(0)[4].default.call(undefined, Dog, [{ key: "makeSound", value: makeSound }], [{ key: "create", value: create }]);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[4].default.call(undefined, Dog, [{ key: "makeSound", value: makeSound }], [{ key: "create", value: create }]);
}