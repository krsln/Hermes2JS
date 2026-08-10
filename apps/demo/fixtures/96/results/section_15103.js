function nestedObjectDestructureTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4814>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start")
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 200>
    // USED → r2 = 200;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 2, string_id: 235>  # String: 'status' (Identifier)
    r0.status = 200
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 6, UInt8: 1>
    // USED → r6 = 1;
    // CODE → <NewObjectWithBuffer>: <Reg8: 3, UInt16: 2, UInt16: 2, UInt16: 12808, UInt16: 23461>  # Object: {'id': 1, 'name': 'Ada'}
    r3 = { "id": 1, "name": "Ada" }
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 7459>  # String: 'user' (Identifier)
    r2.user = r3
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <PutNewOwnById>: <Reg8: 3, Reg8: 6, string_id: 12920>  # String: 'page' (Identifier)
    r3.page = 1
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 3, string_id: 10786>  # String: 'meta' (Identifier)
    r2.meta = r3
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 7222>  # String: 'body' (Identifier)
    r0.body = r2
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 0, UInt8: 3, string_id: 235>  # String: 'status' (Identifier)
    // USED → r5 = r0.status;
    // CODE → <GetById>: <Reg8: 0, Reg8: 0, UInt8: 4, string_id: 7222>  # String: 'body' (Identifier)
    // USED → r0 = r0.body;
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 7459>  # String: 'user' (Identifier)
    // USED → r2 = r0.body.user;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 6, string_id: 176>  # String: 'name' (Identifier)
    // USED → r4 = r0.body.user.name;
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 7, string_id: 10786>  # String: 'meta' (Identifier)
    // USED → r2 = r0.body.meta;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    if (r0.body.meta === undefined) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <NewObject>: <Reg8: 2>
        r2 = {  }
    }
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 8, string_id: 12920>  # String: 'page' (Identifier)
    // USED → r2 = r2.page;
    if (r2.page !== undefined) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <Mov>: <Reg8: 6, Reg8: 2>
        // USED → r6 = r2.page;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call4>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4, Reg8: 6>
    console.log(r0.status, r0.body.user.name, r2.page)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4813>  # String: '__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}