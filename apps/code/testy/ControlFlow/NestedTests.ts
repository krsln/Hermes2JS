export function nestedLoopTest() {
    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/start");

    for (let i = 0; i < 3; i++) {

        let j = 0;

        while (j < 4) {

            if (i === 1) {

                if (j === 2) {
                    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/deep-if");
                    console.log("nested");
                }

            }

            j++;
        }
    }

    console.log("__BC:ControlFlow/NestedTests/nestedLoopTest/end");
}
