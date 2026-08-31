function callRegExpTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 5000>  # String: '__BC:Strings/RegExpTests/callRegExpTests/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/callRegExpTests/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 33 | <LoadConstString>: <Reg8: 2, string_id: 4999>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → addr: 37 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → addr: 42 | <CreateRegExp>: <Reg8: 5, string_id: 4696, string_id: 6457, UInt32: 155>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    r5 = /^\\d+$/
    // CODE → addr: 56 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 62 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 67 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r5.test;
    // CODE → addr: 72 | <LoadConstString>: <Reg8: 6, string_id: 4772>  # String: 'abc123' (String)
    // USED → r6 = "abc123";
    // CODE → addr: 76 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    r2 = r5.test("abc123")
    // CODE → addr: 81 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 86 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 92 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = r6.match;
    // CODE → addr:102 | <CreateRegExp>: <Reg8: 2, string_id: 6471, string_id: 6578, UInt32: 156>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    r2 = /a/g
    // CODE → addr:116 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    r2 = r6.match(r2)
    // CODE → addr:121 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:126 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:132 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:137 | <LoadConstString>: <Reg8: 2, string_id: 4998>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → addr:141 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → addr:146 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:152 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:157 | <LoadConstString>: <Reg8: 2, string_id: 5003>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → addr:161 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → addr:166 | <CreateRegExp>: <Reg8: 7, string_id: 6140, string_id: 280, UInt32: 157>  # String: 'hello' (String)  # String: 'i' (String)
    r7 = /hello/i
    // CODE → addr:180 | <CreateRegExp>: <Reg8: 5, string_id: 4706, string_id: 6516, UInt32: 158>  # String: '^line' (String)  # String: 'm' (Identifier)
    r5 = /^line/m
    // CODE → addr:194 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:200 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:205 | <GetByIdShort>: <Reg8: 2, Reg8: 7, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r7.test;
    // CODE → addr:210 | <LoadConstString>: <Reg8: 6, string_id: 3377>  # String: 'Hello\nline two' (String)
    // USED → r6 = "Hello\\nline two";
    // CODE → addr:214 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 7, Reg8: 6>
    r2 = r7.test("Hello\\nline two")
    // CODE → addr:219 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:224 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:230 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:235 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = r5.test;
    // CODE → addr:240 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    r2 = r5.test("Hello\\nline two")
    // CODE → addr:245 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:250 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:256 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:261 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = r6.match;
    // CODE → addr:266 | <CreateRegExp>: <Reg8: 2, string_id: 1961, string_id: 2193, UInt32: 159>  # String: '\\w+' (String)  # String: 'gu' (String)
    r2 = /\\w+/gu
    // CODE → addr:280 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    r2 = r6.match(r2)
    // CODE → addr:285 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:290 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:296 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:301 | <LoadConstString>: <Reg8: 2, string_id: 5001>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → addr:305 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → addr:310 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:316 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:321 | <LoadConstString>: <Reg8: 2, string_id: 5007>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → addr:325 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → addr:330 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:336 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:341 | <LoadConstString>: <Reg8: 7, string_id: 3872>  # String: "it's a test - really" (String)
    r7 = "it's a test - really"
    // CODE → addr:345 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = r7.replace;
    // CODE → addr:350 | <LoadConstString>: <Reg8: 5, string_id: 6445>  # String: '’' (String)
    // USED → r5 = "\u2019";
    // CODE → addr:354 | <CreateRegExp>: <Reg8: 2, string_id: 833, string_id: 6578, UInt32: 160>  # String: "'" (String)  # String: 'g' (Identifier)
    r2 = /'/g
    // CODE → addr:368 | <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    r2 = r7.replace(r2, "\u2019")
    // CODE → addr:374 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:379 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:385 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:390 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = r7.replace;
    // CODE → addr:395 | <LoadConstString>: <Reg8: 5, string_id: 362>  # String: '_' (String)
    // USED → r5 = "_";
    // CODE → addr:399 | <CreateRegExp>: <Reg8: 2, string_id: 2515, string_id: 6578, UInt32: 161>  # String: "['-]" (String)  # String: 'g' (Identifier)
    r2 = /['-]/g
    // CODE → addr:413 | <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    r2 = r7.replace(r2, "_")
    // CODE → addr:419 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:424 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:430 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:435 | <LoadConstString>: <Reg8: 2, string_id: 5006>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → addr:439 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → addr:444 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:450 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:455 | <LoadConstString>: <Reg8: 2, string_id: 5005>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → addr:459 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → addr:464 | <CreateRegExp>: <Reg8: 5, string_id: 1955, string_id: 6457, UInt32: 162>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    r5 = /(\\d{4})-(\\d{2})-(\\d{2})/
    // CODE → addr:478 | <LoadConstString>: <Reg8: 4, string_id: 2233>  # String: '2024-01-15' (String)
    r4 = "2024-01-15"
    // CODE → addr:482 | <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r2 = r4.match;
    // CODE → addr:487 | <Call2>: <Reg8: 6, Reg8: 2, Reg8: 4, Reg8: 5>
    r6 = r4.match(r5)
    // CODE → addr:492 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:498 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:503 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log(r6)
    // CODE → addr:508 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r3 = r4.replace;
    // CODE → addr:513 | <LoadConstString>: <Reg8: 2, string_id: 1684>  # String: '$3/$2/$1' (String)
    // USED → r2 = "$3/$2/$1";
    // CODE → addr:517 | <Call3>: <Reg8: 4, Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 2>
    r4 = r4.replace(r5, "$3/$2/$1")
    // CODE → addr:523 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:529 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:534 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → addr:539 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:545 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:550 | <LoadConstString>: <Reg8: 2, string_id: 5004>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → addr:554 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → addr:559 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:565 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:570 | <LoadConstString>: <Reg8: 1, string_id: 4119>  # String: '__BC:Strings/RegExpTests/callRegExpTests/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/callRegExpTests/end";
    // CODE → addr:574 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/end")
    // CODE → addr:579 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:581 | <Ret>: <Reg8: 0>
    return undefined;
}