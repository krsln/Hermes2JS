function arrayTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → addr:  2 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  4 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 10 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 15 | <LoadConstString>: <Reg8: 2, string_id: 1448>  # String: '__BC:Arrays/ArrayTests/arrayTest/start' (String)
    // USED → r2 = "__BC:Arrays/ArrayTests/arrayTest/start";
    // CODE → addr: 19 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Arrays/ArrayTests/arrayTest/start")
    // CODE → addr: 24 | <NewArrayWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 5, UInt16: 17493>  # Array: [5, 3, 8, 1, 9]
    r4 = [5, 3, 8, 1, 9]
    // CODE → addr: 32 | <TryGetById>: <Reg8: 5, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 38 | <GetByIdShort>: <Reg8: 3, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 43 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
    // USED → r2 = r4.length;
    // CODE → addr: 48 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 2>
    console.log(r4.length)
    // CODE → addr: 53 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 4, string_id: 207>  # String: 'push' (Identifier)
    // USED → r3 = r4.push;
    // CODE → addr: 58 | <LoadConstUInt8>: <Reg8: 2, UInt8: 100>
    // USED → r2 = 100;
    // CODE → addr: 61 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r4.push(100)
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 5, string_id: 199>  # String: 'pop' (Identifier)
    // USED → r2 = r4.pop;
    // CODE → addr: 71 | <Call1>: <Reg8: 2, Reg8: 2, Reg8: 4>
    r2 = r4.pop()
    // CODE → addr: 75 | <NewArray>: <Reg8: 6, UInt16: 0>
    r6 = []
    // CODE → addr: 79 | <LoadConstZero>: <Reg8: 5>
    r5 = 0
    // CODE → addr: 81 | <Mov>: <Reg8: 9, Reg8: 6>
    r9 = r6
    // CODE → addr: 84 | <Mov>: <Reg8: 8, Reg8: 4>
    r8 = r4
    // CODE → addr: 87 | <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → addr: 89 | <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = arraySpread(r9, r8, r7, r6)
    // CODE → addr: 93 | <GetById>: <Reg8: 3, Reg8: 6, UInt8: 6, string_id: 7576>  # String: 'sort' (Identifier)
    // USED → r3 = r6.sort;
    // CODE → addr: 99 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15111>  # Function: [#15111  of 12 bytes]: 3 params @ offset 0x001f6a9c
    // USED → r2 = function_15111(param1, param2);
    // CODE → addr:104 | <Call2>: <Reg8: 6, Reg8: 3, Reg8: 6, Reg8: 2>
    r6 = r6.sort(function_15111(param1, param2))
    // CODE → addr:109 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:120 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → addr:125 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 7, string_id: 170>  # String: 'map' (Identifier)
    // USED → r3 = r4.map;
    // CODE → addr:130 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15112>  # Function: [#15112  of 12 bytes]: 2 params @ offset 0x00269c4e
    // USED → r2 = function_15112(param1);
    // CODE → addr:135 | <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    r6 = r4.map(function_15112(param1))
    // CODE → addr:140 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:146 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:151 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → addr:156 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 8, string_id: 137>  # String: 'filter' (Identifier)
    // USED → r3 = r4.filter;
    // CODE → addr:161 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15113>  # Function: [#15113  of 12 bytes]: 2 params @ offset 0x00269c5a
    // USED → r2 = function_15113(param1);
    // CODE → addr:166 | <Call2>: <Reg8: 6, Reg8: 3, Reg8: 4, Reg8: 2>
    r6 = r4.filter(function_15113(param1))
    // CODE → addr:171 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:177 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:182 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → addr:187 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 9, string_id: 210>  # String: 'reduce' (Identifier)
    // USED → r3 = r4.reduce;
    // CODE → addr:192 | <CreateClosure>: <Reg8: 2, Reg8: 1, function_id: 15114>  # Function: [#15114  of 12 bytes]: 3 params @ offset 0x00269c66
    // USED → r2 = function_15114(param1, param2);
    // CODE → addr:197 | <Call3>: <Reg8: 5, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 5>
    r5 = r4.reduce(function_15114(param1, param2), r5)
    // CODE → addr:203 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:209 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:214 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5>
    console.log(r5)
    // CODE → addr:219 | <GetById>: <Reg8: 2, Reg8: 4, UInt8: 10, string_id: 8819>  # String: 'find' (Identifier)
    // USED → r2 = r4.find;
    // CODE → addr:225 | <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 15115>  # Function: [#15115  of 12 bytes]: 2 params @ offset 0x00269c72
    // USED → r1 = function_15115(param1);
    // CODE → addr:230 | <Call2>: <Reg8: 3, Reg8: 2, Reg8: 4, Reg8: 1>
    r3 = r4.find(function_15115(param1))
    // CODE → addr:235 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:241 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:246 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:251 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 11, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r3 = r4.slice;
    // CODE → addr:256 | <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
    // USED → r2 = 1;
    // CODE → addr:259 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → addr:262 | <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 1>
    r3 = r4.slice(1, 3)
    // CODE → addr:268 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:274 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:279 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
    console.log(r3)
    // CODE → addr:284 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:290 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:295 | <LoadConstString>: <Reg8: 0, string_id: 1011>  # String: '__BC:Arrays/ArrayTests/arrayTest/end' (String)
    // USED → r0 = "__BC:Arrays/ArrayTests/arrayTest/end";
    // CODE → addr:299 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Arrays/ArrayTests/arrayTest/end")
    // CODE → addr:304 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:306 | <Ret>: <Reg8: 0>
    return r0;
}