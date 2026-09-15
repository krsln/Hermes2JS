function generatorTryFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    // USED → r0 = r1[0];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[0];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 13 | <JStrictEqualLong>: <Addr32: 405, Reg8: 0, Reg8: 4>  # Address: 000001a2
    if (r0 === 2) goto label_418;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 26 | <Mov>: <Reg8: 12, Reg8: 2>
    r12 = r1[0]
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
    // USED → r7 = 3;
    // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 35 | <LoadConstZero>: <Reg8: 11>
    // USED → r11 = 0;
    // CODE → addr: 37 | <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → addr: 39 | <LoadConstString>: <Reg8: 9, string_id: 4942>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/start' (String)
    // USED → r9 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/start";
    // CODE → addr: 43 | <LoadConstString>: <Reg8: 8, string_id: 4940>  # String: '__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup' (String)
    // USED → r8 = "__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup";
    // CODE → addr: 47 | <JStrictEqualLong>: <Addr32: 341, Reg8: 12, Reg8: 7>  # Address: 00000184
    if (r12 === 3) goto label_388;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 54 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 57 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
    r1[0] = 2
    // CODE → addr: 61 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 1>
    r12 = r1[1]
    // CODE → addr: 65 | <JStrictEqualLong>: <Addr32: 213, Reg8: 11, Reg8: 12>  # Address: 00000116
    if (0 === r12) goto label_278;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 72 | <JStrictEqualLong>: <Addr32: 177, Reg8: 5, Reg8: 12>  # Address: 000000f9
    if (1 === r12) goto label_249;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 79 | <JStrictEqual>: <Addr8: 95, Reg8: 4, Reg8: 12>  # Address: 000000ae
    if (2 === r12) goto label_174;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 83 | <JStrictEqual>: <Addr8: 82, Reg8: 3, Reg8: 5>  # Address: 000000a5
    if (param1 === 1) goto label_165;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 87 | <JStrictEqual>: <Addr8: 39, Reg8: 3, Reg8: 4>  # Address: 0000007e
    if (param1 === 2) goto label_126;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 91 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
    r1[3] = 0
    // CODE → addr: 95 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr:106 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:111 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:114 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:118 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r12 = { "value": null, "done": true }
    // CODE → addr:124 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:126 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
    r1[3] = 0
    // CODE → addr:130 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr:136 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr:141 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:146 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:149 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:153 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r12 = { "value": null, "done": true }
    // CODE → addr:159 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
    r12.slot_0 = param2
    // CODE → addr:163 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:165 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:168 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:172 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:174 | <JStrictEqual>: <Addr8: 66, Reg8: 3, Reg8: 5>  # Address: 000000f0
    if (param1 === 1) goto label_240;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:178 | <JStrictEqual>: <Addr8: 23, Reg8: 3, Reg8: 4>  # Address: 000000c9
    if (param1 === 2) goto label_201;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:182 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 7>
    r1[1] = 3
    // CODE → addr:186 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:189 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = 1
    // CODE → addr:193 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48826>  # Object: {'value': 'b', 'done': false}
    r12 = { "value": "b", "done": false }
    // CODE → addr:199 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:201 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
    r1[3] = 0
    // CODE → addr:205 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr:211 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr:216 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:221 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:224 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:228 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r12 = { "value": null, "done": true }
    // CODE → addr:234 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
    r12.slot_0 = param2
    // CODE → addr:238 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:240 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:243 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:247 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:249 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 2>
    // USED → r12 = r1[2];
    // CODE → addr:253 | <Mov>: <Reg8: 6, Reg8: 12>
    r6 = r1[2]
    // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
    r1[3] = 0
    // CODE → addr:260 | <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r14 = console;
    // CODE → addr:266 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r13 = console.log;
    // CODE → addr:271 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
    // CODE → addr:276 | <Throw>: <Reg8: 12>
    throw r12;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:278 | <JStrictEqual>: <Addr8: 66, Reg8: 3, Reg8: 5>  # Address: 00000158
    if (param1 === 1) goto label_344;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:282 | <JStrictEqual>: <Addr8: 43, Reg8: 3, Reg8: 4>  # Address: 00000145
    if (param1 === 2) goto label_325;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:286 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r13 = console;
    // CODE → addr:292 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r12 = console.log;
    // CODE → addr:297 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 9>
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start")
    // CODE → addr:302 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
    r1[3] = 1
    // CODE → addr:306 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
    r1[1] = 2
    // CODE → addr:310 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:313 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = 1
    // CODE → addr:317 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48822>  # Object: {'value': 'a', 'done': false}
    r12 = { "value": "a", "done": false }
    // CODE → addr:323 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:325 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:328 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:332 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r12 = { "value": null, "done": true }
    // CODE → addr:338 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
    r12.slot_0 = param2
    // CODE → addr:342 | <Ret>: <Reg8: 12>
    return r12;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:344 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:347 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:351 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:353 | <Catch>: <Reg8: 12>
    // USED → r12 = caughtException;
    // CODE → addr:355 | <Mov>: <Reg8: 6, Reg8: 12>
    r6 = caughtException
    // CODE → addr:358 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 12>
    r1[2] = caughtException
    // CODE → addr:362 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 3>
    r12 = r1[3]
    // CODE → addr:366 | <JStrictEqual>: <Addr8: 13, Reg8: 11, Reg8: 12>  # Address: 0000017b
    if (0 === r12) goto label_379;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:370 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = 1
    // CODE → addr:374 | <JmpLong>: <Addr32: -320>  # Address: 00000036
    goto label_54;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:379 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:382 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = 3
    // CODE → addr:386 | <Throw>: <Reg8: 6>
    throw r6;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:388 | <JStrictEqual>: <Addr8: 28, Reg8: 3, Reg8: 5>  # Address: 000001a0
    if (param1 === 1) goto label_416;
    // ──────────────── Block 25 ──────────────── 
    // CODE → addr:392 | <JStrictEqual>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 00000194
    if (param1 === 2) goto label_404;
    // ──────────────── Block 26 ──────────────── 
    // CODE → addr:396 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:402 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 27 ──────────────── 
    // CODE → addr:404 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:410 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
    r3.slot_0 = param2
    // CODE → addr:414 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr:416 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 29 ──────────────── 
    // CODE → addr:418 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:421 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 3
    // CODE → addr:424 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = 3
    // CODE → addr:428 | <LoadConstString>: <Reg8: 15, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
    r15 = "Generator functions may not be called on executing generators"
    // CODE → addr:432 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r0 = throwTypeError(r15, r14)
}