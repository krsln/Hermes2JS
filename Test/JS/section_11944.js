function function_11944(param0) {
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
    // CODE -> <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
    r1 = r1.default.call(this, undefined, r1)
    // CODE -> <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    r0 = setEnvSlot(0, r1)  // StoreToEnvironment: env=r0, slot=0, value=r1
    // CODE -> <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
    // USED -> r0 = // Closure fetchMovies with env r0
    // CODE -> <Ret>: <Reg8: 0>
    return // Closure fetchMovies with env r0;
}