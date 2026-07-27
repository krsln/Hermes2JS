export function tryCatchTest() {

    try {

        throw new Error("test");

    } catch (e) {

        console.log(e);

    } finally {

        console.log("finally");

    }

}