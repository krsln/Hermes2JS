function classTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    // USED → r2 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3972>  # String: '__BC:Classes/ClassTests/classTest/start' (String)
    // USED → r3 = "__BC:Classes/ClassTests/classTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/ClassTests/classTest/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = getParentEnvironment(0)[0];
    // CODE → <CreateThisForNew>: <Reg8: 4, Reg8: 3, UInt8: 2>
    r4 = __uninitialized_this_for_new__
    // CODE → <JmpTypeOfIs>: <Addr32: 16, Reg8: 3, UInt16: 128>  # Address: 00000031
    if (typeof getParentEnvironment(0)[0] === "function") goto label_49;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r8 = "Trying to call a non-function"
    // CODE → <CallBuiltin>: <Reg8: 4, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r4 = copyDataProperties(r2, r3)
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r3 = getParentEnvironment(0)[0].prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 3, Reg8: 3>
    // USED → r3 = Object.create(getParentEnvironment(0)[0].prototype);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 2576>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r4 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Classes/ClassTests/Animal/constructor")
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 3351>  # String: 'Generic' (String)
    // USED → r4 = "Generic";
    // CODE → <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 187>  # String: 'name' (Identifier)
    Object.create(getParentEnvironment(0)[0].prototype).name = "Generic"
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 765>  # String: '...' (String)
    // USED → r4 = "...";
    // CODE → <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 11958>  # String: 'sound' (Identifier)
    Object.create(getParentEnvironment(0)[0].prototype).sound = "..."
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r4 = Object.create(getParentEnvironment(0)[0].prototype).makeSound;
    // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 3>
    r4 = Object.create(getParentEnvironment(0)[0].prototype).makeSound()
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 11115>  # String: 'description' (Identifier)
    // USED → r3 = Object.create(getParentEnvironment(0)[0].prototype).description;
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(Object.create(getParentEnvironment(0)[0].prototype).description)
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = getParentEnvironment(0)[1];
    // CODE → <CreateThisForNew>: <Reg8: 3, Reg8: 4, UInt8: 2>
    r3 = __uninitialized_this_for_new__
    // CODE → <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000099
    if (typeof getParentEnvironment(0)[1] === "function") goto label_153;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r8 = "Trying to call a non-function"
    // CODE → <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r3 = copyDataProperties(r1, r2)
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 4>
    // USED → r2 = getParentEnvironment(0)[4];
    // CODE → <LoadParentNoTraps>: <Reg8: 6, Reg8: 2>
    // USED → r6 = __getPrototypeOfNoTraps__(getParentEnvironment(0)[4]);
    // CODE → <CreateThisForSuper>: <Reg8: 3, Reg8: 6, Reg8: 4, UInt8: 2>
    // USED → r3 = __uninitialized_this_for_super__;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 4424>  # String: 'Woof' (String)
    r7 = "Woof"
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 3592>  # String: 'Rex' (String)
    r8 = "Rex"
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = __uninitialized_this_for_super__
    // CODE → <CallWithNewTarget>: <Reg8: 2, Reg8: 6, Reg8: 4, UInt8: 3>
    // USED → r2 = Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1]);
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])];
    // CODE → <LoadConstEmpty>: <Reg8: 2>
    // USED → r2 = /* empty */;
    // CODE → <ThrowIfThisInitialized>: <Reg8: 2>
    __throwIfThisInitialized__(/* empty */)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2259>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2387>  # String: 'Labrador' (String)
    // USED → r2 = "Labrador";
    // CODE → <PutByIdStrict>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 16255>  # String: 'breed' (Identifier)
    __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])].breed = "Labrador"
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])].makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])].makeSound()
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])].makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = __uninitialized_this_for_super__[Reflect.construct(__getPrototypeOfNoTraps__(getParentEnvironment(0)[4]), [r3, r4, r5], getParentEnvironment(0)[1])].makeSound()
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 5, string_id: 44>  # String: 'create' (Identifier)
    // USED → r3 = getParentEnvironment(0)[1].create;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2777>  # String: 'Buddy' (String)
    // USED → r2 = "Buddy";
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r3 = getParentEnvironment(0)[1].create("Buddy");
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = getParentEnvironment(0)[1].create("Buddy").makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = getParentEnvironment(0)[1].create("Buddy").makeSound()
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4251>  # String: '__BC:Classes/ClassTests/classTest/end' (String)
    // USED → r1 = "__BC:Classes/ClassTests/classTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/classTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}