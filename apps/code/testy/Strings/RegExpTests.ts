// RegExp literals compile through the CreateRegExp opcode. Includes a
// pattern containing a literal single-quote character on purpose -
// this is a regression test for the CreateRegExp/OpcodeEntry parsing
// bug (the disassembler switches to double-quote delimiting for such
// patterns, e.g. `String: "'" (String)`, which the old regex-based
// comment parser failed to recognize).

export function basicRegExpTest(input: string) {
    console.log("__BC:Strings/RegExpTests/basicRegExpTest/start");

    const digitsOnly = /^\d+$/;
    console.log(digitsOnly.test(input));

    const global = /a/g;
    console.log(input.match(global));

    console.log("__BC:Strings/RegExpTests/basicRegExpTest/end");
}

export function regExpFlagsTest(input: string) {
    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/start");

    const caseInsensitive = /hello/i;
    const multiline = /^line/m;
    const globalSticky = /\w+/gu;

    console.log(caseInsensitive.test(input));
    console.log(multiline.test(input));
    console.log(input.match(globalSticky));

    console.log("__BC:Strings/RegExpTests/regExpFlagsTest/end");
}

// Regression test: pattern is a single apostrophe character.
export function regExpSingleQuotePatternTest(input: string) {
    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/start");

    const apostrophe = /'/g;
    console.log(input.replace(apostrophe, "\u2019"));

    const quoteOrDash = /['-]/g;
    console.log(input.replace(quoteOrDash, "_"));

    console.log("__BC:Strings/RegExpTests/regExpSingleQuotePatternTest/end");
}

export function regExpGroupsAndReplaceTest(input: string) {
    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/start");

    const dateRe = /(\d{4})-(\d{2})-(\d{2})/;
    const match = input.match(dateRe);
    console.log(match);

    const swapped = input.replace(dateRe, "$3/$2/$1");
    console.log(swapped);

    console.log("__BC:Strings/RegExpTests/regExpGroupsAndReplaceTest/end");
}

export function callRegExpTests() {
    console.log("__BC:Strings/RegExpTests/callRegExpTests/start");

    basicRegExpTest("abc123");
    regExpFlagsTest("Hello\nline two");
    regExpSingleQuotePatternTest("it's a test - really");
    regExpGroupsAndReplaceTest("2024-01-15");

    console.log("__BC:Strings/RegExpTests/callRegExpTests/end");
}
