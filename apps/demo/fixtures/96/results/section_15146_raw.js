function makeCounter() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = 0
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15147>  # Function: [#15147 increment of 16 bytes]: 1 params @ offset 0x0026a98b
    // USED → r2 = increment();
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 10830>  # String: 'increment' (Identifier)
    r0.increment = increment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15148>  # Function: [#15148 decrement of 16 bytes]: 1 params @ offset 0x0026a99b
    // USED → r2 = decrement();
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 10333>  # String: 'decrement' (Identifier)
    r0.decrement = decrement()
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15149>  # Function: [#15149 value of 9 bytes]: 1 params @ offset 0x000f7bb4
    // USED → r1 = value();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = value()
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}