function nestedArrayDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → addr:  2 | <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → addr:  4 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → addr:  6 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  8 | <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → addr: 10 | <TryGetById>: <Reg8: 4, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 16 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 21 | <LoadConstString>: <Reg8: 1, string_id: 4967>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start";
    // CODE → addr: 25 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start")
    // CODE → addr: 30 | <NewArray>: <Reg8: 2, UInt16: 3>
    r2 = []
    // CODE → addr: 34 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 42665>  # Array: [1, 2]
    r1 = [1, 2]
    // CODE → addr: 42 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2[0] = r1
    // CODE → addr: 46 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 48477>  # Array: [3, 4]
    r1 = [3, 4]
    // CODE → addr: 54 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 1>
    r2[1] = r1
    // CODE → addr: 58 | <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 15101>  # Array: [5, 6]
    r1 = [5, 6]
    // CODE → addr: 66 | <DefineOwnInDenseArray>: <Reg8: 2, Reg8: 1, UInt8: 2>
    r2[2] = r1
    // CODE → addr: 70 | <Mov>: <Reg8: 6, Reg8: 2>
    r6 = r2
    // CODE → addr: 73 | <IteratorBegin>: <Reg8: 1, Reg8: 6>
    r1 = GetIterator(r6)
    // CODE → addr: 76 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = r2
    // CODE → addr: 79 | <IteratorNext>: <Reg8: 2, Reg8: 1, Reg8: 2>
    r2 = r1.next()
    // CODE → addr: 83 | <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = r1;
    // CODE → addr: 86 | <StrictEq>: <Reg8: 4, Reg8: 4, Reg8: 3>
    // USED → r4 = r1 === undefined;
    // CODE → addr: 90 | <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE → addr: 92 | <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 00000062
    // → r1 = GetIterator(r6)
    if (r1 === undefined) goto label_98;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 95 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = r2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 98 | <Mov>: <Reg8: 11, Reg8: 5>
    r11 = r2
    // CODE → addr:101 | <IteratorBegin>: <Reg8: 2, Reg8: 11>
    r2 = GetIterator(r11)
    // CODE → addr:104 | <Mov>: <Reg8: 5, Reg8: 11>
    r5 = r2
    // CODE → addr:107 | <IteratorNext>: <Reg8: 12, Reg8: 2, Reg8: 5>
    r12 = r2.next()
    // CODE → addr:111 | <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = r2;
    // CODE → addr:114 | <StrictEq>: <Reg8: 5, Reg8: 5, Reg8: 3>
    // USED → r5 = r2 === undefined;
    // CODE → addr:118 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:120 | <JmpTrue>: <Addr8: 6, Reg8: 5>  # Address: 0000007e
    // → r2 = GetIterator(r11)
    if (r2 === undefined) goto label_126;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:123 | <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r12;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:126 | <Mov>: <Reg8: 8, Reg8: 9>
    // USED → r8 = r12;
    // CODE → addr:129 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:131 | <JmpTrue>: <Addr8: 28, Reg8: 5>  # Address: 0000009f
    if (r2 === undefined) goto label_159;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:134 | <IteratorNext>: <Reg8: 12, Reg8: 2, Reg8: 11>
    r12 = r2.next()
    // CODE → addr:138 | <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = r2;
    // CODE → addr:141 | <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 3>
    // USED → r11 = r2 === undefined;
    // CODE → addr:145 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:147 | <Mov>: <Reg8: 5, Reg8: 11>
    r5 = r2 === undefined
    // CODE → addr:150 | <JmpTrue>: <Addr8: 9, Reg8: 11>  # Address: 0000009f
    if (r2 === undefined) goto label_159;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:153 | <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r12;
    // CODE → addr:156 | <Mov>: <Reg8: 5, Reg8: 11>
    // USED → r5 = r2 === undefined;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:159 | <Mov>: <Reg8: 7, Reg8: 9>
    // USED → r7 = r12;
    // CODE → addr:162 | <JmpTrue>: <Addr8: 6, Reg8: 5>  # Address: 000000a8
    if (r2 === undefined) goto label_168;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:165 | <IteratorClose>: <Reg8: 2, UInt8: 0>
    r2.return()
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:168 | <Mov>: <Reg8: 5, Reg8: 4>
    r5 = r1 === undefined
    // CODE → addr:171 | <JmpTrue>: <Addr8: 17, Reg8: 4>  # Address: 000000bc
    if (r1 === undefined) goto label_188;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:174 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = r2
    // CODE → addr:177 | <IteratorNext>: <Reg8: 2, Reg8: 1, Reg8: 2>
    r2 = r1.next()
    // CODE → addr:181 | <Mov>: <Reg8: 2, Reg8: 1>
    // USED → r2 = r1;
    // CODE → addr:184 | <StrictEq>: <Reg8: 5, Reg8: 2, Reg8: 3>
    // USED → r5 = r1 === undefined;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:188 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:190 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = r1 === undefined
    // CODE → addr:193 | <JmpTrue>: <Addr8: 28, Reg8: 5>  # Address: 000000dd
    if (r1 === undefined) goto label_221;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:196 | <IteratorNext>: <Reg8: 11, Reg8: 1, Reg8: 6>
    r11 = r1.next()
    // CODE → addr:200 | <Mov>: <Reg8: 6, Reg8: 1>
    // USED → r6 = r1;
    // CODE → addr:203 | <StrictEq>: <Reg8: 6, Reg8: 6, Reg8: 3>
    // USED → r6 = r1 === undefined;
    // CODE → addr:207 | <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → addr:209 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = r1 === undefined
    // CODE → addr:212 | <JmpTrue>: <Addr8: 9, Reg8: 6>  # Address: 000000dd
    if (r1 === undefined) goto label_221;
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:215 | <Mov>: <Reg8: 9, Reg8: 11>
    // USED → r9 = r11;
    // CODE → addr:218 | <Mov>: <Reg8: 2, Reg8: 6>
    // USED → r2 = r1 === undefined;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:221 | <Mov>: <Reg8: 12, Reg8: 9>
    r12 = r11
    // CODE → addr:224 | <IteratorBegin>: <Reg8: 6, Reg8: 12>
    r6 = GetIterator(r12)
    // CODE → addr:227 | <Mov>: <Reg8: 9, Reg8: 12>
    r9 = r11
    // CODE → addr:230 | <IteratorNext>: <Reg8: 9, Reg8: 6, Reg8: 9>
    r9 = r6.next()
    // CODE → addr:234 | <Mov>: <Reg8: 9, Reg8: 6>
    // USED → r9 = r6;
    // CODE → addr:237 | <StrictEq>: <Reg8: 9, Reg8: 9, Reg8: 3>
    // USED → r9 = r6 === undefined;
    // CODE → addr:241 | <LoadConstUndefined>: <Reg8: 11>
    r11 = undefined
    // CODE → addr:243 | <JmpTrue>: <Addr8: 28, Reg8: 9>  # Address: 0000010f
    // → r6 = GetIterator(r12)
    if (r6 === undefined) goto label_271;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:246 | <IteratorNext>: <Reg8: 13, Reg8: 6, Reg8: 12>
    r13 = r6.next()
    // CODE → addr:250 | <Mov>: <Reg8: 12, Reg8: 6>
    // USED → r12 = r6;
    // CODE → addr:253 | <StrictEq>: <Reg8: 12, Reg8: 12, Reg8: 3>
    // USED → r12 = r6 === undefined;
    // CODE → addr:257 | <LoadConstUndefined>: <Reg8: 11>
    r11 = undefined
    // CODE → addr:259 | <Mov>: <Reg8: 9, Reg8: 12>
    r9 = r6 === undefined
    // CODE → addr:262 | <JmpTrue>: <Addr8: 9, Reg8: 12>  # Address: 0000010f
    if (r6 === undefined) goto label_271;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:265 | <Mov>: <Reg8: 11, Reg8: 13>
    // USED → r11 = r13;
    // CODE → addr:268 | <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r6 === undefined;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:271 | <Mov>: <Reg8: 0, Reg8: 11>
    // USED → r0 = r13;
    // CODE → addr:274 | <JmpTrue>: <Addr8: 9, Reg8: 9>  # Address: 0000011b
    if (r6 === undefined) goto label_283;
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:277 | <Mov>: <Reg8: 9, Reg8: 6>
    // USED → r9 = r6;
    // CODE → addr:280 | <IteratorClose>: <Reg8: 9, UInt8: 0>
    r6.return()
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:283 | <JmpTrue>: <Addr8: 9, Reg8: 2>  # Address: 00000124
    if (r1 === undefined) goto label_292;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:286 | <Mov>: <Reg8: 9, Reg8: 1>
    // USED → r9 = r1;
    // CODE → addr:289 | <IteratorClose>: <Reg8: 9, UInt8: 0>
    r1.return()
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:292 | <TryGetById>: <Reg8: 11, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:298 | <GetByIdShort>: <Reg8: 9, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:303 | <Call4>: <Reg8: 0, Reg8: 9, Reg8: 11, Reg8: 8, Reg8: 7, Reg8: 0>
    console.log(r8, r7, r0)
    // CODE → addr:310 | <NewArrayWithBuffer>: <Reg8: 17, UInt16: 1, UInt16: 1, UInt16: 20024>  # Array: [10]
    r17 = [10]
    // CODE → addr:318 | <IteratorBegin>: <Reg8: 7, Reg8: 17>
    r7 = GetIterator(r17)
    // CODE → addr:321 | <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → addr:323 | <Mov>: <Reg8: 0, Reg8: 17>
    r0 = r17
    // CODE → addr:326 | <IteratorNext>: <Reg8: 0, Reg8: 7, Reg8: 0>
    r0 = r7.next()
    // CODE → addr:330 | <Mov>: <Reg8: 8, Reg8: 7>
    // USED → r8 = r7;
    // CODE → addr:333 | <StrictEq>: <Reg8: 9, Reg8: 8, Reg8: 3>
    // USED → r9 = r7 === undefined;
    // CODE → addr:337 | <JmpTrue>: <Addr8: 10, Reg8: 9>  # Address: 0000015b
    // → r7 = GetIterator(r17)
    if (r7 === undefined) goto label_347;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:340 | <Mov>: <Reg8: 12, Reg8: 0>
    r12 = r0
    // CODE → addr:343 | <JStrictNotEqual>: <Addr8: 6, Reg8: 0, Reg8: 3>  # Address: 0000015d
    if (r0 !== undefined) goto label_349;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:347 | <LoadConstZero>: <Reg8: 12>
    // USED → r12 = 0;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:349 | <Mov>: <Reg8: 15, Reg8: 12>
    // USED → r15 = 0;
    // CODE → addr:352 | <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → addr:354 | <Mov>: <Reg8: 11, Reg8: 9>
    r11 = r7 === undefined
    // CODE → addr:357 | <JmpTrue>: <Addr8: 29, Reg8: 9>  # Address: 00000182
    if (r7 === undefined) goto label_386;
    // ──────────────── Block 25 ──────────────── 
    // CODE → addr:360 | <Mov>: <Reg8: 0, Reg8: 17>
    r0 = r17
    // CODE → addr:363 | <IteratorNext>: <Reg8: 13, Reg8: 7, Reg8: 0>
    r13 = r7.next()
    // CODE → addr:367 | <Mov>: <Reg8: 0, Reg8: 7>
    // USED → r0 = r7;
    // CODE → addr:370 | <StrictEq>: <Reg8: 0, Reg8: 0, Reg8: 3>
    // USED → r0 = r7 === undefined;
    // CODE → addr:374 | <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = r7 === undefined;
    // CODE → addr:377 | <JmpTrue>: <Addr8: 22, Reg8: 8>  # Address: 0000018f
    if (r7 === undefined) goto label_399;
    // ──────────────── Block 26 ──────────────── 
    // CODE → addr:380 | <Mov>: <Reg8: 12, Reg8: 13>
    // USED → r12 = r13;
    // CODE → addr:383 | <Mov>: <Reg8: 11, Reg8: 0>
    // USED → r11 = r7 === undefined;
    // ──────────────── Block 27 ──────────────── 
    // CODE → addr:386 | <Mov>: <Reg8: 0, Reg8: 12>
    r0 = r13
    // CODE → addr:389 | <Mov>: <Reg8: 8, Reg8: 11>
    // USED → r8 = r7 === undefined;
    // CODE → addr:392 | <Mov>: <Reg8: 11, Reg8: 8>
    r11 = r7 === undefined
    // CODE → addr:395 | <JStrictNotEqual>: <Addr8: 15, Reg8: 0, Reg8: 3>  # Address: 0000019a
    // → r0 = r13
    if (r0 !== undefined) goto label_410;
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr:399 | <LoadConstZero>: <Reg8: 12>
    // USED → r12 = 0;
    // CODE → addr:401 | <Mov>: <Reg8: 11, Reg8: 8>
    // USED → r11 = r7 === undefined;
    // CODE → addr:404 | <Jmp>: <Addr8: 6>  # Address: 0000019a
    goto label_410;
    // ──────────────── Block 29 ──────────────── 
    // CODE → addr:406 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:408 | <Jmp>: <Addr8: 99>  # Address: 000001fb
    goto label_507;
    // ──────────────── Block 30 ──────────────── 
    // CODE → addr:410 | <Mov>: <Reg8: 14, Reg8: 12>
    // USED → r14 = 0;
    // CODE → addr:413 | <NewArray>: <Reg8: 13, UInt16: 0>
    // USED → r13 = [];
    // CODE → addr:417 | <LoadConstUInt8>: <Reg8: 12, UInt8: 1>
    // USED → r12 = 1;
    // CODE → addr:420 | <LoadConstZero>: <Reg8: 16>
    // USED → r16 = 0;
    // CODE → addr:422 | <JmpTrue>: <Addr8: 40, Reg8: 11>  # Address: 000001ce
    if (r7 === undefined) goto label_462;
    // ──────────────── Block 31 ──────────────── 
    // CODE → addr:425 | <Mov>: <Reg8: 11, Reg8: 17>
    r11 = r17
    // CODE → addr:428 | <IteratorNext>: <Reg8: 19, Reg8: 7, Reg8: 11>
    r19 = r7.next()
    // CODE → addr:432 | <Mov>: <Reg8: 11, Reg8: 7>
    // USED → r11 = r7;
    // CODE → addr:435 | <StrictEq>: <Reg8: 11, Reg8: 11, Reg8: 3>
    // USED → r11 = r7 === undefined;
    // CODE → addr:439 | <Mov>: <Reg8: 18, Reg8: 16>
    // USED → r18 = 0;
    // CODE → addr:442 | <JmpTrue>: <Addr8: 20, Reg8: 11>  # Address: 000001ce
    if (r7 === undefined) goto label_462;
    // ──────────────── Block 32 ──────────────── 
    // CODE → addr:445 | <PutByValStrict>: <Reg8: 13, Reg8: 18, Reg8: 19>
    r13[0] = r19
    // CODE → addr:449 | <AddN>: <Reg8: 16, Reg8: 18, Reg8: 12>
    r16 = r18 + 1
    // CODE → addr:453 | <Jmp>: <Addr8: -28>  # Address: 000001a9
    goto label_425;
    // ──────────────── Block 33 ──────────────── 
    // CODE → addr:455 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:457 | <Mov>: <Reg8: 8, Reg8: 11>
    r8 = r7 === undefined
    // CODE → addr:460 | <Jmp>: <Addr8: 47>  # Address: 000001fb
    goto label_507;
    // ──────────────── Block 34 ──────────────── 
    // CODE → addr:462 | <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = console;
    // CODE → addr:468 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = console.log;
    // CODE → addr:473 | <Call4>: <Reg8: 11, Reg8: 11, Reg8: 12, Reg8: 15, Reg8: 14, Reg8: 13>
    console.log(r15, r14, r13)
    // CODE → addr:480 | <TryGetById>: <Reg8: 12, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r12 = console;
    // CODE → addr:486 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r11 = console.log;
    // CODE → addr:491 | <LoadConstString>: <Reg8: 10, string_id: 4966>  # String: '__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end' (String)
    // USED → r10 = "__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end";
    // CODE → addr:495 | <Call2>: <Reg8: 10, Reg8: 11, Reg8: 12, Reg8: 10>
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end")
    // CODE → addr:500 | <Ret>: <Reg8: 3>
    return r3;
    // CODE → addr:502 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:504 | <Mov>: <Reg8: 8, Reg8: 9>
    // USED → r8 = r7 === undefined;
    // ──────────────── Block 35 ──────────────── 
    // CODE → addr:507 | <JmpTrue>: <Addr8: 6, Reg8: 8>  # Address: 00000201
    if (r7 === undefined) goto label_513;
    // ──────────────── Block 36 ──────────────── 
    // CODE → addr:510 | <IteratorClose>: <Reg8: 7, UInt8: 1>
    r7.return()
    // ──────────────── Block 37 ──────────────── 
    // CODE → addr:513 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr:515 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:517 | <IteratorClose>: <Reg8: 6, UInt8: 1>
    r6.return()
    // CODE → addr:520 | <Throw>: <Reg8: 0>
    throw r0;
    // CODE → addr:522 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:524 | <Jmp>: <Addr8: 20>  # Address: 00000220
    goto label_544;
    // ──────────────── Block 38 ──────────────── 
    // CODE → addr:526 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:528 | <Mov>: <Reg8: 2, Reg8: 5>
    r2 = r1 === undefined
    // CODE → addr:531 | <Jmp>: <Addr8: 13>  # Address: 00000220
    goto label_544;
    // ──────────────── Block 39 ──────────────── 
    // CODE → addr:533 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:535 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = r1 === undefined
    // CODE → addr:538 | <Jmp>: <Addr8: 6>  # Address: 00000220
    goto label_544;
    // ──────────────── Block 40 ──────────────── 
    // CODE → addr:540 | <Catch>: <Reg8: 0>
    r0 = caughtException
    // CODE → addr:542 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // ──────────────── Block 41 ──────────────── 
    // CODE → addr:544 | <JmpTrue>: <Addr8: 6, Reg8: 2>  # Address: 00000226
    if (undefined) goto label_550;
    // ──────────────── Block 42 ──────────────── 
    // CODE → addr:547 | <IteratorClose>: <Reg8: 1, UInt8: 1>
    r1.return()
    // ──────────────── Block 43 ──────────────── 
    // CODE → addr:550 | <Throw>: <Reg8: 0>
    throw r0;
}