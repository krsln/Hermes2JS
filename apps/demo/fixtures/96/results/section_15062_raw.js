function ifTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4603>  # String: '__BC:ControlFlow/IfTests/ifTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/start")
    // CODE → addr: 25 | <LoadConstUInt8>: <Reg8: 1, UInt8: 10>
    // USED → r1 = 10;
    // CODE → addr: 28 | <JGreaterLong>: <Addr32: 149, Reg8: 2, Reg8: 1>  # Address: 000000b1
    if (param1 > 10) goto label_177;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 35 | <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → addr: 38 | <JGreater>: <Addr8: 97, Reg8: 2, Reg8: 1>  # Address: 00000087
    if (param1 > 5) goto label_135;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → addr: 44 | <JStrictEqual>: <Addr8: 49, Reg8: 2, Reg8: 1>  # Address: 0000005d
    if (param1 === 0) goto label_93;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 48 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 54 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 59 | <LoadConstString>: <Reg8: 1, string_id: 523>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-small' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-small";
    // CODE → addr: 63 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-small")
    // CODE → addr: 68 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 74 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 79 | <LoadConstString>: <Reg8: 1, string_id: 9676>  # String: 'small' (Identifier)
    // USED → r1 = "small";
    // CODE → addr: 83 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("small")
    // CODE → addr: 88 | <JmpLong>: <Addr32: 129>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 93 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 99 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:104 | <LoadConstString>: <Reg8: 1, string_id: 4598>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-zero' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-zero";
    // CODE → addr:108 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-zero")
    // CODE → addr:113 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:119 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:124 | <LoadConstString>: <Reg8: 1, string_id: 615>  # String: 'zero' (String)
    // USED → r1 = "zero";
    // CODE → addr:128 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("zero")
    // CODE → addr:133 | <Jmp>: <Addr8: 84>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:135 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:141 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:146 | <LoadConstString>: <Reg8: 1, string_id: 4597>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-medium' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-medium";
    // CODE → addr:150 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-medium")
    // CODE → addr:155 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:161 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:166 | <LoadConstString>: <Reg8: 1, string_id: 10914>  # String: 'medium' (Identifier)
    // USED → r1 = "medium";
    // CODE → addr:170 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("medium")
    // CODE → addr:175 | <Jmp>: <Addr8: 42>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:177 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:183 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:188 | <LoadConstString>: <Reg8: 1, string_id: 1939>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-big' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-big";
    // CODE → addr:192 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-big")
    // CODE → addr:197 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:203 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:208 | <LoadConstString>: <Reg8: 1, string_id: 2969>  # String: 'big' (String)
    // USED → r1 = "big";
    // CODE → addr:212 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("big")
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:217 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:223 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:228 | <LoadConstString>: <Reg8: 0, string_id: 4600>  # String: '__BC:ControlFlow/IfTests/ifTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/IfTests/ifTest/end";
    // CODE → addr:232 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/IfTests/ifTest/end")
    // CODE → addr:237 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:239 | <Ret>: <Reg8: 0>
    return undefined;
}