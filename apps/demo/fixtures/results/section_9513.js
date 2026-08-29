function callDefaultParameterTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 6, string_id: 4934>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start' (String)
    // USED → r6 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 8, string_id: 4935>  # String: '__BC:Functions/DefaultParameterTests/defaultParameterTest/start' (String)
    // USED → r8 = "__BC:Functions/DefaultParameterTests/defaultParameterTest/start";
    // CODE → addr: 37 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → addr: 42 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 53 | <LoadConstUInt8>: <Reg8: 0, UInt8: 15>
    // USED → r0 = 15;
    // CODE → addr: 56 | <LoadConstString>: <Reg8: 9, string_id: 7900>  # String: 'result' (Identifier)
    // USED → r9 = "result";
    // CODE → addr: 60 | <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 0>
    console.log("result", 15)
    // CODE → addr: 66 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 72 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 77 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → addr: 82 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 88 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 93 | <LoadConstUInt8>: <Reg8: 0, UInt8: 25>
    // USED → r0 = 25;
    // CODE → addr: 96 | <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 0>
    console.log("result", 25)
    // CODE → addr:102 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:108 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:113 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 8>
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start")
    // CODE → addr:118 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:124 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:129 | <LoadConstString>: <Reg8: 6, string_id: 1414>  # String: 'sum' (String)
    // USED → r6 = "sum";
    // CODE → addr:133 | <Call3>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 0>
    console.log("sum", 25)
    // CODE → addr:139 | <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
    r6 = getParentEnvironment(0)
    // CODE → addr:142 | <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 0>
    // USED → r6 = r6[0];
    // CODE → addr:146 | <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → addr:148 | <Call1>: <Reg8: 4, Reg8: 6, Reg8: 3>
    r4 = r6[0].call(r3)
    // CODE → addr:152 | <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    // USED → r1 = 4;
    // CODE → addr:155 | <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → addr:158 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:161 | <Call4>: <Reg8: 4, Reg8: 6, Reg8: 3, Reg8: 0, Reg8: 2, Reg8: 1>
    r4 = r6[0].call(r3, 2, 3, 4)
    // CODE → addr:168 | <TryGetById>: <Reg8: 7, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:174 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:179 | <LoadConstString>: <Reg8: 5, string_id: 4933>  # String: '__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end' (String)
    // USED → r5 = "__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end";
    // CODE → addr:183 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end")
    // CODE → addr:188 | <Ret>: <Reg8: 3>
    return undefined;
}