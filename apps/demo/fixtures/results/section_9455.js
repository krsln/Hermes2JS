function arrayTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4690>  # String: '__BC:Arrays/ArrayTests/arrayTest/start' (String)
    // USED → r4 = "__BC:Arrays/ArrayTests/arrayTest/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    r4 = globalThis.console.log("__BC:Arrays/ArrayTests/arrayTest/start");
    // CODE → <NewArrayWithBuffer>: <Reg8: 5, UInt16: 5, UInt16: 5, UInt16: 48408>  # Array: [5, 3, 8, 1, 9]
    // USED → r5 = [5, 3, 8, 1, 9];
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r7 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r6 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 176>  # String: 'length' (Identifier)
    // USED → r4 = [5, 3, 8, 1, 9].length;
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 4>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].length);
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 86>  # String: 'push' (Identifier)
    // USED → r4 = [5, 3, 8, 1, 9].push;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 100>
    // USED → r0 = 100;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 0>
    r4 = [5, 3, 8, 1, 9].push(100);
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 207>  # String: 'pop' (Identifier)
    // USED → r4 = [5, 3, 8, 1, 9].pop;
    // CODE → <Call1>: <Reg8: 4, Reg8: 4, Reg8: 5>
    r4 = [5, 3, 8, 1, 9].pop();
    // CODE → <NewArray>: <Reg8: 7, UInt16: 0>
    // USED → r7 = [];
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Mov>: <Reg8: 10, Reg8: 7>
    r10 = [];
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    r9 = [5, 3, 8, 1, 9];
    // CODE → <LoadConstZero>: <Reg8: 8>
    r8 = 0;
    // CODE → <CallBuiltin>: <Reg8: 1, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r1 = builtin_48(r-3, r-2, r-1, r0);
    // CODE → <GetById>: <Reg8: 6, Reg8: 7, UInt8: 5, string_id: 7558>  # String: 'sort' (Identifier)
    // USED → r6 = [].sort;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12398>  # Function: [#12398  of 12 bytes]: 3 params @ offset 0x00234096
    // USED → r4 = function_12398;
    // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 7, Reg8: 4>
    // USED → r7 = [].sort(function_12398);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    r4 = globalThis.console.log([].sort(function_12398));
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 6, string_id: 125>  # String: 'map' (Identifier)
    // USED → r6 = [5, 3, 8, 1, 9].map;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12399>  # Function: [#12399  of 12 bytes]: 2 params @ offset 0x0023e3a7
    // USED → r4 = function_12399;
    // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = [5, 3, 8, 1, 9].map(function_12399);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].map(function_12399));
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 7, string_id: 141>  # String: 'filter' (Identifier)
    // USED → r6 = [5, 3, 8, 1, 9].filter;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12400>  # Function: [#12400  of 12 bytes]: 2 params @ offset 0x0023e3b3
    // USED → r4 = function_12400;
    // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = [5, 3, 8, 1, 9].filter(function_12400);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].filter(function_12400));
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 8, string_id: 214>  # String: 'reduce' (Identifier)
    // USED → r6 = [5, 3, 8, 1, 9].reduce;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12401>  # Function: [#12401  of 12 bytes]: 3 params @ offset 0x0023e3bf
    // USED → r4 = function_12401;
    // CODE → <Call3>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 0>
    // USED → r7 = [5, 3, 8, 1, 9].reduce(function_12401, 0);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].reduce(function_12401, 0));
    // CODE → <GetById>: <Reg8: 6, Reg8: 5, UInt8: 9, string_id: 8661>  # String: 'find' (Identifier)
    // USED → r6 = [5, 3, 8, 1, 9].find;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12402>  # Function: [#12402  of 12 bytes]: 2 params @ offset 0x0023e3cb
    // USED → r4 = function_12402;
    // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = [5, 3, 8, 1, 9].find(function_12402);
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].find(function_12402));
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 10, string_id: 118>  # String: 'slice' (Identifier)
    // USED → r4 = [5, 3, 8, 1, 9].slice;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <Call3>: <Reg8: 6, Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 1>
    // USED → r6 = [5, 3, 8, 1, 9].slice(1, 3);
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
    r4 = globalThis.console.log([5, 3, 8, 1, 9].slice(1, 3));
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 106>  # String: 'console' (Identifier)
    // USED → r5 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 177>  # String: 'log' (Identifier)
    // USED → r4 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4689>  # String: '__BC:Arrays/ArrayTests/arrayTest/end' (String)
    // USED → r3 = "__BC:Arrays/ArrayTests/arrayTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    r3 = globalThis.console.log("__BC:Arrays/ArrayTests/arrayTest/end");
    // CODE → <Ret>: <Reg8: 2>
    return undefined;
}