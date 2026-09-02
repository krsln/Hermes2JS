function ifTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 4, string_id: 4777>  # String: '__BC:ControlFlow/IfTests/ifTest/start' (String)
    // USED → r4 = "__BC:ControlFlow/IfTests/ifTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:ControlFlow/IfTests/ifTest/start")
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 0, UInt8: 10>
    // USED → r0 = 10;
    // CODE → addr: 28 | <JGreaterLong>: <Addr32: 149, Reg8: 3, Reg8: 0>  # Address: 000000b1
    if (param1 > 10) goto label_177;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 0, UInt8: 5>
    // USED → r0 = 5;
    // CODE → addr: 38 | <JGreater>: <Addr8: 97, Reg8: 3, Reg8: 0>  # Address: 00000087
    if (param1 > 5) goto label_135;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 44 | <JStrictEqual>: <Addr8: 49, Reg8: 3, Reg8: 0>  # Address: 0000005d
    if (param1 === 0) goto label_93;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 48 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 54 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 59 | <LoadConstString>: <Reg8: 3, string_id: 1946>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-small' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-small";
    // CODE → addr: 63 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-small")
    // CODE → addr: 68 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 74 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 79 | <LoadConstString>: <Reg8: 3, string_id: 9615>  # String: 'small' (Identifier)
    // USED → r3 = "small";
    // CODE → addr: 83 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("small")
    // CODE → addr: 88 | <JmpLong>: <Addr32: 129>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 93 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 99 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:104 | <LoadConstString>: <Reg8: 3, string_id: 4775>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-zero' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-zero";
    // CODE → addr:108 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-zero")
    // CODE → addr:113 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:119 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:124 | <LoadConstString>: <Reg8: 3, string_id: 597>  # String: 'zero' (String)
    // USED → r3 = "zero";
    // CODE → addr:128 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("zero")
    // CODE → addr:133 | <Jmp>: <Addr8: 84>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:135 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:141 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:146 | <LoadConstString>: <Reg8: 3, string_id: 4774>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-medium' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-medium";
    // CODE → addr:150 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-medium")
    // CODE → addr:155 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:161 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:166 | <LoadConstString>: <Reg8: 3, string_id: 11186>  # String: 'medium' (Identifier)
    // USED → r3 = "medium";
    // CODE → addr:170 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("medium")
    // CODE → addr:175 | <Jmp>: <Addr8: 42>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:177 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:183 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:188 | <LoadConstString>: <Reg8: 3, string_id: 1925>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-big' (String)
    // USED → r3 = "__BC:ControlFlow/IfTests/ifTest/branch-big";
    // CODE → addr:192 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-big")
    // CODE → addr:197 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:203 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:208 | <LoadConstString>: <Reg8: 3, string_id: 3074>  # String: 'big' (String)
    // USED → r3 = "big";
    // CODE → addr:212 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("big")
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:217 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:223 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:228 | <LoadConstString>: <Reg8: 2, string_id: 4416>  # String: '__BC:ControlFlow/IfTests/ifTest/end' (String)
    // USED → r2 = "__BC:ControlFlow/IfTests/ifTest/end";
    // CODE → addr:232 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:ControlFlow/IfTests/ifTest/end")
    // CODE → addr:237 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr:239 | <Ret>: <Reg8: 1>
    return r1;
}