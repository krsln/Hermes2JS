// Dedicated destructuring depth tests - the existing files only touch
// destructuring lightly (a flat object/array pick). This covers
// nested patterns, defaults, renaming, and destructuring directly in
// a function's parameter list, each of which lowers differently.

export function nestedObjectDestructureTest() {
    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/start");

    const response = {
        status: 200,
        body: {
            user: { id: 1, name: "Ada" },
            meta: { page: 1 }
        }
    };

    const { status, body: { user: { name }, meta: { page = 1 } = {} } } = response;
    console.log(status, name, page);

    console.log("__BC:Objects/DestructuringTests/nestedObjectDestructureTest/end");
}

export function renamedDefaultDestructureTest() {
    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/start");

    const config: { timeout?: number; retries?: number } = { timeout: 500 };

    const { timeout: timeoutMs = 1000, retries: retryCount = 3 } = config;
    console.log(timeoutMs, retryCount);

    console.log("__BC:Objects/DestructuringTests/renamedDefaultDestructureTest/end");
}

export function nestedArrayDestructureTest() {
    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/start");

    const matrix = [[1, 2], [3, 4], [5, 6]];
    const [[a, b], , [, d]] = matrix;
    console.log(a, b, d);

    const [first = 0, second = 0, ...remaining] = [10];
    console.log(first, second, remaining);

    console.log("__BC:Objects/DestructuringTests/nestedArrayDestructureTest/end");
}

export function parameterDestructureTest({ id, name = "anon" }: { id: number; name?: string }, [x, y]: [number, number]) {
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/start");
    console.log(id, name, x, y);
    console.log("__BC:Objects/DestructuringTests/parameterDestructureTest/end");
}

export function swapViaDestructureTest() {
    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/start");

    let a = 1;
    let b = 2;
    [a, b] = [b, a];
    console.log(a, b);

    console.log("__BC:Objects/DestructuringTests/swapViaDestructureTest/end");
}

export function callDestructuringTests() {
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/start");

    nestedObjectDestructureTest();
    renamedDefaultDestructureTest();
    nestedArrayDestructureTest();
    parameterDestructureTest({ id: 7 }, [9, 10]);
    swapViaDestructureTest();

    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/end");
}
