// Rest parameters and the implicit `arguments` object - distinct from
// DefaultParameterTests' single minimal case; exercises rest-only
// signatures, rest-after-required, and legacy `arguments` access side
// by side.

export function restOnlyTest(...values: number[]) {
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/start");
    console.log(values.length, values);
    console.log("__BC:Functions/RestParameterTests/restOnlyTest/end");
}

export function restAfterRequiredTest(first: string, second: string, ...rest: string[]) {
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/start");
    console.log(first, second, rest);
    console.log("__BC:Functions/RestParameterTests/restAfterRequiredTest/end");
}

// eslint-disable-next-line prefer-rest-params
export function legacyArgumentsTest() {
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/start");
    // eslint-disable-next-line prefer-rest-params
    console.log(arguments.length);
    for (let i = 0; i < arguments.length; i++) {
        // eslint-disable-next-line prefer-rest-params
        console.log(arguments[i]);
    }
    console.log("__BC:Functions/RestParameterTests/legacyArgumentsTest/end");
}

export function callRestParameterTests() {
    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/start");

    restOnlyTest();
    restOnlyTest(1, 2, 3);

    restAfterRequiredTest("a", "b");
    restAfterRequiredTest("a", "b", "c", "d");

    legacyArgumentsTest();

    console.log("__BC:Functions/RestParameterTests/callRestParameterTests/end");
}
