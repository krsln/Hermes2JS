export function forTest() {
    console.log("__BC:ControlFlow/ForTests/forTest/start");
    for (let i = 0; i < 10; i++) {

        if (i === 3) {
            console.log("__BC:ControlFlow/ForTests/forTest/if-continue");
            continue;
        }

        if (i === 8) {
            console.log("__BC:ControlFlow/ForTests/forTest/if-break");
            break;
        }

        console.log(i);
    }
    console.log("__BC:ControlFlow/ForTests/forTest/end");
}
