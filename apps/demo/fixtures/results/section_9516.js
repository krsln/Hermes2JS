function legacyArgumentsTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 4>
    // USED → r4 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:  4 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:  6 | <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 12 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 6, string_id: 4953>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/start' (String)
    // USED → r6 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/start";
    // CODE → addr: 21 | <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/start")
    // CODE → addr: 26 | <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 32 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 37 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = undefined
    // CODE → addr: 40 | <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
    r6 = arguments.length
    // CODE → addr: 43 | <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
    console.log(r6)
    // CODE → addr: 48 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = undefined
    // CODE → addr: 51 | <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
    // USED → r6 = arguments.length;
    // CODE → addr: 54 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 56 | <Less>: <Reg8: 3, Reg8: 0, Reg8: 6>
    // USED → r3 = 0 < arguments.length;
    // CODE → addr: 60 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    if (0 < arguments.length) {
        // LOOP → START (do_while)
        do {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 66 | <TryGetById>: <Reg8: 9, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r9 = console;
            // CODE → addr: 72 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r8 = console.log;
            // CODE → addr: 77 | <GetArgumentsPropByValStrict>: <Reg8: 6, Reg8: 0, Reg8: 7>
            r6 = arguments[0]
            // CODE → addr: 81 | <Call2>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 6>
            console.log(r6)
            // CODE → addr: 86 | <AddN>: <Reg8: 0, Reg8: 0, Reg8: 1>
            r0 = r0 + 1
            // CODE → addr: 90 | <Mov>: <Reg8: 6, Reg8: 7>
            r6 = undefined
            // CODE → addr: 93 | <GetArgumentsLength>: <Reg8: 6, Reg8: 6>
            r6 = arguments.length
        // → r0 = r0 + 1; r6 = arguments.length
        } while (r0 < r6);
        // LOOP → END
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:100 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:106 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:111 | <LoadConstString>: <Reg8: 5, string_id: 4952>  # String: '__BC:Functions/RestParameterTests/legacyArgumentsTest/end' (String)
    // USED → r5 = "__BC:Functions/RestParameterTests/legacyArgumentsTest/end";
    // CODE → addr:115 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/end")
    // CODE → addr:120 | <Ret>: <Reg8: 4>
    return undefined;
}