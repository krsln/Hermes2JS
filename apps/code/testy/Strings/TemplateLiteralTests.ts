// Template literals - string concatenation with embedded expressions
// compiles very differently from plain string constants (a chain of
// ToString + concat calls, or a dedicated template-object opcode for
// tagged templates).

export function basicTemplateTest(name: string, age: number) {
    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/start");

    const greeting = `Hello, ${name}! You are ${age} years old.`;
    console.log(greeting);

    const multiline = `line one
line two`;
    console.log(multiline);

    console.log("__BC:Strings/TemplateLiteralTests/basicTemplateTest/end");
}

export function nestedTemplateTest(a: number, b: number) {
    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/start");

    const result = `sum is ${a + b > 10 ? `big (${a + b})` : `small (${a + b})`}`;
    console.log(result);

    console.log("__BC:Strings/TemplateLiteralTests/nestedTemplateTest/end");
}

function tag(strings: TemplateStringsArray, ...values: unknown[]) {
    console.log("__BC:Strings/TemplateLiteralTests/tag/invoked");
    return strings.reduce((acc, s, i) => acc + s + (values[i] !== undefined ? String(values[i]) : ""), "");
}

export function taggedTemplateTest(x: number) {
    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/start");

    const output = tag`x squared is ${x * x}`;
    console.log(output);

    console.log("__BC:Strings/TemplateLiteralTests/taggedTemplateTest/end");
}
