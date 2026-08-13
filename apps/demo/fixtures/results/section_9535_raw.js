function privateStaticTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    // USED → r5 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4735>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/start' (String)
    // USED → r4 = "__BC:Classes/PrivateStaticTests/privateStaticTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 4>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 5, UInt8: 0>
    // USED → r4 = getParentEnvironment(0)[0];
    // CODE → <CreateThisForNew>: <Reg8: 6, Reg8: 4, UInt8: 2>
    r6 = __uninitialized_this_for_new__
    // CODE → <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000031
    if (typeof getParentEnvironment(0)[0] === "function") goto label_49;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 13, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r13 = "Trying to call a non-function"
    // CODE → <CallBuiltin>: <Reg8: 6, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r6 = copyDataProperties(r4, r5)
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r6 = getParentEnvironment(0)[0].prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 9, Reg8: 6>
    // USED → r9 = Object.create(getParentEnvironment(0)[0].prototype);
    // CODE → <LoadFromEnvironment>: <Reg8: 12, Reg8: 5, UInt8: 5>
    // USED → r12 = getParentEnvironment(0)[5];
    // CODE → <PrivateIsIn>: <Reg8: 1, Reg8: 12, Reg8: 9, Reg8: 0>
    // USED → r1 = getParentEnvironment(0)[5] in Object.create(getParentEnvironment(0)[0].prototype);
    // CODE → <JmpTrueLong>: <Addr32: 329, Reg8: 1>  # Address: 0000018b
    if (getParentEnvironment(0)[5] in Object.create(getParentEnvironment(0)[0].prototype)) goto label_395;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <AddOwnPrivateBySym>: <Reg8: 9, Reg8: 1, Reg8: 12>
    Object.create(getParentEnvironment(0)[0].prototype).#__private_1__ = getParentEnvironment(0)[5]
    // CODE → <LoadFromEnvironment>: <Reg8: 10, Reg8: 5, UInt8: 6>
    // USED → r10 = getParentEnvironment(0)[6];
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <AddOwnPrivateBySym>: <Reg8: 9, Reg8: 0, Reg8: 10>
    Object.create(getParentEnvironment(0)[0].prototype).#__private_0__ = getParentEnvironment(0)[6]
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 11, string_id: 4728>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
    // USED → r11 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 11>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 2>
    // USED → r8 = getParentEnvironment(0)[2];
    // CODE → <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 4>
    r7 = getParentEnvironment(0)[4]
    // CODE → <GetOwnPrivateBySym>: <Reg8: 6, Reg8: 8, UInt8: 1, Reg8: 7>
    r6 = getParentEnvironment(0)[2].#__private_7__
    // CODE → <Inc>: <Reg8: 6, Reg8: 6>
    // USED → r6 = r6 + 1;
    // CODE → <PutOwnPrivateBySym>: <Reg8: 8, Reg8: 6, UInt8: 1, Reg8: 7>
    getParentEnvironment(0)[2].#__private_7__ = r6 + 1
    // CODE → <CreateThisForNew>: <Reg8: 6, Reg8: 4, UInt8: 2>
    r6 = __uninitialized_this_for_new__
    // CODE → <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000095
    if (typeof getParentEnvironment(0)[0] === "function") goto label_149;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 13, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r13 = "Trying to call a non-function"
    // CODE → <CallBuiltin>: <Reg8: 6, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r6 = copyDataProperties(r4, r5)
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r6 = getParentEnvironment(0)[0].prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 6, Reg8: 6>
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype);
    // CODE → <PrivateIsIn>: <Reg8: 2, Reg8: 12, Reg8: 6, Reg8: 2>
    // USED → r2 = getParentEnvironment(0)[5] in Object.create(getParentEnvironment(0)[0].prototype);
    // CODE → <JmpTrueLong>: <Addr32: 225, Reg8: 2>  # Address: 00000183
    if (getParentEnvironment(0)[5] in Object.create(getParentEnvironment(0)[0].prototype)) goto label_387;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <AddOwnPrivateBySym>: <Reg8: 6, Reg8: 1, Reg8: 12>
    Object.create(getParentEnvironment(0)[0].prototype).#__private_1__ = getParentEnvironment(0)[5]
    // CODE → <AddOwnPrivateBySym>: <Reg8: 6, Reg8: 0, Reg8: 10>
    Object.create(getParentEnvironment(0)[0].prototype).#__private_0__ = getParentEnvironment(0)[6]
    // CODE → <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 10, Reg8: 11>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → <GetOwnPrivateBySym>: <Reg8: 6, Reg8: 8, UInt8: 1, Reg8: 7>
    r6 = getParentEnvironment(0)[2].#__private_7__
    // CODE → <Inc>: <Reg8: 6, Reg8: 6>
    // USED → r6 = r6 + 1;
    // CODE → <PutOwnPrivateBySym>: <Reg8: 8, Reg8: 6, UInt8: 1, Reg8: 7>
    getParentEnvironment(0)[2].#__private_7__ = r6 + 1
    // CODE → <GetById>: <Reg8: 6, Reg8: 9, UInt8: 3, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype).increment;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    r6 = Object.create(getParentEnvironment(0)[0].prototype).increment()
    // CODE → <GetById>: <Reg8: 6, Reg8: 9, UInt8: 3, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype).increment;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    r6 = Object.create(getParentEnvironment(0)[0].prototype).increment()
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → <PutByIdStrict>: <Reg8: 9, Reg8: 0, UInt8: 0, string_id: 211>  # String: 'value' (Identifier)
    Object.create(getParentEnvironment(0)[0].prototype).value = 200
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 9, UInt8: 4, string_id: 211>  # String: 'value' (Identifier)
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype).value;
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r6)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 6, Reg8: 9, UInt8: 5, string_id: 8661>  # String: 'describe' (Identifier)
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype).describe;
    // CODE → <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    // USED → r6 = Object.create(getParentEnvironment(0)[0].prototype).describe();
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r6)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 6, Reg8: 4, UInt8: 6, string_id: 9807>  # String: 'instanceCount' (Identifier)
    // USED → r6 = getParentEnvironment(0)[0].instanceCount;
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r6)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 1>
    // USED → r8 = getParentEnvironment(0)[1];
    // CODE → <GetById>: <Reg8: 5, Reg8: 8, UInt8: 7, string_id: 11346>  # String: 'describeLabel' (Identifier)
    // USED → r5 = getParentEnvironment(0)[1].describeLabel;
    // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 8>
    // USED → r5 = getParentEnvironment(0)[1].describeLabel();
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log(r5)
    // CODE → <GetById>: <Reg8: 5, Reg8: 4, UInt8: 8, string_id: 7259>  # String: 'reset' (Identifier)
    // USED → r5 = getParentEnvironment(0)[0].reset;
    // CODE → <Call1>: <Reg8: 5, Reg8: 5, Reg8: 4>
    r5 = getParentEnvironment(0)[0].reset()
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 6, string_id: 9807>  # String: 'instanceCount' (Identifier)
    // USED → r4 = getParentEnvironment(0)[0].instanceCount;
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log(r4)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4734>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/end' (String)
    // USED → r3 = "__BC:Classes/PrivateStaticTests/privateStaticTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/end")
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 13, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
    r13 = "Cannot initialize private field twice."
    // CODE → <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r3 = copyDataProperties(r1, r2)
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 13, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
    r13 = "Cannot initialize private field twice."
    // CODE → <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
    r3 = copyDataProperties(r1, r2)
}