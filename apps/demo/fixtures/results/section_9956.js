async function* anon_9956(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield /* ResumeGenerator -> r0 */
    // CODE → <JmpTrue>: <Addr8: 57, Reg8: 1>  # Address: 0000003d
    if (r1) { /* jump to label_61 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 3>
    // USED → r1 = getEnvironment(3)
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
    // USED → r1 = r1[16]
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r3 = r1.default
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 137>  # String: 'get' (Identifier)
    // USED → r2 = r3.get
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 7880>  # String: 'https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=' (String)
    // USED → r4 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr="
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1
    // CODE → <Add>: <Reg8: 1, Reg8: 4, Reg8: 1>
    // USED → r1 = r4 + r1;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
     = await // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 0000002c
    yield label_44;
    // LOOP → START (while)
    while (r2) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <ResumeGenerator>: <Reg8: 1, Reg8: 2>
        // USED → r1 = await yield /* ResumeGenerator -> r1 */
        // CODE → <JmpTrue>: <Addr8: 11, Reg8: 2>  # Address: 0000003a
        if (r2) { /* jump to label_58 */ }
        // ──────────────── Block 2 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        // Unhandled opcode: Ret
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'data' (Identifier)
    r2 = r1.data
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 2>
    // Unhandled opcode: Ret
    // ──────────────── Block 5 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 1>
    // Unhandled opcode: Ret
    // ──────────────── Block 6 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}