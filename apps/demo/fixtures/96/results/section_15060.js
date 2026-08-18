function complexTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4573>  # String: '__BC:ControlFlow/ComplexTests/complexTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ComplexTests/complexTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 12, UInt16: 5, UInt16: 5, UInt16: 23616>  # Array: [1, 2, 3, 4, 5]
    r12 = [1, 2, 3, 4, 5]
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 12, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r1 = r12.length;
    // CODE → <Less>: <Reg8: 1, Reg8: 11, Reg8: 1>
    // USED → r1 = 0 < r12.length;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 855>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-1' (String)
    // USED → r10 = "__BC:ControlFlow/ComplexTests/complexTest/case-1";
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 4563>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-2-continue' (String)
    // USED → r9 = "__BC:ControlFlow/ComplexTests/complexTest/case-2-continue";
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4566>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-3' (String)
    // USED → r8 = "__BC:ControlFlow/ComplexTests/complexTest/case-3";
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 11999>  # String: 'three' (Identifier)
    // USED → r7 = "three";
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4567>  # String: '__BC:ControlFlow/ComplexTests/complexTest/case-default' (String)
    // USED → r6 = "__BC:ControlFlow/ComplexTests/complexTest/case-default";
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 1881>  # String: 'other' (String)
    // USED → r5 = "other";
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 3>
    // USED → r4 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 2>
    // USED → r3 = 2;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // → r12 = [1, 2, 3, 4, 5]
    if (0 < r12.length) {
        // LOOP → START (for)
        // → r1 = 0
        for (r11 = 0; r11 < r1; r1 = r12.length) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <GetByVal>: <Reg8: 13, Reg8: 12, Reg8: 11>
            r13 = r12[r11]
            // CODE → <Mov>: <Reg8: 1, Reg8: 11>
            r1 = 0
            // Switch → START
            switch (r13) {
                case 1:
                    // ──────────────── Block 7 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 10>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-1")
                    break;
                case 2:
                    // ──────────────── Block 6 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 9>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-2-continue")
                    break;
                case 3:
                    // ──────────────── Block 5 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-3")
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 7>
                    console.log("three")
                    break;
                default:
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 6>
                    console.log("__BC:ControlFlow/ComplexTests/complexTest/case-default")
                    // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                    // USED → r14 = console;
                    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                    // USED → r13 = console.log;
                    // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 5>
                    console.log("other")
                    break;
            }
            // Switch → END
            // ──────────────── Block 8 ──────────────── 
            // CODE → <Inc>: <Reg8: 11, Reg8: 1>
            r11 = r1 + 1
        }
        // LOOP → END
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4570>  # String: '__BC:ControlFlow/ComplexTests/complexTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ComplexTests/complexTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/ComplexTests/complexTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}