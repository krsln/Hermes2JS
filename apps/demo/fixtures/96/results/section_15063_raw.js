function ifElseChainTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4118>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/start' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/start")
    // CODE → <JmpFalse>: <Addr8: 6, Reg8: 1>  # Address: 00000022
    if (!param1) goto label_34;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 93, Reg8: 2>  # Address: 0000007c
    if (param2) goto label_124;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 48, Reg8: 1>  # Address: 00000052
    if (param1) goto label_82;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 45, Reg8: 2>  # Address: 00000052
    if (param2) goto label_82;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4588>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1908>  # String: 'neither' (String)
    // USED → r2 = "neither";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("neither")
    // CODE → <Jmp>: <Addr8: 84>  # Address: 000000a4
    goto label_164;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4587>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-either' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-either";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-either")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1909>  # String: 'either' (String)
    // USED → r2 = "either";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("either")
    // CODE → <Jmp>: <Addr8: 42>  # Address: 000000a4
    goto label_164;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4586>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-both' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-both";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-both")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 757>  # String: 'both' (String)
    // USED → r2 = "both";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("both")
    // ──────────────── Block 7 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 43, Reg8: 1>  # Address: 000000cf
    if (param1) goto label_207;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4590>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 680>  # String: 'not a' (String)
    // USED → r1 = "not a";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("not a")
    // ──────────────── Block 9 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4592>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/IfTests/ifElseChainTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}