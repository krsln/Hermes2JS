function arrayTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1448>  # String: '__BC:Arrays/ArrayTests/arrayTest/start' (String)
    // USED → r2 = "__BC:Arrays/ArrayTests/arrayTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Arrays/ArrayTests/arrayTest/start")
    // CODE → <NewArrayWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 5, UInt16: 17493>  # Array: [5, 3, 8, 1, 9]
    r4 = [5, 3, 8, 1, 9]
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = r4.length;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log(r2)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 4, string_id: 207>  # String: 'push' (Identifier)
    // USED → r3 = r4.push;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 100>
    // USED → r2 = 100;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r4.push(100)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 5, string_id: 199>  # String: 'pop' (Identifier)
    // USED → r2 = r4.pop;
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 4>
    r2 = r4.pop()
    // CODE → <NewArray>: <Reg8: 6, UInt16: 0>
    r6 = []
    // CODE → <LoadConstZero>: <Reg8: 5>
    // USED → r5 = 0;
    // CODE → <Mov>: <Reg8: 9, Reg8: 6>
    r9 = r6
    // CODE → <Mov>: <Reg8: 8, Reg8: 4>
    r8 = r4
    // CODE → <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = arraySpread(r-2, r-1, r0, r1)
    // CODE → <GetById>: <Reg8: 3, Reg8: 6, UInt8: 6, string_id: 7576>  # String: 'sort' (Identifier)
    // USED → r3 = r6.sort;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15111>  # Function: [#15111  of 12 bytes]: 3 params @ offset 0x001f6a9c
    // USED → r2 = function_15111(param1, param2);
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 6, Reg8: 2>
    // USED → r6 = r6.sort(function_15111(param1, param2));
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 7, string_id: 170>  # String: 'map' (Identifier)
    // USED → r3 = r4.map;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15112>  # Function: [#15112  of 12 bytes]: 2 params @ offset 0x00269c4e
    // USED → r2 = function_15112(param1);
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r6 = r4.map(function_15112(param1));
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 137>  # String: 'filter' (Identifier)
    // USED → r3 = r4.filter;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15113>  # Function: [#15113  of 12 bytes]: 2 params @ offset 0x00269c5a
    // USED → r2 = function_15113(param1);
    // CODE → <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r6 = r4.filter(function_15113(param1));
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 9, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r3 = r4.reduce;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15114>  # Function: [#15114  of 12 bytes]: 3 params @ offset 0x00269c66
    // USED → r2 = function_15114(param1, param2);
    // CODE → <Call3>: <Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    // USED → r5 = r4.reduce(function_15114(param1, param2), r5);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
    console.log(r5)
    // CODE → <GetById>: <Reg8: 2, Reg8: 4, UInt8: 10, string_id: 8819>  # String: 'find' (Identifier)
    // USED → r2 = r4.find;
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15115>  # Function: [#15115  of 12 bytes]: 2 params @ offset 0x00269c72
    // USED → r1 = function_15115(param1);
    // CODE → <Call2>: <Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 1>
    // USED → r3 = r4.find(function_15115(param1));
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 11, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r3 = r4.slice;
    // CODE → <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r3 = r4.slice(1, 3);
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 1011>  # String: '__BC:Arrays/ArrayTests/arrayTest/end' (String)
    // USED → r0 = "__BC:Arrays/ArrayTests/arrayTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Arrays/ArrayTests/arrayTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}