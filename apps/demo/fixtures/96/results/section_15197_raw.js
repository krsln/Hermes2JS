function function_15197() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 4>
    // USED → r4 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 4, function_id: 15198>  # Function: [#15198 Animal of 72 bytes]: 3 params @ offset 0x0026b86f
    // USED → r3 = Animal(param1, param2);
    // CODE → <StoreToEnvironment>: <Reg8: 4, UInt8: 0, Reg8: 3>
    createEnvironment()[0] = Animal(param1, param2)
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = getEnvironment(0)[4];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = getEnvironment(0)[4].default;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "makeSound"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 4, function_id: 15199>  # Function: [#15199 makeSound of 62 bytes]: 1 params @ offset 0x0026b8b7
    // USED → r1 = makeSound();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = makeSound()
    // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
    r1 = []
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = r1[0] = r0;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 10805>  # String: 'description' (Identifier)
    // USED → r5 = "description";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "description"
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 4, function_id: 15200>  # Function: [#15200 get of 57 bytes]: 1 params @ offset 0x0026b8f5
    // USED → r4 = get();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 4, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = (r1[0] = r0)[1] = r0;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3, Reg8: 1>
    // USED → r0 = getEnvironment(0)[4].default.call(undefined, Animal(param1, param2), r1);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[4].default.call(undefined, Animal(param1, param2), r1);
}