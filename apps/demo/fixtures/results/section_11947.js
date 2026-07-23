async function* anon_11947(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // LINE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this
    // LINE → <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    r0 = await yield
    // LINE → <JmpTrueLong>: <Addr32: 311, Reg8: 5>  # Address: 0000013e
    if (r5) { /* jump to label_318 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1
    // LINE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2
    // LINE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // LINE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 17057>  # String: '_request' (Identifier)
    // USED → r7 = this._request
    // LINE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 4, Reg8: 3>
    // USED → r3 = await this._request(param1, param2)
    // LINE → <SaveGenerator>: <Addr8: 4>  # Address: 00000029
    yield label_41;  // SaveGenerator: suspend and jump to 41
    // ──────────────── Block 2 ──────────────── 
    // LINE → <Ret>: <Reg8: 3>
    return await this._request(param1, param2);
    // ──────────────── Block 3 ──────────────── 
    // LINE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    r3 = await yield
    // LINE → <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 00000032
    if (param1) { /* jump to label_50 */ }
    // ──────────────── Block 4 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 3>
    return undefined_r3;
    // ──────────────── Block 5 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 3>
    return undefined_r3;
    // LINE → <Catch>: <Reg8: 7>
    // USED → r7 = caughtException
    // LINE → <Mov>: <Reg8: 1, Reg8: 7>
    // USED → r1 = r7
    // LINE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis
    // LINE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error
    // LINE → <InstanceOf>: <Reg8: 4, Reg8: 7, Reg8: 4>
    // USED → r4 = caughtException instanceof globalThis.Error
    // LINE → <JmpFalseLong>: <Addr32: 246, Reg8: 4>  # Address: 0000013c
    if (!caughtException instanceof globalThis.Error) { /* jump to label_316 */ }
    // ──────────────── Block 6 ──────────────── 
    // LINE → <NewObject>: <Reg8: 6>
    r6 = {}
    // LINE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error
    // LINE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r4 = globalThis.Error.captureStackTrace
    // LINE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r8 = globalThis.Error
    // LINE → <JmpTrue>: <Addr8: 25, Reg8: 4>  # Address: 00000079
    if (globalThis.Error.captureStackTrace) { /* jump to label_121 */ }
    // ──────────────── Block 7 ──────────────── 
    // LINE → <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 4, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r4 = globalThis.Error.prototype
    // LINE → <CreateThis>: <Reg8: 7, Reg8: 4, Reg8: 8>
    // USED → r7 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
    // LINE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = r7
    // LINE → <Construct>: <Reg8: 4, Reg8: 8, UInt8: 1>
    r4 = new globalThis.Error(createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
    // LINE → <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
    // USED → r6 = r7[r4]
    // LINE → <Jmp>: <Addr8: 16>  # Address: 00000087
    goto label_135;
    // ──────────────── Block 8 ──────────────── 
    // LINE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r7 = globalThis.Error.captureStackTrace
    // LINE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = r6
    // LINE → <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
    r4 = globalThis.Error.captureStackTrace(r6)
    // ──────────────── Block 9 ──────────────── 
    // LINE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = r6
    // LINE → <GetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r7 = r6.stack
    // LINE → <LoadConstString>: <Reg8: 8, string_id: 11303>  # String: '' (Identifier)
    // USED → r8 = ""
    // LINE → <Mov>: <Reg8: 4, Reg8: 8>
    r4 = r8
    // LINE → <JmpFalse>: <Addr8: 34, Reg8: 7>  # Address: 000000b9
    if (!r6.stack) { /* jump to label_185 */ }
    // ──────────────── Block 10 ──────────────── 
    // LINE → <GetById>: <Reg8: 9, Reg8: 6, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r9 = r7[r4].stack
    // LINE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
    // USED → r7 = r7[r4].stack.replace
    // LINE → <CreateRegExp>: <Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168>  # String: '^.+\\n' (String)  # String: '' (Identifier)
    // USED → r6 = /^.+\\n/
    // LINE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 9, Reg8: 6, Reg8: 8>
    r4 = r7[r4].stack.replace(/^.+\\n/, "")
    // ──────────────── Block 11 ──────────────── 
    // LINE → <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r4
    // LINE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = r1
    // LINE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r4 = r1.stack
    // LINE → <JmpTrue>: <Addr8: 17, Reg8: 4>  # Address: 000000d6
    if (r1.stack) { /* jump to label_214 */ }
    // ──────────────── Block 12 ──────────────── 
    // LINE → <Mov>: <Reg8: 6, Reg8: 1>
    // USED → r6 = r1
    // LINE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = r2
    // LINE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
    r6 = { stack: r2 }
    // LINE → <Jmp>: <Addr8: 100>  # Address: 00000138
    goto label_312;
    // ──────────────── Block 13 ──────────────── 
    // LINE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = r2
    // LINE → <JmpFalse>: <Addr8: 95, Reg8: 4>  # Address: 00000138
    if (!r2) { /* jump to label_312 */ }
    // ──────────────── Block 14 ──────────────── 
    // LINE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 7, string_id: 50>  # String: 'String' (Identifier)
    // USED → r4 = globalThis.String
    // LINE → <Mov>: <Reg8: 3, Reg8: 1>
    // USED → r3 = r1
    // LINE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r3 = r1.stack
    // LINE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
    // USED → r5 = globalThis.String(r1.stack)
    // LINE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 8, string_id: 19080>  # String: 'endsWith' (Identifier)
    // USED → r4 = globalThis.String(r1.stack).endsWith
    // LINE → <Mov>: <Reg8: 7, Reg8: 2>
    // USED → r7 = r2
    // LINE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
    // USED → r6 = r2.replace
    // LINE → <CreateRegExp>: <Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169>  # String: '^.+\\n.+\\n' (String)  # String: '' (Identifier)
    // USED → r3 = /^.+\\n.+\\n/
    // LINE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 8>
    // USED → r3 = r2.replace(/^.+\\n.+\\n/, "")
    // LINE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    // USED → r3 = globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, ""))
    // LINE → <JmpTrue>: <Addr8: 33, Reg8: 3>  # Address: 00000138
    if (globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, ""))) { /* jump to label_312 */ }
    // ──────────────── Block 15 ──────────────── 
    // LINE → <Mov>: <Reg8: 3, Reg8: 1>
    // USED → r3 = r1
    // LINE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r4 = r1.stack
    // LINE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = r2
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 12321>  # String: '\n' (Identifier)
    // USED → r2 = "\n"
    // LINE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = "\n" + r2
    // LINE → <Add>: <Reg8: 2, Reg8: 4, Reg8: 2>
    // USED → r2 = r1.stack + "\n" + r2
    // LINE → <PutById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
    r3 = { stack: r1.stack + "\n" + r2 }
    // ──────────────── Block 16 ──────────────── 
    // LINE → <Jmp>: <Addr8: 4>  # Address: 0000013c
    goto label_316;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 18 ──────────────── 
        // LINE → <Throw>: <Reg8: 1>
        r1 = throw r7
        // ──────────────── Block 17 ──────────────── 
        // LINE → <Catch>: <Reg8: 2>
        r2 = caughtException
    }
    // LOOP → END
    // ──────────────── Block 19 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 0>
    return undefined_r0;
}