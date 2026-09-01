function classTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 3, string_id: 3972>  # String: '__BC:Classes/ClassTests/classTest/start' (String)
    // USED → r3 = "__BC:Classes/ClassTests/classTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/ClassTests/classTest/start")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 0>
    // USED → r3 = r2[0];
    // CODE → addr: 29 | <CreateThisForNew>: <Reg8: 4, Reg8: 3, UInt8: 2>
    r4 = CreateThisForNew(r3)
    // CODE → addr: 33 | <JmpTypeOfIs>: <Addr32: 16, Reg8: 3, UInt16: 128>  # Address: 00000031
    // → r2 = getParentEnvironment(0)
    if (typeof r2[0] === "function") goto label_49;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r8 = "Trying to call a non-function"
    // CODE → addr: 45 | <CallBuiltin>: <Reg8: 4, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r4 = throwTypeError(r8, r7)
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r3 = r3.prototype;
    // CODE → addr: 54 | <NewObjectWithParent>: <Reg8: 3, Reg8: 3>
    r3 = Object.create(r3.prototype)
    // CODE → addr: 57 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 63 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 68 | <LoadConstString>: <Reg8: 4, string_id: 2576>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r4 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → addr: 72 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Classes/ClassTests/Animal/constructor")
    // CODE → addr: 77 | <LoadConstString>: <Reg8: 4, string_id: 3351>  # String: 'Generic' (String)
    // USED → r4 = "Generic";
    // CODE → addr: 81 | <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 187>  # String: 'name' (Identifier)
    r3.name = "Generic"
    // CODE → addr: 87 | <LoadConstString>: <Reg8: 4, string_id: 765>  # String: '...' (String)
    // USED → r4 = "...";
    // CODE → addr: 91 | <PutByIdStrict>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 11958>  # String: 'sound' (Identifier)
    r3.sound = "..."
    // CODE → addr: 97 | <GetById>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r4 = r3.makeSound;
    // CODE → addr:103 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 3>
    r4 = r3.makeSound()
    // CODE → addr:107 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:113 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:118 | <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 11115>  # String: 'description' (Identifier)
    // USED → r3 = r3.description;
    // CODE → addr:124 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3.description)
    // CODE → addr:129 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 2, UInt8: 1>
    // USED → r4 = r2[1];
    // CODE → addr:133 | <CreateThisForNew>: <Reg8: 3, Reg8: 4, UInt8: 2>
    r3 = CreateThisForNew(r4)
    // CODE → addr:137 | <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000099
    if (typeof r2[1] === "function") goto label_153;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:145 | <LoadConstString>: <Reg8: 8, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r8 = "Trying to call a non-function"
    // CODE → addr:149 | <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r3 = throwTypeError(r8, r7)
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:153 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 4>
    // USED → r2 = r2[4];
    // CODE → addr:157 | <LoadParentNoTraps>: <Reg8: 6, Reg8: 2>
    r6 = __getPrototypeOfNoTraps__(r2[4])
    // CODE → addr:160 | <CreateThisForSuper>: <Reg8: 3, Reg8: 6, Reg8: 4, UInt8: 2>
    // USED → r3 = CreateThisForSuper(r6);
    // CODE → addr:165 | <LoadConstString>: <Reg8: 7, string_id: 4424>  # String: 'Woof' (String)
    r7 = "Woof"
    // CODE → addr:169 | <LoadConstString>: <Reg8: 8, string_id: 3592>  # String: 'Rex' (String)
    r8 = "Rex"
    // CODE → addr:173 | <Mov>: <Reg8: 9, Reg8: 3>
    r9 = CreateThisForSuper(r6)
    // CODE → addr:176 | <CallWithNewTarget>: <Reg8: 2, Reg8: 6, Reg8: 4, UInt8: 3>
    r2 = Reflect.construct(r6, [r3, r4, r5], r2[1])
    // CODE → addr:181 | <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = CreateThisForSuper(r6)[r2];
    // CODE → addr:185 | <LoadConstEmpty>: <Reg8: 2>
    // USED → r2 = /* empty */;
    // CODE → addr:187 | <ThrowIfThisInitialized>: <Reg8: 2>
    __throwIfThisInitialized__(/* empty */)
    // CODE → addr:189 | <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:195 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:200 | <LoadConstString>: <Reg8: 2, string_id: 2259>  # String: '__BC:Classes/ClassTests/Dog/constructor' (String)
    // USED → r2 = "__BC:Classes/ClassTests/Dog/constructor";
    // CODE → addr:204 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log("__BC:Classes/ClassTests/Dog/constructor")
    // CODE → addr:209 | <LoadConstString>: <Reg8: 2, string_id: 2387>  # String: 'Labrador' (String)
    // USED → r2 = "Labrador";
    // CODE → addr:213 | <PutByIdStrict>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 16255>  # String: 'breed' (Identifier)
    CreateThisForSuper(r6)[r2].breed = "Labrador"
    // CODE → addr:219 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → addr:225 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → addr:229 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → addr:235 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → addr:239 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 5, string_id: 44>  # String: 'create' (Identifier)
    // USED → r3 = r4.create;
    // CODE → addr:244 | <LoadConstString>: <Reg8: 2, string_id: 2777>  # String: 'Buddy' (String)
    // USED → r2 = "Buddy";
    // CODE → addr:248 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2>
    r3 = r4.create("Buddy")
    // CODE → addr:253 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 10532>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → addr:259 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → addr:263 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:269 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:274 | <LoadConstString>: <Reg8: 1, string_id: 4251>  # String: '__BC:Classes/ClassTests/classTest/end' (String)
    // USED → r1 = "__BC:Classes/ClassTests/classTest/end";
    // CODE → addr:278 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/classTest/end")
    // CODE → addr:283 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:285 | <Ret>: <Reg8: 0>
    return r0;
}