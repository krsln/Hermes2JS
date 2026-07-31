function create(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 550>  # String: '__BC:Classes/ClassTests/Dog/static-create' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Dog/static-create";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Classes/ClassTests/Dog/static-create")
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 0, UInt8: 2>
    // USED → r5 = getParentEnvironment(0)[2];
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 5, UInt8: 2>
    r2 = __uninitialized_this_for_new__
    if (typeof getParentEnvironment(0)[2] !== "<128>") {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstString>: <Reg8: 7, string_id: 4299>  # String: 'Trying to call a non-function' (String)
        r7 = "Trying to call a non-function"
        // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
        r2 = builtin_44(r0, r1)
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 1>
    r7 = param1
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = getParentEnvironment(0)[4];
    // CODE → <LoadParentNoTraps>: <Reg8: 3, Reg8: 0>
    // USED → r3 = __getPrototypeOfNoTraps__(getParentEnvironment(0)[4]);
    // CODE → <CreateThisForSuper>: <Reg8: 2, Reg8: 3, Reg8: 5, UInt8: 2>
    // USED → r2 = __uninitialized_this_for_super__;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4424>  # String: 'Woof' (String)
    r6 = "Woof"
    // CODE → <Mov>: <Reg8: 8, Reg8: 2>
    r8 = __uninitialized_this_for_super__
    // CODE → <CallWithNewTarget>: <Reg8: 0, Reg8: 3, Reg8: 5, UInt8: 3>
    // USED → r0 = Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], getParentEnvironment(0)[2]);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], getParentEnvironment(0)[2])];
    // CODE → <LoadConstEmpty>: <Reg8: 2>
    // USED → r2 = /* empty */;
    // CODE → <ThrowIfThisInitialized>: <Reg8: 2>
    __throwIfThisInitialized__(/* empty */)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2259>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3660>  # String: 'Mixed' (String)
    // USED → r1 = "Mixed";
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 16255>  # String: 'breed' (Identifier)
    __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], getParentEnvironment(0)[2])].breed = "Mixed"
    // CODE → <Ret>: <Reg8: 0>
    return __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], getParentEnvironment(0)[2])];
}