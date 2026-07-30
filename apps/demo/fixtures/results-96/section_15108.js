function function_15108(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 4>
    // USED → r4 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 4, function_id: 15109>  # Function: [#15109 Animal of 72 bytes]: 3 params @ offset 0x002659c4
    // USED → r3 = Animal;
    // CODE → <StoreToEnvironment>: <Reg8: 4, UInt8: 0, Reg8: 3>
    createEnvironment()[0] = Animal
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = getEnvironment(0)[4];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 108>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[4].default;
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 118>  # String: 'key' (Identifier)
    // USED → r0 = { key: "makeSound" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 4, function_id: 15110>  # Function: [#15110 makeSound of 62 bytes]: 1 params @ offset 0x00265a0c
    // USED → r1 = makeSound;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 206>  # String: 'value' (Identifier)
    // USED → r0 = { key: "makeSound", value: makeSound };
    // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
    // USED → r1 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = [{ key: "makeSound", value: makeSound }];
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 10660>  # String: 'description' (Identifier)
    // USED → r5 = "description";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 118>  # String: 'key' (Identifier)
    // USED → r0 = { key: "description" };
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 4, function_id: 15111>  # Function: [#15111 get of 57 bytes]: 1 params @ offset 0x00265a4a
    // USED → r4 = get;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 4, string_id: 51>  # String: 'get' (Identifier)
    // USED → r0 = { key: "description", get: get };
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = [{ key: "makeSound", value: makeSound }, { key: "description", get: get }];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3, Reg8: 1>
    // USED → r0 = getEnvironment(0)[4].default.call(undefined, Animal, [{ key: "makeSound", value: makeSound }, { key: "description", get: get }]);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[4].default.call(undefined, Animal, [{ key: "makeSound", value: makeSound }, { key: "description", get: get }]);
}