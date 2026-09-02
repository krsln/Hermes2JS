function arrowFunctionTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 3, string_id: 4908>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/start' (String)
    // USED → r3 = "__BC:Functions/ArrowTests/arrowFunctionTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 0, UInt8: 5>
    // USED → r0 = 5;
    // CODE → addr: 36 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(5)
    // CODE → addr: 41 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 47 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 52 | <LoadConstUInt8>: <Reg8: 0, UInt8: 16>
    // USED → r0 = 16;
    // CODE → addr: 55 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(16)
    // CODE → addr: 60 | <NewArrayWithBuffer>: <Reg8: 5, UInt16: 4, UInt16: 4, UInt16: 37098>  # Array: [1, 2, 3, 4]
    r5 = [1, 2, 3, 4]
    // CODE → addr: 68 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 126>  # String: 'map' (Identifier)
    // USED → r4 = r5.map;
    // CODE → addr: 73 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr: 75 | <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 12479>  # Function: [#12479  of 12 bytes]: 2 params @ offset 0x00243e0c
    // USED → r3 = function_12479(param1);
    // CODE → addr: 80 | <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
    r5 = r5.map(function_12479(param1))
    // CODE → addr: 85 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 91 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 96 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → addr:101 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:107 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:112 | <LoadConstUInt8>: <Reg8: 0, UInt8: 15>
    // USED → r0 = 15;
    // CODE → addr:115 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 0>
    console.log(15)
    // CODE → addr:120 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:126 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:131 | <LoadConstString>: <Reg8: 2, string_id: 4907>  # String: '__BC:Functions/ArrowTests/arrowFunctionTest/end' (String)
    // USED → r2 = "__BC:Functions/ArrowTests/arrowFunctionTest/end";
    // CODE → addr:135 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/end")
    // CODE → addr:140 | <Ret>: <Reg8: 1>
    return r1;
}