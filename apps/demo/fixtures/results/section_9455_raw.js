function ifElseChainTest(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 4, string_id: 4773>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/IfTests/ifElseChainTest/start";
    // CODE → addr: 23 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/start")
    // CODE → addr: 28 | <JmpFalse>: <Addr8: 6, Reg8: 2>  # Address: 00000022
    if (!param1) goto label_34;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 31 | <JmpTrue>: <Addr8: 93, Reg8: 3>  # Address: 0000007c
    if (param2) goto label_124;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 34 | <JmpTrue>: <Addr8: 48, Reg8: 2>  # Address: 00000052
    if (param1) goto label_82;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 37 | <JmpTrue>: <Addr8: 45, Reg8: 3>  # Address: 00000052
    if (param2) goto label_82;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 40 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 46 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 51 | <LoadConstString>: <Reg8: 3, string_id: 4770>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither";
    // CODE → addr: 55 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither")
    // CODE → addr: 60 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 71 | <LoadConstString>: <Reg8: 3, string_id: 1889>  # String: 'neither' (String)
    // USED → r3 = "neither";
    // CODE → addr: 75 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("neither")
    // CODE → addr: 80 | <Jmp>: <Addr8: 84>  # Address: 000000a4
    goto label_164;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 82 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 88 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 93 | <LoadConstString>: <Reg8: 3, string_id: 4769>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-either' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-either";
    // CODE → addr: 97 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-either")
    // CODE → addr:102 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:108 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:113 | <LoadConstString>: <Reg8: 3, string_id: 1890>  # String: 'either' (String)
    // USED → r3 = "either";
    // CODE → addr:117 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("either")
    // CODE → addr:122 | <Jmp>: <Addr8: 42>  # Address: 000000a4
    goto label_164;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:124 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:130 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:135 | <LoadConstString>: <Reg8: 3, string_id: 4768>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-both' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-both";
    // CODE → addr:139 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-both")
    // CODE → addr:144 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:150 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:155 | <LoadConstString>: <Reg8: 3, string_id: 381>  # String: 'both' (String)
    // USED → r3 = "both";
    // CODE → addr:159 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("both")
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:164 | <JmpTrue>: <Addr8: 43, Reg8: 2>  # Address: 000000cf
    if (param1) goto label_207;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:167 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:173 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:178 | <LoadConstString>: <Reg8: 2, string_id: 4771>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a";
    // CODE → addr:182 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a")
    // CODE → addr:187 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:193 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:198 | <LoadConstString>: <Reg8: 2, string_id: 669>  # String: 'not a' (String)
    // USED → r2 = "not a";
    // CODE → addr:202 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("not a")
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:207 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:213 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:218 | <LoadConstString>: <Reg8: 1, string_id: 2026>  # String: '__BC:ControlFlow/IfTests/ifElseChainTest/end' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifElseChainTest/end";
    // CODE → addr:222 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/end")
    // CODE → addr:227 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:229 | <Ret>: <Reg8: 0>
    return r0;
}