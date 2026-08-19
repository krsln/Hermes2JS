function function_15197() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 4>
    r4 = createEnvironment()
    // CODE → addr:  2 | <CreateClosure>: <Reg8: 3, Reg8: 4, function_id: 15198>  # Function: [#15198 Animal of 72 bytes]: 3 params @ offset 0x0026b86f
    // USED → r3 = Animal(param1, param2);
    // CODE → addr:  7 | <StoreToEnvironment>: <Reg8: 4, UInt8: 0, Reg8: 3>
    r4[0] = Animal(param1, param2)
    // CODE → addr: 11 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 14 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    r0 = r0[4]
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r0.default;
    // CODE → addr: 23 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 1, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → addr: 29 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "makeSound"
    // CODE → addr: 33 | <CreateClosure>: <Reg8: 1, Reg8: 4, function_id: 15199>  # Function: [#15199 makeSound of 62 bytes]: 1 params @ offset 0x0026b8b7
    // USED → r1 = makeSound();
    // CODE → addr: 38 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = makeSound()
    // CODE → addr: 42 | <NewArray>: <Reg8: 1, UInt16: 2>
    r1 = []
    // CODE → addr: 46 | <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = r1[0] = r0;
    // CODE → addr: 50 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 5, string_id: 10805>  # String: 'description' (Identifier)
    // USED → r5 = "description";
    // CODE → addr: 56 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "description"
    // CODE → addr: 60 | <CreateClosure>: <Reg8: 4, Reg8: 4, function_id: 15200>  # Function: [#15200 get of 57 bytes]: 1 params @ offset 0x0026b8f5
    // USED → r4 = get();
    // CODE → addr: 65 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 4, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → addr: 69 | <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = (r1[0] = r0)[1] = r0;
    // CODE → addr: 73 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 75 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3, Reg8: 1>
    r0 = r0.default(Animal(param1, param2), r1)
    // CODE → addr: 81 | <Ret>: <Reg8: 0>
    return r0;
}