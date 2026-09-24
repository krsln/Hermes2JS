async function _anon_0_callAsyncTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 2>
    // USED → r0 = r1[2];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[2];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 13 | <JStrictEqualLong>: <Addr32: 516, Reg8: 0, Reg8: 4>  # Address: 00000211
    if (r0 === 2) goto label_529;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 26 | <Mov>: <Reg8: 5, Reg8: 2>
    r5 = r1[2]
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 32 | <JStrictEqualLong>: <Addr32: 464, Reg8: 5, Reg8: 6>  # Address: 000001f0
    if (r5 === 3) goto label_496;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 4>
    r1[2] = 2
    // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 1>
    r7 = r1[1]
    // CODE → addr: 50 | <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → addr: 52 | <JStrictEqualLong>: <Addr32: 332, Reg8: 5, Reg8: 7>  # Address: 00000180
    if (0 === r7) goto label_384;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 59 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 62 | <JStrictEqualLong>: <Addr32: 249, Reg8: 5, Reg8: 7>  # Address: 00000137
    if (1 === r7) goto label_311;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 69 | <JStrictEqualLong>: <Addr32: 160, Reg8: 4, Reg8: 7>  # Address: 000000e5
    if (2 === r7) goto label_229;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 76 | <JStrictEqual>: <Addr8: 77, Reg8: 6, Reg8: 7>  # Address: 00000099
    if (3 === r7) goto label_153;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr: 80 | <JStrictEqual>: <Addr8: 64, Reg8: 3, Reg8: 5>  # Address: 00000090
    if (param1 === 1) goto label_144;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 84 | <JStrictEqual>: <Addr8: 41, Reg8: 3, Reg8: 4>  # Address: 0000007d
    if (param1 === 2) goto label_125;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 88 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr: 90 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:101 | <LoadConstString>: <Reg8: 7, string_id: 4919>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
    // USED → r7 = "__BC:Functions/AsyncTests/callAsyncTests/end";
    // CODE → addr:105 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
    // CODE → addr:110 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:113 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:117 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r7 = { "value": undefined, "done": true }
    // CODE → addr:123 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:125 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:128 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:132 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:138 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7.slot_0 = param2
    // CODE → addr:142 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:144 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:147 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:151 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:153 | <JStrictEqual>: <Addr8: 67, Reg8: 3, Reg8: 5>  # Address: 000000dc
    if (param1 === 1) goto label_220;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:157 | <JStrictEqual>: <Addr8: 44, Reg8: 3, Reg8: 4>  # Address: 000000c9
    if (param1 === 2) goto label_201;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:161 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:165 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 4>
    // USED → r8 = r1[0][4];
    // CODE → addr:169 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:171 | <Call1>: <Reg8: 8, Reg8: 8, Reg8: 7>
    r8 = r1[0][4].call(undefined)
    // CODE → addr:175 | <LoadConstUInt8>: <Reg8: 7, UInt8: 4>
    // USED → r7 = 4;
    // CODE → addr:178 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 7>
    r1[1] = 4
    // CODE → addr:182 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:185 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
    r1[2] = 1
    // CODE → addr:189 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r7 = { "value": null, "done": false }
    // CODE → addr:195 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 8, UInt8: 0>
    r7.slot_0 = r8
    // CODE → addr:199 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:201 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:204 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:208 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:214 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7.slot_0 = param2
    // CODE → addr:218 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:220 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:223 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:227 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:229 | <JStrictEqual>: <Addr8: 73, Reg8: 3, Reg8: 5>  # Address: 0000012e
    if (param1 === 1) goto label_302;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:233 | <JStrictEqual>: <Addr8: 50, Reg8: 3, Reg8: 4>  # Address: 0000011b
    if (param1 === 2) goto label_283;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:237 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:241 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 3>
    // USED → r9 = r1[0][3];
    // CODE → addr:245 | <LoadConstUndefined>: <Reg8: 8>
    // USED → r8 = undefined;
    // CODE → addr:247 | <NewArrayWithBuffer>: <Reg8: 7, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    r7 = [1, 2, 3]
    // CODE → addr:255 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 8, Reg8: 7>
    r8 = r1[0][3].call(undefined, r7)
    // CODE → addr:260 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 6>
    r1[1] = 3
    // CODE → addr:264 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:267 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
    r1[2] = 1
    // CODE → addr:271 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r7 = { "value": null, "done": false }
    // CODE → addr:277 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 8, UInt8: 0>
    r7.slot_0 = r8
    // CODE → addr:281 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:283 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:286 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:290 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r7 = { "value": null, "done": true }
    // CODE → addr:296 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7.slot_0 = param2
    // CODE → addr:300 | <Ret>: <Reg8: 7>
    return r7;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:302 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:305 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:309 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:311 | <JStrictEqual>: <Addr8: 64, Reg8: 3, Reg8: 5>  # Address: 00000177
    if (param1 === 1) goto label_375;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:315 | <JStrictEqual>: <Addr8: 41, Reg8: 3, Reg8: 4>  # Address: 00000164
    if (param1 === 2) goto label_356;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:319 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:323 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 2>
    // USED → r8 = r1[0][2];
    // CODE → addr:327 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:329 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
    r7 = r1[0][2].call(undefined)
    // CODE → addr:333 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
    r1[1] = 2
    // CODE → addr:337 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:340 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
    r1[2] = 1
    // CODE → addr:344 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r5 = { "value": null, "done": false }
    // CODE → addr:350 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
    r5.slot_0 = r7
    // CODE → addr:354 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:356 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:359 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:363 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:369 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:373 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 25 ──────────────── 
    // CODE → addr:375 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:378 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:382 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 26 ──────────────── 
    // CODE → addr:384 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:387 | <JStrictEqual>: <Addr8: 89, Reg8: 3, Reg8: 5>  # Address: 000001dc
    if (param1 === 1) goto label_476;
    // ──────────────── Block 27 ──────────────── 
    // CODE → addr:391 | <JStrictEqual>: <Addr8: 66, Reg8: 3, Reg8: 4>  # Address: 000001c9
    if (param1 === 2) goto label_457;
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr:395 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1)
    // CODE → addr:398 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = r7
    // CODE → addr:402 | <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → addr:404 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:410 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:415 | <LoadConstString>: <Reg8: 8, string_id: 4920>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
    // USED → r8 = "__BC:Functions/AsyncTests/callAsyncTests/start";
    // CODE → addr:419 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
    // CODE → addr:424 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 1>
    // USED → r8 = r7[1];
    // CODE → addr:428 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:430 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
    r7 = r7[1]()
    // CODE → addr:434 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = 1
    // CODE → addr:438 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:441 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
    r1[2] = 1
    // CODE → addr:445 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r5 = { "value": null, "done": false }
    // CODE → addr:451 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
    r5.slot_0 = r7
    // CODE → addr:455 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 29 ──────────────── 
    // CODE → addr:457 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:460 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:464 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:470 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:474 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 30 ──────────────── 
    // CODE → addr:476 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:479 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:483 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 31 ──────────────── 
    // CODE → addr:485 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:487 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:490 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:494 | <Throw>: <Reg8: 5>
    throw r5;
    // ──────────────── Block 32 ──────────────── 
    // CODE → addr:496 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:499 | <JStrictEqual>: <Addr8: 28, Reg8: 3, Reg8: 5>  # Address: 0000020f
    if (param1 === 1) goto label_527;
    // ──────────────── Block 33 ──────────────── 
    // CODE → addr:503 | <JStrictEqual>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 00000203
    if (param1 === 2) goto label_515;
    // ──────────────── Block 34 ──────────────── 
    // CODE → addr:507 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r3 = { "value": undefined, "done": true }
    // CODE → addr:513 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 35 ──────────────── 
    // CODE → addr:515 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:521 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
    r3.slot_0 = param2
    // CODE → addr:525 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 36 ──────────────── 
    // CODE → addr:527 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 37 ──────────────── 
    // CODE → addr:529 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:532 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 3
    // CODE → addr:535 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
    r1[2] = 3
    // CODE → addr:539 | <LoadConstString>: <Reg8: 11, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
    r11 = "Generator functions may not be called on executing generators"
    // CODE → addr:543 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r0 = throwTypeError(r11, r10)
}