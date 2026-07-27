export function complexTest() {

    const numbers = [1, 2, 3, 4, 5];

    for (let i = 0; i < numbers.length; i++) {

        switch (numbers[i]) {

            case 1:
                break;

            case 2:
                continue;

            case 3:
                console.log("three");
                break;

            default:
                console.log("other");
        }

    }

}