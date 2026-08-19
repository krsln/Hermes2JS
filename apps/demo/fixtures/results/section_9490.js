function callDestructuringTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 5, string_id: 4965>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/callDestructuringTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 5, string_id: 4969>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → addr: 37 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → addr: 42 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1917, UInt16: 48463>  # Object: {'id': 1, 'name': 'Ada'}
    r5 = { "id": 1, "name": "Ada" }
    // CODE → addr: 48 | <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r8 = r5.name;
    // CODE → addr: 53 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1918, UInt16: 93>  # Object: {'page': 1}
    r5 = { "page": 1 }
    // CODE → addr: 59 | <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 12200>  # String: 'page' (Identifier)
    r7 = (r7 !== undefined) ? r5.page : 1
    // CODE → addr: 65 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 74 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 80 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 85 | <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → addr: 88 | <Call4>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 8, Reg8: 7>
    console.log(200, r5.name, (r7 !== undefined) ? r5.page : 1)
    // CODE → addr: 95 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:101 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:106 | <LoadConstString>: <Reg8: 5, string_id: 4968>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → addr:110 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → addr:115 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 5, string_id: 4980>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → addr:130 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → addr:135 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1919, UInt16: 19946>  # Object: {'timeout': 500}
    r5 = { "timeout": 500 }
    // CODE → addr:141 | <GetById>: <Reg8: 9, Reg8: 5, UInt8: 4, string_id: 8581>  # String: 'timeout' (Identifier)
    r9 = (r9 !== undefined) ? r5.timeout : 1000
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:157 | <GetById>: <Reg8: 8, Reg8: 5, UInt8: 5, string_id: 9071>  # String: 'retries' (Identifier)
    r8 = (r8 !== undefined) ? r5.retries : 3
    // ──────────────── Block 6 ──────────────── 
    // CODE → addr:170 | <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    r5 = getParentEnvironment(0)
    // CODE → addr:173 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:179 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:184 | <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 8>
    console.log(r9, (r8 !== undefined) ? r5.retries : 3)
    // CODE → addr:190 | <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:196 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:201 | <LoadConstString>: <Reg8: 6, string_id: 4979>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r6 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → addr:205 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → addr:210 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
    // USED → r5 = r5[0];
    // CODE → addr:214 | <Call1>: <Reg8: 1, Reg8: 5, Reg8: 2>
    r1 = r5[0].call(r2)
    // CODE → addr:218 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1920, UInt16: 48495>  # Object: {'id': 7}
    r5 = { "id": 7 }
    // CODE → addr:224 | <GetByIdShort>: <Reg8: 10, Reg8: 5, UInt8: 6, string_id: 28>  # String: 'id' (Identifier)
    // USED → r10 = r5.id;
    // CODE → addr:229 | <GetByIdShort>: <Reg8: 9, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    r9 = (r9 !== undefined) ? r5.name : "anon"
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr:242 | <NewArrayWithBuffer>: <Reg8: 7, UInt16: 2, UInt16: 2, UInt16: 48486>  # Array: [9, 10]
    r7 = [9, 10]
    // CODE → addr:250 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → addr:253 | <IteratorBegin>: <Reg8: 5, Reg8: 6>
    r5 = GetIterator(r6)
    // CODE → addr:256 | <Mov>: <Reg8: 7, Reg8: 6>
    r7 = r7
    // CODE → addr:259 | <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    r7 = r5.next()
    // CODE → addr:263 | <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = r5;
    // CODE → addr:266 | <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = r5 === undefined;
    // CODE → addr:270 | <LoadConstUndefined>: <Reg8: 8>
    r8 = (r5 === undefined) ? undefined : r7
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:278 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (r5 !== undefined) {
        // ──────────────── Block 11 ──────────────── 
        // CODE → addr:283 | <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
        r6 = r5.next()
        // CODE → addr:287 | <Mov>: <Reg8: 11, Reg8: 5>
        // USED → r11 = r5;
        // CODE → addr:290 | <StrictEq>: <Reg8: 3, Reg8: 11, Reg8: 2>
        // USED → r3 = r5 === undefined;
        // CODE → addr:294 | <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        // CODE → addr:296 | <Mov>: <Reg8: 1, Reg8: 3>
        r1 = r5 === undefined || r5 === undefined
    }
    if (r5 !== undefined) {
        // ──────────────── Block 14 ──────────────── 
        // CODE → addr:311 | <IteratorClose>: <Reg8: 5, UInt8: 0>
        r5.return()
    }
    // ──────────────── Block 15 ──────────────── 
    // CODE → addr:314 | <TryGetById>: <Reg8: 11, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr:320 | <GetByIdShort>: <Reg8: 6, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:325 | <LoadConstString>: <Reg8: 5, string_id: 4978>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → addr:329 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 11, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → addr:334 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:340 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:345 | <Mov>: <Reg8: 16, Reg8: 6>
    r16 = console
    // CODE → addr:348 | <Mov>: <Reg8: 15, Reg8: 10>
    r15 = r5.id
    // CODE → addr:351 | <Mov>: <Reg8: 14, Reg8: 9>
    r14 = (r9 !== undefined) ? r5.name : "anon"
    // CODE → addr:354 | <Mov>: <Reg8: 13, Reg8: 8>
    r13 = (r5 === undefined) ? undefined : r7
    // CODE → addr:357 | <Mov>: <Reg8: 12, Reg8: 7>
    r12 = r6
    // CODE → addr:360 | <Call>: <Reg8: 5, Reg8: 5, UInt8: 5>
    console.log(r16, r15, r14, r13, r12)
    // CODE → addr:364 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:370 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:375 | <LoadConstString>: <Reg8: 5, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → addr:379 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → addr:384 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:390 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:395 | <LoadConstString>: <Reg8: 5, string_id: 4986>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → addr:399 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → addr:404 | <NewArray>: <Reg8: 7, UInt16: 2>
    r7 = []
    // CODE → addr:408 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:411 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7[0] = 2
    // CODE → addr:415 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr:418 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    r7[1] = 1
    // CODE → addr:422 | <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → addr:425 | <IteratorBegin>: <Reg8: 5, Reg8: 6>
    r5 = GetIterator(r6)
    // CODE → addr:428 | <Mov>: <Reg8: 7, Reg8: 6>
    r7 = r7
    // CODE → addr:431 | <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    r7 = r5.next()
    // CODE → addr:435 | <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = r5;
    // CODE → addr:438 | <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = r5 === undefined || r5 === undefined;
    // CODE → addr:442 | <LoadConstUndefined>: <Reg8: 8>
    r8 = (r5 === undefined) ? undefined : r7
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:450 | <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (r5 !== undefined) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → addr:455 | <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
        r6 = r5.next()
        // CODE → addr:459 | <Mov>: <Reg8: 9, Reg8: 5>
        // USED → r9 = r5;
        // CODE → addr:462 | <StrictEq>: <Reg8: 3, Reg8: 9, Reg8: 2>
        // USED → r3 = r5 === undefined || r5 === undefined;
        // CODE → addr:466 | <LoadConstUndefined>: <Reg8: 7>
        r7 = undefined
        // CODE → addr:468 | <Mov>: <Reg8: 1, Reg8: 3>
        r1 = r5 === undefined || r5 === undefined || (r5 === undefined || r5 === undefined)
    }
    if (r5 !== undefined) {
        // ──────────────── Block 21 ──────────────── 
        // CODE → addr:483 | <IteratorClose>: <Reg8: 5, UInt8: 0>
        r5.return()
    }
    // ──────────────── Block 22 ──────────────── 
    // CODE → addr:486 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:492 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:497 | <Call3>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 8, Reg8: 7>
    console.log(r8, r7)
    // CODE → addr:503 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr:509 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr:514 | <LoadConstString>: <Reg8: 5, string_id: 4984>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → addr:518 | <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → addr:523 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:529 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:534 | <LoadConstString>: <Reg8: 4, string_id: 4964>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/end' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/callDestructuringTests/end";
    // CODE → addr:538 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/end")
    // CODE → addr:543 | <Ret>: <Reg8: 2>
    return undefined;
}