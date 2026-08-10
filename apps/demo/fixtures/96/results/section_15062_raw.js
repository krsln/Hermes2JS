function ifTest(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4603>  # String: '__BC:ControlFlow/IfTests/ifTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/start")
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 10>
    // USED → r1 = 10;
    // CODE → <JGreaterLong>: <Addr32: 149, Reg8: 2, Reg8: 1>  # Address: 000000b1
    if (param1 > 10) goto label_177;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 5>
    // USED → r1 = 5;
    // CODE → <JGreater>: <Addr8: 97, Reg8: 2, Reg8: 1>  # Address: 00000087
    if (param1 > 5) goto label_135;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → <JStrictEqual>: <Addr8: 49, Reg8: 2, Reg8: 1>  # Address: 0000005d
    if (param1 === 0) goto label_93;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 523>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-small' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-small";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-small")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 9676>  # String: 'small' (Identifier)
    // USED → r1 = "small";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("small")
    // CODE → <JmpLong>: <Addr32: 129>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4598>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-zero' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-zero";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-zero")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 615>  # String: 'zero' (String)
    // USED → r1 = "zero";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("zero")
    // CODE → <Jmp>: <Addr8: 84>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4597>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-medium' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-medium";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-medium")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10914>  # String: 'medium' (Identifier)
    // USED → r1 = "medium";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("medium")
    // CODE → <Jmp>: <Addr8: 42>  # Address: 000000d9
    goto label_217;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1939>  # String: '__BC:ControlFlow/IfTests/ifTest/branch-big' (String)
    // USED → r1 = "__BC:ControlFlow/IfTests/ifTest/branch-big";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:ControlFlow/IfTests/ifTest/branch-big")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2969>  # String: 'big' (String)
    // USED → r1 = "big";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("big")
    // ──────────────── Block 7 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4600>  # String: '__BC:ControlFlow/IfTests/ifTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/IfTests/ifTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/IfTests/ifTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}