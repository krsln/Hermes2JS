function complexTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4573>  # String: '__BC:ControlFlow/ComplexTests/complexTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ComplexTests/complexTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 12, UInt16: 5, UInt16: 5, UInt16: 23616>  # Array: [1, 2, 3, 4, 5]
    // USED → r12 = [1, 2, 3, 4, 5];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 12, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r1 = [1, 2, 3, 4, 5].length;
    // CODE → <LoadConstZero>: <Reg8: 11>
    // USED → r11 = 0;
    // CODE → <Less>: <Reg8: 1, Reg8: 11, Reg8: 1>
    // USED → r1 = 0 < [1, 2, 3, 4, 5].length;
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
    if (0 < [1, 2, 3, 4, 5].length) {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <GetByVal>: <Reg8: 13, Reg8: 12, Reg8: 11>
            // USED → r13 = [1, 2, 3, 4, 5][0];
            // CODE → <Mov>: <Reg8: 1, Reg8: 11>
            // USED → r1 = 0;
            if (1 !== [1, 2, 3, 4, 5][0]) {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <JStrictEqual>: <Addr8: 76, Reg8: 3, Reg8: 13>  # Address: 000000a7
                if (2 === [1, 2, 3, 4, 5][0]) goto label_167;
                // ──────────────── Block 3 ──────────────── 
                // CODE → <JStrictEqual>: <Addr8: 38, Reg8: 4, Reg8: 13>  # Address: 00000085
                if (3 === [1, 2, 3, 4, 5][0]) goto label_133;
                // ──────────────── Block 4 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 6>
                r13 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/case-default")
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 5>
                r13 = globalThis.console.log("other")
                // CODE → <Jmp>: <Addr8: 70>  # Address: 000000c9
                goto label_201;
                // ──────────────── Block 5 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
                r13 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/case-3")
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 7>
                r13 = globalThis.console.log("three")
                // CODE → <Jmp>: <Addr8: 36>  # Address: 000000c9
                goto label_201;
                // ──────────────── Block 6 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 9>
                r13 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/case-2-continue")
                // CODE → <Jmp>: <Addr8: 18>  # Address: 000000c9
                goto label_201;
                // ──────────────── Block 7 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 14, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
                // USED → r14 = globalThis.console;
                // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
                // USED → r13 = globalThis.console.log;
                // CODE → <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 10>
                r13 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/case-1")
                // ──────────────── Block 8 ──────────────── 
                // CODE → <Inc>: <Reg8: 11, Reg8: 1>
                // USED → r11 = 0 + 1;
                // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 12, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
                // USED → r1 = [1, 2, 3, 4, 5].length;
                // CODE → <JLessLong>: <Addr32: -129, Reg8: 11, Reg8: 1>  # Address: 00000050
                if (0 + 1 < [1, 2, 3, 4, 5].length) goto label_80;
            }
        }
        // LOOP → END
    }
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4570>  # String: '__BC:ControlFlow/ComplexTests/complexTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ComplexTests/complexTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:ControlFlow/ComplexTests/complexTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}