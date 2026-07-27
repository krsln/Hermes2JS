export function nestedLoopTest() {

    for (let i = 0; i < 3; i++) {

        let j = 0;

        while (j < 4) {

            if (i === 1) {

                if (j === 2) {
                    console.log("nested");
                }

            }

            j++;
        }
    }

}