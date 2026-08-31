function describe() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 3, UInt8: 0>
    // USED → r3 = this;
    // CODE → addr:  3 | <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → addr:  6 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  8 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 14 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 19 | <LoadConstString>: <Reg8: 4, string_id: 2588>  # String: '__BC:Classes/PrivateStaticTests/Counter/describe' (String)
    // USED → r4 = "__BC:Classes/PrivateStaticTests/Counter/describe";
    // CODE → addr: 23 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Classes/PrivateStaticTests/Counter/describe")
    // CODE → addr: 28 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 5>
    // USED → r4 = r2[5];
    // CODE → addr: 32 | <PrivateIsIn>: <Reg8: 0, Reg8: 4, Reg8: 3, Reg8: 0>
    // USED → r0 = r2[5] in this;
    // → r2 = getParentEnvironment(0)
    if (!(r2[5] in this)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 40 | <LoadConstString>: <Reg8: 7, string_id: 3847>  # String: 'Private element not found' (String)
        r7 = "Private element not found"
        // CODE → addr: 44 | <CallBuiltin>: <Reg8: 4, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r4 = throwTypeError(r7, r6)
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 48 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 6>
    r2 = r2[6]
    // CODE → addr: 52 | <GetOwnPrivateBySym>: <Reg8: 3, Reg8: 3, UInt8: 1, Reg8: 2>
    // USED → r3 = this.#__private_2__;
    // CODE → addr: 57 | <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = HermesInternal;
    // CODE → addr: 63 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r2 = HermesInternal.concat;
    // CODE → addr: 68 | <LoadConstString>: <Reg8: 1, string_id: 3789>  # String: 'count=' (String)
    // USED → r1 = "count=";
    // CODE → addr: 72 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 1, Reg8: 3>
    r1 = HermesInternal.concat.call("count=", r3)
    // CODE → addr: 77 | <Ret>: <Reg8: 1>
    return r1;
}