function callRegExpTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4844>  # String: '__BC:Strings/RegExpTests/callRegExpTests/start' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/callRegExpTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 0>
    // USED → r4 = r2[0];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 31 | <LoadConstString>: <Reg8: 3, string_id: 4591>  # String: 'abc123' (String)
    // USED → r3 = "abc123";
    // CODE → addr: 35 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[0].call(r0, "abc123")
    // CODE → addr: 40 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → addr: 44 | <LoadConstString>: <Reg8: 3, string_id: 3232>  # String: 'Hello\nline two' (String)
    // USED → r3 = "Hello\\nline two";
    // CODE → addr: 48 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[1].call(r0, "Hello\\nline two")
    // CODE → addr: 53 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 2>
    // USED → r4 = r2[2];
    // CODE → addr: 57 | <LoadConstString>: <Reg8: 3, string_id: 3760>  # String: "it's a test - really" (String)
    // USED → r3 = "it's a test - really";
    // CODE → addr: 61 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[2].call(r0, "it's a test - really")
    // CODE → addr: 66 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = r2[3];
    // CODE → addr: 70 | <LoadConstString>: <Reg8: 2, string_id: 2296>  # String: '2024-01-15' (String)
    // USED → r2 = "2024-01-15";
    // CODE → addr: 74 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2>
    r2 = r2[3].call(r0, "2024-01-15")
    // CODE → addr: 79 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 90 | <LoadConstString>: <Reg8: 1, string_id: 4841>  # String: '__BC:Strings/RegExpTests/callRegExpTests/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/callRegExpTests/end";
    // CODE → addr: 94 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/end")
    // CODE → addr: 99 | <Ret>: <Reg8: 0>
    return undefined;
}