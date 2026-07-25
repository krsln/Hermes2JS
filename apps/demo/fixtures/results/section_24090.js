function onPress(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1)
    // CODE → <JmpTrue>: <Addr8: 113, Reg8: 2>  # Address: 0000007b
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 10>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 158>  # String: 'prototype' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    r8 = Identifier(name='r3')
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 11>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182>  # Object: {'message': 'You have joined the list', 'type': 'success'}
    // USED → r2 = {'message': 'You have joined the list', 'type': 'success'}
    // CODE → <Call2>: <Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 4>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 14996>  # String: 'setItem' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5555>  # String: 'compjoin' (String)
    // USED → r3 = "compjoin"
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 12320>  # String: 'true' (Identifier)
    // USED → r2 = "true"
    // CODE → <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 3>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 14155>  # String: 'goBack' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Jmp>: <Addr8: 32>  # Address: 00000099
    goto label_153;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <LoadConstUndefined>: <Reg8: 0>
        // USED → r0 = undefined
        // CODE → <Ret>: <Reg8: 0>
        ReturnStatement(argument=Identifier(name='r0'))
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 12>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 12341>  # String: 'open' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <NewObjectWithBuffer>: <Reg8: 0, UInt16: 4, UInt16: 4, UInt16: 11077, UInt16: 9225>  # Object: {'title': 'Join Coachify AI Competition', 'message': 'Join Coachify AI Competition', 'url': 'https://coachify.ai/download?ref=compshare', 'subject': 'Join Coachify AI Competition'}
        // USED → r0 = {'title': 'Join Coachify AI Competition', 'message': 'Join Coachify AI Competition', 'url': 'https://coachify.ai/download?ref=compshare', 'subject': 'Join Coachify AI Competition'}
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        // Error: sequence item 0: expected str instance, Identifier found
    }
    // LOOP → END
}