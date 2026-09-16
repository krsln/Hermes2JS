function ?anon_0_parallelAwaitTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 4>
    // USED → r0 = r1[4];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[4];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → addr: 13 | <JStrictEqualLong>: <Addr32: 469, Reg8: 0, Reg8: 4>  # Address: 000001e2
    if (r0 === 2) goto label_482;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
    // USED → r3 = param1;
    // CODE → addr: 26 | <Mov>: <Reg8: 5, Reg8: 2>
    r5 = r1[4]
    // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 6, UInt8: 3>
    // USED → r6 = 3;
    // CODE → addr: 32 | <JStrictEqualLong>: <Addr32: 417, Reg8: 5, Reg8: 6>  # Address: 000001c1
    if (r5 === 3) goto label_449;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 4>
    r1[4] = 2
    // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 3>
    r5 = r1[3]
    // CODE → addr: 50 | <LoadConstZero>: <Reg8: 11>
    // USED → r11 = 0;
    // CODE → addr: 52 | <JStrictEqualLong>: <Addr32: 233, Reg8: 11, Reg8: 5>  # Address: 0000011d
    if (0 === r5) goto label_285;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 59 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 62 | <JStrictEqualLong>: <Addr32: 214, Reg8: 3, Reg8: 5>  # Address: 00000114
    if (param1 === 1) goto label_276;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 69 | <JStrictEqualLong>: <Addr32: 188, Reg8: 3, Reg8: 4>  # Address: 00000101
    if (param1 === 2) goto label_257;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 76 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = param2
    // CODE → addr: 80 | <Mov>: <Reg8: 5, Reg8: 0>
    r5 = param2
    // CODE → addr: 83 | <IteratorBegin>: <Reg8: 8, Reg8: 5>
    r8 = GetIterator(r5)
    // CODE → addr: 86 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
    r1[0] = param2
    // CODE → addr: 90 | <LoadConstUndefined>: <Reg8: 9>
    // USED → r9 = undefined;
    // CODE → addr: 92 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 9>
    r1[1] = undefined
    // CODE → addr: 96 | <Mov>: <Reg8: 7, Reg8: 8>
    // USED → r7 = r8;
    // CODE → addr: 99 | <IteratorNext>: <Reg8: 5, Reg8: 7, Reg8: 5>
    r5 = r8.next()
    // CODE → addr:103 | <Mov>: <Reg8: 12, Reg8: 7>
    // USED → r12 = r8;
    // CODE → addr:106 | <StrictEq>: <Reg8: 7, Reg8: 12, Reg8: 9>
    // USED → r7 = r8 === undefined;
    // CODE → addr:110 | <JmpTrue>: <Addr8: 7, Reg8: 7>  # Address: 00000075
    if (r8 === undefined) goto label_117;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:113 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = r5
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:117 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 2>
    // USED → r8 = r1[2];
    // CODE → addr:121 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 1>
    // USED → r5 = r1[1];
    // CODE → addr:125 | <StoreToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 5>
    r1[2][0] = r1[1]
    // CODE → addr:129 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 9>
    r1[1] = undefined
    // CODE → addr:133 | <Mov>: <Reg8: 5, Reg8: 12>
    r5 = r8
    // CODE → addr:136 | <JmpTrue>: <Addr8: 37, Reg8: 7>  # Address: 000000ad
    if (r8 === undefined) goto label_173;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:139 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 1, UInt8: 0>
    r10 = r1[0]
    // CODE → addr:143 | <Mov>: <Reg8: 8, Reg8: 12>
    // USED → r8 = r8;
    // CODE → addr:146 | <IteratorNext>: <Reg8: 10, Reg8: 8, Reg8: 10>
    r10 = r8.next()
    // CODE → addr:150 | <StrictEq>: <Reg8: 9, Reg8: 8, Reg8: 9>
    // USED → r9 = r8 === undefined;
    // CODE → addr:154 | <Mov>: <Reg8: 7, Reg8: 9>
    r7 = r8 === undefined
    // CODE → addr:157 | <Mov>: <Reg8: 5, Reg8: 8>
    r5 = r8
    // CODE → addr:160 | <JmpTrue>: <Addr8: 13, Reg8: 9>  # Address: 000000ad
    if (r8 === undefined) goto label_173;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:163 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 10>
    r1[1] = r10
    // CODE → addr:167 | <Mov>: <Reg8: 7, Reg8: 9>
    // USED → r7 = r8 === undefined;
    // CODE → addr:170 | <Mov>: <Reg8: 5, Reg8: 8>
    // USED → r5 = r8;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:173 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 1, UInt8: 2>
    // USED → r9 = r1[2];
    // CODE → addr:177 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 1>
    // USED → r8 = r1[1];
    // CODE → addr:181 | <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 8>
    r1[2][1] = r1[1]
    // CODE → addr:185 | <JmpTrue>: <Addr8: 6, Reg8: 7>  # Address: 000000bf
    if (r8 === undefined) goto label_191;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:188 | <IteratorClose>: <Reg8: 5, UInt8: 0>
    r8.return()
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:191 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 2>
    // USED → r7 = r1[2];
    // CODE → addr:195 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:197 | <TryGetById>: <Reg8: 10, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:203 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:208 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 0>
    r8 = r1[2][0]
    // CODE → addr:212 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 7, UInt8: 1>
    r7 = r1[2][1]
    // CODE → addr:216 | <Call3>: <Reg8: 7, Reg8: 9, Reg8: 10, Reg8: 8, Reg8: 7>
    console.log(r8, r7)
    // CODE → addr:222 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:228 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:233 | <LoadConstString>: <Reg8: 5, string_id: 4921>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
    // USED → r5 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
    // CODE → addr:237 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end")
    // CODE → addr:242 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:245 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:249 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:255 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:257 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:260 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:264 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:270 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:274 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:276 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:279 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:283 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:285 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:288 | <JStrictEqualLong>: <Addr32: 141, Reg8: 3, Reg8: 5>  # Address: 000001ad
    if (param1 === 1) goto label_429;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:295 | <JStrictEqual>: <Addr8: 115, Reg8: 3, Reg8: 4>  # Address: 0000019a
    if (param1 === 2) goto label_410;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:299 | <CreateTopLevelEnvironment>: <Reg8: 8, UInt32: 2>
    // USED → r8 = __environment__;
    // CODE → addr:305 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 8>
    r1[2] = __environment__
    // CODE → addr:309 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:311 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 7>
    __environment__[0] = undefined
    // CODE → addr:315 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 1, Reg8: 7>
    __environment__[1] = undefined
    // CODE → addr:319 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:321 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:327 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:332 | <LoadConstString>: <Reg8: 8, string_id: 4922>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
    // USED → r8 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
    // CODE → addr:336 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start")
    // CODE → addr:341 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 26>  # String: 'Promise' (Identifier)
    // USED → r9 = Promise;
    // CODE → addr:347 | <GetById>: <Reg8: 8, Reg8: 9, UInt8: 3, string_id: 6842>  # String: 'all' (Identifier)
    // USED → r8 = Promise.all;
    // CODE → addr:353 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1)
    // CODE → addr:356 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 0>
    // USED → r10 = r7[0];
    // CODE → addr:360 | <Call2>: <Reg8: 12, Reg8: 10, Reg8: 11, Reg8: 5>
    r12 = r7[0].call(r11, 1)
    // CODE → addr:365 | <NewArray>: <Reg8: 7, UInt16: 2>
    r7 = []
    // CODE → addr:369 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 12, UInt8: 0>
    r7[0] = r12
    // CODE → addr:373 | <Call2>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 4>
    r10 = r7[0].call(r11, 2)
    // CODE → addr:378 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 10, UInt8: 1>
    r7[1] = r10
    // CODE → addr:382 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    r7 = Promise.all(r7)
    // CODE → addr:387 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
    r1[3] = 1
    // CODE → addr:391 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = 1
    // CODE → addr:394 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 5>
    r1[4] = 1
    // CODE → addr:398 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
    r5 = { "value": null, "done": false }
    // CODE → addr:404 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
    r5.slot_0 = r7
    // CODE → addr:408 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:410 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:413 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:417 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:423 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
    r5.slot_0 = param2
    // CODE → addr:427 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:429 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:432 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:436 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:438 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:440 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:443 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
    r1[4] = 3
    // CODE → addr:447 | <Throw>: <Reg8: 5>
    throw r5;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:449 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr:452 | <JStrictEqual>: <Addr8: 28, Reg8: 3, Reg8: 5>  # Address: 000001e0
    if (param1 === 1) goto label_480;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:456 | <JStrictEqual>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 000001d4
    if (param1 === 2) goto label_468;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:460 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:466 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:468 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r3 = { "value": null, "done": true }
    // CODE → addr:474 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
    r3.slot_0 = param2
    // CODE → addr:478 | <Ret>: <Reg8: 3>
    return r3;
    // ──────────────── Block 25 ──────────────── 
    // CODE → addr:480 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 26 ──────────────── 
    // CODE → addr:482 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:485 | <Mov>: <Reg8: 2, Reg8: 0>
    r2 = 3
    // CODE → addr:488 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 0>
    r1[4] = 3
    // CODE → addr:492 | <LoadConstString>: <Reg8: 14, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
    r14 = "Generator functions may not be called on executing generators"
    // CODE → addr:496 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r0 = throwTypeError(r14, r13)
}