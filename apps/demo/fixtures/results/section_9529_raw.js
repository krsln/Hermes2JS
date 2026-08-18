function Animal(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetNewTarget>: <Reg8: 0>
    r0 = new.target
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 0, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r0 = r0.prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 0, Reg8: 0>
    r0 = Object.create(r0.prototype)
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2576>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Classes/ClassTests/Animal/constructor")
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 187>  # String: 'name' (Identifier)
    r0.name = param1
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 11958>  # String: 'sound' (Identifier)
    r0.sound = param2
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}