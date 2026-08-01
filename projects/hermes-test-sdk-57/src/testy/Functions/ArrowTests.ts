export function arrowFunctionTest() {
    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/start");

    const add = (a: number, b: number) => a + b;
    console.log(add(2, 3));

    const square = (n: number) => {
        return n * n;
    };
    console.log(square(4));

    const numbers = [1, 2, 3, 4];
    const doubled = numbers.map(n => n * 2);
    console.log(doubled);

    const makeMultiplier = (factor: number) => (value: number) => value * factor;
    const triple = makeMultiplier(3);
    console.log(triple(5));

    console.log("__BC:Functions/ArrowTests/arrowFunctionTest/end");
}
