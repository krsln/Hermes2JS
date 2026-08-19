function callDestructuringTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4965>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/callDestructuringTests/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/start")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4969>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1917, UInt16: 48463>  # Object: {'id': 1, 'name': 'Ada'}
    r5 = { "id": 1, "name": "Ada" }
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r8 = r5.name;
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1918, UInt16: 93>  # Object: {'page': 1}
    r5 = { "page": 1 }
    // CODE → <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 12200>  # String: 'page' (Identifier)
    r7 = r5.page
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <JStrictNotEqual>: <Addr8: 7, Reg8: 7, Reg8: 2>  # Address: 0000004a
    // → r7 = r5.page
    if (r7 !== undefined) goto label_74;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
    // USED → r7 = 1;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → <Call4>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 8, Reg8: 7>
    console.log(200, r5.name, 1)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4968>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4980>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1919, UInt16: 19946>  # Object: {'timeout': 500}
    r5 = { "timeout": 500 }
    // CODE → <GetById>: <Reg8: 9, Reg8: 5, UInt8: 4, string_id: 8581>  # String: 'timeout' (Identifier)
    r9 = r5.timeout
    // CODE → <JStrictNotEqual>: <Addr8: 10, Reg8: 9, Reg8: 2>  # Address: 0000009d
    // → r9 = r5.timeout
    if (r9 !== undefined) goto label_157;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 1000>
    // USED → r9 = 1000;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetById>: <Reg8: 8, Reg8: 5, UInt8: 5, string_id: 9071>  # String: 'retries' (Identifier)
    r8 = r5.retries
    // CODE → <JStrictNotEqual>: <Addr8: 7, Reg8: 8, Reg8: 2>  # Address: 000000aa
    // → r8 = r5.retries
    if (r8 !== undefined) goto label_170;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 3>
    // USED → r8 = 3;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    r5 = getParentEnvironment(0)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 8>
    console.log(r9, 3)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4979>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r6 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
    // USED → r5 = r5[0];
    // CODE → <Call1>: <Reg8: 1, Reg8: 5, Reg8: 2>
    r1 = r5[0].call(r2)
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1920, UInt16: 48495>  # Object: {'id': 7}
    r5 = { "id": 7 }
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 5, UInt8: 6, string_id: 28>  # String: 'id' (Identifier)
    // USED → r10 = r5.id;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    r9 = r5.name
    // CODE → <JStrictNotEqual>: <Addr8: 8, Reg8: 9, Reg8: 2>  # Address: 000000f2
    // → r9 = r5.name
    if (r9 !== undefined) goto label_242;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 514>  # String: 'anon' (String)
    // USED → r9 = "anon";
    // ──────────────── Block 8 ──────────────── 
    // CODE → <NewArrayWithBuffer>: <Reg8: 7, UInt16: 2, UInt16: 2, UInt16: 48486>  # Array: [9, 10]
    r7 = [9, 10]
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 6>
    r5 = GetIterator(r6)
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    r7 = r7
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    r7 = r5.next()
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = r5;
    // CODE → <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = r5 === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 00000116
    // → r5 = GetIterator(r6)
    if (r5 === undefined) goto label_278;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 7>
    // USED → r8 = r7;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <JmpTrue>: <Addr8: 28, Reg8: 1>  # Address: 00000134
    if (r5 === undefined) goto label_308;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
    r6 = r5.next()
    // CODE → <Mov>: <Reg8: 11, Reg8: 5>
    // USED → r11 = r5;
    // CODE → <StrictEq>: <Reg8: 3, Reg8: 11, Reg8: 2>
    // USED → r3 = r5 === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    r1 = r5 === undefined
    // CODE → <JmpTrue>: <Addr8: 9, Reg8: 3>  # Address: 00000134
    if (r5 === undefined) goto label_308;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    // USED → r7 = r6;
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    // USED → r1 = r5 === undefined;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 0000013a
    if (r5 === undefined) goto label_314;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <IteratorClose>: <Reg8: 5, UInt8: 0>
    r5.return()
    // ──────────────── Block 15 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4978>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 11, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <Mov>: <Reg8: 16, Reg8: 6>
    r16 = console
    // CODE → <Mov>: <Reg8: 15, Reg8: 10>
    r15 = r5.id
    // CODE → <Mov>: <Reg8: 14, Reg8: 9>
    r14 = "anon"
    // CODE → <Mov>: <Reg8: 13, Reg8: 8>
    r13 = r7
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = r6
    // CODE → <Call>: <Reg8: 5, Reg8: 5, UInt8: 5>
    console.log(r16, r15, r14, r13, r12)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4986>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 7, UInt16: 2>
    r7 = []
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    r7[0] = 2
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    r7[1] = 1
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    r6 = r7
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 6>
    r5 = GetIterator(r6)
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    r7 = r7
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    r7 = r5.next()
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = r5;
    // CODE → <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = r5 === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 000001c2
    // → r5 = GetIterator(r6)
    if (r5 === undefined) goto label_450;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 7>
    // USED → r8 = r7;
    // ──────────────── Block 17 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <JmpTrue>: <Addr8: 28, Reg8: 1>  # Address: 000001e0
    if (r5 === undefined) goto label_480;
    // ──────────────── Block 18 ──────────────── 
    // CODE → <IteratorNext>: <Reg8: 6, Reg8: 5, Reg8: 6>
    r6 = r5.next()
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r5;
    // CODE → <StrictEq>: <Reg8: 3, Reg8: 9, Reg8: 2>
    // USED → r3 = r5 === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    r1 = r5 === undefined
    // CODE → <JmpTrue>: <Addr8: 9, Reg8: 3>  # Address: 000001e0
    if (r5 === undefined) goto label_480;
    // ──────────────── Block 19 ──────────────── 
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    // USED → r7 = r6;
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    // USED → r1 = r5 === undefined;
    // ──────────────── Block 20 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 1>  # Address: 000001e6
    if (r5 === undefined) goto label_486;
    // ──────────────── Block 21 ──────────────── 
    // CODE → <IteratorClose>: <Reg8: 5, UInt8: 0>
    r5.return()
    // ──────────────── Block 22 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <Call3>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 8, Reg8: 7>
    console.log(r8, r7)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4984>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4964>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/end' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/callDestructuringTests/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/end")
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}