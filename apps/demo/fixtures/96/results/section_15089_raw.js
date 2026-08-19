function loopBreakCrossesTryBoundaryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <Mov>: <Reg8: 8, Reg8: 2>
    // USED → r8 = param1;
    // CODE → addr:  6 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:  8 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 3, string_id: 4656>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start")
    // CODE → addr: 32 | <LoadConstZero>: <Reg8: 7>
    // USED → r7 = 0;
    // CODE → addr: 34 | <LoadConstZero>: <Reg8: 9>
    // USED → r9 = 0;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r2 = r2.length
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 3, string_id: 4653>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally' (String)
    // USED → r3 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally";
    // CODE → addr: 45 | <LoadConstString>: <Reg8: 6, string_id: 4650>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue' (String)
    // USED → r6 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue";
    // CODE → addr: 49 | <LoadConstString>: <Reg8: 5, string_id: 4655>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item";
    // CODE → addr: 53 | <JNotLessLong>: <Addr32: 171, Reg8: 7, Reg8: 2>  # Address: 000000e0
    // → r2 = r2.length
    if (!(0 < r2)) goto label_224;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 60 | <Mov>: <Reg8: 4, Reg8: 8>
    // USED → r4 = param1;
    // CODE → addr: 63 | <Mov>: <Reg8: 2, Reg8: 9>
    r2 = 0
    // CODE → addr: 66 | <GetByVal>: <Reg8: 2, Reg8: 4, Reg8: 2>
    r2 = param1[r2]
    // CODE → addr: 70 | <JLess>: <Addr8: 118, Reg8: 2, Reg8: 7>  # Address: 000000bc
    // → r2 = param1[r2]
    if (r2 < 0) goto label_188;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 74 | <Mov>: <Reg8: 4, Reg8: 8>
    // USED → r4 = param1;
    // CODE → addr: 77 | <Mov>: <Reg8: 2, Reg8: 9>
    r2 = 0
    // CODE → addr: 80 | <GetByVal>: <Reg8: 2, Reg8: 4, Reg8: 2>
    r2 = param1[r2]
    // CODE → addr: 84 | <JStrictEqual>: <Addr8: 49, Reg8: 2, Reg8: 7>  # Address: 00000085
    // → r2 = param1[r2]
    if (r2 === 0) goto label_133;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 88 | <TryGetById>: <Reg8: 10, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr: 94 | <GetByIdShort>: <Reg8: 4, Reg8: 10, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 99 | <Mov>: <Reg8: 11, Reg8: 8>
    // USED → r11 = param1;
    // CODE → addr:102 | <Mov>: <Reg8: 2, Reg8: 9>
    r2 = 0
    // CODE → addr:105 | <GetByVal>: <Reg8: 2, Reg8: 11, Reg8: 2>
    // USED → r2 = param1[r2];
    // CODE → addr:109 | <Call3>: <Reg8: 2, Reg8: 4, Reg8: 10, Reg8: 5, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item", r2)
    // CODE → addr:115 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:126 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // CODE → addr:131 | <Jmp>: <Addr8: 34>  # Address: 000000a5
    goto label_165;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:133 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:139 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:144 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 4, Reg8: 6>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue")
    // CODE → addr:149 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:155 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:160 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:165 | <Mov>: <Reg8: 2, Reg8: 9>
    r2 = 0
    // CODE → addr:168 | <Inc>: <Reg8: 4, Reg8: 2>
    // USED → r4 = r2 + 1;
    // CODE → addr:171 | <Mov>: <Reg8: 9, Reg8: 4>
    r9 = r2 + 1
    // CODE → addr:174 | <Mov>: <Reg8: 2, Reg8: 8>
    r2 = param1
    // CODE → addr:177 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    r2 = r2.length
    // CODE → addr:182 | <JLess>: <Addr8: -122, Reg8: 4, Reg8: 2>  # Address: 0000003c
    // → r2 = r2.length; r4 = r2 + 1
    if (r4 < r2) goto label_60;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:186 | <Jmp>: <Addr8: 38>  # Address: 000000e0
    goto label_224;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:188 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:194 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:199 | <LoadConstString>: <Reg8: 2, string_id: 4648>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break";
    // CODE → addr:203 | <Call2>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break")
    // CODE → addr:208 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:214 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:219 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 4, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:224 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:230 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:235 | <LoadConstString>: <Reg8: 2, string_id: 4652>  # String: '__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end' (String)
    // USED → r2 = "__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end";
    // CODE → addr:239 | <Call2>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 2>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end")
    // CODE → addr:244 | <Ret>: <Reg8: 0>
    return undefined;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:246 | <Catch>: <Reg8: 0>
    // USED → r0 = caughtException;
    // CODE → addr:248 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:254 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:259 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally")
    // CODE → addr:264 | <Throw>: <Reg8: 0>
    throw caughtException;
}