async function* anon_11947(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    // USED → r0 = await yield /* ResumeGenerator -> r0 */
    // CODE → <JmpTrueLong>: <Addr32: 311, Reg8: 5>  # Address: 0000013e
    // Error: 'Identifier' object has no attribute 'render'
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
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 4, Reg8: 3>
     = await // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000029
    yield label_41;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Ret>: <Reg8: 3>
    ReturnStatement(argument=Identifier(name='r3'))
    // ──────────────── Block 2 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r3 = await yield /* ResumeGenerator -> r3 */
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 00000032
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    ReturnStatement(argument=Identifier(name='r3'))
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    ReturnStatement(argument=Identifier(name='r3'))
    // CODE → <Catch>: <Reg8: 7>
    // USED → r7 = caughtException
    // CODE → <Mov>: <Reg8: 1, Reg8: 7>
    // USED → r1 = Identifier(name='r7')
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <InstanceOf>: <Reg8: 4, Reg8: 7, Reg8: 4>
    // USED → r4 = BinaryExpression(left=Identifier(name='r7'), operator=<BinaryOperator.INSTANCEOF: 'instanceof'>, right=Identifier(name='r4'))
    // CODE → <JmpFalseLong>: <Addr32: 246, Reg8: 4>  # Address: 0000013c
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  }
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <JmpTrue>: <Addr8: 25, Reg8: 4>  # Address: 00000079
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 4, string_id: 158>  # String: 'prototype' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CreateThis>: <Reg8: 7, Reg8: 4, Reg8: 8>
    // Error: 'BinaryExpression' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = Identifier(name='r7')
    // CODE → <Construct>: <Reg8: 4, Reg8: 8, UInt8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Jmp>: <Addr8: 16>  # Address: 00000087
    goto label_135;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 4 ──────────────── 
        // CODE → <Mov>: <Reg8: 4, Reg8: 6>
        // USED → r4 = Identifier(name='r6')
        // CODE → <GetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstString>: <Reg8: 8, string_id: 11303>  # String: '' (Identifier)
        // USED → r8 = ""
        // CODE → <Mov>: <Reg8: 4, Reg8: 8>
        // USED → r4 = Identifier(name='r8')
        // CODE → <JmpFalse>: <Addr8: 34, Reg8: 7>  # Address: 000000b9
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 9, Reg8: 6, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CreateRegExp>: <Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168>  # String: '^.+\\n' (String)  # String: '' (Identifier)
        // USED → r6 = /^.+\\n/
        // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 9, Reg8: 6, Reg8: 8>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <Mov>: <Reg8: 2, Reg8: 4>
        // USED → r2 = Identifier(name='r8')
        // CODE → <Mov>: <Reg8: 4, Reg8: 1>
        // USED → r4 = Identifier(name='r7')
        // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpTrue>: <Addr8: 17, Reg8: 4>  # Address: 000000d6
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 6, Reg8: 1>
        // USED → r6 = Identifier(name='r7')
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        // USED → r4 = Identifier(name='r8')
        // CODE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Jmp>: <Addr8: 100>  # Address: 00000138
        goto label_312;
        // ──────────────── Block 3 ──────────────── 
        // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 4, Reg8: 6>
        // USED → r4 = Identifier(name='r6')
        // CODE → <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
        // Error: sequence item 0: expected str instance, Identifier found
    }
    // LOOP → END
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 6 ──────────────── 
        // CODE → <Jmp>: <Addr8: 4>  # Address: 0000013c
        goto label_316;
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Mov>: <Reg8: 4, Reg8: 2>
        // USED → r4 = Identifier(name='r8')
        // CODE → <JmpFalse>: <Addr8: 95, Reg8: 4>  # Address: 00000138
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 7, string_id: 50>  # String: 'String' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 3, Reg8: 1>
        // USED → r3 = Identifier(name='r7')
        // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 8, string_id: 19080>  # String: 'endsWith' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 7, Reg8: 2>
        // USED → r7 = Identifier(name='r8')
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CreateRegExp>: <Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169>  # String: '^.+\\n.+\\n' (String)  # String: '' (Identifier)
        // USED → r3 = /^.+\\n.+\\n/
        // CODE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 8>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <JmpTrue>: <Addr8: 33, Reg8: 3>  # Address: 00000138
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 3, Reg8: 1>
        // USED → r3 = Identifier(name='r7')
        // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        // USED → r5 = Identifier(name='r8')
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 12321>  # String: '\n' (Identifier)
        // USED → r2 = "\\n"
        // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 5>
        // USED → r2 = BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r8'))
        // CODE → <Add>: <Reg8: 2, Reg8: 4, Reg8: 2>
        // USED → r2 = BinaryExpression(left=Identifier(name='r8'), operator=<BinaryOperator.ADD: '+'>, right=BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r8')))
        // CODE → <PutById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
    }
    // LOOP → END
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <Throw>: <Reg8: 1>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CompleteGenerator>: <>
        // CompleteGenerator
        // CODE → <Ret>: <Reg8: 0>
        ReturnStatement(argument=Identifier(name='r0'))
        // ──────────────── Block 7 ──────────────── 
        // CODE → <Catch>: <Reg8: 2>
        r2 = caughtException
    }
    // LOOP → END
}