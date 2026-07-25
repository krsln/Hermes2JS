async function* anon_9594(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield /* ResumeGenerator -> r0 */
    // CODE → <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = getEnvironment(4)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 98>  # String: 'concat' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 8724>  # String: 'https://coachify.ai/api/checkUsernameAvailable?username=' (String)
    // USED → r5 = "https://coachify.ai/api/checkUsernameAvailable?username="
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 5, Reg8: 1>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
     = await // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003a
    yield label_58;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        // USED → r1 = await yield /* ResumeGenerator -> r1 */
        // CODE → <JmpTrue>: <Addr8: 38, Reg8: 3>  # Address: 00000063
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 6, string_id: 171>  # String: 'log' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12563>  # String: 'available' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 2>
        // Unhandled opcode: Ret
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 1>
        // Unhandled opcode: Ret
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        // Unhandled opcode: Ret
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        // Unhandled opcode: Ret
    }
    // LOOP → END
}