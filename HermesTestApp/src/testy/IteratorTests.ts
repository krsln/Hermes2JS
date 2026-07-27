export function forOfTest() {

    const arr = [1, 2, 3, 4];

    for (const item of arr) {
        console.log(item);
    }

}

export function forInTest() {

    const obj = {
        a: 1,
        b: 2,
        c: 3
    };

    for (const key in obj) {
        const typedKey = key as keyof typeof obj;
        console.log(typedKey, obj[typedKey]);
    }

}