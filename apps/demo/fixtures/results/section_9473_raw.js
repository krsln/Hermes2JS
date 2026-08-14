function tryCatchInsideLoopTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4879>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start' (String)
    // USED → r0 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start")
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 10, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r0 = param1.length;
    // CODE → <LoadConstZero>: <Reg8: 9>
    // USED → r9 = 0;
    // CODE → <Less>: <Reg8: 2, Reg8: 9, Reg8: 0>
    // USED → r2 = 0 < param1.length;
    // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    // USED → r8 = 1;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4874>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught' (String)
    // USED → r7 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught";
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 1440>  # String: 'negative value' (String)
    // USED → r6 = "negative value";
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4877>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok' (String)
    // USED → r5 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok";
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <LoadConstZero>: <Reg8: 3>
    // USED → r3 = 0;
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <JmpFalse>: <Addr8: 111, Reg8: 2>  # Address: 000000a8
    if (!(0 < param1.length)) goto label_168;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 4>
    // USED → r2 = 0;
    // CODE → <Mov>: <Reg8: 11, Reg8: 3>
    // USED → r11 = 0;
    // CODE → <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 2>
    // USED → r12 = param1[0];
    // CODE → <JLess>: <Addr8: 30, Reg8: 12, Reg8: 9>  # Address: 00000064
    // → r12 = param1[0]
    if (r12 < 0) goto label_100;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 14, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = globalThis.console.log;
    // CODE → <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 2>
    // USED → r12 = param1[0];
    // CODE → <Call3>: <Reg8: 12, Reg8: 13, Reg8: 14, Reg8: 5, Reg8: 12>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", r12)
    // CODE → <Mov>: <Reg8: 12, Reg8: 11>
    r12 = 0
    // CODE → <Jmp>: <Addr8: 51>  # Address: 00000095
    goto label_149;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 13, Reg8: 1, UInt8: 3, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r13 = globalThis.Error;
    // CODE → <CreateThisForNew>: <Reg8: 14, Reg8: 13, UInt8: 4>
    // USED → r14 = CreateThisForNew(r13);
    // CODE → <Mov>: <Reg8: 18, Reg8: 14>
    // USED → r18 = CreateThisForNew(r13);
    // CODE → <Mov>: <Reg8: 17, Reg8: 6>
    // USED → r17 = "negative value";
    // CODE → <Construct>: <Reg8: 13, Reg8: 13, UInt8: 2>
    // USED → r13 = new globalThis.Error("negative value");
    // CODE → <SelectObject>: <Reg8: 13, Reg8: 14, Reg8: 13>
    // USED → r13 = new globalThis.Error("negative value");
    // CODE → <Throw>: <Reg8: 13>
    throw new globalThis.Error("negative value");
    // CODE → <Catch>: <Reg8: 15>
    // USED → r15 = caughtException;
    // CODE → <TryGetById>: <Reg8: 14, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 7, Reg8: 15>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", r15)
    // CODE → <AddN>: <Reg8: 12, Reg8: 11, Reg8: 8>
    // USED → r12 = 0 + 1;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <AddN>: <Reg8: 4, Reg8: 2, Reg8: 8>
    // USED → r4 = 0 + 1;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 10, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r2 = param1.length;
    // CODE → <Mov>: <Reg8: 3, Reg8: 12>
    // USED → r3 = 0 + 1;
    // CODE → <Mov>: <Reg8: 0, Reg8: 3>
    // USED → r0 = 0 + 1;
    // CODE → <JLess>: <Addr8: -104, Reg8: 4, Reg8: 2>  # Address: 0000003c
    // → r2 = param1.length; r4 = 0 + 1
    if (r4 < r2) goto label_60;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4876>  # String: '__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end' (String)
    // USED → r1 = "__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return 0 + 1;
}