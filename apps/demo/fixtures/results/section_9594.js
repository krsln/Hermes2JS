async function* anon_9594(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield
    // CODE → <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    if (r1) { /* jump to label_102 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = getEnvironment(4)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    // USED → r1 = getEnvironment(4)[16]
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r4 = getEnvironment(4)[16].default
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // USED → r3 = getEnvironment(4)[16].default.get
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = r2.HermesInternal
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r6 = r2.HermesInternal.concat
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 8724>  # String: 'https://coachify.ai/api/checkUsernameAvailable?username=' (String)
    // USED → r5 = "https://coachify.ai/api/checkUsernameAvailable?username="
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 5, Reg8: 1>
    // USED → r1 = r2.HermesInternal.concat("https://coachify.ai/api/checkUsernameAvailable?username=", r1)
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    // USED → r1 = await getEnvironment(4)[16].default.get(getEnvironment(4)[16].default, r2.HermesInternal.concat("https://coachify.ai/api/checkUsernameAvailable?username=", r1))
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003a
    yield label_58;  // SaveGenerator: suspend and jump to 58
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return await getEnvironment(4)[16].default.get(getEnvironment(4)[16].default, r2.HermesInternal.concat("https://coachify.ai/api/checkUsernameAvailable?username=", r1));
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield
    // CODE → <JmpTrue>: <Addr8: 38, Reg8: 3>  # Address: 00000063
    if (getEnvironment(4)[16].default.get) { /* jump to label_99 */ }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = r2.console
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 6, string_id: 171>  # String: 'log' (Identifier)
    // USED → r3 = r2.console.log
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = r1.data
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r2.console.log(r2.console, r1.data)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = r1.data
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12563>  # String: 'available' (Identifier)
    // USED → r2 = r1.data.available
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // CODE → <Ret>: <Reg8: 2>
    return r1.data.available;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // CODE → <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}