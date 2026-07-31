function callMapSetTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4736>  # String: '__BC:Collections/MapSetTests/callMapSetTests/start' (String)
    // USED → r4 = "__BC:Collections/MapSetTests/callMapSetTests/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Collections/MapSetTests/callMapSetTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
    // USED → r4 = getParentEnvironment(0)[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 1, Reg8: 4, Reg8: 0>
    r1 = getParentEnvironment(0)[0].call(undefined)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = getParentEnvironment(0)[1];
    // CODE → <Call1>: <Reg8: 1, Reg8: 3, Reg8: 0>
    r1 = getParentEnvironment(0)[1].call(undefined)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4746>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 6821>  # String: 'WeakMap' (Identifier)
    // USED → r3 = globalThis.WeakMap;
    // CODE → <CreateThisForNew>: <Reg8: 4, Reg8: 3, UInt8: 3>
    // USED → r4 = __uninitialized_this_for_new__;
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = new globalThis.WeakMap(__uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 7, Reg8: 4, Reg8: 3>
    // USED → r7 = new globalThis.WeakMap(__uninitialized_this_for_new__);
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r4 = new globalThis.WeakMap(__uninitialized_this_for_new__).set;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 211>  # String: 'value' (Identifier)
    // USED → r3 = "value";
    // CODE → <Call3>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 6, Reg8: 3>
    r3 = new globalThis.WeakMap(__uninitialized_this_for_new__).set({  }, "value")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 5, string_id: 11>  # String: 'has' (Identifier)
    // USED → r3 = new globalThis.WeakMap(__uninitialized_this_for_new__).has;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    // USED → r3 = new globalThis.WeakMap(__uninitialized_this_for_new__).has({  });
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log(new globalThis.WeakMap(__uninitialized_this_for_new__).has({  }))
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 6, string_id: 49>  # String: 'get' (Identifier)
    // USED → r3 = new globalThis.WeakMap(__uninitialized_this_for_new__).get;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    // USED → r3 = new globalThis.WeakMap(__uninitialized_this_for_new__).get({  });
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log(new globalThis.WeakMap(__uninitialized_this_for_new__).get({  }))
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3088>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 293>  # String: '__BC:Collections/MapSetTests/callMapSetTests/end' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/callMapSetTests/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Collections/MapSetTests/callMapSetTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}