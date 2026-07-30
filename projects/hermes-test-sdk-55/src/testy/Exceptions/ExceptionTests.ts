export function tryCatchTest() {
    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/try-block");
        throw new Error("test");

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/catch-block");
        console.log(e);

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/finally-block");
        console.log("finally");

    }

    console.log("__BC:Exceptions/ExceptionTests/tryCatchTest/end");
}
