function makeCounter() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → addr:  2 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  4 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = 0
    // CODE → addr:  8 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 10 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15147>  # Function: [#15147 increment of 16 bytes]: 1 params @ offset 0x0026a98b
    // USED → r2 = increment();
    // CODE → addr: 15 | <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 10830>  # String: 'increment' (Identifier)
    r0.increment = increment()
    // CODE → addr: 20 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15148>  # Function: [#15148 decrement of 16 bytes]: 1 params @ offset 0x0026a99b
    // USED → r2 = decrement();
    // CODE → addr: 25 | <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 10333>  # String: 'decrement' (Identifier)
    r0.decrement = decrement()
    // CODE → addr: 30 | <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15149>  # Function: [#15149 value of 9 bytes]: 1 params @ offset 0x000f7bb4
    // USED → r1 = value();
    // CODE → addr: 35 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = value()
    // CODE → addr: 39 | <Ret>: <Reg8: 0>
    return r0;
}