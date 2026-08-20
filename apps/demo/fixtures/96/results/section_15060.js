function complexTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4573>  # String: '__BC:ControlFlow/ComplexTests/complexTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ComplexTests/complexTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 12, UInt16: 5, UInt16: 5, UInt16: 23616>  # Array: [1, 2, 3, 4, 5]
    r12 = [1, 2, 3, 4, 5]
    // CODE → addr: 30 | <GetByIdShort>: <Reg8: 1, Reg8: 12, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r1 = r12.length;
    // CODE → addr: 37 | <Less>: <Reg8: 1, Reg8: 11, Reg8: 1>
    // USED → r1 = 0 < r12.length;
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 10, string_id: 855>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-1' (String)
    // USED → r10 = "__BC:ControlFlow/ComplexTests/complexTest/case-1";
    // CODE → addr: 45 | <LoadConstString>: <Reg8: 9, string_id: 4563>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-2-continue' (String)
    // USED → r9 = "__BC:ControlFlow/ComplexTests/complexTest/case-2-continue";
    // CODE → addr: 49 | <LoadConstString>: <Reg8: 8, string_id: 4566>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-3' (String)
    // USED → r8 = "__BC:ControlFlow/ComplexTests/complexTest/case-3";
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 7, string_id: 11999>  # String: 'three' (Identifier)
    // USED → r7 = "three";
    // CODE → addr: 57 | <LoadConstString>: <Reg8: 6, string_id: 4567>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-default' (String)
    // USED → r6 = "__BC:ControlFlow/ComplexTests/complexTest/case-default";
    // CODE → addr: 61 | <LoadConstString>: <Reg8: 5, string_id: 1881>  # String: 'other' (String)
    // USED → r5 = "other";
    // CODE → addr: 65 | <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    // USED → r4 = 3;
    // CODE → addr: 68 | <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → addr: 71 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // → r12 = [1, 2, 3, 4, 5]
    if (0 < r12.length) {
        // LOOP → START (for)
        // → r1 = 0
        for (r11 = 0; r11 < r1; r11 = r1 + 1) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → addr: 80 | <GetByVal>: <Reg8: 13, Reg8: 12, Reg8: 11>
            r13 = r12[r11]
            // CODE → addr: 84 | <Mov>: <Reg8: 1, Reg8: 11>
            r1 = 0
            // Switch → START
            switch (r13) {
                case 1:
                    // ──────────────── Block 7 ──────────────── 
                    // CODE → addr:185 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:191 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:196 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 10>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-1")
                    break;
                case 2:
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → addr:167 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:173 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:178 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 9>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-2-continue")
                    break;
                case 3:
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → addr:133 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:139 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:144 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-3")
                    // CODE → addr:149 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:155 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:160 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 7>
                    console.log("three")
                    break;
                default:
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → addr: 99 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:105 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:110 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 6>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-default")
                    // CODE → addr:115 | <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → addr:121 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → addr:126 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 5>
                    console.log("other")
                    break;
            }
            // Switch → END
            // ──────────────── Block 8 ──────────────── 
            // CODE → addr:204 | <GetByIdShort>: <Reg8: 1, Reg8: 12, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
            r1 = r12.length
        }
        // LOOP → END
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:216 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:222 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:227 | <LoadConstString>: <Reg8: 0, string_id: 4570>  # String: '__BC:ControlFlow/ComplexTests/complexTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ComplexTests/complexTest/end";
    // CODE → addr:231 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/end")
    // CODE → addr:236 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:238 | <Ret>: <Reg8: 0>
    return undefined;
}