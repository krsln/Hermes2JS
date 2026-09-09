function Dog(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetNewTarget>: <Reg8: 4>
    // USED → r4 = new.target;
    // CODE → addr:  2 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr:  5 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = r0[4];
    // CODE → addr:  9 | <LoadParentNoTraps>: <Reg8: 3, Reg8: 0>
    r3 = __getPrototypeOfNoTraps__(r0[4])
    // CODE → addr: 12 | <CreateThisForSuper>: <Reg8: 1, Reg8: 3, Reg8: 4, UInt8: 0>
    // USED → r1 = CreateThisForSuper(r3);
    // CODE → addr: 17 | <LoadConstString>: <Reg8: 5, string_id: 4424>  # String: 'Woof' (String)
    r5 = "Woof"
    // CODE → addr: 21 | <LoadParam>: <Reg8: 6, UInt8: 1>
    r6 = param1
    // CODE → addr: 24 | <Mov>: <Reg8: 7, Reg8: 1>
    r7 = CreateThisForSuper(r3)
    // CODE → addr: 27 | <CallWithNewTarget>: <Reg8: 0, Reg8: 3, Reg8: 4, UInt8: 3>
    r0 = Reflect.construct(r3, [r0, r1, r2], new.target)
    // CODE → addr: 32 | <SelectObject>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = CreateThisForSuper(r3)[r0];
    // CODE → addr: 36 | <LoadConstEmpty>: <Reg8: 1>
    // USED → r1 = /* empty */;
    // CODE → addr: 38 | <ThrowIfThisInitialized>: <Reg8: 1>
    __throwIfThisInitialized__(/* empty */)
    // CODE → addr: 40 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr: 42 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 1, string_id: 2259>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → addr: 57 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → addr: 62 | <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → addr: 65 | <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 16255>  # String: 'breed' (Identifier)
    CreateThisForSuper(r3)[r0].breed = param2
    // CODE → addr: 71 | <Ret>: <Reg8: 0>
    return r0;
}