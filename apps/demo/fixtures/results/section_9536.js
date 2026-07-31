function Counter(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <GetNewTarget>: <Reg8: 2>
    // USED → r2 = new.target;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 0, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r2 = new.target.prototype;
    // CODE → <NewObjectWithParent>: <Reg8: 2, Reg8: 2>
    // USED → r2 = Object.create(new.target.prototype);
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 5>
    // USED → r4 = getParentEnvironment(0)[5];
    // CODE → <PrivateIsIn>: <Reg8: 1, Reg8: 4, Reg8: 2, Reg8: 0>
    // USED → r1 = getParentEnvironment(0)[5] in Object.create(new.target.prototype);
    if (getParentEnvironment(0)[5] in Object.create(new.target.prototype)) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <LoadConstString>: <Reg8: 7, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
        r7 = "Cannot initialize private field twice."
        // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 2>  # Built-in function: [#44 copyDataProperties]
        r2 = copyDataProperties(r0, r1)
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <LoadConstUndefined>: <Reg8: 1>
        r1 = undefined
        // CODE → <AddOwnPrivateBySym>: <Reg8: 2, Reg8: 1, Reg8: 4>
        Object.create(new.target.prototype).#__private_1__ = getParentEnvironment(0)[5]
        // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 6>
        // USED → r4 = getParentEnvironment(0)[6];
        // CODE → <LoadConstZero>: <Reg8: 0>
        r0 = 0
        // CODE → <AddOwnPrivateBySym>: <Reg8: 2, Reg8: 0, Reg8: 4>
        Object.create(new.target.prototype).#__private_0__ = getParentEnvironment(0)[6]
        // CODE → <GetGlobalObject>: <Reg8: 4>
        // USED → r4 = globalThis;
        // CODE → <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 108>  # String: 'console' (Identifier)
        // USED → r6 = globalThis.console;
        // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 178>  # String: 'log' (Identifier)
        // USED → r5 = globalThis.console.log;
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 4728>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
        // USED → r4 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
        // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
        r4 = globalThis.console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
        // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 2>
        // USED → r5 = getParentEnvironment(0)[2];
        // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 4>
        r4 = getParentEnvironment(0)[4]
        // CODE → <GetOwnPrivateBySym>: <Reg8: 3, Reg8: 5, UInt8: 1, Reg8: 4>
        // USED → r3 = getParentEnvironment(0)[2].#__private_4__;
        // CODE → <Inc>: <Reg8: 3, Reg8: 3>
        // USED → r3 = getParentEnvironment(0)[2].#__private_4__ + 1;
        // CODE → <PutOwnPrivateBySym>: <Reg8: 5, Reg8: 3, UInt8: 1, Reg8: 4>
        getParentEnvironment(0)[2].#__private_4__ = getParentEnvironment(0)[2].#__private_4__ + 1
        // CODE → <Ret>: <Reg8: 2>
        return Object.create(new.target.prototype);
    }
}