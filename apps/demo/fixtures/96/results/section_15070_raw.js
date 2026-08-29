function ternaryTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 1, string_id: 4641>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/start' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/ternaryTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/start")
    // CODE → addr: 25 | <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → addr: 27 | <Greater>: <Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r3 = param1 > 0;
    // CODE → addr: 31 | <LoadConstString>: <Reg8: 5, string_id: 866>  # String: 'positive' (String)
    r5 = "positive"
    // CODE → addr: 35 | <JmpTrue>: <Addr8: 21, Reg8: 3>  # Address: 00000038
    if (param1 > 0) goto label_56;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 38 | <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r4 = param1 < 0;
    // CODE → addr: 42 | <LoadConstString>: <Reg8: 3, string_id: 615>  # String: 'zero' (String)
    r3 = "zero"
    // CODE → addr: 46 | <JmpFalse>: <Addr8: 7, Reg8: 4>  # Address: 00000035
    if (!(param1 < 0)) goto label_53;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <LoadConstString>: <Reg8: 3, string_id: 1323>  # String: 'negative' (String)
    // USED → r3 = "negative";
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 53 | <Mov>: <Reg8: 5, Reg8: 3>
    // USED → r5 = "negative";
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 56 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 62 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 67 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → addr: 72 | <LoadConstUInt8>: <Reg8: 3, UInt8: 100>
    // USED → r3 = 100;
    // CODE → addr: 75 | <Greater>: <Reg8: 4, Reg8: 2, Reg8: 3>
    // USED → r4 = param1 > 100;
    // CODE → addr: 79 | <JmpTrue>: <Addr8: 18, Reg8: 4>  # Address: 00000061
    if (param1 > 100) goto label_97;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 82 | <Less>: <Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r4 = param1 < 0;
    // CODE → addr: 86 | <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // CODE → addr: 88 | <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 0000005e
    if (param1 < 0) goto label_94;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 91 | <Mov>: <Reg8: 1, Reg8: 2>
    // USED → r1 = param1;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 94 | <Mov>: <Reg8: 3, Reg8: 1>
    // USED → r3 = param1;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 97 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:103 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:108 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:113 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:119 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:124 | <LoadConstString>: <Reg8: 0, string_id: 3481>  # String: '__BC:ControlFlow/TernaryTests/ternaryTest/end' (String)
    // USED → r0 = "__BC:ControlFlow/TernaryTests/ternaryTest/end";
    // CODE → addr:128 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/end")
    // CODE → addr:133 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:135 | <Ret>: <Reg8: 0>
    return r0;
}