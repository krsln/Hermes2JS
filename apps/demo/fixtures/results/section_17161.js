async function* anon_17161(param0, param1) {
    // CODE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // CODE → <JmpTrueLong>: <Addr32: 161, Reg8: 1>  # Address: 000000a8
    if (r1) { /* jump to label_168 */ }
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 13438>  # String: 'fetch' (Identifier)
    // USED → r3 = globalThis.fetch
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 7>
    // USED → r1 = await globalThis.fetch(param1)
    // CODE → <Ret>: <Reg8: 1>
    return await globalThis.fetch(param1);
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    r1 = await yield
    // CODE → <JmpTrueLong>: <Addr32: 130, Reg8: 3>  # Address: 000000a5
    if (globalThis.fetch) { /* jump to label_165 */ }
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 14168>  # String: 'ok' (Identifier)
    // USED → r3 = r1.ok
    if (!(r1.ok)) {
        // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
        // USED → r4 = r1.status
        // CODE → <LoadConstZero>: <Reg8: 3>
        // USED → r3 = 0
        // CODE → <JStrictNotEqual>: <Addr8: 22, Reg8: 4, Reg8: 3>  # Address: 00000050
        if (r1.status !== 0) { /* jump to label_80 */ }
        // CODE → <GetById>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 19693>  # String: 'startsWith' (Identifier)
        // USED → r4 = param1.startsWith
        // CODE → <LoadConstString>: <Reg8: 3, string_id: 1058>  # String: 'file://' (String)
        // USED → r3 = "file://"
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
        // USED → r3 = param1.startsWith("file://")
        if (!(param1.startsWith("file://"))) {
            // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 14>  # String: 'Error' (Identifier)
            // USED → r4 = globalThis.Error
            // CODE → <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
            // USED → r6 = r1.status
            // CODE → <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 6, string_id: 21>  # String: 'HermesInternal' (Identifier)
            // USED → r2 = globalThis.HermesInternal
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 7, string_id: 98>  # String: 'concat' (Identifier)
            // USED → r5 = globalThis.HermesInternal.concat
            // CODE → <LoadConstString>: <Reg8: 3, string_id: 2430>  # String: 'Fetching ' (String)
            // USED → r3 = "Fetching "
            // CODE → <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: ' failed with status ' (String)
            // USED → r2 = " failed with status "
            // CODE → <Call4>: <Reg8: 10, Reg8: 5, Reg8: 3, Reg8: 7, Reg8: 2, Reg8: 6>
            r10 = globalThis.HermesInternal.concat.call(this, "Fetching ", param1, " failed with status ", r1.status)
            // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 158>  # String: 'prototype' (Identifier)
            // USED → r3 = globalThis.Error.prototype
            // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
            // USED → r3 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
            // CODE → <Mov>: <Reg8: 11, Reg8: 3>
            r11 = r3
            // CODE → <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
            r2 = new globalThis.Error(" failed with status ", createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
            // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
            // USED → r2 = r3[r2]
        }
    }
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 9, string_id: 229>  # String: 'text' (Identifier)
    // USED → r2 = r1.text
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    // USED → r2 = await r1.text()
    // CODE → <Ret>: <Reg8: 2>
    return await r1.text();
    // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    r2 = await yield
    if (!(createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))) {
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator: No output needed
        // CODE → <Ret>: <Reg8: 2>
        return undefined_r2;
    }
    // CODE → <Ret>: <Reg8: 2>
    return undefined_r2;
    // CODE → <Ret>: <Reg8: 1>
    return undefined_r1;
    // CODE → <Ret>: <Reg8: 0>
    return undefined_r0;
}