function get() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4532>  # String: '__BC:Classes/ClassTests/Animal/get-description' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/get-description";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Animal/get-description")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    r1 = this
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r3 = r1.name;
    // CODE → <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 4, string_id: 14>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 96>  # String: 'concat' (Identifier)
    // USED → r2 = HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 7163>  # String: '' (Identifier)
    // USED → r1 = "";
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 1072>  # String: ' the animal' (String)
    // USED → r0 = " the animal";
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 1, Reg8: 3, Reg8: 0>
    r0 = HermesInternal.concat.call("", r3, " the animal")
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}