export function ifTest(v: number) {
    console.log("__BC:ControlFlow/IfTests/ifTest/start");

    if (v > 10) {
        console.log("__BC:ControlFlow/IfTests/ifTest/branch-big");
        console.log("big");
    } else if (v > 5) {
        console.log("__BC:ControlFlow/IfTests/ifTest/branch-medium");
        console.log("medium");
    } else if (v === 0) {
        console.log("__BC:ControlFlow/IfTests/ifTest/branch-zero");
        console.log("zero");
    } else {
        console.log("__BC:ControlFlow/IfTests/ifTest/branch-small");
        console.log("small");
    }

    console.log("__BC:ControlFlow/IfTests/ifTest/end");
}

export function ifElseChainTest(a: boolean, b: boolean) {
    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/start");

    if (a && b) {
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-both");
        console.log("both");
    } else if (a || b) {
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-either");
        console.log("either");
    } else {
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-neither");
        console.log("neither");
    }

    if (!a) {
        console.log("__BC:ControlFlow/IfTests/ifElseChainTest/branch-not-a");
        console.log("not a");
    }

    console.log("__BC:ControlFlow/IfTests/ifElseChainTest/end");
}
