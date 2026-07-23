async function* anon_9594(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // LINE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // LINE → <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    if (r1) { /* jump to label_102 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <GetEnvironment>: <Reg8: 1, UInt8: 4>
    r1 = getEnvironment(4)
    // LINE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    r1 = r1[16]
    // LINE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r4 = r1.default
    // LINE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // USED → r3 = r1.default.get
    // LINE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // LINE → <TryGetById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = globalThis.HermesInternal
    // LINE → <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r6 = globalThis.HermesInternal.concat
    // LINE → <LoadConstString>: <Reg8: 5, string_id: 8724>  # String: 'https://coachify.ai/api/checkUsernameAvailable?username=' (String)
    // USED → r5 = "https://coachify.ai/api/checkUsernameAvailable?username="
    // LINE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1
    // LINE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 5, Reg8: 1>
    // USED → r1 = globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1)
    // LINE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    // USED → r1 = await r1.default.get(globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1))
    // LINE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003a
    yield label_58;  // SaveGenerator: suspend and jump to 58
    // ──────────────── Block 2 ──────────────── 
    // LINE → <Ret>: <Reg8: 1>
    return await r1.default.get(globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1));
    // ──────────────── Block 3 ──────────────── 
    // LINE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    r1 = await yield
    // LINE → <JmpTrue>: <Addr8: 38, Reg8: 3>  # Address: 00000063
    if (r1.default.get) { /* jump to label_99 */ }
    // ──────────────── Block 4 ──────────────── 
    // LINE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console
    // LINE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 6, string_id: 171>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = r1.data
    // LINE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(r1.data)
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = r1.data
    // LINE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12563>  # String: 'available' (Identifier)
    // USED → r2 = r1.data.available
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 2>
    return r1.data.available;
    // ──────────────── Block 5 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 1>
    return undefined_r1;
    // ──────────────── Block 6 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 0>
    return undefined_r0;
}