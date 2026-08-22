export function forOfTest() {
    console.log("__BC:Iterators/IteratorTests/forOfTest/start");

    const arr = [1, 2, 3, 4];

    for (const item of arr) {
        console.log(item);
    }

    console.log("__BC:Iterators/IteratorTests/forOfTest/end");
}

export function forInTest() {
    console.log("__BC:Iterators/IteratorTests/forInTest/start");

    const obj = {
        a: 1,
        b: 2,
        c: 3
    };

    for (const key in obj) {
        const typedKey = key as keyof typeof obj;
        console.log(typedKey, obj[typedKey]);
    }

    console.log("__BC:Iterators/IteratorTests/forInTest/end");
}
