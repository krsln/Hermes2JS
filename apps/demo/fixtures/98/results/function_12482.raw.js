function simpleGeneratorTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    // USED → r0 = r1[0];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[0];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 13 | <JStrictEqualLong>: <Addr32: 367, Reg8: 0, Reg8: 4>  # Address: 0000017c
    if (r0 === 2) goto label_380;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 26 | <Mov>: <Reg8: 5, Reg8: 2>
    r5 = r1[0]
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 32 | <JStrictEqualLong>: <Addr32: 315, Reg8: 5, Reg8: 6>  # Address: 0000015b
    if (r5 === 3) goto label_347;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
    r1[0] = 2
    // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 1>
    r7 = r1[1]
    // CODE → addr: 50 | <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → addr: 52 | <JStrictEqualLong>: <Addr32: 204, Reg8: 5, Reg8: 7>  # Address: 00000100
    if (0 === r7) goto label_256;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 59 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 62 | <JStrictEqualLong>: <Addr32: 139, Reg8: 5, Reg8: 7>  # Address: 000000c9
    if (1 === r7) goto label_201;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 69 | <JStrictEqual>: <Addr8: 77, Reg8: 4, Reg8: 7>  # Address: 00000092
    if (2 === r7) goto label_146;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 73 | <JStrictEqual>: <Addr8: 64, Reg8: 3, Reg8: 5>  # Address: 00000089
    if (param1 === 1) goto label_137;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 77 | <JStrictEqual>: <Addr8: 41, Reg8: 3, Reg8: 4>  # Address: 00000076
    if (param1 === 2) goto label_118;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 81 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr: 83 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 89 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr: 94 | <LoadConstString>: <Reg8: 7, string_id: 4948>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
    // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
    // CODE → addr: 98 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
    // CODE → addr:103 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:106 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:110 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:116 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:118 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:121 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:125 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:131 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7.slot_0 = param2
    // CODE → addr:135 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:137 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:140 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:144 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:146 | <JStrictEqual>: <Addr8: 46, Reg8: 3, Reg8: 5>  # Address: 000000c0
    if (param1 === 1) goto label_192;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:150 | <JStrictEqual>: <Addr8: 23, Reg8: 3, Reg8: 4>  # Address: 000000ad
    if (param1 === 2) goto label_173;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:154 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 6>
    r1[1] = 3
    // CODE → addr:158 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:161 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = 1
    // CODE → addr:165 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 48816>  # Object: {'value': 3, 'done': false}
    r7 = { "value": 3, "done": false }
    // CODE → addr:171 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:173 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:176 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:180 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:186 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7.slot_0 = param2
    // CODE → addr:190 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:192 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:195 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:199 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:201 | <JStrictEqual>: <Addr8: 46, Reg8: 3, Reg8: 5>  # Address: 000000f7
    if (param1 === 1) goto label_247;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:205 | <JStrictEqual>: <Addr8: 23, Reg8: 3, Reg8: 4>  # Address: 000000e4
    if (param1 === 2) goto label_228;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:209 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
    r1[1] = 2
    // CODE → addr:213 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:216 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = 1
    // CODE → addr:220 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 1525>  # Object: {'value': 2, 'done': false}
    r5 = { "value": 2, "done": false }
    // CODE → addr:226 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:228 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:231 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:235 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:241 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:245 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:247 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:250 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:254 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:256 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:259 | <JStrictEqual>: <Addr8: 68, Reg8: 3, Reg8: 5>  # Address: 00000147
    if (param1 === 1) goto label_327;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:263 | <JStrictEqual>: <Addr8: 45, Reg8: 3, Reg8: 4>  # Address: 00000134
    if (param1 === 2) goto label_308;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:267 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:269 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr:275 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:280 | <LoadConstString>: <Reg8: 7, string_id: 4949>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
    // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
    // CODE → addr:284 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
    // CODE → addr:289 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = 1
    // CODE → addr:293 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:296 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = 1
    // CODE → addr:300 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 48810>  # Object: {'value': 1, 'done': false}
    r5 = { "value": 1, "done": false }
    // CODE → addr:306 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:308 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:311 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:315 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:321 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:325 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:327 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:330 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:334 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 25 ──────────────── 
    // CODE → addr:336 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:338 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:341 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
    r1[0] = 3
    // CODE → addr:345 | <Throw>: <Reg8: 5>
    throw r5;
    // ──────────────── Block 26 ──────────────── 
    // CODE → addr:347 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:350 | <JStrictEqual>: <Addr8: 28, Reg8: 3, Reg8: 5>  # Address: 0000017a
    if (param1 === 1) goto label_378;
    // ──────────────── Block 27 ──────────────── 
    // CODE → addr:354 | <JStrictEqual>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 0000016e
    if (param1 === 2) goto label_366;
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr:358 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:364 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 29 ──────────────── 
    // CODE → addr:366 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:372 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
    r3.slot_0 = param2
    // CODE → addr:376 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 30 ──────────────── 
    // CODE → addr:378 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 31 ──────────────── 
    // CODE → addr:380 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:383 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 3
    // CODE → addr:386 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = 3
    // CODE → addr:390 | <LoadConstString>: <Reg8: 10, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
    r10 = "Generator functions may not be called on executing generators"
    // CODE → addr:394 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r0 = throwTypeError(r10, r9)
}