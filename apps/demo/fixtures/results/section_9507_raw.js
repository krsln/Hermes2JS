function callRegExpTests(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5000>  # String: '__BC:Strings/RegExpTests/callRegExpTests/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/callRegExpTests/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/start")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4999>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start")
    // CODE → <CreateRegExp>: <Reg8: 5, string_id: 4696, string_id: 6457, UInt32: 155>  # String: '^\\d+$' (String)  # String: '' (Identifier)
    // USED → r5 = /^\\d+$/;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /^\\d+$/.test;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 4772>  # String: 'abc123' (String)
    // USED → r6 = "abc123";
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    // USED → r2 = /^\\d+$/.test("abc123");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(/^\\d+$/.test("abc123"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = "abc123".match;
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 6471, string_id: 6578, UInt32: 156>  # String: 'a' (Identifier)  # String: 'g' (Identifier)
    // USED → r2 = /a/g;
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    // USED → r2 = "abc123".match(/a/g);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("abc123".match(/a/g))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4998>  # String: '__BC:Strings/RegExpTests/basicRegExpTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/basicRegExpTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5003>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start")
    // CODE → <CreateRegExp>: <Reg8: 7, string_id: 6140, string_id: 280, UInt32: 157>  # String: 'hello' (String)  # String: 'i' (String)
    // USED → r7 = /hello/i;
    // CODE → <CreateRegExp>: <Reg8: 5, string_id: 4706, string_id: 6516, UInt32: 158>  # String: '^line' (String)  # String: 'm' (Identifier)
    // USED → r5 = /^line/m;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 7, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /hello/i.test;
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 3377>  # String: 'Hello\nline two' (String)
    // USED → r6 = "Hello\\nline two";
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 7, Reg8: 6>
    // USED → r2 = /hello/i.test("Hello\\nline two");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(/hello/i.test("Hello\\nline two"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 47>  # String: 'test' (Identifier)
    // USED → r2 = /^line/m.test;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    // USED → r2 = /^line/m.test("Hello\\nline two");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(/^line/m.test("Hello\\nline two"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r5 = "Hello\\nline two".match;
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 1961, string_id: 2193, UInt32: 159>  # String: '\\w+' (String)  # String: 'gu' (String)
    // USED → r2 = /\\w+/gu;
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    // USED → r2 = "Hello\\nline two".match(/\\w+/gu);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("Hello\\nline two".match(/\\w+/gu))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5001>  # String: '__BC:Strings/RegExpTests/regExpFlagsTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpFlagsTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5007>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 7, string_id: 3872>  # String: "it's a test - really" (String)
    // USED → r7 = "it's a test - really";
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = "it's a test - really".replace;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 6445>  # String: '’' (String)
    // USED → r5 = "\u2019";
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 833, string_id: 6578, UInt32: 160>  # String: "'" (String)  # String: 'g' (Identifier)
    // USED → r2 = /'/g;
    // CODE → <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = "it's a test - really".replace(/'/g, "\u2019");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("it's a test - really".replace(/'/g, "\u2019"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r6 = "it's a test - really".replace;
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 362>  # String: '_' (String)
    // USED → r5 = "_";
    // CODE → <CreateRegExp>: <Reg8: 2, string_id: 2515, string_id: 6578, UInt32: 161>  # String: "['-]" (String)  # String: 'g' (Identifier)
    // USED → r2 = /['-]/g;
    // CODE → <Call3>: <Reg8: 2, Reg8: 6, Reg8: 7, Reg8: 2, Reg8: 5>
    // USED → r2 = "it's a test - really".replace(/['-]/g, "_");
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("it's a test - really".replace(/['-]/g, "_"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5006>  # String: '__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5005>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start")
    // CODE → <CreateRegExp>: <Reg8: 5, string_id: 1955, string_id: 6457, UInt32: 162>  # String: '(\\d{4})-(\\d{2})-(\\d{2})' (String)  # String: '' (Identifier)
    // USED → r5 = /(\\d{4})-(\\d{2})-(\\d{2})/;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 2233>  # String: '2024-01-15' (String)
    // USED → r4 = "2024-01-15";
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 3, string_id: 180>  # String: 'match' (Identifier)
    // USED → r2 = "2024-01-15".match;
    // CODE → <Call2>: <Reg8: 6, Reg8: 2, Reg8: 4, Reg8: 5>
    // USED → r6 = "2024-01-15".match(/(\\d{4})-(\\d{2})-(\\d{2})/);
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 6>
    console.log("2024-01-15".match(/(\\d{4})-(\\d{2})-(\\d{2})/))
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 4, string_id: 217>  # String: 'replace' (Identifier)
    // USED → r3 = "2024-01-15".replace;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1684>  # String: '$3/$2/$1' (String)
    // USED → r2 = "$3/$2/$1";
    // CODE → <Call3>: <Reg8: 4, Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 2>
    // USED → r4 = "2024-01-15".replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1");
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log("2024-01-15".replace(/(\\d{4})-(\\d{2})-(\\d{2})/, "$3/$2/$1"))
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 5004>  # String: '__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end' (String)
    // USED → r2 = "__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4119>  # String: '__BC:Strings/RegExpTests/callRegExpTests/end' (String)
    // USED → r1 = "__BC:Strings/RegExpTests/callRegExpTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Strings/RegExpTests/callRegExpTests/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}