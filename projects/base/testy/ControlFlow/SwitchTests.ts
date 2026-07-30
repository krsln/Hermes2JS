export function switchTest(v: number) {
    console.log("__BC:ControlFlow/SwitchTests/switchTest/start");

    switch (v) {

        case 0:
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-0");
            return "zero";

        case 1:
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-1");
            return "one";

        case 2:
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-2");
            return "two";

        case 3:
        case 4:
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-3-4");
            return "three-four";

        default:
            console.log("__BC:ControlFlow/SwitchTests/switchTest/case-default");
            return "other";
    }

}
