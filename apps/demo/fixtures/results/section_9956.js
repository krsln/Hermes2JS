async function* anon_9956(param0, param1) {
    // CODE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield; // Resume generator
    // CODE → <JmpTrue>: <Addr8: 57, Reg8: 1>  # Address: 0000003d
    if (r1) {
        // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 3>
        r1 = getEnvironment(3)
        // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
        r1 = r1[16]
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED → r3 = r1.default
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
        // USED → r2 = r1.default.get
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 7880>  # String: 'https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=' (String)
        // USED → r4 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr="
        // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
        // USED → r1 = param1
        // CODE → <Add>: <Reg8: 1, Reg8: 4, Reg8: 1>
        // USED → r1 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1
        // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
        // USED → r1 = await r1.default.get("https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1)
        // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000002c
        // await yield; // check: OpcodeDispatcher.dispatch_all // Resume at label_44
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // label_44:
        r1 = await yield; // Resume generator
        // CODE → <JmpTrue>: <Addr8: 11, Reg8: 2>  # Address: 0000003a
        if (r1.default.get) {
            // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'data' (Identifier)
            // USED → r2 = r1.data
            // CODE → <CompleteGenerator>: <>
            // CODE → <Ret>: <Reg8: 2>
            return r1.data;
        }
        // CODE → <CompleteGenerator>: <>
        // label_58:
        // CODE → <Ret>: <Reg8: 1>
        return undefined_r1;
    }
    // CODE → <CompleteGenerator>: <>
    // label_61:
    // CODE → <Ret>: <Reg8: 0>
    return undefined_r0;
}