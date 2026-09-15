function greet() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → addr: 16 | <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 176>  # String: 'name' (Identifier)
    // USED → r1 = this.name;
    // CODE → addr: 21 | <LoadConstString>: <Reg8: 0, string_id: 6584>  # String: 'hello' (String)
    // USED → r0 = "hello";
    // CODE → addr: 25 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    console.log("hello", this.name)
    // CODE → addr: 31 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 33 | <Ret>: <Reg8: 0>
    return undefined;
}