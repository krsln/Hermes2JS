async function* anon_17161(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    // USED → r7 = param1
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    // USED → r0 = await yield /* ResumeGenerator -> r0 */
    // CODE → <JmpTrueLong>: <Addr32: 161, Reg8: 1>  # Address: 000000a8
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 13438>  # String: 'fetch' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 7>
     = await // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000020
    yield label_32;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    ReturnStatement(argument=Identifier(name='r1'))
    // ──────────────── Block 2 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 3>
    // USED → r1 = await yield /* ResumeGenerator -> r1 */
    // CODE → <JmpTrueLong>: <Addr32: 130, Reg8: 3>  # Address: 000000a5
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 14168>  # String: 'ok' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <JmpTrue>: <Addr8: 93, Reg8: 3>  # Address: 0000008c
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0
    // CODE → <JStrictNotEqual>: <Addr8: 22, Reg8: 4, Reg8: 3>  # Address: 00000050
    if (Identifier(name='r4') !== Identifier(name='r3')) { /* jump to label_80 */ }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 19693>  # String: 'startsWith' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 1058>  # String: 'file://' (String)
    // USED → r3 = "file://"
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 3>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <JmpTrue>: <Addr8: 63, Reg8: 3>  # Address: 0000008c
    // Error: 'Identifier' object has no attribute 'render'
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 14>  # String: 'Error' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 6, Reg8: 1, UInt8: 3, string_id: 12514>  # String: 'status' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 6, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 7, string_id: 98>  # String: 'concat' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 2430>  # String: 'Fetching ' (String)
    // USED → r3 = "Fetching "
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: ' failed with status ' (String)
    // USED → r2 = " failed with status "
    // CODE → <Call4>: <Reg8: 10, Reg8: 5, Reg8: 3, Reg8: 7, Reg8: 2, Reg8: 6>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 158>  # String: 'prototype' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 11, Reg8: 3>
    r11 = Identifier(name='r3')
    // CODE → <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Throw>: <Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 9, string_id: 229>  # String: 'text' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
     = await // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000099
    yield label_153;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Ret>: <Reg8: 2>
    ReturnStatement(argument=Identifier(name='r2'))
    // ──────────────── Block 6 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 2, Reg8: 3>
    // USED → r2 = await yield /* ResumeGenerator -> r2 */
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 3>  # Address: 000000a2
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    ReturnStatement(argument=Identifier(name='r2'))
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    ReturnStatement(argument=Identifier(name='r2'))
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    ReturnStatement(argument=Identifier(name='r1'))
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}