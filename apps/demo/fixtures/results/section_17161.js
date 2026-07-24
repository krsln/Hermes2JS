async function* anon_17161(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield /* ResumeGenerator -> r0 */
    // CODE → <JmpTrueLong>: <Addr32: 161, Reg8: 1>  # Address: 000000a8
    if (r1) { /* jump to label_168 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 13438>  # String: 'fetch' (Identifier)
    // USED → r3 = r2.fetch
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 7>
    // USED → r1 = await r2.fetch(undefined, r7)
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000020
    yield label_32;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield /* ResumeGenerator -> r1 */
    // CODE → <JmpTrueLong>: <Addr32: 130, Reg8: 3>  # Address: 000000a5
    if (r2.fetch) { /* jump to label_165 */ }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 14168>  # String: 'ok' (Identifier)
    // USED → r3 = await yield /* ResumeGenerator -> r1 */.ok
    // CODE → <JmpTrue>: <Addr8: 93, Reg8: 3>  # Address: 0000008c
    if (await yield /* ResumeGenerator -> r1 */.ok) { /* jump to label_140 */ }
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r4 = await yield /* ResumeGenerator -> r1 */.status
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0
    // CODE → <JStrictNotEqual>: <Addr8: 22, Reg8: 4, Reg8: 3>  # Address: 00000050
    if (await yield /* ResumeGenerator -> r1 */.status !== 0) { /* jump to label_80 */ }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 19693>  # String: 'startsWith' (Identifier)
    // USED → r4 = r7.startsWith
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1058>  # String: 'file://' (String)
    // USED → r3 = "file://"
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    // USED → r3 = r7.startsWith(r7, "file://")
    // CODE → <JmpTrue>: <Addr8: 63, Reg8: 3>  # Address: 0000008c
    if (r7.startsWith(r7, "file://")) { /* jump to label_140 */ }
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = r2.Error
    // CODE → <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // USED → r6 = await yield /* ResumeGenerator -> r1 */.status
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 6, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r2 = r2.HermesInternal
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 7, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r5 = r2.HermesInternal.concat
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 2430>  # String: 'Fetching ' (String)
    // USED → r3 = "Fetching "
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: ' failed with status ' (String)
    // USED → r2 = " failed with status "
    // CODE → <Call4>: <Reg8: 10, Reg8: 5, Reg8: 3, Reg8: 7, Reg8: 2, Reg8: 6>
    r10 = r2.HermesInternal.concat("Fetching ", r7, " failed with status ", await yield /* ResumeGenerator -> r1 */.status)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r3 = r2.Error.prototype
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // USED → r3 = createThis(prototype=r2.Error.prototype, constructor=r2.Error)
    // CODE → <Mov>: <Reg8: 11, Reg8: 3>
    r11 = createThis(prototype=r2.Error.prototype, constructor=r2.Error)
    // CODE → <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
    r2 = new r2.Error(" failed with status ", createThis(prototype=r2.Error.prototype, constructor=r2.Error))
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = r3[r2]
    // CODE → <Throw>: <Reg8: 2>
    throw r2;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 9, string_id: 229>  # String: 'text' (Identifier)
    // USED → r2 = await yield /* ResumeGenerator -> r1 */.text
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
    // USED → r2 = await await yield /* ResumeGenerator -> r1 */.text(await yield /* ResumeGenerator -> r1 */)
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000099
    yield label_153;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    // USED → r2 = await yield /* ResumeGenerator -> r2 */
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 3>  # Address: 000000a2
    if (createThis(prototype=r2.Error.prototype, constructor=r2.Error)) { /* jump to label_162 */ }
    // ──────────────── Block 11 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    return await yield /* ResumeGenerator -> r2 */;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    return await yield /* ResumeGenerator -> r2 */;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    return await yield /* ResumeGenerator -> r1 */;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield /* ResumeGenerator -> r0 */;
}