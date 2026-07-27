import { whileTest } from "./WhileTests";
import { doWhileTest } from "./DoWhileTests";
import { forTest } from "./ForTests";
import { forEachTest } from "./ForEachTests";
import { switchTest } from "./SwitchTests";
import { forOfTest, forInTest } from "./IteratorTests";
import { tryCatchTest } from "./ExceptionTests";
import { nestedLoopTest } from "./NestedTests";
import { complexTest } from "./ComplexTests";

export function runAllTests() {
    whileTest();
    doWhileTest();
    forTest();
    forEachTest();

    console.log(switchTest(4));

    forOfTest();
    forInTest();

    tryCatchTest();

    nestedLoopTest();

    complexTest();
}