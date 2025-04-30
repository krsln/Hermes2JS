function func_11944(param0) {
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
    // CODE -> <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
    // CODE -> <Ret>: <Reg8: 0>
    return // Closure function_11947 with env r0;
}