function nestedObjectDestructureTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4814>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → addr: 22 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 24 | <LoadConstUInt8>: <Reg8: 2, UInt8: 200>
    // USED → r2 = 200;
    // CODE → addr: 27 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 2, string_id: 235>  # String: 'status' (Identifier)
    r0.status = 200
    // CODE → addr: 31 | <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → addr: 33 | <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → addr: 36 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 2, UInt16: 2, UInt16: 12808, UInt16: 23461>  # Object: {'id': 1, 'name': 'Ada'}
    r3 = { "id": 1, "name": "Ada" }
    // CODE → addr: 46 | <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7459>  # String: 'user' (Identifier)
    r2.user = r3
    // CODE → addr: 51 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr: 53 | <PutNewOwnById>: <Reg8: 3, Reg8: 6, string_id: 12920>  # String: 'page' (Identifier)
    r3.page = 1
    // CODE → addr: 58 | <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 10786>  # String: 'meta' (Identifier)
    r2.meta = r3
    // CODE → addr: 63 | <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 7222>  # String: 'body' (Identifier)
    r0.body = r2
    // CODE → addr: 68 | <GetByIdShort>: <Reg8: 5, Reg8: 0, UInt8: 3, string_id: 235>  # String: 'status' (Identifier)
    // USED → r5 = r0.status;
    // CODE → addr: 73 | <GetById>: <Reg8: 0, Reg8: 0, UInt8: 4, string_id: 7222>  # String: 'body' (Identifier)
    r0 = r0.body
    // CODE → addr: 79 | <GetById>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 7459>  # String: 'user' (Identifier)
    r2 = r0.user
    // CODE → addr: 85 | <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 6, string_id: 176>  # String: 'name' (Identifier)
    // USED → r4 = r2.name;
    // CODE → addr: 90 | <GetById>: <Reg8: 2, Reg8: 0, UInt8: 7, string_id: 10786>  # String: 'meta' (Identifier)
    r2 = r0.meta
    // CODE → addr: 96 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // → r2 = r0.meta
    if (r2 === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:102 | <NewObject>: <Reg8: 2>
        r2 = {  }
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr:104 | <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12920>  # String: 'page' (Identifier)
    r2 = r2.page
    // → r2 = r2.page
    if (r2 !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → addr:114 | <Mov>: <Reg8: 6, Reg8: 2>
        r6 = r2.page
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr:117 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:123 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:128 | <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 6>
    console.log(r0.status, r2.name, r6)
    // CODE → addr:135 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:141 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:146 | <LoadConstString>: <Reg8: 1, string_id: 4813>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → addr:150 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → addr:155 | <Ret>: <Reg8: 0>
    return undefined;
}