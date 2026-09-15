function generatorWithLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 3>
    // USED → r0 = r1[3];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[3];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 13 | <JStrictEqualLong>: <Addr32: 368, Reg8: 0, Reg8: 4>  # Address: 0000017d
    if (r0 === 2) goto label_381;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 26 | <Mov>: <Reg8: 5, Reg8: 2>
    r5 = r1[3]
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 32 | <JStrictEqualLong>: <Addr32: 316, Reg8: 5, Reg8: 6>  # Address: 0000015c
    if (r5 === 3) goto label_348;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 4>
    r1[3] = 2
    // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 2>
    r5 = r1[2]
    // CODE → addr: 50 | <LoadConstZero>: <Reg8: 8>
    // USED → r8 = 0;
    // CODE → addr: 52 | <JStrictEqual>: <Addr8: 46, Reg8: 8, Reg8: 5>  # Address: 00000062
    if (0 === r5) goto label_98;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 56 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 59 | <JStrictEqual>: <Addr8: 30, Reg8: 3, Reg8: 5>  # Address: 00000059
    if (param1 === 1) goto label_89;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 63 | <JStrictNotEqualLong>: <Addr32: 182, Reg8: 3, Reg8: 4>  # Address: 000000f5
    if (param1 !== 2) goto label_245;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 70 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr: 73 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr: 77 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr: 83 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr: 87 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 89 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr: 92 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr: 96 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 98 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:101 | <JStrictEqualLong>: <Addr32: 227, Reg8: 3, Reg8: 5>  # Address: 00000148
    if (param1 === 1) goto label_328;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:108 | <JStrictEqualLong>: <Addr32: 201, Reg8: 3, Reg8: 4>  # Address: 00000135
    if (param1 === 2) goto label_309;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:115 | <CreateTopLevelEnvironment>: <Reg8: 5, UInt32: 2>
    // USED → r5 = __environment__;
    // CODE → addr:121 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = __environment__
    // CODE → addr:125 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:129 | <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 7>
    __environment__[0] = r1[0]
    // CODE → addr:133 | <LoadConstUndefined>: <Reg8: 9>
    // USED → r9 = undefined;
    // CODE → addr:135 | <StoreNPToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 9>
    __environment__[1] = undefined
    // CODE → addr:139 | <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → addr:141 | <TryGetById>: <Reg8: 11, Reg8: 9, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:147 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr:152 | <LoadConstString>: <Reg8: 9, string_id: 4947>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/start' (String)
    // USED → r9 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/start";
    // CODE → addr:156 | <Call2>: <Reg8: 9, Reg8: 10, Reg8: 11, Reg8: 9>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start")
    // CODE → addr:161 | <StoreNPToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 8>
    __environment__[1] = 0
    // CODE → addr:165 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 1>
    r5 = __environment__[1]
    // CODE → addr:169 | <JNotLess>: <Addr8: 103, Reg8: 5, Reg8: 7>  # Address: 00000110
    if (!(r5 < r7)) goto label_272;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:173 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 1>
    // USED → r5 = r1[1];
    // CODE → addr:177 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 1>
    r7 = r1[1][1]
    // CODE → addr:181 | <JStrictEqual>: <Addr8: 42, Reg8: 7, Reg8: 4>  # Address: 000000df
    if (r7 === 2) goto label_223;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:185 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 1>
    // USED → r7 = r1[1][1];
    // CODE → addr:189 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 1>
    // USED → r5 = r1[1][1];
    // CODE → addr:193 | <LoadConstUInt8>: <Reg8: 8, UInt8: 1>
    r8 = 1
    // CODE → addr:196 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 8>
    r1[2] = r8
    // CODE → addr:200 | <Mov>: <Reg8: 2, Reg8: 8>
    r2 = r8
    // CODE → addr:203 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 8>
    r1[3] = r8
    // CODE → addr:207 | <Mul>: <Reg8: 7, Reg8: 7, Reg8: 5>
    r7 = r1[1][1] * r1[1][1]
    // CODE → addr:211 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r5 = { "value": null, "done": false }
    // CODE → addr:217 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
    r5.slot_0 = r7
    // CODE → addr:221 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:223 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:225 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:231 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:236 | <LoadConstString>: <Reg8: 5, string_id: 4944>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/skip' (String)
    // USED → r5 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/skip";
    // CODE → addr:240 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip")
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:245 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 1>
    // USED → r5 = r1[1];
    // CODE → addr:249 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 1>
    r7 = r1[1][1]
    // CODE → addr:253 | <Inc>: <Reg8: 7, Reg8: 7>
    r7 = r7 + 1
    // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 7>
    r1[1][1] = r7
    // CODE → addr:260 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 1>
    r7 = r1[1][1]
    // CODE → addr:264 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
    r5 = r1[1][0]
    // CODE → addr:268 | <JLess>: <Addr8: -95, Reg8: 7, Reg8: 5>  # Address: 000000ad
    if (r7 < r5) goto label_173;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:272 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:274 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:280 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:285 | <LoadConstString>: <Reg8: 5, string_id: 4943>  # String: '__BC:Functions/GeneratorTests/generatorWithLoopTest/end' (String)
    // USED → r5 = "__BC:Functions/GeneratorTests/generatorWithLoopTest/end";
    // CODE → addr:289 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end")
    // CODE → addr:294 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:297 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr:301 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:307 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:309 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:312 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr:316 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:322 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:326 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:328 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:331 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr:335 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:337 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:339 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:342 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 6>
    r1[3] = 3
    // CODE → addr:346 | <Throw>: <Reg8: 5>
    throw r5;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:348 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:351 | <JStrictEqual>: <Addr8: 28, Reg8: 3, Reg8: 5>  # Address: 0000017b
    if (param1 === 1) goto label_379;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:355 | <JStrictEqual>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 0000016f
    if (param1 === 2) goto label_367;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:359 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:365 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:367 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:373 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
    r3.slot_0 = param2
    // CODE → addr:377 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:379 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:381 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:384 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 3
    // CODE → addr:387 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    r1[3] = 3
    // CODE → addr:391 | <LoadConstString>: <Reg8: 12, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
    r12 = "Generator functions may not be called on executing generators"
    // CODE → addr:395 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r0 = throwTypeError(r12, r11)
}