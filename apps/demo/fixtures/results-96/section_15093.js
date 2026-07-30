function makeCounter(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 1>
    // USED → r1 = createEnvironment();
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    createEnvironment()[0] = 0
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15094>  # Function: [#15094 increment of 16 bytes]: 1 params @ offset 0x00265552
    // USED → r2 = increment;
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 8421>  # String: 'increment' (Identifier)
    // USED → r0 = { increment: increment };
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15095>  # Function: [#15095 decrement of 16 bytes]: 1 params @ offset 0x00265562
    // USED → r2 = decrement;
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 14314>  # String: 'decrement' (Identifier)
    // USED → r0 = { increment: increment, decrement: decrement };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15096>  # Function: [#15096 value of 9 bytes]: 1 params @ offset 0x000f46a0
    // USED → r1 = value;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 206>  # String: 'value' (Identifier)
    // USED → r0 = { increment: increment, decrement: decrement, value: value };
    // CODE → <Ret>: <Reg8: 0>
    return { increment: increment, decrement: decrement, value: value };
}