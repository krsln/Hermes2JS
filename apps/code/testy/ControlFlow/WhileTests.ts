export function whileTest() {
    console.log("__BC:ControlFlow/WhileTests/whileTest/start");
    let i = 0;

    while (i < 5) {
        console.log("while", i);

        if (i === 2) {
            console.log("__BC:ControlFlow/WhileTests/whileTest/if-continue");
            i++;
            continue;
        }

        i++;
    }
    console.log("__BC:ControlFlow/WhileTests/whileTest/end");
}
