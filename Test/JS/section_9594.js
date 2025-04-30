async function* anon_9594(param0, param1) {
    // CODE -> <StartGenerator>: <>
    // CODE -> <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield; // Resume generator
    // CODE -> <JmpTrue>: <Addr8: 98, Reg8: 1>  # Address: 00000066
    label_4:
    if (r1) {
        // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 4>
        r1 = getEnvironment(4);
        // CODE -> <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
        r1 = r1[16]
        // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r4 = r1.default
        // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
        // USED -> r3 = r1.default.get
        // CODE -> <GetGlobalObject>: <Reg8: 2>
        // USED -> r2 = this
        // CODE -> <TryGetById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 21>  # String: 'HermesInternal' (Identifier)
        // USED -> r1 = this.HermesInternal
        // CODE -> <GetByIdShort>: <Reg8: 6, Reg8: 1, UInt8: 4, string_id: 98>  # String: 'concat' (Identifier)
        // USED -> r6 = this.HermesInternal.concat
        // CODE -> <LoadConstString>: <Reg8: 5, string_id: 8724>  # String: 'https://coachify.ai/api/checkUsernameAvailable?username=' (String)
        // USED -> r5 = "https://coachify.ai/api/checkUsernameAvailable?username="
        // CODE -> <LoadParam>: <Reg8: 1, UInt8: 1>
        // USED -> r1 = param1
        // CODE -> <Call2>: <Reg8: 1, Reg8: 6, Reg8: 5, Reg8: 1>
        r1 = this.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1)
        // CODE -> <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
        r1 = r1.default.get.call(this, r1.default, r1)
        // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 0000003a
        await yield; // Resume at label_4
        // CODE -> <Ret>: <Reg8: 1>
        return r1;
        // CODE -> <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        r1 = await yield; // Resume generator
        // CODE -> <JmpTrue>: <Addr8: 38, Reg8: 3>  # Address: 00000063
        if (r1.default.get) {
            // CODE -> <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
            // USED -> r4 = this.console
            // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 6, string_id: 171>  # String: 'log' (Identifier)
            // USED -> r3 = this.console.log
            // CODE -> <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
            // USED -> r2 = r1.data
            // CODE -> <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
            r2 = this.console.log(r1.data)
            // CODE -> <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 7, string_id: 107>  # String: 'data' (Identifier)
            // USED -> r2 = r1.data
            // CODE -> <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12563>  # String: 'available' (Identifier)
            // USED -> r2 = r1.data.available
            // CODE -> <CompleteGenerator>: <>
            // CODE -> <Ret>: <Reg8: 2>
            return r1.data.available;
            // CODE -> <CompleteGenerator>: <>
        }
        label_99:
        // CODE -> <Ret>: <Reg8: 1>
        return r1;
        // CODE -> <CompleteGenerator>: <>
    }
    label_102:
    // CODE -> <Ret>: <Reg8: 0>
    return r0;
}