function function_11944(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment()
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    // USED → r1 = getEnvironment(1)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined
    // CODE → <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 11946>  # Function: [#11946  of 9 bytes]: 3 params @ offset 0x002b9c07
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11945>  # Function: [#11945 request of 30 bytes]: 3 params @ offset 0x00189110
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}