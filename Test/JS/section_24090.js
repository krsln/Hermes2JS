function onPress(param0) {
    // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0);
    // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2 = r1[0]
    // CODE -> <GetEnvironment>: <Reg8: 0, UInt8: 1>
    r0 = getEnvironment(1);
    // CODE -> <JmpTrue>: <Addr8: 113, Reg8: 2>  # Address: 0000007b
    if (r2) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 10>
        r2 = r0[10]
        // CODE -> <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r2 = r2.default
        // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 158>  # String: 'prototype' (Identifier)
        r3 = r2.default.prototype
        // CODE -> <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
        r3 = createThis(r3, r2);
        // CODE -> <Mov>: <Reg8: 8, Reg8: 3>
        r8 = r3;
        // CODE -> <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
        r2 = new r2.default(arg0);
        // CODE -> <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
        // USED -> r3 = r3[r2]
        // CODE -> <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 21914>  # String: 'trackJoinCompetitionList' (Identifier)
        // USED -> r2 = r3[r2].trackJoinCompetitionList
        // CODE -> <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
        r2 = r3[r2].trackJoinCompetitionList()
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 11>
        r2 = r0[11]
        // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r4 = r2.default
        // CODE -> <LoadConstUndefined>: <Reg8: 3>
        // USED -> r3 = undefined
        // CODE -> <NewObjectWithBuffer>: <Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182>  # Object: {'message': 'You have joined the list', 'type': 'success'}
        // USED -> r2 = { message: "You have joined the list", type: "success" }
        // CODE -> <Call2>: <Reg8: 2, Reg8: 4, Reg8: 3, Reg8: 2>
        r2 = r2.default({ message: "You have joined the list", type: "success" })
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 4>
        r2 = r0[4]
        // CODE -> <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r5 = r2.default
        // CODE -> <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 14996>  # String: 'setItem' (Identifier)
        // USED -> r4 = r2.default.setItem
        // CODE -> <LoadConstString>: <Reg8: 3, string_id: 5555>  # String: 'compjoin' (String)
        // USED -> r3 = "compjoin"
        // CODE -> <LoadConstString>: <Reg8: 2, string_id: 12320>  # String: 'true' (Identifier)
        // USED -> r2 = "true"
        // CODE -> <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 2>
        r2 = r2.default.setItem("compjoin", "true")
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 3>
        r2 = r1[3]
        // CODE -> <GetById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 14155>  # String: 'goBack' (Identifier)
        // USED -> r1 = r2.goBack
        // CODE -> <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
        r1 = r2.goBack()
        // CODE -> <Jmp>: <Addr8: 32>  # Address: 00000099
        goto label_153;
    }
    // CODE -> <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 12>
    // label_123:
    r0 = r0[12]
    // CODE -> <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED -> r2 = r0.default
    // CODE -> <GetById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 12341>  # String: 'open' (Identifier)
    // USED -> r1 = r0.default.open
    // CODE -> <NewObjectWithBuffer>: <Reg8: 0, UInt16: 4, UInt16: 4, UInt16: 11077, UInt16: 9225>  # Object: {'title': 'Join Coachify AI Competition', 'message': 'Join Coachify AI Competition', 'url': 'https://coachify.ai/download?ref=compshare', 'subject': 'Join Coachify AI Competition'}
    // USED -> r0 = { title: "Join Coachify AI Competition", message: "Join Coachify AI Competition", url: "https://coachify.ai/download?ref=compshare", subject: "Join Coachify AI Competition" }
    // CODE -> <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = r0.default.open({ title: "Join Coachify AI Competition", message: "Join Coachify AI Competition", url: "https://coachify.ai/download?ref=compshare", subject: "Join Coachify AI Competition" })
    // CODE -> <LoadConstUndefined>: <Reg8: 0>
    // label_153:
    // USED -> r0 = undefined
    // CODE -> <Ret>: <Reg8: 0>
    return undefined;
}