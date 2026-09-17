async function* ?anon_0_asyncTryCatchTest() {
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 75 | <Mov>: <Reg8: 2, Reg8: 4>
    r2 = 2
    // CODE → addr: 78 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 4>
    r1[4] = 2
    // CODE → addr: 82 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 1>
    r18 = r1[1]
    // CODE → addr: 86 | <JStrictEqualLong>: <Addr32: 250, Reg8: 17, Reg8: 18>  # Address: 00000150
    if (0 === r18) goto label_336;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 93 | <JStrictEqualLong>: <Addr32: 214, Reg8: 5, Reg8: 18>  # Address: 00000133
    if (1 === r18) goto label_307;
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:100 | <JStrictEqualLong>: <Addr32: 132, Reg8: 4, Reg8: 18>  # Address: 000000e8
    if (2 === r18) goto label_232;
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr:107 | <JStrictEqual>: <Addr8: 116, Reg8: 3, Reg8: 5>  # Address: 000000df
    if (param1 === 1) goto label_223;
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:111 | <JStrictEqual>: <Addr8: 73, Reg8: 3, Reg8: 4>  # Address: 000000b8
    if (param1 === 2) goto label_184;
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr:115 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 0>
    // USED → r18 = r1[0];
    // CODE → addr:119 | <StoreToEnvironment>: <Reg8: 18, UInt8: 0, Reg8: 0>
    r1[0][0] = param2
    // CODE → addr:123 | <TryGetById>: <Reg8: 21, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r21 = console;
    // CODE → addr:129 | <GetByIdShort>: <Reg8: 20, Reg8: 21, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r20 = console.log;
    // CODE → addr:134 | <LoadFromEnvironment>: <Reg8: 19, Reg8: 18, UInt8: 0>
    r19 = r1[0][0]
    // CODE → addr:138 | <Call3>: <Reg8: 19, Reg8: 20, Reg8: 21, Reg8: 8, Reg8: 19>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/awaited", r19)
    // CODE → addr:144 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 18, UInt8: 0>
    r18 = r1[0][0]
    // CODE → addr:148 | <JStrictEqual>: <Addr8: 10, Reg8: 18, Reg8: 5>  # Address: 0000009e
    if (r18 === 1) goto label_158;
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:152 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
    r1[3] = 1
    // CODE → addr:156 | <Jmp>: <Addr8: 100>  # Address: 00000100
    goto label_256;
    // ──────────────── Block 9 ──────────────── 
    // CODE → addr:158 | <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
    // USED → r18 = Error;
    // CODE → addr:164 | <CreateThisForNew>: <Reg8: 19, Reg8: 18, UInt8: 3>
    r19 = CreateThisForNew(r18)
    // CODE → addr:168 | <Mov>: <Reg8: 24, Reg8: 19>
    // USED → r24 = r19;
    // CODE → addr:171 | <Mov>: <Reg8: 23, Reg8: 9>
    // USED → r23 = "post-await failure";
    // CODE → addr:174 | <Construct>: <Reg8: 18, Reg8: 18, UInt8: 2>
    // USED → r18 = new Error("post-await failure", r19);
    // CODE → addr:178 | <SelectObject>: <Reg8: 18, Reg8: 19, Reg8: 18>
    r18 = new Error("post-await failure", r19)
    // CODE → addr:182 | <Throw>: <Reg8: 18>
    throw r18;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:184 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
    r1[3] = 0
    // CODE → addr:188 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r19 = console;
    // CODE → addr:194 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r18 = console.log;
    // CODE → addr:199 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 12>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:204 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:207 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:211 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r18 = { "value": null, "done": true }
    // CODE → addr:217 | <PutOwnBySlotIdx>: <Reg8: 18, Reg8: 0, UInt8: 0>
    r18.slot_0 = param2
    // CODE → addr:221 | <Ret>: <Reg8: 18>
    return r18;
    // ──────────────── Block 11 ──────────────── 
    // CODE → addr:223 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:226 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:230 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:232 | <LoadFromEnvironment>: <Reg8: 6, Reg8: 1, UInt8: 2>
    r6 = r1[2]
    // CODE → addr:236 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
    r1[3] = 1
    // CODE → addr:240 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r19 = console;
    // CODE → addr:246 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r18 = console.log;
    // CODE → addr:251 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 10>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/caught")
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
    r1[3] = 0
    // CODE → addr:260 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r19 = console;
    // CODE → addr:266 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r18 = console.log;
    // CODE → addr:271 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 12>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:276 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r19 = console;
    // CODE → addr:282 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r18 = console.log;
    // CODE → addr:287 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 11>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/end")
    // CODE → addr:292 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:295 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:299 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r18 = { "value": null, "done": true }
    // CODE → addr:305 | <Ret>: <Reg8: 18>
    return r18;
    // ──────────────── Block 14 ──────────────── 
    // CODE → addr:307 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 2>
    // USED → r18 = r1[2];
    // CODE → addr:311 | <Mov>: <Reg8: 6, Reg8: 18>
    r6 = r1[2]
    // CODE → addr:314 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
    r1[3] = 0
    // CODE → addr:318 | <TryGetById>: <Reg8: 20, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r20 = console;
    // CODE → addr:324 | <GetByIdShort>: <Reg8: 19, Reg8: 20, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r19 = console.log;
    // CODE → addr:329 | <Call2>: <Reg8: 19, Reg8: 19, Reg8: 20, Reg8: 12>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
    // CODE → addr:334 | <Throw>: <Reg8: 18>
    throw r18;
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:336 | <JStrictEqual>: <Addr8: 93, Reg8: 3, Reg8: 5>  # Address: 000001ad
    if (param1 === 1) goto label_429;
    // ──────────────── Block 16 ──────────────── 
    // CODE → addr:340 | <JStrictEqual>: <Addr8: 70, Reg8: 3, Reg8: 4>  # Address: 0000019a
    if (param1 === 2) goto label_410;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:344 | <CreateTopLevelEnvironment>: <Reg8: 18, UInt32: 1>
    // USED → r18 = __environment__;
    // CODE → addr:350 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 18>
    r1[0] = __environment__
    // CODE → addr:354 | <StoreNPToEnvironment>: <Reg8: 18, UInt8: 0, Reg8: 16>
    __environment__[0] = undefined
    // CODE → addr:358 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r19 = console;
    // CODE → addr:364 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r18 = console.log;
    // CODE → addr:369 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 14>
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/start")
    // CODE → addr:374 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 4>
    r1[3] = 2
    // CODE → addr:378 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 13, UInt8: 0>
    // USED → r18 = r13[0];
    // CODE → addr:382 | <Call2>: <Reg8: 19, Reg8: 18, Reg8: 17, Reg8: 5>
    await r13[0].call(r17, 1)
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:410 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:413 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:417 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r18 = { "value": null, "done": true }
    // CODE → addr:423 | <PutOwnBySlotIdx>: <Reg8: 18, Reg8: 0, UInt8: 0>
    r18.slot_0 = param2
    // CODE → addr:427 | <Ret>: <Reg8: 18>
    return r18;
    // ──────────────── Block 19 ──────────────── 
    // CODE → addr:429 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:432 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:436 | <Throw>: <Reg8: 0>
    throw param2;
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:438 | <Catch>: <Reg8: 18>
    // USED → r18 = caughtException;
    // CODE → addr:440 | <Mov>: <Reg8: 6, Reg8: 18>
    r6 = caughtException
    // CODE → addr:443 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 18>
    r1[2] = caughtException
    // CODE → addr:447 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 3>
    r18 = r1[3]
    // CODE → addr:451 | <JStrictEqual>: <Addr8: 26, Reg8: 17, Reg8: 18>  # Address: 000001dd
    if (0 === r18) goto label_477;
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:455 | <JStrictEqual>: <Addr8: 13, Reg8: 5, Reg8: 18>  # Address: 000001d4
    if (1 === r18) goto label_468;
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:459 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
    r1[1] = 2
    // CODE → addr:463 | <JmpLong>: <Addr32: -388>  # Address: 0000004b
    goto label_75;
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:468 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
    r1[1] = 1
    // CODE → addr:472 | <JmpLong>: <Addr32: -397>  # Address: 0000004b
    goto label_75;
    // ──────────────── Block 24 ──────────────── 
    // CODE → addr:477 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:480 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
    r1[4] = 3
    // CODE → addr:484 | <Throw>: <Reg8: 6>
    throw r6;
}