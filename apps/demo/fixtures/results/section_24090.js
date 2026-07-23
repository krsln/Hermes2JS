function onPress(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    // USED → r2 = getEnvironment(0)[0]
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1)
    // CODE → <JmpTrue>: <Addr8: 113, Reg8: 2>  # Address: 0000007b
    if (getEnvironment(0)[0]) { /* jump to label_123 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 10>
    // USED → r2 = getEnvironment(1)[10]
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r2 = r2.default
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r3 = r2.default.prototype
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = createThis(prototype=r2.default.prototype, constructor=r2.default)
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    r8 = createThis(prototype=r2.default.prototype, constructor=r2.default)
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    r2 = new r2.default(getEnvironment(0))
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = r3[r2]
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
    // USED → r2 = r3.trackJoinCompetitionList
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.trackJoinCompetitionList()
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 11>
    // USED → r2 = getEnvironment(1)[11]
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r4 = r2.default
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined
    // CODE → <NewObjectWithBuffer>: <Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182>  # Object: {'message': 'You have joined the list', 'type': 'success'}
    // USED → r2 = { message: "You have joined the list", type: "success" }
    // CODE → <Call2>: <Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 2>
    r2 = r2.default()
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 4>
    // USED → r2 = getEnvironment(1)[4]
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r5 = r2.default
    // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 14996>  # String: 'setItem' (Identifier)
    // USED → r4 = r2.default.setItem
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5555>  # String: 'compjoin' (String)
    // USED → r3 = "compjoin"
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 12320>  # String: 'true' (Identifier)
    // USED → r2 = "true"
    // CODE → <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
    r2 = r2.default.setItem("compjoin", "true")
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 3>
    // USED → r2 = getEnvironment(0)[3]
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 14155>  # String: 'goBack' (Identifier)
    // USED → r1 = r2.goBack
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r2.goBack()
    // CODE → <Jmp>: <Addr8: 32>  # Address: 00000099
    goto label_153;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 12>
    // USED → r0 = getEnvironment(1)[12]
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r2 = r0.default
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 12341>  # String: 'open' (Identifier)
    // USED → r1 = r0.default.open
    // CODE → <NewObjectWithBuffer>: <Reg8: 0, UInt16: 4, UInt16: 4, UInt16: 11077, UInt16: 9225>  # Object: {'title': 'Join Coachify AI Competition', 'message': 'Join Coachify AI Competition', 'url': 'https://coachify.ai/download?ref=compshare', 'subject': 'Join Coachify AI Competition'}
    // USED → r0 = { title: "Join Coachify AI Competition", message: "Join Coachify AI Competition", url: "https://coachify.ai/download?ref=compshare", subject: "Join Coachify AI Competition" }
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = r0.default.open(r0)
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}