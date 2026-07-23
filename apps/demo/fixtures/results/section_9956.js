async function* anon_9956(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // LINE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield
    // LINE → <JmpTrue>: <Addr8: 57, Reg8: 1>  # Address: 0000003d
    if (r1) { /* jump to label_61 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <GetEnvironment>: <Reg8: 1, UInt8: 3>
    r1 = getEnvironment(3)
    // LINE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    r1 = r1[16]
    // LINE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r3 = r1.default
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // USED → r2 = r1.default.get
    // LINE → <LoadConstString>: <Reg8: 4, string_id: 7880>  # String: 'https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=' (String)
    // USED → r4 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr="
    // LINE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1
    // LINE → <Add>: <Reg8: 1, Reg8: 4, Reg8: 1>
    // USED → r1 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1
    // LINE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    // USED → r1 = await r1.default.get("https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1)
    // LINE → <SaveGenerator>: <Addr8: 4>  # Address: 0000002c
    yield label_44;  // SaveGenerator: suspend and jump to 44
    // ──────────────── Block 2 ──────────────── 
    // LINE → <Ret>: <Reg8: 1>
    return await r1.default.get("https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1);
    // ──────────────── Block 3 ──────────────── 
    // LINE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
    r1 = await yield
    // LINE → <JmpTrue>: <Addr8: 11, Reg8: 2>  # Address: 0000003a
    if (r1.default.get) { /* jump to label_58 */ }
    // ──────────────── Block 4 ──────────────── 
    // LINE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'data' (Identifier)
    // USED → r2 = r1.data
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 2>
    return r1.data;
    // ──────────────── Block 5 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 1>
    return undefined_r1;
    // ──────────────── Block 6 ──────────────── 
    // LINE → <CompleteGenerator>: <>
    // CompleteGenerator: No output needed
    // LINE → <Ret>: <Reg8: 0>
    return undefined_r0;
}