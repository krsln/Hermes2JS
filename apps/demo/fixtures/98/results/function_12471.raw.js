function greet() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr: 16 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r2 = this.name;
    // CODE → addr: 21 | <LoadConstString>: <Reg8: 1, string_id: 6140>  # String: 'hello' (String)
    // USED → r1 = "hello";
    // CODE → addr: 25 | <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 2>
    console.log("hello", this.name)
    // CODE → addr: 31 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 33 | <Ret>: <Reg8: 0>
    return r0;
}