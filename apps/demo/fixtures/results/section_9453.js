function complexTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 6>
    // USED → r6 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 9, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 7, string_id: 4754>  # String: '__BC:ControlFlow/ComplexTests/complexTest/start' (String)
    // USED → r7 = "__BC:ControlFlow/ComplexTests/complexTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 14, UInt16: 5, UInt16: 5, UInt16: 4497>  # Array: [1, 2, 3, 4, 5]
    r14 = [1, 2, 3, 4, 5]
    // CODE → addr: 30 | <GetByIdShort>: <Reg8: 7, Reg8: 14, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r7 = r14.length;
    // CODE → addr: 37 | <Less>: <Reg8: 5, Reg8: 0, Reg8: 7>
    // USED → r5 = 0 < r14.length;
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr: 44 | <LoadConstString>: <Reg8: 13, string_id: 1718>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-1' (String)
    // USED → r13 = "__BC:ControlFlow/ComplexTests/complexTest/case-1";
    // CODE → addr: 48 | <LoadConstString>: <Reg8: 12, string_id: 783>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-2-continue' (String)
    // USED → r12 = "__BC:ControlFlow/ComplexTests/complexTest/case-2-continue";
    // CODE → addr: 52 | <LoadConstString>: <Reg8: 11, string_id: 4747>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-3' (String)
    // USED → r11 = "__BC:ControlFlow/ComplexTests/complexTest/case-3";
    // CODE → addr: 56 | <LoadConstString>: <Reg8: 10, string_id: 10340>  # String: 'three' (Identifier)
    // USED → r10 = "three";
    // CODE → addr: 60 | <LoadConstString>: <Reg8: 9, string_id: 4748>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-default' (String)
    // USED → r9 = "__BC:ControlFlow/ComplexTests/complexTest/case-default";
    // CODE → addr: 64 | <LoadConstString>: <Reg8: 8, string_id: 1861>  # String: 'other' (String)
    // USED → r8 = "other";
    // CODE → addr: 68 | <LoadConstUInt8>: <Reg8: 3, UInt8: 3>
    // USED → r3 = 3;
    // CODE → addr: 71 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // → r14 = [1, 2, 3, 4, 5]
    if (0 < r14.length) {
        // LOOP → START (for)
        // → r7 = r14[r0]
        for (r0 = 0; r0 < r7; r0 = r0 + 1) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 80 | <GetByVal>: <Reg8: 7, Reg8: 14, Reg8: 0>
            r7 = r14[r0]
            // Switch → START
            switch (r7) {
                case 1:
                    // ──────────────── Block 7 ──────────────── 
                    // CODE → addr:185 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:191 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:196 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 13>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-1")
                    break;
                case 2:
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → addr:167 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:173 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:178 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 12>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-2-continue")
                    break;
                case 3:
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → addr:133 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:139 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:144 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 11>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-3")
                    // CODE → addr:149 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:155 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:160 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 10>
                    console.log("three")
                    break;
                default:
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → addr: 99 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:105 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:110 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 9>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-default")
                    // CODE → addr:115 | <TryGetById>: <Reg8: 15, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r15 = console;
                    // CODE → addr:121 | <GetByIdShort>: <Reg8: 7, Reg8: 15, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r7 = console.log;
                    // CODE → addr:126 | <Call2>: <Reg8: 7, Reg8: 7, Reg8: 15, Reg8: 8>
                    console.log("other")
                    break;
            }
            // Switch → END
            // ──────────────── Block 8 ──────────────── 
            // CODE → addr:205 | <GetByIdShort>: <Reg8: 7, Reg8: 14, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
            r7 = r14.length
        }
        // LOOP → END
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:217 | <TryGetById>: <Reg8: 8, Reg8: 6, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:223 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:228 | <LoadConstString>: <Reg8: 6, string_id: 4751>  # String: '__BC:ControlFlow/ComplexTests/complexTest/end' (String)
    // USED → r6 = "__BC:ControlFlow/ComplexTests/complexTest/end";
    // CODE → addr:232 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/end")
    // CODE → addr:237 | <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined;
    // CODE → addr:239 | <Ret>: <Reg8: 5>
    return undefined;
}