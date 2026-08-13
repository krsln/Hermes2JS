function optionalChainingTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4837>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/start' (String)
    // USED → r0 = "__BC:Objects/PropertyTests/optionalChainingTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/start")
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 2, string_id: 38>  # String: 'b' (Identifier)
    r0.b = r2
    // CODE → <PutNewOwnById>: <Reg8: 3, Reg8: 0, string_id: 7189>  # String: 'a' (Identifier)
    r3.a = r0
    // CODE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null;
    // CODE → <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
    // USED → r5 = r3 == null;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <JmpTrue>: <Addr8: 38, Reg8: 5>  # Address: 00000055
    // r3 = {  }
    if (r3 == null) goto label_85;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 3, string_id: 7189>  # String: 'a' (Identifier)
    // USED → r3 = r3.a;
    // CODE → <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
    // USED → r5 = r3.a == null;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <JmpTrue>: <Addr8: 23, Reg8: 5>  # Address: 00000055
    // r3 = r3.a
    if (r3.a == null) goto label_85;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 38>  # String: 'b' (Identifier)
    // USED → r3 = r3.a.b;
    // CODE → <Eq>: <Reg8: 5, Reg8: 3, Reg8: 2>
    // USED → r5 = r3.a.b == null;
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <JmpTrue>: <Addr8: 9, Reg8: 5>  # Address: 00000055
    // r3 = r3.a.b
    if (r3.a.b == null) goto label_85;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 7241>  # String: 'c' (Identifier)
    r4 = r3.a.b.c
    // ──────────────── Block 4 ──────────────── 
    // CODE → <JNotEqual>: <Addr8: 10, Reg8: 4, Reg8: 2>  # Address: 0000005f
    if (r4 != null) goto label_95;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstInt>: <Reg8: 4, Imm32: -1>
    // USED → r4 = -1;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(-1)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4830>  # String: '__BC:Objects/PropertyTests/optionalChainingTest/end' (String)
    // USED → r1 = "__BC:Objects/PropertyTests/optionalChainingTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/PropertyTests/optionalChainingTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}