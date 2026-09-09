function Counter() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetNewTarget>: <Reg8: 2>
    r2 = new.target
    // CODE → addr:  5 | <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 0, string_id: 212>  # String: 'prototype' (Identifier)
    // USED → r2 = r2.prototype;
    // CODE → addr: 10 | <NewObjectWithParent>: <Reg8: 2, Reg8: 2>
    r2 = Object.create(r2.prototype)
    // CODE → addr: 13 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 5>
    // USED → r4 = r3[5];
    // CODE → addr: 17 | <PrivateIsIn>: <Reg8: 1, Reg8: 4, Reg8: 2, Reg8: 0>
    // USED → r1 = r3[5] in r2;
    // CODE → addr: 22 | <JmpTrue>: <Addr8: 64, Reg8: 1>  # Address: 00000056
    // → r2 = Object.create(r2.prototype); r3 = getParentEnvironment(0)
    if (r3[5] in r2) goto label_86;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 25 | <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → addr: 27 | <AddOwnPrivateBySym>: <Reg8: 2, Reg8: 1, Reg8: 4>
    r2.#__private_1__ = r3[5]
    // CODE → addr: 31 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 6>
    // USED → r4 = r3[6];
    // CODE → addr: 35 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 37 | <AddOwnPrivateBySym>: <Reg8: 2, Reg8: 0, Reg8: 4>
    r2.#__private_0__ = r3[6]
    // CODE → addr: 41 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr: 43 | <TryGetById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 2, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 54 | <LoadConstString>: <Reg8: 4, string_id: 4728>  # String: '__BC:Classes/PrivateStaticTests/Counter/constructor' (String)
    // USED → r4 = "__BC:Classes/PrivateStaticTests/Counter/constructor";
    // CODE → addr: 58 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Classes/PrivateStaticTests/Counter/constructor")
    // CODE → addr: 63 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 2>
    // USED → r5 = r3[2];
    // CODE → addr: 67 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 4>
    r4 = r3[4]
    // CODE → addr: 71 | <GetOwnPrivateBySym>: <Reg8: 3, Reg8: 5, UInt8: 1, Reg8: 4>
    r3 = r3[2].#__private_4__
    // CODE → addr: 76 | <Inc>: <Reg8: 3, Reg8: 3>
    // USED → r3 = r3 + 1;
    // CODE → addr: 79 | <PutOwnPrivateBySym>: <Reg8: 5, Reg8: 3, UInt8: 1, Reg8: 4>
    r3[2].#__private_4__ = r3 + 1
    // CODE → addr: 84 | <Ret>: <Reg8: 2>
    return r2;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 86 | <LoadConstString>: <Reg8: 7, string_id: 2847>  # String: 'Cannot initialize private field twice.' (String)
    r7 = "Cannot initialize private field twice."
    // CODE → addr: 90 | <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
    r2 = throwTypeError(r7, r6)
}