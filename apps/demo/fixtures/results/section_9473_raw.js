function tryCatchInsideLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 0, string_id: 4879>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start")
    // CODE → addr: 25 | <GetByIdShort>: <Reg8: 0, Reg8: 10, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r0 = param1.length;
    // CODE → addr: 30 | <LoadConstZero>: <Reg8: 9>
    // USED → r9 = 0;
    // CODE → addr: 32 | <Less>: <Reg8: 2, Reg8: 9, Reg8: 0>
    // USED → r2 = 0 < param1.length;
    // CODE → addr: 36 | <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    // USED → r8 = 1;
    // CODE → addr: 39 | <LoadConstString>: <Reg8: 7, string_id: 4874>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught' (String)
    // USED → r7 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught";
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 6, string_id: 1440>  # String: 'negative value' (String)
    // USED → r6 = "negative value";
    // CODE → addr: 47 | <LoadConstString>: <Reg8: 5, string_id: 4877>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok";
    // CODE → addr: 51 | <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → addr: 53 | <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → addr: 55 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 57 | <JmpFalse>: <Addr8: 111, Reg8: 2>  # Address: 000000a8
    if (!(0 < param1.length)) goto label_168;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 60 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 0
    // CODE → addr: 63 | <Mov>: <Reg8: 11, Reg8: 3>
    // USED → r11 = 0;
    // CODE → addr: 66 | <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 2>
    r12 = param1[r2]
    // CODE → addr: 70 | <JLess>: <Addr8: 30, Reg8: 12, Reg8: 9>  # Address: 00000064
    // → r12 = param1[r2]
    if (r12 < 0) goto label_100;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 74 | <TryGetById>: <Reg8: 14, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = console;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = console.log;
    // CODE → addr: 85 | <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 2>
    r12 = param1[r2]
    // CODE → addr: 89 | <Call3>: <Reg8: 12, Reg8: 13, Reg8: 14, Reg8: 5, Reg8: 12>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", r12)
    // CODE → addr: 95 | <Mov>: <Reg8: 12, Reg8: 11>
    r12 = 0
    // CODE → addr: 98 | <Jmp>: <Addr8: 51>  # Address: 00000095
    goto label_149;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:100 | <TryGetById>: <Reg8: 13, Reg8: 1, UInt8: 3, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r13 = Error;
    // CODE → addr:106 | <CreateThisForNew>: <Reg8: 14, Reg8: 13, UInt8: 4>
    // USED → r14 = CreateThisForNew(r13);
    // CODE → addr:110 | <Mov>: <Reg8: 18, Reg8: 14>
    // USED → r18 = CreateThisForNew(r13);
    // CODE → addr:113 | <Mov>: <Reg8: 17, Reg8: 6>
    // USED → r17 = "negative value";
    // CODE → addr:116 | <Construct>: <Reg8: 13, Reg8: 13, UInt8: 2>
    // USED → r13 = new Error("negative value");
    // CODE → addr:120 | <SelectObject>: <Reg8: 13, Reg8: 14, Reg8: 13>
    r13 = new Error("negative value")
    // CODE → addr:124 | <Throw>: <Reg8: 13>
    throw r13;
    // CODE → addr:126 | <Catch>: <Reg8: 15>
    r15 = caughtException
    // CODE → addr:128 | <TryGetById>: <Reg8: 14, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = console;
    // CODE → addr:134 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = console.log;
    // CODE → addr:139 | <Call3>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 7, Reg8: 15>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", r15)
    // CODE → addr:145 | <AddN>: <Reg8: 12, Reg8: 11, Reg8: 8>
    // USED → r12 = r11 + 1;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:149 | <AddN>: <Reg8: 4, Reg8: 2, Reg8: 8>
    r4 = r2 + 1
    // CODE → addr:153 | <GetByIdShort>: <Reg8: 2, Reg8: 10, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    r2 = param1.length
    // CODE → addr:158 | <Mov>: <Reg8: 3, Reg8: 12>
    // USED → r3 = r11 + 1;
    // CODE → addr:161 | <Mov>: <Reg8: 0, Reg8: 3>
    r0 = r11 + 1
    // CODE → addr:164 | <JLess>: <Addr8: -104, Reg8: 4, Reg8: 2>  # Address: 0000003c
    // → r2 = param1.length; r4 = r2 + 1
    if (r4 < r2) goto label_60;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:168 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:174 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:179 | <LoadConstString>: <Reg8: 1, string_id: 4876>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end";
    // CODE → addr:183 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end")
    // CODE → addr:188 | <Ret>: <Reg8: 0>
    return r0;
}