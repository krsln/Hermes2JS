function sideEffect(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4634>  # String: '__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect' (String)
    // USED → r1 = "__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect";
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 1, Reg8: 0>
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", r0)
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → <Ret>: <Reg8: 0>
    return param2;
}