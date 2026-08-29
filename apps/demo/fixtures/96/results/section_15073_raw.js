function sideEffect(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4634>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect";
    // CODE → addr: 17 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr: 20 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", param1)
    // CODE → addr: 26 | <LoadParam>: <Reg8: 0, UInt8: 2>
    r0 = param2
    // CODE → addr: 29 | <Ret>: <Reg8: 0>
    return r0;
}