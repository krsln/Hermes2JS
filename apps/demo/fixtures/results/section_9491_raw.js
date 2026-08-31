function arrayTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 4, string_id: 4712>  # String: '__BC:Arrays/ArrayTests/arrayTest/start' (String)
    // USED → r4 = "__BC:Arrays/ArrayTests/arrayTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Arrays/ArrayTests/arrayTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 5, UInt16: 5, UInt16: 5, UInt16: 15071>  # Array: [5, 3, 8, 1, 9]
    r5 = [5, 3, 8, 1, 9]
    // CODE → addr: 30 | <TryGetById>: <Reg8: 7, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r7 = console;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r6 = console.log;
    // CODE → addr: 41 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 177>  # String: 'length' (Identifier)
    // USED → r4 = r5.length;
    // CODE → addr: 46 | <Call2>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 4>
    console.log(r5.length)
    // CODE → addr: 51 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 3, string_id: 88>  # String: 'push' (Identifier)
    // USED → r4 = r5.push;
    // CODE → addr: 56 | <LoadConstUInt8>: <Reg8: 0, UInt8: 100>
    // USED → r0 = 100;
    // CODE → addr: 59 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 0>
    r4 = r5.push(100)
    // CODE → addr: 64 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 206>  # String: 'pop' (Identifier)
    // USED → r4 = r5.pop;
    // CODE → addr: 69 | <Call1>: <Reg8: 4, Reg8: 4, Reg8: 5>
    r4 = r5.pop()
    // CODE → addr: 73 | <NewArray>: <Reg8: 7, UInt16: 0>
    r7 = []
    // CODE → addr: 77 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 79 | <Mov>: <Reg8: 10, Reg8: 7>
    r10 = r7
    // CODE → addr: 82 | <Mov>: <Reg8: 9, Reg8: 5>
    r9 = r5
    // CODE → addr: 85 | <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → addr: 87 | <CallBuiltin>: <Reg8: 1, UInt8: 48, UInt8: 4>  # Built-in function: [#48 arraySpread]
    r1 = arraySpread(r10, r9, r8, r7)
    // CODE → addr: 91 | <GetById>: <Reg8: 6, Reg8: 7, UInt8: 5, string_id: 7762>  # String: 'sort' (Identifier)
    // USED → r6 = r7.sort;
    // CODE → addr: 97 | <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → addr: 99 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12472>  # Function: [#12472  of 12 bytes]: 3 params @ offset 0x00239ae7
    // USED → r4 = function_12472(param1, param2);
    // CODE → addr:104 | <Call2>: <Reg8: 7, Reg8: 6, Reg8: 7, Reg8: 4>
    // USED → r7 = r7.sort(function_12472(param1, param2));
    // CODE → addr:109 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:115 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:120 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:125 | <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 6, string_id: 126>  # String: 'map' (Identifier)
    // USED → r6 = r5.map;
    // CODE → addr:130 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12473>  # Function: [#12473  of 12 bytes]: 2 params @ offset 0x00243e0c
    // USED → r4 = function_12473(param1);
    // CODE → addr:135 | <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = r5.map(function_12473(param1));
    // CODE → addr:140 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:146 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:151 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:156 | <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 7, string_id: 142>  # String: 'filter' (Identifier)
    // USED → r6 = r5.filter;
    // CODE → addr:161 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12474>  # Function: [#12474  of 12 bytes]: 2 params @ offset 0x00243e18
    // USED → r4 = function_12474(param1);
    // CODE → addr:166 | <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = r5.filter(function_12474(param1));
    // CODE → addr:171 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:177 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:182 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:187 | <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 8, string_id: 213>  # String: 'reduce' (Identifier)
    // USED → r6 = r5.reduce;
    // CODE → addr:192 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12475>  # Function: [#12475  of 12 bytes]: 3 params @ offset 0x00243e24
    // USED → r4 = function_12475(param1, param2);
    // CODE → addr:197 | <Call3>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 0>
    // USED → r7 = r5.reduce(function_12475(param1, param2), r0);
    // CODE → addr:203 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:209 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:214 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:219 | <GetById>: <Reg8: 6, Reg8: 5, UInt8: 9, string_id: 8919>  # String: 'find' (Identifier)
    // USED → r6 = r5.find;
    // CODE → addr:225 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 12476>  # Function: [#12476  of 12 bytes]: 2 params @ offset 0x00243e30
    // USED → r4 = function_12476(param1);
    // CODE → addr:230 | <Call2>: <Reg8: 7, Reg8: 6, Reg8: 5, Reg8: 4>
    // USED → r7 = r5.find(function_12476(param1));
    // CODE → addr:235 | <TryGetById>: <Reg8: 6, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:241 | <GetByIdShort>: <Reg8: 4, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:246 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 6, Reg8: 7>
    console.log(r7)
    // CODE → addr:251 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 10, string_id: 120>  # String: 'slice' (Identifier)
    // USED → r4 = r5.slice;
    // CODE → addr:256 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → addr:259 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr:262 | <Call3>: <Reg8: 6, Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 1>
    // USED → r6 = r5.slice(1, 3);
    // CODE → addr:268 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:274 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:279 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 6>
    console.log(r6)
    // CODE → addr:284 | <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:290 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:295 | <LoadConstString>: <Reg8: 3, string_id: 4711>  # String: '__BC:Arrays/ArrayTests/arrayTest/end' (String)
    // USED → r3 = "__BC:Arrays/ArrayTests/arrayTest/end";
    // CODE → addr:299 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Arrays/ArrayTests/arrayTest/end")
    // CODE → addr:304 | <Ret>: <Reg8: 2>
    return r2;
}