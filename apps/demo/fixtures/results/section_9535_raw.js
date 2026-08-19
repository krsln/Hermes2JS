function privateStaticTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    r5 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 4, string_id: 4735>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/start' (String)
    // USED → r4 = "__BC:Classes/PrivateStaticTests/privateStaticTest/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 4>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/start")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 5, UInt8: 0>
    // USED → r4 = r5[0];
    // CODE → addr: 29 | <CreateThisForNew>: <Reg8: 6, Reg8: 4, UInt8: 2>
    r6 = CreateThisForNew(r4)
    // CODE → addr: 33 | <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000031
    // → r5 = getParentEnvironment(0)
    if (typeof r5[0] === "function") goto label_49;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 41 | <LoadConstString>: <Reg8: 13, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r13 = "Trying to call a non-function"
    // CODE → addr: 45 | <CallBuiltin>: <Reg8: 6, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r6 = throwTypeError(r4, r5)
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r6 = r4.prototype;
    // CODE → addr: 54 | <NewObjectWithParent>: <Reg8: 9, Reg8: 6>
    r9 = Object.create(r4.prototype)
    // CODE → addr: 57 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 5, UInt8: 5>
    // USED → r12 = r5[5];
    // CODE → addr: 61 | <PrivateIsIn>: <Reg8: 1, Reg8: 12, Reg8: 9, Reg8: 0>
    // USED → r1 = r5[5] in r9;
    // CODE → addr: 66 | <JmpTrueLong>: <Addr32: 329, Reg8: 1>  # Address: 0000018b
    // → r9 = Object.create(r4.prototype)
    if (r5[5] in r9) goto label_395;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 72 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 74 | <AddOwnPrivateBySym>: <Reg8: 9, Reg8: 1, Reg8: 12>
    r9.#__private_1__ = r5[5]
    // CODE → addr: 78 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 5, UInt8: 6>
    // USED → r10 = r5[6];
    // CODE → addr: 82 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 84 | <AddOwnPrivateBySym>: <Reg8: 9, Reg8: 0, Reg8: 10>
    r9.#__private_0__ = r5[6]
    // CODE → addr: 88 | <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 94 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 99 | <LoadConstString>: <Reg8: 11, string_id: 4728>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
    // USED → r11 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
    // CODE → addr:103 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 11>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → addr:108 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 2>
    // USED → r8 = r5[2];
    // CODE → addr:112 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 4>
    r7 = r5[4]
    // CODE → addr:116 | <GetOwnPrivateBySym>: <Reg8: 6, Reg8: 8, UInt8: 1, Reg8: 7>
    r6 = r5[2].#__private_7__
    // CODE → addr:121 | <Inc>: <Reg8: 6, Reg8: 6>
    // USED → r6 = r6 + 1;
    // CODE → addr:124 | <PutOwnPrivateBySym>: <Reg8: 8, Reg8: 6, UInt8: 1, Reg8: 7>
    r5[2].#__private_7__ = r6 + 1
    // CODE → addr:129 | <CreateThisForNew>: <Reg8: 6, Reg8: 4, UInt8: 2>
    r6 = CreateThisForNew(r4)
    // CODE → addr:133 | <JmpTypeOfIs>: <Addr32: 16, Reg8: 4, UInt16: 128>  # Address: 00000095
    if (typeof r5[0] === "function") goto label_149;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:141 | <LoadConstString>: <Reg8: 13, string_id: 4299>  # String: 'Trying to call a non-function' (String)
    r13 = "Trying to call a non-function"
    // CODE → addr:145 | <CallBuiltin>: <Reg8: 6, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r6 = throwTypeError(r4, r5)
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:149 | <GetByIdShort>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r6 = r4.prototype;
    // CODE → addr:154 | <NewObjectWithParent>: <Reg8: 6, Reg8: 6>
    r6 = Object.create(r4.prototype)
    // CODE → addr:157 | <PrivateIsIn>: <Reg8: 2, Reg8: 12, Reg8: 6, Reg8: 2>
    // USED → r2 = r5[5] in r6;
    // CODE → addr:162 | <JmpTrueLong>: <Addr32: 225, Reg8: 2>  # Address: 00000183
    // → r6 = Object.create(r4.prototype)
    if (r5[5] in r6) goto label_387;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:168 | <AddOwnPrivateBySym>: <Reg8: 6, Reg8: 1, Reg8: 12>
    r6.#__private_1__ = r5[5]
    // CODE → addr:172 | <AddOwnPrivateBySym>: <Reg8: 6, Reg8: 0, Reg8: 10>
    r6.#__private_0__ = r5[6]
    // CODE → addr:176 | <TryGetById>: <Reg8: 10, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:182 | <GetByIdShort>: <Reg8: 6, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:187 | <Call2>: <Reg8: 6, Reg8: 6, Reg8: 10, Reg8: 11>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → addr:192 | <GetOwnPrivateBySym>: <Reg8: 6, Reg8: 8, UInt8: 1, Reg8: 7>
    r6 = r5[2].#__private_7__
    // CODE → addr:197 | <Inc>: <Reg8: 6, Reg8: 6>
    // USED → r6 = r6 + 1;
    // CODE → addr:200 | <PutOwnPrivateBySym>: <Reg8: 8, Reg8: 6, UInt8: 1, Reg8: 7>
    r5[2].#__private_7__ = r6 + 1
    // CODE → addr:205 | <GetById>: <Reg8: 6, Reg8: 9, UInt8: 3, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r6 = r9.increment;
    // CODE → addr:211 | <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    r6 = r9.increment()
    // CODE → addr:215 | <GetById>: <Reg8: 6, Reg8: 9, UInt8: 3, string_id: 11123>  # String: 'increment' (Identifier)
    // USED → r6 = r9.increment;
    // CODE → addr:221 | <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    r6 = r9.increment()
    // CODE → addr:225 | <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → addr:228 | <PutByIdStrict>: <Reg8: 9, Reg8: 0, UInt8: 0, string_id: 211>  # String: 'value' (Identifier)
    r9.value = 200
    // CODE → addr:234 | <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:240 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:245 | <GetByIdShort>: <Reg8: 6, Reg8: 9, UInt8: 4, string_id: 211>  # String: 'value' (Identifier)
    // USED → r6 = r9.value;
    // CODE → addr:250 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r9.value)
    // CODE → addr:255 | <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:261 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:266 | <GetById>: <Reg8: 6, Reg8: 9, UInt8: 5, string_id: 8661>  # String: 'describe' (Identifier)
    // USED → r6 = r9.describe;
    // CODE → addr:272 | <Call1>: <Reg8: 6, Reg8: 6, Reg8: 9>
    // USED → r6 = r9.describe();
    // CODE → addr:276 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r6)
    // CODE → addr:281 | <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:287 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:292 | <GetById>: <Reg8: 6, Reg8: 4, UInt8: 6, string_id: 9807>  # String: 'instanceCount' (Identifier)
    // USED → r6 = r4.instanceCount;
    // CODE → addr:298 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log(r4.instanceCount)
    // CODE → addr:303 | <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:309 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:314 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 1>
    r8 = r5[1]
    // CODE → addr:318 | <GetById>: <Reg8: 5, Reg8: 8, UInt8: 7, string_id: 11346>  # String: 'describeLabel' (Identifier)
    // USED → r5 = r8.describeLabel;
    // CODE → addr:324 | <Call1>: <Reg8: 5, Reg8: 5, Reg8: 8>
    // USED → r5 = r8.describeLabel();
    // CODE → addr:328 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log(r5)
    // CODE → addr:333 | <GetById>: <Reg8: 5, Reg8: 4, UInt8: 8, string_id: 7259>  # String: 'reset' (Identifier)
    // USED → r5 = r4.reset;
    // CODE → addr:339 | <Call1>: <Reg8: 5, Reg8: 5, Reg8: 4>
    r5 = r4.reset()
    // CODE → addr:343 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:349 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:354 | <GetById>: <Reg8: 4, Reg8: 4, UInt8: 6, string_id: 9807>  # String: 'instanceCount' (Identifier)
    // USED → r4 = r4.instanceCount;
    // CODE → addr:360 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log(r4.instanceCount)
    // CODE → addr:365 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:371 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:376 | <LoadConstString>: <Reg8: 3, string_id: 4734>  # String: '__BC:Classes/PrivateStaticTests/privateStaticTest/end' (String)
    // USED → r3 = "__BC:Classes/PrivateStaticTests/privateStaticTest/end";
    // CODE → addr:380 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Classes/PrivateStaticTests/privateStaticTest/end")
    // CODE → addr:385 | <Ret>: <Reg8: 1>
    return undefined;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:387 | <LoadConstString>: <Reg8: 13, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
    r13 = "Cannot initialize private field twice."
    // CODE → addr:391 | <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r3 = throwTypeError(r1, r2)
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:395 | <LoadConstString>: <Reg8: 13, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
    r13 = "Cannot initialize private field twice."
    // CODE → addr:399 | <CallBuiltin>: <Reg8: 3, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r3 = throwTypeError(r1, r2)
}