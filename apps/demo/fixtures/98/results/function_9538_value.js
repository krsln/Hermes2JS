function value(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 3, string_id: 4730>  # String: '__BC:Classes/PrivateStaticTests/Counter/set-value' (String)
    // USED → r3 = "__BC:Classes/PrivateStaticTests/Counter/set-value";
    // CODE → addr: 20 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/PrivateStaticTests/Counter/set-value")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 6>
    r3 = r1[6]
    // CODE → addr: 29 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 2, string_id: 19>  # String: 'Math' (Identifier)
    // USED → r5 = Math;
    // CODE → addr: 35 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 184>  # String: 'min' (Identifier)
    // USED → r4 = Math.min;
    // CODE → addr: 40 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 2>
    r1 = r1[2]
    // CODE → addr: 44 | <GetById>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 10140>  # String: 'MAX' (Identifier)
    // USED → r2 = r1.MAX;
    // CODE → addr: 50 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr: 53 | <Call3>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2>
    r2 = Math.min(param1, r1.MAX)
    // CODE → addr: 59 | <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → addr: 62 | <PutOwnPrivateBySym>: <Reg8: 1, Reg8: 2, UInt8: 0, Reg8: 3>
    this.#__private_3__ = r2
    // CODE → addr: 67 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 69 | <Ret>: <Reg8: 0>
    return undefined;
}