function function_15201(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15202>  # Function: [#15202 Dog of 98 bytes]: 3 params @ offset 0x0026b998
    // USED → r4 = Dog(param1, param2);
    // CODE → addr:  7 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    r0[0] = Dog(param1, param2)
    // CODE → addr: 11 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 14 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 2>
    r2 = r1[2]
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r5 = r2.default;
    // CODE → addr: 23 | <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // CODE → addr: 25 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr: 28 | <Call3>: <Reg8: 2, Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r2.default.call(r3, Dog(param1, param2), param1)
    // CODE → addr: 34 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 4>
    r1 = r1[4]
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r1.default;
    // CODE → addr: 43 | <NewObject>: <Reg8: 5>
    r5 = {  }
    // CODE → addr: 45 | <LoadConstString>: <Reg8: 1, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = "makeSound";
    // CODE → addr: 49 | <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r5.key = "makeSound"
    // CODE → addr: 53 | <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 15203>  # Function: [#15203 makeSound of 106 bytes]: 1 params @ offset 0x0026b9fa
    // USED → r1 = makeSound();
    // CODE → addr: 58 | <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r5.value = makeSound()
    // CODE → addr: 62 | <NewArray>: <Reg8: 1, UInt16: 1>
    r1 = []
    // CODE → addr: 66 | <PutOwnByIndex>: <Reg8: 1, Reg8: 5, UInt8: 0>
    // USED → r1 = r1[0] = r5;
    // CODE → addr: 70 | <NewObject>: <Reg8: 5>
    r5 = {  }
    // CODE → addr: 72 | <LoadConstString>: <Reg8: 6, string_id: 103>  # String: 'create' (Identifier)
    // USED → r6 = "create";
    // CODE → addr: 76 | <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 6, string_id: 117>  # String: 'key' (Identifier)
    r5.key = "create"
    // CODE → addr: 80 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15204>  # Function: [#15204 create of 58 bytes]: 2 params @ offset 0x0026ba64
    // USED → r0 = create(param1);
    // CODE → addr: 85 | <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r5.value = create(param1)
    // CODE → addr: 89 | <NewArray>: <Reg8: 0, UInt16: 1>
    r0 = []
    // CODE → addr: 93 | <PutOwnByIndex>: <Reg8: 0, Reg8: 5, UInt8: 0>
    // USED → r0 = r0[0] = r5;
    // CODE → addr: 97 | <Call4>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0>
    r0 = r1.default.call(r3, Dog(param1, param2), r1, r0)
    // CODE → addr:104 | <Ret>: <Reg8: 0>
    return r0;
}