export function forEachTest() {

    const list = [10, 20, 30, 40];

    list.forEach((value, index) => {

        if (index === 2) {
            console.log("middle");
        }

        console.log(index, value);

    });

}