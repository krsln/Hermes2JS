function privateStaticTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4554>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/start' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/privateStaticTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/start")
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 8>
    r2 = r1[8]
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r3 = r2.prototype;
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = CreateThis(r3);
    // CODE → <Mov>: <Reg8: 7, Reg8: 3>
    // USED → r7 = CreateThis(r3);
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new r1[8]();
    // CODE → <SelectObject>: <Reg8: 5, Reg8: 3, Reg8: 2>
    r5 = new r1[8]()
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 8>
    r3 = r1[8]
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = r3.prototype;
    // CODE → <CreateThis>: <Reg8: 7, Reg8: 2, Reg8: 3>
    // USED → r7 = CreateThis(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 3, UInt8: 1>
    r2 = new r1[8]()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 200>
    // USED → r2 = 200;
    // CODE → <PutById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 205>  # String: 'value' (Identifier)
    new r1[8]().value = 200
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 205>  # String: 'value' (Identifier)
    // USED → r2 = r5.value;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r5.value)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 6, string_id: 10172>  # String: 'describe' (Identifier)
    // USED → r2 = r5.describe;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.describe();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 8>
    r2 = r1[8]
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 7, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r2 = r2.instanceCount;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.instanceCount)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 10>
    r5 = r1[10]
    // CODE → <GetById>: <Reg8: 2, Reg8: 5, UInt8: 8, string_id: 8574>  # String: 'describeLabel' (Identifier)
    // USED → r2 = r5.describeLabel;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.describeLabel();
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 8>
    r3 = r1[8]
    // CODE → <GetById>: <Reg8: 2, Reg8: 3, UInt8: 9, string_id: 7840>  # String: 'reset' (Identifier)
    // USED → r2 = r3.reset;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.reset()
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 8>
    r1 = r1[8]
    // CODE → <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r1 = r1.instanceCount;
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1.instanceCount)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4551>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/end' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/privateStaticTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}