function callDestructuringTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4965>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/callDestructuringTests/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/callDestructuringTests/start")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4969>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1917, UInt16: 48463>  # Object: {'id': 1, 'name': 'Ada'}
    // USED → r5 = { "id": 1, "name": "Ada" };
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r8 = { "id": 1, "name": "Ada" }.name;
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1918, UInt16: 93>  # Object: {'page': 1}
    // USED → r5 = { "page": 1 };
    // CODE → <GetById>: <Reg8: 7, Reg8: 5, UInt8: 3, string_id: 12200>  # String: 'page' (Identifier)
    // USED → r7 = { "page": 1 }.page;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    if ({ "page": 1 }.page === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 1>
        // USED → r7 = 1;
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 200>
    // USED → r0 = 200;
    // CODE → <Call4>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 8, Reg8: 7>
    r5 = globalThis.console.log(200, { "id": 1, "name": "Ada" }.name, 1)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4968>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4980>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start")
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1919, UInt16: 19946>  # Object: {'timeout': 500}
    // USED → r5 = { "timeout": 500 };
    // CODE → <GetById>: <Reg8: 9, Reg8: 5, UInt8: 4, string_id: 8581>  # String: 'timeout' (Identifier)
    // USED → r9 = { "timeout": 500 }.timeout;
    if ({ "timeout": 500 }.timeout === undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 1000>
        // USED → r9 = 1000;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetById>: <Reg8: 8, Reg8: 5, UInt8: 5, string_id: 9071>  # String: 'retries' (Identifier)
    // USED → r8 = { "timeout": 500 }.retries;
    if ({ "timeout": 500 }.retries === undefined) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <LoadConstUInt8>: <Reg8: 8, UInt8: 3>
        // USED → r8 = 3;
    }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 5, UInt8: 0>
    // USED → r5 = getParentEnvironment(0);
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 6, Reg8: 6, Reg8: 7, Reg8: 9, Reg8: 8>
    r6 = globalThis.console.log(1000, 3)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4979>  # String: '__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end' (String)
    // USED → r6 = "__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end";
    // CODE → <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    r6 = globalThis.console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end")
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 5, UInt8: 0>
    // USED → r5 = getParentEnvironment(0)[0];
    // CODE → <Call1>: <Reg8: 1, Reg8: 5, Reg8: 2>
    r1 = getParentEnvironment(0)[0].call(undefined)
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1920, UInt16: 48495>  # Object: {'id': 7}
    // USED → r5 = { "id": 7 };
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 5, UInt8: 6, string_id: 28>  # String: 'id' (Identifier)
    // USED → r10 = { "id": 7 }.id;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 5, UInt8: 2, string_id: 187>  # String: 'name' (Identifier)
    // USED → r9 = { "id": 7 }.name;
    if ({ "id": 7 }.name === undefined) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → <LoadConstString>: <Reg8: 9, string_id: 514>  # String: 'anon' (String)
        // USED → r9 = "anon";
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <NewArrayWithBuffer>: <Reg8: 7, UInt16: 2, UInt16: 2, UInt16: 48486>  # Array: [9, 10]
    // USED → r7 = [9, 10];
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    // USED → r6 = [9, 10];
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 6>
    // USED → r5 = GetIterator(r6);
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    r7 = [9, 10]
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    // USED → r7 = GetIterator(r6).next();
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = GetIterator(r6);
    // CODE → <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = GetIterator(r6) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    if (GetIterator(r6) !== undefined) {
        // ──────────────── Block 9 ──────────────── 
        // CODE → <Mov>: <Reg8: 8, Reg8: 7>
        // USED → r8 = GetIterator(r6).next();
    }
    // ──────────────── Block 10 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (GetIterator(r6) !== undefined && GetIterator(r6) !== undefined) {
        // ──────────────── Block 12 ──────────────── 
        // CODE → <Mov>: <Reg8: 7, Reg8: 6>
        // USED → r7 = GetIterator(r6).next();
        // CODE → <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = GetIterator(r6) === undefined;
    }
    if (GetIterator(r6) !== undefined) {
        // ──────────────── Block 14 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 5, UInt8: 0>
        GetIterator(r6).return()
    }
    // ──────────────── Block 15 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4978>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 11, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <Mov>: <Reg8: 16, Reg8: 6>
    r16 = globalThis.console
    // CODE → <Mov>: <Reg8: 15, Reg8: 10>
    r15 = { "id": 7 }.id
    // CODE → <Mov>: <Reg8: 14, Reg8: 9>
    r14 = "anon"
    // CODE → <Mov>: <Reg8: 13, Reg8: 8>
    r13 = GetIterator(r6).next()
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    r12 = GetIterator(r6).next()
    // CODE → <Call>: <Reg8: 5, Reg8: 5, UInt8: 5>
    r5 = globalThis.console.log(r0, r1, r2, r3, r4)
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4975>  # String: '__BC:Objects/DestructuringTests/parameterDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/parameterDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4986>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/start' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/start";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start")
    // CODE → <NewArray>: <Reg8: 7, UInt16: 2>
    // USED → r7 = [];
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 0>
    [][0] = 2
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 0, UInt8: 1>
    [][1] = 1
    // CODE → <Mov>: <Reg8: 6, Reg8: 7>
    // USED → r6 = [];
    // CODE → <IteratorBegin>: <Reg8: 5, Reg8: 6>
    // USED → r5 = GetIterator(r6);
    // CODE → <Mov>: <Reg8: 7, Reg8: 6>
    r7 = []
    // CODE → <IteratorNext>: <Reg8: 7, Reg8: 5, Reg8: 7>
    // USED → r7 = GetIterator(r6).next();
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    // USED → r8 = GetIterator(r6);
    // CODE → <StrictEq>: <Reg8: 1, Reg8: 8, Reg8: 2>
    // USED → r1 = GetIterator(r6) === undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    if (GetIterator(r6) !== undefined) {
        // ──────────────── Block 16 ──────────────── 
        // CODE → <Mov>: <Reg8: 8, Reg8: 7>
        // USED → r8 = GetIterator(r6).next();
    }
    // ──────────────── Block 17 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    if (GetIterator(r6) !== undefined && GetIterator(r6) !== undefined) {
        // ──────────────── Block 19 ──────────────── 
        // CODE → <Mov>: <Reg8: 7, Reg8: 6>
        // USED → r7 = GetIterator(r6).next();
        // CODE → <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = GetIterator(r6) === undefined;
    }
    if (GetIterator(r6) !== undefined) {
        // ──────────────── Block 21 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 5, UInt8: 0>
        GetIterator(r6).return()
    }
    // ──────────────── Block 22 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 8, Reg8: 7>
    r5 = globalThis.console.log(GetIterator(r6).next(), GetIterator(r6).next())
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 4984>  # String: '__BC:Objects/DestructuringTests/swapViaDestructureTest/end' (String)
    // USED → r5 = "__BC:Objects/DestructuringTests/swapViaDestructureTest/end";
    // CODE → <Call2>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 5>
    r5 = globalThis.console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end")
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4964>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/end' (String)
    // USED → r4 = "__BC:Objects/DestructuringTests/callDestructuringTests/end";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Objects/DestructuringTests/callDestructuringTests/end")
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}