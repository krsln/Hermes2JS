function classTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4524>  # String: '__BC:Classes/ClassTests/classTest/start' (String)
    // USED → r1 = "__BC:Classes/ClassTests/classTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/classTest/start")
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 5>
    // USED → r5 = getEnvironment(0)[5];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 207>  # String: 'prototype' (Identifier)
    // USED → r2 = getEnvironment(0)[5].prototype;
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]);
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 3156>  # String: 'Generic' (String)
    r7 = "Generic"
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 602>  # String: '...' (String)
    r6 = "..."
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    r8 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])
    // CODE → <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4);
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    // USED → r2 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])[new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4)];
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r3 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])[new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4)].makeSound;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])[new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4)].makeSound()
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 10660>  # String: 'description' (Identifier)
    // USED → r2 = createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])[new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4)].description;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log(createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5])[new getEnvironment(0)[5](getEnvironment(0)[5].prototype, createThis(getEnvironment(0)[5].prototype, getEnvironment(0)[5]), r4)].description)
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 6>
    // USED → r5 = getEnvironment(0)[6];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 207>  # String: 'prototype' (Identifier)
    // USED → r2 = getEnvironment(0)[6].prototype;
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]);
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 3854>  # String: 'Rex' (String)
    r7 = "Rex"
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 3366>  # String: 'Labrador' (String)
    r6 = "Labrador"
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    r8 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])
    // CODE → <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console);
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])[new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console)];
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r2 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])[new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console)].makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])[new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console)].makeSound()
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r2 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])[new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console)].makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6])[new getEnvironment(0)[6](getEnvironment(0)[6].prototype, createThis(getEnvironment(0)[6].prototype, getEnvironment(0)[6]), globalThis.console)].makeSound()
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 6>
    // USED → r3 = getEnvironment(0)[6];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 6, string_id: 104>  # String: 'create' (Identifier)
    // USED → r2 = getEnvironment(0)[6].create;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 702>  # String: 'Buddy' (String)
    // USED → r1 = "Buddy";
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 1>
    // USED → r2 = getEnvironment(0)[6].create("Buddy");
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 10199>  # String: 'makeSound' (Identifier)
    // USED → r1 = getEnvironment(0)[6].create("Buddy").makeSound;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = getEnvironment(0)[6].create("Buddy").makeSound()
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4523>  # String: '__BC:Classes/ClassTests/classTest/end' (String)
    // USED → r0 = "__BC:Classes/ClassTests/classTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Classes/ClassTests/classTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}