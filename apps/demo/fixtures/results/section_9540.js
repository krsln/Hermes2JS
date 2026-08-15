function describe() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 0>
    // USED → r3 = this;
    // CODE → <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 2588>  # String: '__BC:Classes/PrivateStaticTests/Counter/describe' (String)
    // USED → r4 = "__BC:Classes/PrivateStaticTests/Counter/describe";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Classes/PrivateStaticTests/Counter/describe")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 5>
    // USED → r4 = getParentEnvironment(0)[5];
    // CODE → <PrivateIsIn>: <Reg8: 0, Reg8: 4, Reg8: 3, Reg8: 0>
    // USED → r0 = getParentEnvironment(0)[5] in this;
    if (!(getParentEnvironment(0)[5] in this)) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstString>: <Reg8: 7, string_id: 3847>  # String: 'Private element not found' (String)
        r7 = "Private element not found"
        // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r4 = throwTypeError(r2, r3)
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 6>
    r2 = getParentEnvironment(0)[6]
    // CODE → <GetOwnPrivateBySym>: <Reg8: 3, Reg8: 3, UInt8: 1, Reg8: 2>
    // USED → r3 = this.#__private_2__;
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'HermesInternal' (Identifier)
    // USED → r1 = globalThis.HermesInternal;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 105>  # String: 'concat' (Identifier)
    // USED → r2 = globalThis.HermesInternal.concat;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3789>  # String: 'count=' (String)
    // USED → r1 = "count=";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 1, Reg8: 3>
    // USED → r1 = globalThis.HermesInternal.concat.call("count=", r3);
    // CODE → <Ret>: <Reg8: 1>
    return globalThis.HermesInternal.concat.call("count=", r3);
}