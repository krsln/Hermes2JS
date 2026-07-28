function Animal(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetNewTarget>: <Reg8: 0>
    // USED → r0 = new.target;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 0, UInt8: 0, string_id: 213>  # String: 'prototype' (Identifier)
    // USED → r0 = new.target.prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 0, Reg8: 0>
    // USED → r0 = Object.create(new.target.prototype);
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 106>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 177>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 2550>  # String: '__BC:Classes/ClassTests/Animal/constructor' (String)
    // USED → r1 = "__BC:Classes/ClassTests/Animal/constructor";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Classes/ClassTests/Animal/constructor");
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 0, string_id: 186>  # String: 'name' (Identifier)
    Object.create(new.target.prototype).name = param1;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <PutByIdStrict>: <Reg8: 0, Reg8: 1, UInt8: 1, string_id: 11460>  # String: 'sound' (Identifier)
    Object.create(new.target.prototype).sound = param2;
    // CODE → <Ret>: <Reg8: 0>
    return Object.create(new.target.prototype);
}