function create(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 2, string_id: 550>  # String: '__BC:Classes/ClassTests/Dog/static-create' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Dog/static-create";
    // CODE → addr: 20 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Classes/ClassTests/Dog/static-create")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 0, UInt8: 2>
    // USED → r5 = r0[2];
    // CODE → addr: 29 | <CreateThisForNew>: <Reg8: 2, Reg8: 5, UInt8: 2>
    r2 = CreateThisForNew(r5)
    // CODE → addr: 33 | <JmpTypeOfIs>: <Addr32: 16, Reg8: 5, UInt16: 128>  # Address: 00000031
    // → r0 = getParentEnvironment(0)
    if (typeof r0[2] === "function") goto label_49;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 7, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r7 = "Trying to call a non-function"
    // CODE → addr: 45 | <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r2 = throwTypeError(r7, r6)
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <LoadParam>: <Reg8: 7, UInt8: 1>
    r7 = param1
    // CODE → addr: 52 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 4>
    // USED → r0 = r0[4];
    // CODE → addr: 56 | <LoadParentNoTraps>: <Reg8: 3, Reg8: 0>
    r3 = __getPrototypeOfNoTraps__(r0[4])
    // CODE → addr: 59 | <CreateThisForSuper>: <Reg8: 2, Reg8: 3, Reg8: 5, UInt8: 2>
    // USED → r2 = CreateThisForSuper(r3);
    // CODE → addr: 64 | <LoadConstString>: <Reg8: 6, string_id: 4424>  # String: 'Woof' (String)
    r6 = "Woof"
    // CODE → addr: 68 | <Mov>: <Reg8: 8, Reg8: 2>
    r8 = CreateThisForSuper(r3)
    // CODE → addr: 71 | <CallWithNewTarget>: <Reg8: 0, Reg8: 3, Reg8: 5, UInt8: 3>
    r0 = Reflect.construct(r3, [r0, r1, r2], r0[2])
    // CODE → addr: 76 | <SelectObject>: <Reg8: 0, Reg8: 2, Reg8: 0>
    // USED → r0 = CreateThisForSuper(r3)[r0];
    // CODE → addr: 80 | <LoadConstEmpty>: <Reg8: 2>
    // USED → r2 = /* empty */;
    // CODE → addr: 82 | <ThrowIfThisInitialized>: <Reg8: 2>
    __throwIfThisInitialized__(/* empty */)
    // CODE → addr: 84 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 90 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 95 | <LoadConstString>: <Reg8: 1, string_id: 2259>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → addr: 99 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → addr:104 | <LoadConstString>: <Reg8: 1, string_id: 3660>  # String: 'Mixed' (String)
    // USED → r1 = "Mixed";
    // CODE → addr:108 | <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 16255>  # String: 'breed' (Identifier)
    CreateThisForSuper(r3)[r0].breed = "Mixed"
    // CODE → addr:114 | <Ret>: <Reg8: 0>
    return r0;
}