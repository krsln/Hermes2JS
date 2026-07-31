// Ternary expressions and short-circuit logical/nullish assignment
// operators - these lower to conditional-jump patterns similar to
// if/else but *inside an expression*, which is a different structuring
// surface than a statement-level `if`.

export function ternaryTest(v: number) {
    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/start");

    const label = v > 0 ? "positive" : v < 0 ? "negative" : "zero";
    console.log(label);

    const clamped = v > 100 ? 100 : (v < 0 ? 0 : v);
    console.log(clamped);

    console.log("__BC:ControlFlow/TernaryTests/ternaryTest/end");
}

export function shortCircuitAssignTest() {
    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/start");

    let a: number | null = null;
    a ??= 5;
    console.log(a);

    let b = 0;
    b ||= 10;
    console.log(b);

    let c = 1;
    c &&= 20;
    console.log(c);

    const obj: { count?: number } = {};
    obj.count ??= 0;
    obj.count += 1;
    console.log(obj.count);

    console.log("__BC:ControlFlow/TernaryTests/shortCircuitAssignTest/end");
}

export function logicalShortCircuitTest(a: boolean, b: boolean) {
    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/start");

    function sideEffect(tag: string, value: boolean) {
        console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/side-effect", tag);
        return value;
    }

    const and = sideEffect("and-left", a) && sideEffect("and-right", b);
    const or = sideEffect("or-left", a) || sideEffect("or-right", b);
    const nullish = (a ? null : "left") ?? sideEffect("nullish-right", b);

    console.log(and, or, nullish);

    console.log("__BC:ControlFlow/TernaryTests/logicalShortCircuitTest/end");
}
