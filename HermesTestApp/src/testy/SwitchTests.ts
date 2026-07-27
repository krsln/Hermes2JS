export function switchTest(v: number) {

    switch (v) {

        case 0:
            return "zero";

        case 1:
            return "one";

        case 2:
            return "two";

        case 3:
        case 4:
            return "three-four";

        default:
            return "other";
    }

}