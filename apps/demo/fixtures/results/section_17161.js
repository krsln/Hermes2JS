async function* anon_17161(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator;
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield;
    // CODE → <JmpTrueLong>: <Addr32: 161, Reg8: 1>  # Address: 000000a8
    if (r1) goto label_168;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 13438>  # String: 'fetch' (Identifier)
    // USED → r3 = globalThis.fetch;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 7>
    r1 = await CallExpression(callee=MemberExpression(receiver=Identifier(name='globalThis'), member=Identifier(name='fetch'), computed=False, optional=False), arguments=(UndefinedLiteral(), Identifier(name='param1')), optional=False)
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000020
    goto label_32;
    // LOOP → START (while)
    while (globalThis.fetch) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        // USED → r1 = await yield;
        // CODE → <JmpTrueLong>: <Addr32: 130, Reg8: 3>  # Address: 000000a5
        if (globalThis.fetch) goto label_165;
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        // Unhandled opcode: Ret
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 14168>  # String: 'ok' (Identifier)
    // USED → r3 = await yield.ok;
    // CODE → <JmpTrue>: <Addr8: 93, Reg8: 3>  # Address: 0000008c
    if (await yield.ok) goto label_140;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r4 = await yield.status;
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → <JStrictNotEqual>: <Addr8: 22, Reg8: 4, Reg8: 3>  # Address: 00000050
    if (await yield.status !== 0) goto label_80;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 19693>  # String: 'startsWith' (Identifier)
    // USED → r4 = param1.startsWith;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1058>  # String: 'file://' (String)
    // USED → r3 = "file://";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    // USED → r3 = param1.startsWith(param1, "file://");
    // CODE → <JmpTrue>: <Addr8: 63, Reg8: 3>  # Address: 0000008c
    if (param1.startsWith(param1, "file://")) goto label_140;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error;
    // CODE → <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r6 = await yield.status;
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 6, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r2 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 7, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r5 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 2430>  # String: 'Fetching ' (String)
    // USED → r3 = "Fetching ";
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: ' failed with status ' (String)
    // USED → r2 = " failed with status ";
    // CODE → <Call4>: <Reg8: 10, Reg8: 5, Reg8: 3, Reg8: 7, Reg8: 2, Reg8: 6>
    r10 = globalThis.HermesInternal.concat("Fetching ", param1, " failed with status ", await yield.status);
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r3 = globalThis.Error.prototype;
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = createThis(globalThis.Error.prototype, globalThis.Error);
    // CODE → <Mov>: <Reg8: 11, Reg8: 3>
    r11 = createThis(globalThis.Error.prototype, globalThis.Error);
    // CODE → <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
    // USED → r2 = new globalThis.Error(" failed with status ", createThis(globalThis.Error.prototype, globalThis.Error));
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(" failed with status ", createThis(globalThis.Error.prototype, globalThis.Error))];
    // CODE → <Throw>: <Reg8: 2>
    throw createThis(globalThis.Error.prototype, globalThis.Error)[new globalThis.Error(" failed with status ", createThis(globalThis.Error.prototype, globalThis.Error))];
    // ──────────────── Block 8 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 9, string_id: 229>  # String: 'text' (Identifier)
    // USED → r2 = await yield.text;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    r2 = await CallExpression(callee=MemberExpression(receiver=AwaitExpression(argument=YieldExpression(argument=None, delegate=False)), member=Identifier(name='text'), computed=False, optional=False), arguments=(AwaitExpression(argument=YieldExpression(argument=None, delegate=False)),), optional=False)
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000099
    goto label_153;
    // LOOP → START (while)
    while (createThis(globalThis.Error.prototype, globalThis.Error)) {
        // ──────────────── Block 10 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
        r2 = await yield;
        // CODE → <JmpTrue>: <Addr8: 6, Reg8: 3>  # Address: 000000a2
        if (createThis(globalThis.Error.prototype, globalThis.Error)) goto label_162;
        // ──────────────── Block 9 ──────────────── 
        // CODE → <Ret>: <Reg8: 2>
        // Unhandled opcode: Ret
    }
    // LOOP → END
    // ──────────────── Block 11 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 2>
    // Unhandled opcode: Ret
    // ──────────────── Block 12 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 2>
    // Unhandled opcode: Ret
    // ──────────────── Block 13 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 1>
    // Unhandled opcode: Ret
    // ──────────────── Block 14 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator;
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}