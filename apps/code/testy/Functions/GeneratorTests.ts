// Generator functions compile through a distinct opcode path
// (CreateGeneratorClosure et al.) and involve implicit state-machine
// control flow (each `yield` is a suspend/resume point) that a normal
// function's CFG doesn't have.

export function* simpleGeneratorTest() {
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start");
    yield 1;
    yield 2;
    yield 3;
    console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end");
}

export function* generatorWithLoopTest(n: number) {
    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/start");

    for (let i = 0; i < n; i++) {
        if (i === 2) {
            console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/skip");
            continue;
        }
        yield i * i;
    }

    console.log("__BC:Functions/GeneratorTests/generatorWithLoopTest/end");
}

export function* generatorTryFinallyTest() {
    console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start");

    try {
        yield "a";
        yield "b";
    } finally {
        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup");
    }
}

export function callGeneratorTests() {
    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/start");

    for (const value of simpleGeneratorTest()) {
        console.log(value);
    }

    for (const value of generatorWithLoopTest(5)) {
        console.log(value);
    }

    const it = generatorTryFinallyTest();
    console.log(it.next());
    console.log(it.return(undefined));

    console.log("__BC:Functions/GeneratorTests/callGeneratorTests/end");
}
