function description(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4693>  # String: '__BC:Classes/ClassTests/Animal/get-description' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/get-description";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/Animal/get-description")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 186>  # String: 'name' (Identifier)
    // USED → r3 = this.name;
    // CODE → <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 3, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 103>  # String: 'concat' (Identifier)
    // USED → r2 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 1410>  # String: ' the animal' (String)
    // USED → r1 = " the animal";
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 6250>  # String: '' (Identifier)
    // USED → r0 = "";
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 0, Reg8: 3, Reg8: 1>
    // USED → r0 = globalThis.HermesInternal.concat.call("", this.name, " the animal");
    // CODE → <Ret>: <Reg8: 0>
    return globalThis.HermesInternal.concat.call("", this.name, " the animal");
}