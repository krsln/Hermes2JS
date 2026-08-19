function description() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4723>  # String: '__BC:Classes/ClassTests/Animal/get-description' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/get-description";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Animal/get-description")
    // CODE → addr: 22 | <LoadParam>: <Reg8: 1, UInt8: 0>
    r1 = this
    // CODE → addr: 25 | <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → addr: 30 | <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 3, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = HermesInternal;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r2 = HermesInternal.concat;
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 1, string_id: 1429>  # String: ' the animal' (String)
    // USED → r1 = " the animal";
    // CODE → addr: 45 | <LoadConstString>: <Reg8: 0, string_id: 6457>  # String: '' (Identifier)
    // USED → r0 = "";
    // CODE → addr: 49 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3, Reg8: 1>
    r0 = HermesInternal.concat.call("", r1.name, " the animal")
    // CODE → addr: 55 | <Ret>: <Reg8: 0>
    return r0;
}