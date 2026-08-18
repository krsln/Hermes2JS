function callRegExpTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4844>  # String: '__BC:Strings/RegExpTests/callRegExpTests/start' (String)
    // USED → r0 = "__BC:Strings/RegExpTests/callRegExpTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 0>
    // USED → r4 = r2[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4591>  # String: 'abc123' (String)
    // USED → r3 = "abc123";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[0].call(undefined, "abc123")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3232>  # String: 'Hello\nline two' (String)
    // USED → r3 = "Hello\\nline two";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[1].call(undefined, "Hello\\nline two")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 2>
    // USED → r4 = r2[2];
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3760>  # String: "it's a test - really" (String)
    // USED → r3 = "it's a test - really";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r2[2].call(undefined, "it's a test - really")
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = r2[3];
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2296>  # String: '2024-01-15' (String)
    // USED → r2 = "2024-01-15";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2>
    r2 = r2[3].call(undefined, "2024-01-15")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4841>  # String: '__BC:Strings/RegExpTests/callRegExpTests/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/callRegExpTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}