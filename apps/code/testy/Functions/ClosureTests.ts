export function closureTest() {
    console.log("__BC:Functions/ClosureTests/closureTest/start");

    function makeCounter() {
        let count = 0;
        return {
            increment: () => ++count,
            decrement: () => --count,
            value: () => count
        };
    }

    const counter = makeCounter();
    counter.increment();
    counter.increment();
    counter.decrement();

    console.log(counter.value());

    console.log("__BC:Functions/ClosureTests/closureTest/end");
}

export function closureLoopTest() {
    console.log("__BC:Functions/ClosureTests/closureLoopTest/start");

    const fns: (() => number)[] = [];

    for (let i = 0; i < 3; i++) {
        fns.push(() => i);
    }

    for (const fn of fns) {
        console.log(fn());
    }

    console.log("__BC:Functions/ClosureTests/closureLoopTest/end");
}
