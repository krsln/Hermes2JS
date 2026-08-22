export function complexTest() {
    console.log("__BC:ControlFlow/ComplexTests/complexTest/start");

    const numbers = [1, 2, 3, 4, 5];

    for (let i = 0; i < numbers.length; i++) {

        switch (numbers[i]) {

            case 1:
                console.log("__BC:ControlFlow/ComplexTests/complexTest/case-1");
                break;

            case 2:
                console.log("__BC:ControlFlow/ComplexTests/complexTest/case-2-continue");
                continue;

            case 3:
                console.log("__BC:ControlFlow/ComplexTests/complexTest/case-3");
                console.log("three");
                break;

            default:
                console.log("__BC:ControlFlow/ComplexTests/complexTest/case-default");
                console.log("other");
        }

    }

    console.log("__BC:ControlFlow/ComplexTests/complexTest/end");
}
