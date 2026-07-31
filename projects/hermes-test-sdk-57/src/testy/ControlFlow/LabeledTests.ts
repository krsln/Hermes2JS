// Labeled break/continue - these compile to multi-level jumps in
// Hermes bytecode (a break/continue that targets an outer loop, not
// the innermost one), which is a distinct structuring challenge from
// ordinary single-level break/continue already covered elsewhere.

export function labeledBreakTest() {
    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/start");

    outer:
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (i === 1 && j === 1) {
                console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/break-outer");
                break outer;
            }
            console.log(i, j);
        }
    }

    console.log("__BC:ControlFlow/LabeledTests/labeledBreakTest/end");
}

export function labeledContinueTest() {
    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/start");

    outer:
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (j === 1) {
                console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/continue-outer");
                continue outer;
            }
            console.log(i, j);
        }
        console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/unreachable-with-j1");
    }

    console.log("__BC:ControlFlow/LabeledTests/labeledContinueTest/end");
}

export function labeledBlockBreakTest() {
    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/start");

    block: {
        console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/before-break");
        if (Math.random() < 2) {
            break block;
        }
        console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/unreachable");
    }

    console.log("__BC:ControlFlow/LabeledTests/labeledBlockBreakTest/end");
}

export function tripleNestedLabeledTest() {
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/start");

    let hits = 0;

    outer:
    for (let i = 0; i < 3; i++) {
        middle:
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                hits++;

                if (k === 1) {
                    continue middle;
                }

                if (i === 2 && j === 2) {
                    break outer;
                }
            }
        }
    }

    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/hits", hits);
    console.log("__BC:ControlFlow/LabeledTests/tripleNestedLabeledTest/end");
}
