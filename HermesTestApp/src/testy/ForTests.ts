export function forTest() {
    for (let i = 0; i < 10; i++) {

        if (i === 3)
            continue;

        if (i === 8)
            break;

        console.log(i);
    }
}