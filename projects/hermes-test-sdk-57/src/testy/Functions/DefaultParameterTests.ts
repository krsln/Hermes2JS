export function defaultParameterTest(a: number, b: number = 10, label: string = "result") {
    console.log("__BC:Functions/DefaultParameterTests/defaultParameterTest/start");
    console.log(label, a + b);
}

export function defaultWithRestTest(base: number = 1, ...extras: number[]) {
    console.log("__BC:Functions/DefaultParameterTests/defaultWithRestTest/start");
    const total = extras.reduce((acc, v) => acc + v, base);
    console.log(total);
}

export function callDefaultParameterTests() {
    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/start");

    defaultParameterTest(5);
    defaultParameterTest(5, 20);
    defaultParameterTest(5, 20, "sum");

    defaultWithRestTest();
    defaultWithRestTest(2, 3, 4);

    console.log("__BC:Functions/DefaultParameterTests/callDefaultParameterTests/end");
}
