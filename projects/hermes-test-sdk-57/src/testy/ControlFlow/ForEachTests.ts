export function forEachTest() {
    console.log("__BC:ControlFlow/ForEachTests/forEachTest/start");

    const list = [10, 20, 30, 40];

    list.forEach((value, index) => {

        if (index === 2) {
            console.log("__BC:ControlFlow/ForEachTests/forEachTest/if-middle");
            console.log("middle");
        }

        console.log(index, value);

    });

    console.log("__BC:ControlFlow/ForEachTests/forEachTest/end");
}
