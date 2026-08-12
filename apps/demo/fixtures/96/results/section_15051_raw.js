function forTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4585>  # String: '__BC:ControlFlow/ForTests/forTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/ForTests/forTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/ForTests/forTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 10>
    r4 = 10
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4584>  # String: '__BC:ControlFlow/ForTests/forTest/if-continue' (String)
    // USED → r3 = "__BC:ControlFlow/ForTests/forTest/if-continue";
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 8>
    r2 = 8
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    r1 = 3
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 5>
    // USED → r6 = 0;
    // CODE → <JStrictEqual>: <Addr8: 48, Reg8: 6, Reg8: 1>  # Address: 00000058
    if (r6 === r1) goto label_88;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <JStrictEqual>: <Addr8: 22, Reg8: 6, Reg8: 2>  # Address: 00000042
    if (r6 === r2) goto label_66;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(0)
    // CODE → <Jmp>: <Addr8: 40>  # Address: 00000068
    goto label_104;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r9 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r8 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4583>  # String: '__BC:ControlFlow/ForTests/forTest/if-break' (String)
    // USED → r7 = "__BC:ControlFlow/ForTests/forTest/if-break";
    // CODE → <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:ControlFlow/ForTests/forTest/if-break")
    // CODE → <Jmp>: <Addr8: 25>  # Address: 0000006f
    goto label_111;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 7, Reg8: 7, Reg8: 8, Reg8: 3>
    console.log("__BC:ControlFlow/ForTests/forTest/if-continue")
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Inc>: <Reg8: 5, Reg8: 6>
    r5 = r6 + 1
    // CODE → <JLess>: <Addr8: -70, Reg8: 5, Reg8: 4>  # Address: 00000025
    if (r5 < r4) goto label_37;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 3936>  # String: '__BC:ControlFlow/ForTests/forTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/ForTests/forTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/ForTests/forTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}