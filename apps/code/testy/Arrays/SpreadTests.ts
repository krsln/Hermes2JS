export function spreadArrayTest() {
    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start");

    const a = [1, 2, 3];
    const b = [4, 5, 6];

    const combined = [...a, ...b];
    console.log(combined);

    const withExtra = [0, ...a, 99];
    console.log(withExtra);

    const [first, ...rest] = combined;
    console.log(first, rest);

    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end");
}

export function spreadObjectTest() {
    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/start");

    const base = { x: 1, y: 2 };
    const extended = { ...base, z: 3 };

    console.log(extended);

    const { x, ...others } = extended;
    console.log(x, others);

    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/end");
}

export function spreadFunctionArgsTest() {
    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/start");

    function sum(a: number, b: number, c: number) {
        return a + b + c;
    }

    const nums: [number, number, number] = [1, 2, 3];
    console.log(sum(...nums));

    console.log("__BC:Arrays/SpreadTests/spreadFunctionArgsTest/end");
}
