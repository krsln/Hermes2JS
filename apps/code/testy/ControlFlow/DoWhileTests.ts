export function doWhileTest() {
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/start");
    let i = 0;

    do {
        console.log(i);
        i++;
    } while (i < 5);
    console.log("__BC:ControlFlow/DoWhileTests/doWhileTest/end");
}
