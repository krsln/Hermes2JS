function function_11948(param0) {
    // CODE -> <CreateEnvironment>: <Reg8: 0>
    r0 = // Create new environment
    // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0);
    // CODE -> <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    r1 = r1[0]
    // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 131>  # String: 'default' (Identifier)
    // USED -> r3 = r1.default
    // CODE -> <LoadConstUndefined>: <Reg8: 2>
    // USED -> r2 = undefined
    // CODE -> <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 11949>  # Function: [#11949  of 9 bytes]: 2 params @ offset 0x002192cc
    // USED -> r1 = createGeneratorClosure(r0, function_11949)
    // CODE -> <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
    r1 = r1.default(createGeneratorClosure(r0, function_11949))
    // CODE -> <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    r0 = setEnvSlot(0, r1)  // StoreToEnvironment: env=r0, slot=0, value=r1
    // CODE -> <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11951>  # Function: [#11951 fetchMovieDetails of 29 bytes]: 2 params @ offset 0x00150430
    // USED -> r0 = fetchMovieDetails /* Closure with env r0 = undefined */
    // CODE -> <Ret>: <Reg8: 0>
    return fetchMovieDetails /* Closure with env r0 = undefined */;
}