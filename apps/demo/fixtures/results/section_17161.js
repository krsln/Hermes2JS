async function* anon_17161(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // LINE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1
    // LINE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // LINE → <JmpTrueLong>: <Addr32: 161, Reg8: 1>  # Address: 000000a8
    if (r1) { /* jump to label_168 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // LINE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 13438>  # String: 'fetch' (Identifier)
    // USED → r3 = globalThis.fetch
    // LINE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined
    // LINE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 7>
    // USED → r1 = await globalThis.fetch(param1)
    // LINE → <SaveGenerator>: <Addr8: 4>  # Address: 00000020
    yield label_32;  // SaveGenerator: suspend and jump to 32
    // ──────────────── Block 2 ──────────────── 
    // LINE → <Ret>: <Reg8: 1>
    return await globalThis.fetch(param1);
    // ──────────────── Block 3 ──────────────── 
    // LINE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    r1 = await yield
    // LINE → <JmpTrueLong>: <Addr32: 130, Reg8: 3>  # Address: 000000a5
    if (globalThis.fetch) { /* jump to label_165 */ }
    // ──────────────── Block 4 ──────────────── 
    // LINE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 14168>  # String: 'ok' (Identifier)
    // USED → r3 = r1.ok
    // LINE → <JmpTrue>: <Addr8: 93, Reg8: 3>  # Address: 0000008c
    if (r1.ok) { /* jump to label_140 */ }
    // ──────────────── Block 5 ──────────────── 
    // LINE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r4 = r1.status
    // LINE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0
    // LINE → <JStrictNotEqual>: <Addr8: 22, Reg8: 4, Reg8: 3>  # Address: 00000050
    if (r1.status !== 0) { /* jump to label_80 */ }
    // ──────────────── Block 6 ──────────────── 
    // LINE → <GetById>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 19693>  # String: 'startsWith' (Identifier)
    // USED → r4 = param1.startsWith
    // LINE → <LoadConstString>: <Reg8: 3, string_id: 1058>  # String: 'file://' (String)
    // USED → r3 = "file://"
    // LINE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    // USED → r3 = param1.startsWith("file://")
    // LINE → <JmpTrue>: <Addr8: 63, Reg8: 3>  # Address: 0000008c
    if (param1.startsWith("file://")) { /* jump to label_140 */ }
    // ──────────────── Block 7 ──────────────── 
    // LINE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error
    // LINE → <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r6 = r1.status
    // LINE → <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 6, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r2 = globalThis.HermesInternal
    // LINE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 7, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r5 = globalThis.HermesInternal.concat
    // LINE → <LoadConstString>: <Reg8: 3, string_id: 2430>  # String: 'Fetching ' (String)
    // USED → r3 = "Fetching "
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: ' failed with status ' (String)
    // USED → r2 = " failed with status "
    // LINE → <Call4>: <Reg8: 10, Reg8: 5, Reg8: 3, Reg8: 7, Reg8: 2, Reg8: 6>
    r10 = globalThis.HermesInternal.concat.call(this, "Fetching ", param1, " failed with status ", r1.status)
    // LINE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r3 = globalThis.Error.prototype
    // LINE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
    // LINE → <Mov>: <Reg8: 11, Reg8: 3>
    r11 = r3
    // LINE → <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
    r2 = new globalThis.Error(" failed with status ", createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
    // LINE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = r3[r2]
    // LINE → <Throw>: <Reg8: 2>
    r2 = throw r3[r2]
    // ──────────────── Block 8 ──────────────── 
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 9, string_id: 229>  # String: 'text' (Identifier)
    // USED → r2 = r1.text
    // LINE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    // USED → r2 = await r1.text()
    // LINE → <SaveGenerator>: <Addr8: 4>  # Address: 00000099
    yield label_153;  // SaveGenerator: suspend and jump to 153
    // ──────────────── Block 9 ──────────────── 
    // LINE → <Ret>: <Reg8: 2>
    return await r1.text();
    // ──────────────── Block 10 ──────────────── 
    // LINE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    r2 = await yield
    // LINE → <JmpTrue>: <Addr8: 6, Reg8: 3>  # Address: 000000a2
    if (createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)) { /* jump to label_162 */ }
    // ──────────────── Block 11 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 2>
    return undefined_r2;
    // ──────────────── Block 12 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 2>
    return undefined_r2;
    // ──────────────── Block 13 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 1>
    return undefined_r1;
    // ──────────────── Block 14 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 0>
    return undefined_r0;
}