async function* anon_11947(param0, param1, param2) {
    // CODE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    r0 = await yield
    // CODE → <JmpTrueLong>: <Addr32: 311, Reg8: 5>  # Address: 0000013e
    if (r5) { /* jump to label_318 */ }
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 17057>  # String: '_request' (Identifier)
    // USED → r7 = this._request
    // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 4, Reg8: 3>
    // USED → r3 = await this._request(param1, param2)
    // CODE → <Ret>: <Reg8: 3>
    return await this._request(param1, param2);
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    r3 = await yield
    if (!(param1)) {
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator: No output needed
        // CODE → <Ret>: <Reg8: 3>
        return undefined_r3;
    }
    // CODE → <Ret>: <Reg8: 3>
    return undefined_r3;
    // CODE → <Mov>: <Reg8: 1, Reg8: 7>
    // USED → r1 = r7
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error
    // CODE → <InstanceOf>: <Reg8: 4, Reg8: 7, Reg8: 4>
    // USED → r4 = caughtException instanceof globalThis.Error
    // CODE → <JmpFalseLong>: <Addr32: 246, Reg8: 4>  # Address: 0000013c
    if (!caughtException instanceof globalThis.Error) { /* jump to label_316 */ }
    // CODE → <NewObject>: <Reg8: 6>
    r6 = {}
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r4 = globalThis.Error.captureStackTrace
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r8 = globalThis.Error
    if (!(globalThis.Error.captureStackTrace)) {
        // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 4, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r4 = globalThis.Error.prototype
        // CODE → <CreateThis>: <Reg8: 7, Reg8: 4, Reg8: 8>
        // USED → r7 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
        // CODE → <Mov>: <Reg8: 12, Reg8: 7>
        r12 = r7
        // CODE → <Construct>: <Reg8: 4, Reg8: 8, UInt8: 1>
        r4 = new globalThis.Error(createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
        // CODE → <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
        // USED → r6 = r7[r4]
    }
    // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r7 = globalThis.Error.captureStackTrace
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = r6
    // CODE → <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
    r4 = globalThis.Error.captureStackTrace(r6)
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = r6
    // CODE → <GetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r7 = r6.stack
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 11303>  # String: '' (Identifier)
    // USED → r8 = ""
    // CODE → <Mov>: <Reg8: 4, Reg8: 8>
    r4 = r8
    if (r6.stack) {
        // CODE → <GetById>: <Reg8: 9, Reg8: 6, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // USED → r9 = r7[r4].stack
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
        // USED → r7 = r7[r4].stack.replace
        // CODE → <CreateRegExp>: <Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168>  # String: '^.+\\n' (String)  # String: '' (Identifier)
        // USED → r6 = /^.+\\n/
        // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 9, Reg8: 6, Reg8: 8>
        r4 = r7[r4].stack.replace(/^.+\\n/, "")
    }
    // CODE → <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r4
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = r1
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r4 = r1.stack
    if (!(r1.stack)) {
        // CODE → <Mov>: <Reg8: 6, Reg8: 1>
        // USED → r6 = r1
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        // USED → r4 = r2
        // CODE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
        r6 = { stack: r2 }
    }
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = r2
    if (r2) {
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 7, string_id: 50>  # String: 'String' (Identifier)
        // USED → r4 = globalThis.String
        // CODE → <Mov>: <Reg8: 3, Reg8: 1>
        // USED → r3 = r1
        // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // USED → r3 = r1.stack
        // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
        // USED → r5 = globalThis.String(r1.stack)
        // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 8, string_id: 19080>  # String: 'endsWith' (Identifier)
        // USED → r4 = globalThis.String(r1.stack).endsWith
        // CODE → <Mov>: <Reg8: 7, Reg8: 2>
        // USED → r7 = r2
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
        // USED → r6 = r2.replace
        // CODE → <CreateRegExp>: <Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169>  # String: '^.+\\n.+\\n' (String)  # String: '' (Identifier)
        // USED → r3 = /^.+\\n.+\\n/
        // CODE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 8>
        // USED → r3 = r2.replace(/^.+\\n.+\\n/, "")
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        // USED → r3 = globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, ""))
        if (!(globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, "")))) {
            // CODE → <Mov>: <Reg8: 3, Reg8: 1>
            // USED → r3 = r1
            // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
            // USED → r4 = r1.stack
            // CODE → <Mov>: <Reg8: 5, Reg8: 2>
            // USED → r5 = r2
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 12321>  # String: '\n' (Identifier)
            // USED → r2 = "\n"
            // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 5>
            // USED → r2 = "\n" + r2
            // CODE → <Add>: <Reg8: 2, Reg8: 4, Reg8: 2>
            // USED → r2 = r1.stack + "\n" + r2
            // CODE → <PutById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
            r3 = { stack: r1.stack + "\n" + r2 }
        }
    }
    // CODE → <Throw>: <Reg8: 1>
    r1 = throw r7
    // CODE → <Ret>: <Reg8: 0>
    return undefined_r0;
}