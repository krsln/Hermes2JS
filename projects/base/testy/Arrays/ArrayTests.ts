export function arrayTest() {
    console.log("__BC:Arrays/ArrayTests/arrayTest/start");

    const arr = [5, 3, 8, 1, 9];

    console.log(arr.length);

    arr.push(100);
    arr.pop();

    const sorted = [...arr].sort((a, b) => a - b);
    console.log(sorted);

    const doubled = arr.map(v => v * 2);
    console.log(doubled);

    const filtered = arr.filter(v => v > 3);
    console.log(filtered);

    const sum = arr.reduce((acc, v) => acc + v, 0);
    console.log(sum);

    const found = arr.find(v => v > 5);
    console.log(found);

    const sliced = arr.slice(1, 3);
    console.log(sliced);

    console.log("__BC:Arrays/ArrayTests/arrayTest/end");
}
