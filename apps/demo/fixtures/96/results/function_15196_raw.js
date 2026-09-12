function classTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4539>  # String: '__BC:Classes/ClassTests/classTest/start' (String)
    // USED → r1 = "__BC:Classes/ClassTests/classTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/classTest/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 5>
    r5 = r1[5]
    // CODE → addr: 29 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = r5.prototype;
    // CODE → addr: 34 | <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = CreateThis(r2);
    // CODE → addr: 38 | <LoadConstString>: <Reg8: 7, string_id: 3213>  # String: 'Generic' (String)
    // USED → r7 = "Generic";
    // CODE → addr: 42 | <LoadConstString>: <Reg8: 6, string_id: 597>  # String: '...' (String)
    // USED → r6 = "...";
    // CODE → addr: 46 | <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = CreateThis(r2);
    // CODE → addr: 49 | <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new r1[5]("...", "Generic");
    // CODE → addr: 53 | <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
    r2 = new r1[5]("...", "Generic")
    // CODE → addr: 57 | <GetById>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r3 = r2.makeSound;
    // CODE → addr: 63 | <Call1>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = r2.makeSound()
    // CODE → addr: 67 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 73 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 78 | <GetById>: <Reg8: 2, Reg8: 2, UInt8: 5, string_id: 10805>  # String: 'description' (Identifier)
    // USED → r2 = r2.description;
    // CODE → addr: 84 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.description)
    // CODE → addr: 89 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 6>
    r5 = r1[6]
    // CODE → addr: 93 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = r5.prototype;
    // CODE → addr: 98 | <CreateThis>: <Reg8: 3, Reg8: 2, Reg8: 5>
    // USED → r3 = CreateThis(r2);
    // CODE → addr:102 | <LoadConstString>: <Reg8: 7, string_id: 3886>  # String: 'Rex' (String)
    // USED → r7 = "Rex";
    // CODE → addr:106 | <LoadConstString>: <Reg8: 6, string_id: 3434>  # String: 'Labrador' (String)
    // USED → r6 = "Labrador";
    // CODE → addr:110 | <Mov>: <Reg8: 8, Reg8: 3>
    // USED → r8 = CreateThis(r2);
    // CODE → addr:113 | <Construct>: <Reg8: 2, Reg8: 5, UInt8: 3>
    // USED → r2 = new r1[6]("Labrador", "Rex");
    // CODE → addr:117 | <SelectObject>: <Reg8: 3, Reg8: 3, Reg8: 2>
    r3 = new r1[6]("Labrador", "Rex")
    // CODE → addr:121 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → addr:127 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → addr:131 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r2 = r3.makeSound;
    // CODE → addr:137 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.makeSound()
    // CODE → addr:141 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 6>
    r3 = r1[6]
    // CODE → addr:145 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 6, string_id: 103>  # String: 'create' (Identifier)
    // USED → r2 = r3.create;
    // CODE → addr:150 | <LoadConstString>: <Reg8: 1, string_id: 709>  # String: 'Buddy' (String)
    // USED → r1 = "Buddy";
    // CODE → addr:154 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 1>
    r2 = r3.create("Buddy")
    // CODE → addr:159 | <GetById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 10340>  # String: 'makeSound' (Identifier)
    // USED → r1 = r2.makeSound;
    // CODE → addr:165 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
    r1 = r2.makeSound()
    // CODE → addr:169 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:175 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:180 | <LoadConstString>: <Reg8: 0, string_id: 4537>  # String: '__BC:Classes/ClassTests/classTest/end' (String)
    // USED → r0 = "__BC:Classes/ClassTests/classTest/end";
    // CODE → addr:184 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/ClassTests/classTest/end")
    // CODE → addr:189 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:191 | <Ret>: <Reg8: 0>
    return r0;
}