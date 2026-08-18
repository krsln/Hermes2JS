function classTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4539>  # String: '__BC:Classes/ClassTests/classTest/start' (String)
    // USED → r1 = "__BC:Classes/ClassTests/classTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/classTest/start")
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 5>
    // USED → r5 = r1[5];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    r2 = r5.prototype
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = CreateThis(r2);
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 3213>  # String: 'Generic' (String)
    // USED → r7 = "Generic";
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 597>  # String: '...' (String)
    // USED → r6 = "...";
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new r1[5]("...", "Generic");
    // CODE → <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    r2 = new r1[5]("...", "Generic")
    // CODE → <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r3 = r2.makeSound;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = r2.makeSound()
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 10805>  # String: 'description' (Identifier)
    // USED → r2 = r2.description;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 6>
    // USED → r5 = r1[6];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    r2 = r5.prototype
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = CreateThis(r2);
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 3886>  # String: 'Rex' (String)
    // USED → r7 = "Rex";
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 3434>  # String: 'Labrador' (String)
    // USED → r6 = "Labrador";
    // CODE → <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new r1[6]("Labrador", "Rex");
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = new r1[6]("Labrador", "Rex")
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 6>
    r3 = r1[6]
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 6, string_id: 103>  # String: 'create' (Identifier)
    // USED → r2 = r3.create;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 709>  # String: 'Buddy' (String)
    // USED → r1 = "Buddy";
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 1>
    r2 = r3.create("Buddy")
    // CODE → <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = r2.makeSound;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r2.makeSound()
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4537>  # String: '__BC:Classes/ClassTests/classTest/end' (String)
    // USED → r0 = "__BC:Classes/ClassTests/classTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/ClassTests/classTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}