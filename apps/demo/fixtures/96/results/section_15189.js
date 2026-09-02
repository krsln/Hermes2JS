async function* anon_15189() {
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4761>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 4, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start")
    // CODE → addr: 32 | <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 3, string_id: 27>  # String: 'Promise' (Identifier)
    // USED → r8 = Promise;
    // CODE → addr: 38 | <GetById>: <Reg8: 7, Reg8: 8, UInt8: 4, string_id: 7443>  # String: 'all' (Identifier)
    // USED → r7 = Promise.all;
    // CODE → addr: 44 | <GetEnvironment>: <Reg8: 4, UInt8: 2>
    r4 = getEnvironment(2)
    // CODE → addr: 47 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 4, UInt8: 2>
    // USED → r9 = r4[2];
    // CODE → addr: 51 | <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → addr: 53 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    // CODE → addr: 56 | <Call2>: <Reg8: 6, Reg8: 9, Reg8: 2, Reg8: 5>
    r6 = r4[2].call(r2, 1)
    // CODE → addr: 61 | <NewArray>: <Reg8: 1, UInt16: 2>
    r1 = []
    // CODE → addr: 65 | <PutOwnByIndex>: <Reg8: 1, Reg8: 6, UInt8: 0>
    // USED → r1 = r1[0] = r6;
    // CODE → addr: 69 | <LoadConstUInt8>: <Reg8: 6, UInt8: 2>
    // USED → r6 = 2;
    // CODE → addr: 72 | <Call2>: <Reg8: 9, Reg8: 9, Reg8: 2, Reg8: 6>
    r9 = r4[2].call(r2, 2)
    // CODE → addr: 77 | <PutOwnByIndex>: <Reg8: 1, Reg8: 9, UInt8: 1>
    r1 = (r1[0] = r6)[1] = r9
    // CODE → addr: 86 | <SaveGenerator>: <Addr8: 4>  # Address: 0000005a
    r1 = yield await Promise.all(r1)
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 96 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 0>
    r4 = r4[0]
    // CODE → addr:100 | <GetByIdShort>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = r4.default;
    // CODE → addr:105 | <Call3>: <Reg8: 4, Reg8: 4, Reg8: 2, Reg8: 1, Reg8: 6>
    r4 = r4.default.call(r2, r1, 2)
    // CODE → addr:111 | <LoadConstZero>: <Reg8: 6>
    r6 = 0
    // CODE → addr:113 | <GetByVal>: <Reg8: 7, Reg8: 4, Reg8: 6>
    r7 = r4[r6]
    // CODE → addr:117 | <GetByVal>: <Reg8: 6, Reg8: 4, Reg8: 5>
    r6 = r4[r5]
    // CODE → addr:121 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:127 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:132 | <Call3>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 7, Reg8: 6>
    console.log(r7, r6)
    // CODE → addr:138 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:144 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:149 | <LoadConstString>: <Reg8: 3, string_id: 4760>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
    // USED → r3 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
    // CODE → addr:153 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end")
    // CODE → addr:159 | <Ret>: <Reg8: 2>
    return undefined;
}