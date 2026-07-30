function spreadObjectTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4517>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadObjectTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadObjectTest/start")
    // CODE → <NewObject>: <Reg8: 4>
    // USED → r4 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 2, UInt16: 2, UInt16: 338, UInt16: 19818>  # Object: {'x': 1, 'y': 2}
    r6 = { "x": 1, "y": 2 }
    // CODE → <Mov>: <Reg8: 7, Reg8: 4>
    r7 = {  }
    // CODE → <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
    r0 = builtin_44(r-3, r-2, r-1)
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    r2 = 3
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 7402>  # String: 'z' (Identifier)
    r0 = "z"
    // CODE → <PutOwnByVal>: <Reg8: 4, Reg8: 2, Reg8: 0, UInt8: 1>
    // Unhandled opcode: PutOwnByVal
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r0 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    r0 = globalThis.console.log({  })
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 4, UInt8: 3, string_id: 42>  # String: 'x' (Identifier)
    // USED → r5 = {  }.x;
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 1>
    // USED → r2 = getEnvironment(0)[1];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 108>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(0)[1].default;
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = getEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call3>: <Reg8: 4, Reg8: 3, Reg8: 0, Reg8: 4, Reg8: 2>
    // USED → r4 = getEnvironment(0)[1].default.call(undefined, {  }, getEnvironment(0)[0]);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    r2 = globalThis.console.log({  }.x, getEnvironment(0)[1].default.call(undefined, {  }, getEnvironment(0)[0]))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4515>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadObjectTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Arrays/SpreadTests/spreadObjectTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}