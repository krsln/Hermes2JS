async function* anon_9594(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield;
    // CODE → <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    if (r1) goto label_102;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = getEnvironment(4);
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    // USED → r1 = getEnvironment(4)[16];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r4 = getEnvironment(4)[16].default;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // USED → r3 = getEnvironment(4)[16].default.get;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r6 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 8724>  # String: 'https://coachify.ai/api/checkUsernameAvailable?username=' (String)
    // USED → r5 = "https://coachify.ai/api/checkUsernameAvailable?username=";
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 5, Reg8: 1>
    // USED → r1 = globalThis.HermesInternal.concat("https://coachify.ai/api/checkUsernameAvailable?username=", param1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    // USED → r1 = await CallExpression(callee=MemberExpression(receiver=MemberExpression(receiver=MemberExpression(receiver=CallExpression(callee=Identifier(name='getEnvironment'), arguments=(NumericLiteral(value=4),), optional=False), member=NumericLiteral(value=16), computed=True, optional=False), member=Identifier(name='default'), computed=False, optional=False), member=Identifier(name='get'), computed=False, optional=False), arguments=(MemberExpression(receiver=MemberExpression(receiver=CallExpression(callee=Identifier(name='getEnvironment'), arguments=(NumericLiteral(value=4),), optional=False), member=NumericLiteral(value=16), computed=True, optional=False), member=Identifier(name='default'), computed=False, optional=False), CallExpression(callee=MemberExpression(receiver=MemberExpression(receiver=Identifier(name='globalThis'), member=Identifier(name='HermesInternal'), computed=False, optional=False), member=Identifier(name='concat'), computed=False, optional=False), arguments=(StringLiteral(value='https://coachify.ai/api/checkUsernameAvailable?username='), Identifier(name='param1')), optional=False)), optional=False)
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000003a
    goto label_58;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield;
    // CODE → <JmpTrue>: <Addr8: 38, Reg8: 3>  # Address: 00000063
    if (getEnvironment(4)[16].default.get) goto label_99;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 6, string_id: 171>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = await yield.data;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(globalThis.console, await yield.data);
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = await yield.data;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12563>  # String: 'available' (Identifier)
    // USED → r2 = await yield.data.available;
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 2>
    return await yield.data.available;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 1>
    return await yield;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}