// ============================================================
// Exception / try-catch-finally structuring test scenarios.
//
// Each function targets one distinct shape the TryStructurer
// (and CFGBuilder's exception-handler resolution) needs to
// handle correctly. Naming follows the existing
// __BC:Exceptions/ExceptionTests/<fn>/<label> convention so
// output can be matched against markers in the disassembly.
// ============================================================

// ------------------------------------------------------------
// 1. try / catch / finally  (baseline - already covered)
// ------------------------------------------------------------
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

// ------------------------------------------------------------
// 2. try / catch only - NO finally.
//    Single exception handler, handler_block IS the real catch
//    (no wrapping "finally" handler to detect/ignore).
// ------------------------------------------------------------
export function tryCatchNoFinallyTest() {
    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/try-block");
        throw new Error("no finally here");

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/catch-block");
        console.log(e);
    }

    console.log("__BC:Exceptions/ExceptionTests/tryCatchNoFinallyTest/end");
}

// ------------------------------------------------------------
// 3. try / finally only - NO catch.
//    Single exception handler whose handler_block both runs the
//    cleanup code AND unconditionally rethrows - this is the
//    "handler plays double duty" case TryStructurer does NOT yet
//    disambiguate from a real catch-that-rethrows. Included
//    specifically to exercise/expose that gap.
// ------------------------------------------------------------
export function tryFinallyNoCatchTest() {
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/try-block");
        throw new Error("no catch here");

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/finally-block");
    }

    // unreachable in this particular path (try always throws),
    // but keeps the function shape realistic
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNoCatchTest/end");
}

// ------------------------------------------------------------
// 4. try that completes normally (no throw) + finally.
//    Exercises the "normal completion" exit path through
//    finally, as opposed to the exception path - this is the
//    path real try/finally lowering duplicates finally-code
//    into that our current single-throw tests never hit.
// ------------------------------------------------------------
export function tryFinallyNormalCompletionTest() {
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/try-block");
        // no throw - falls through normally

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/finally-block");
    }

    console.log("__BC:Exceptions/ExceptionTests/tryFinallyNormalCompletionTest/end");
}

// ------------------------------------------------------------
// 5. catch that rethrows a DIFFERENT error (not the caught one).
//    Guards the "only strip rethrow if it's a bare identifier
//    matching the caught exception" safety check in
//    _attach_finally - this one must NOT have its throw
//    stripped.
// ------------------------------------------------------------
export function tryCatchRethrowDifferentTest() {
    console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/try-block");
        throw new Error("original");

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/catch-block");
        throw new Error("wrapped: " + e);

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchRethrowDifferentTest/finally-block");
    }
}

// ------------------------------------------------------------
// 6. try body with a loop and MULTIPLE return points inside the
//    try - mirrors the real-world isRenderConsistentWithExternalStores
//    shape: while(true) with nested if/else, several `return`s at
//    different points, single catch (no finally), no explicit throw
//    (an exception can only come from a call inside the loop).
// ------------------------------------------------------------
export function tryLoopMultiReturnTest(items: number[]) {
    console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/start");

    try {
        let i = 0;

        while (true) {
            if (i >= items.length) {
                return false;
            }

            if (items[i] < 0) {
                return true;
            }

            if (items[i] === 0) {
                i++;
                continue;
            }

            console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/positive", items[i]);
            i++;
        }

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryLoopMultiReturnTest/catch-block");
        return false;
    }
}

// ------------------------------------------------------------
// 7. nested try/catch, both WITHOUT finally - the outer catch
//    must stay a real catch, not get misidentified as a finally
//    wrapper for the inner one (different `target`s, non-
//    overlapping semantics - just physically nested).
// ------------------------------------------------------------
export function nestedTryCatchTest() {
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/start");

    try {
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-try");

        try {
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-try");
            throw new Error("inner");

        } catch (innerError) {
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/inner-catch");
            throw new Error("rethrown from inner: " + innerError);
        }

    } catch (outerError) {
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/outer-catch");
        console.log(outerError);
    }

    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchTest/end");
}

// ------------------------------------------------------------
// 8. nested try/catch/finally - inner try/catch/finally sits
//    entirely inside the outer try. Two independent
//    (handler, finally-wrapper) pairs must each be matched to
//    their own inner region, not cross-wired.
// ------------------------------------------------------------
export function nestedTryCatchFinallyTest() {
    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/start");

    try {
        try {
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-try");
            throw new Error("inner");

        } catch (innerError) {
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-catch");

        } finally {
            console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/inner-finally");
        }

        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/after-inner");

    } catch (outerError) {
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-catch");

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/outer-finally");
    }

    console.log("__BC:Exceptions/ExceptionTests/nestedTryCatchFinallyTest/end");
}

// ------------------------------------------------------------
// 9. try/catch/finally where the CATCH itself returns early
//    (not just falls through to the end) - checks that
//    _strip_duplicate_run finds the inlined finally-copy
//    regardless of what follows it (here: an immediate return,
//    vs. tryCatchTest's log+return).
// ------------------------------------------------------------
export function tryCatchFinallyEarlyReturnTest() {
    try {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/try-block");
        throw new Error("test");

    } catch (e) {
        return false;

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyEarlyReturnTest/finally-block");
    }
}

// ------------------------------------------------------------
// 10. try/finally around a loop with break - finally must run
//     on the break-driven exit path too, not just throw/return.
// ------------------------------------------------------------
export function tryFinallyLoopBreakTest(items: number[]) {
    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/start");

    try {
        for (let i = 0; i < items.length; i++) {
            if (items[i] === 0) {
                break;
            }

            console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/item", items[i]);
        }

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/finally-block");
    }

    console.log("__BC:Exceptions/ExceptionTests/tryFinallyLoopBreakTest/end");
}

// ------------------------------------------------------------
// 11. try/catch inside a loop body (as opposed to a loop inside
//     a try) - the try/catch region itself repeats each
//     iteration; exercises handler resolution when try_blocks
//     sit inside a loop's SequenceRegion rather than the
//     function's top-level one.
// ------------------------------------------------------------
export function tryCatchInsideLoopTest(items: number[]) {
    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/start");

    let failures = 0;

    for (let i = 0; i < items.length; i++) {
        try {
            if (items[i] < 0) {
                throw new Error("negative value");
            }

            console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/ok", items[i]);

        } catch (e) {
            console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/caught", e);
            failures++;
        }
    }

    console.log("__BC:Exceptions/ExceptionTests/tryCatchInsideLoopTest/end");
    return failures;
}

// ------------------------------------------------------------
// 12. try/catch/finally with an if/else INSIDE the finally body
//     itself - finally_ body isn't always a flat block; make
//     sure structuring/printing handles a non-trivial region
//     inside finally.
// ------------------------------------------------------------
export function tryCatchFinallyBranchInFinallyTest(shouldLog: boolean) {
    try {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/try-block");
        throw new Error("test");

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/catch-block");

    } finally {
        if (shouldLog) {
            console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-true");
        } else {
            console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyBranchInFinallyTest/finally-false");
        }
    }
}

// ------------------------------------------------------------
// 13. try/catch/finally where try body itself never throws
//     directly but calls into something that might (a plain
//     function call, no explicit `throw` statement at all in
//     source) - the shape most real-world code actually has,
//     as opposed to every other test here using an explicit
//     `throw new Error(...)`.
// ------------------------------------------------------------
function mayThrow(x: number): number {
    if (x < 0) {
        throw new Error("negative");
    }
    return x * 2;
}

export function tryCatchFinallyImplicitThrowTest(x: number) {
    console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/start");

    try {
        const result = mayThrow(x);
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/result", result);
        return result;

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/catch-block");
        return -1;

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/tryCatchFinallyImplicitThrowTest/finally-block");
    }
}

// ------------------------------------------------------------
// 14. loop OUTSIDE the try, but break/continue INSIDE the try
//     targets it - the jump has to cross the try/finally region
//     boundary, so the finally must still run before the loop
//     actually exits/continues.
// ------------------------------------------------------------
export function loopBreakCrossesTryBoundaryTest(items: number[]) {
    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/start");

    for (let i = 0; i < items.length; i++) {
        try {
            if (items[i] < 0) {
                console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/break");
                break;
            }

            if (items[i] === 0) {
                console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/continue");
                continue;
            }

            console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/item", items[i]);

        } finally {
            console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/finally");
        }
    }

    console.log("__BC:Exceptions/ExceptionTests/loopBreakCrossesTryBoundaryTest/end");
}

// ------------------------------------------------------------
// 15. switch statement INSIDE a try/catch - checks that the
//     SwitchRegion nests correctly inside a TryRegion's try_body
//     rather than confusing the exception-handler's block range.
// ------------------------------------------------------------
export function switchInsideTryTest(v: number) {
    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/start");

    try {
        switch (v) {
            case 0:
                console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-0");
                break;

            case 1:
                throw new Error("case 1 throws");

            default:
                console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/case-default");
        }

    } catch (e) {
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/catch-block");

    } finally {
        console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/finally-block");
    }

    console.log("__BC:Exceptions/ExceptionTests/switchInsideTryTest/end");
}