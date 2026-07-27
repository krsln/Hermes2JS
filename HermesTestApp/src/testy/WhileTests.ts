export function whileTest() {
    let i = 0;

    while (i < 5) {
        console.log("while", i);

        if (i === 2) {
            i++;
            continue;
        }

        i++;
    }
}