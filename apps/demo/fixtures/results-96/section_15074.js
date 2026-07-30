function arrayTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1426>  # String: '__BC:Arrays/ArrayTests/arrayTest/start' (String)
    // USED → r2 = "__BC:Arrays/ArrayTests/arrayTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = globalThis.console.log("__BC:Arrays/ArrayTests/arrayTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 5, UInt16: 17500>  # Array: [5, 3, 8, 1, 9]
    // USED → r4 = [5, 3, 8, 1, 9];
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = [5, 3, 8, 1, 9].length;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    r2 = globalThis.console.log([5, 3, 8, 1, 9].length)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 4, string_id: 208>  # String: 'push' (Identifier)
    // USED → r3 = [5, 3, 8, 1, 9].push;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 100>
    // USED → r2 = 100;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = [5, 3, 8, 1, 9].push(100)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 5, string_id: 201>  # String: 'pop' (Identifier)
    // USED → r2 = [5, 3, 8, 1, 9].pop;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 4>
    r2 = [5, 3, 8, 1, 9].pop()
    // CODE → <NewArray>: <Reg8: 6, UInt16: 0>
    // USED → r6 = [];
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → <Mov>: <Reg8: 9, Reg8: 6>
    r9 = []
    // CODE → <Mov>: <Reg8: 8, Reg8: 4>
    r8 = [5, 3, 8, 1, 9]
    // CODE → <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = builtin_46(r-2, r-1, r0, r1)
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 6, string_id: 8127>  # String: 'sort' (Identifier)
    // USED → r3 = [].sort;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15075>  # Function: [#15075  of 12 bytes]: 3 params @ offset 0x001f3588
    // USED → r2 = function_15075;
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 6, Reg8: 2>
    // USED → r6 = [].sort(function_15075);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    r2 = globalThis.console.log([].sort(function_15075))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 7, string_id: 170>  # String: 'map' (Identifier)
    // USED → r3 = [5, 3, 8, 1, 9].map;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15076>  # Function: [#15076  of 12 bytes]: 2 params @ offset 0x00265113
    // USED → r2 = function_15076;
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r6 = [5, 3, 8, 1, 9].map(function_15076);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    r2 = globalThis.console.log([5, 3, 8, 1, 9].map(function_15076))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 137>  # String: 'filter' (Identifier)
    // USED → r3 = [5, 3, 8, 1, 9].filter;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15077>  # Function: [#15077  of 12 bytes]: 2 params @ offset 0x0026511f
    // USED → r2 = function_15077;
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r6 = [5, 3, 8, 1, 9].filter(function_15077);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    r2 = globalThis.console.log([5, 3, 8, 1, 9].filter(function_15077))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 9, string_id: 211>  # String: 'reduce' (Identifier)
    // USED → r3 = [5, 3, 8, 1, 9].reduce;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15078>  # Function: [#15078  of 12 bytes]: 3 params @ offset 0x0026512b
    // USED → r2 = function_15078;
    // CODE → <Call3>: <Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    // USED → r5 = [5, 3, 8, 1, 9].reduce(function_15078, 0);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
    r2 = globalThis.console.log([5, 3, 8, 1, 9].reduce(function_15078, 0))
    // CODE → <GetById>: <Reg8: 2, Reg8: 4, UInt8: 10, string_id: 8627>  # String: 'find' (Identifier)
    // USED → r2 = [5, 3, 8, 1, 9].find;
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15079>  # Function: [#15079  of 12 bytes]: 2 params @ offset 0x00265137
    // USED → r1 = function_15079;
    // CODE → <Call2>: <Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 1>
    // USED → r3 = [5, 3, 8, 1, 9].find(function_15079);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log([5, 3, 8, 1, 9].find(function_15079))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 11, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r3 = [5, 3, 8, 1, 9].slice;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r3 = [5, 3, 8, 1, 9].slice(1, 3);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    r1 = globalThis.console.log([5, 3, 8, 1, 9].slice(1, 3))
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 100>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 91>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 977>  # String: '__BC:Arrays/ArrayTests/arrayTest/end' (String)
    // USED → r0 = "__BC:Arrays/ArrayTests/arrayTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Arrays/ArrayTests/arrayTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}