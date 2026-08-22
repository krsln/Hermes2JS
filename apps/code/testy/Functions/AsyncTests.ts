// async/await is typically lowered to a generator-like state machine
// too (each `await` is a suspend/resume point, similar to `yield`),
// but driven by Promise resolution instead of an explicit iterator
// protocol - worth testing separately from GeneratorTests since the
// bytecode path (and any try/catch interaction around `await`) can
// differ.

function delay<T>(value: T): Promise<T> {
    return Promise.resolve(value);
}

export async function simpleAsyncTest() {
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/start");
    const value = await delay(42);
    console.log(value);
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/end");
    return value;
}

export async function asyncTryCatchTest() {
    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/start");

    try {
        const value = await delay(1);
        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/awaited", value);

        if (value === 1) {
            throw new Error("post-await failure");
        }

    } catch (e) {
        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/caught");

    } finally {
        console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally");
    }

    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/end");
}

export async function asyncLoopTest(items: number[]) {
    console.log("__BC:Functions/AsyncTests/asyncLoopTest/start");

    let total = 0;

    for (const item of items) {
        total += await delay(item);
    }

    console.log(total);
    console.log("__BC:Functions/AsyncTests/asyncLoopTest/end");
    return total;
}

export async function parallelAwaitTest() {
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start");

    const [a, b] = await Promise.all([delay(1), delay(2)]);
    console.log(a, b);

    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end");
}

export async function callAsyncTests() {
    console.log("__BC:Functions/AsyncTests/callAsyncTests/start");

    await simpleAsyncTest();
    await asyncTryCatchTest();
    await asyncLoopTest([1, 2, 3]);
    await parallelAwaitTest();

    console.log("__BC:Functions/AsyncTests/callAsyncTests/end");
}
