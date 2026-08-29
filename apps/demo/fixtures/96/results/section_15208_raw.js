function privateStaticTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4554>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/start' (String)
    // USED → r1 = "__BC:Classes/PrivateStaticTests/privateStaticTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/start")
    // CODE → addr: 22 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 8>
    r2 = r1[8]
    // CODE → addr: 29 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r3 = r2.prototype;
    // CODE → addr: 34 | <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
    // USED → r3 = CreateThis(r3);
    // CODE → addr: 38 | <Mov>: <Reg8: 7, Reg8: 3>
    // USED → r7 = CreateThis(r3);
    // CODE → addr: 41 | <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new r1[8]();
    // CODE → addr: 45 | <SelectObject>: <Reg8: 5, Reg8: 3, Reg8: 2>
    r5 = new r1[8]()
    // CODE → addr: 49 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 8>
    r3 = r1[8]
    // CODE → addr: 53 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 3, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = r3.prototype;
    // CODE → addr: 58 | <CreateThis>: <Reg8: 7, Reg8: 2, Reg8: 3>
    // USED → r7 = CreateThis(r2);
    // CODE → addr: 62 | <Construct>: <Reg8: 2, Reg8: 3, UInt8: 1>
    r2 = new r1[8]()
    // CODE → addr: 66 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → addr: 72 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → addr: 76 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 4, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r2 = r5.increment;
    // CODE → addr: 82 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    r2 = r5.increment()
    // CODE → addr: 86 | <LoadConstUInt8>: <Reg8: 2, UInt8: 200>
    // USED → r2 = 200;
    // CODE → addr: 89 | <PutById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 205>  # String: 'value' (Identifier)
    new r1[8]().value = 200
    // CODE → addr: 95 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:106 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 205>  # String: 'value' (Identifier)
    // USED → r2 = r5.value;
    // CODE → addr:111 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r5.value)
    // CODE → addr:116 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:122 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:127 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 6, string_id: 10172>  # String: 'describe' (Identifier)
    // USED → r2 = r5.describe;
    // CODE → addr:133 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.describe();
    // CODE → addr:137 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:142 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:148 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:153 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 8>
    r2 = r1[8]
    // CODE → addr:157 | <GetById>: <Reg8: 2, Reg8: 2, UInt8: 7, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r2 = r2.instanceCount;
    // CODE → addr:163 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2.instanceCount)
    // CODE → addr:168 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:174 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:179 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 10>
    r5 = r1[10]
    // CODE → addr:183 | <GetById>: <Reg8: 2, Reg8: 5, UInt8: 8, string_id: 8574>  # String: 'describeLabel' (Identifier)
    // USED → r2 = r5.describeLabel;
    // CODE → addr:189 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = r5.describeLabel();
    // CODE → addr:193 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:198 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 8>
    r3 = r1[8]
    // CODE → addr:202 | <GetById>: <Reg8: 2, Reg8: 3, UInt8: 9, string_id: 7840>  # String: 'reset' (Identifier)
    // USED → r2 = r3.reset;
    // CODE → addr:208 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
    r2 = r3.reset()
    // CODE → addr:212 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:218 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:223 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 8>
    r1 = r1[8]
    // CODE → addr:227 | <GetById>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r1 = r1.instanceCount;
    // CODE → addr:233 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1.instanceCount)
    // CODE → addr:238 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:244 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:249 | <LoadConstString>: <Reg8: 0, string_id: 4551>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/end' (String)
    // USED → r0 = "__BC:Classes/PrivateStaticTests/privateStaticTest/end";
    // CODE → addr:253 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/end")
    // CODE → addr:258 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:260 | <Ret>: <Reg8: 0>
    return r0;
}