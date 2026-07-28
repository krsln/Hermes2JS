function Dog(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetNewTarget>: <Reg8: 4>
    // USED → r4 = new.target;
    // CODE → <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getParentEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = getParentEnvironment(0)[4];
    // CODE → <LoadParentNoTraps>: <Reg8: 3, Reg8: 0>
    // USED → r3 = __getPrototypeOfNoTraps__(getParentEnvironment(0)[4]);
    // CODE → <CreateThisForSuper>: <Reg8: 1, Reg8: 3, Reg8: 4, UInt8: 0>
    // USED → r1 = __uninitialized_this__;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 1426>  # String: 'Woof' (String)
    r5 = "Woof";
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    r6 = param1;
    // CODE → <Mov>: <Reg8: 7, Reg8: 1>
    r7 = __uninitialized_this__;
    // CODE → <CallWithNewTarget>: <Reg8: 0, Reg8: 3, Reg8: 4, UInt8: 3>
    // USED → r0 = Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], new.target);
    // CODE → <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = __uninitialized_this__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], new.target)];
    // CODE → <LoadConstEmpty>: <Reg8: 1>
    // USED → r1 = /* empty */;
    // CODE → <ThrowIfThisInitialized>: <Reg8: 1>
    __throwIfThisInitialized__(/* empty */);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2226>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/Dog/constructor");
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 15973>  # String: 'breed' (Identifier)
    __uninitialized_this__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], new.target)].breed = param2;
    // CODE → <Ret>: <Reg8: 0>
    return __uninitialized_this__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r0, r1, r2], new.target)];
}