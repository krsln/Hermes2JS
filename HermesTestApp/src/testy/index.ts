// ControlFlow
import { whileTest } from "./ControlFlow/WhileTests";
import { doWhileTest } from "./ControlFlow/DoWhileTests";
import { forTest } from "./ControlFlow/ForTests";
import { forEachTest } from "./ControlFlow/ForEachTests";
import { switchTest } from "./ControlFlow/SwitchTests";
import { nestedLoopTest } from "./ControlFlow/NestedTests";
import { complexTest } from "./ControlFlow/ComplexTests";
import { ifTest, ifElseChainTest } from "./ControlFlow/IfTests";

// Exceptions
import { tryCatchTest } from "./Exceptions/ExceptionTests";

// Iterators
import { forOfTest, forInTest } from "./Iterators/IteratorTests";

// Objects
import { objectLiteralTest } from "./Objects/ObjectLiteralTests";
import {
    propertyAccessTest,
    computedPropertyTest,
    optionalChainingTest,
} from "./Objects/PropertyTests";

// Arrays
import { arrayTest } from "./Arrays/ArrayTests";
import {
    spreadArrayTest,
    spreadObjectTest,
    spreadFunctionArgsTest,
} from "./Arrays/SpreadTests";

// Functions
import { arrowFunctionTest } from "./Functions/ArrowTests";
import { closureTest, closureLoopTest } from "./Functions/ClosureTests";
import { callDefaultParameterTests } from "./Functions/DefaultParameterTests";

// Classes
import { classTest } from "./Classes/ClassTests";

export function runAllTests() {
    console.log("__BC:index/runAllTests/start");

    // ControlFlow
    whileTest();
    doWhileTest();
    forTest();
    forEachTest();

    console.log(switchTest(4));

    nestedLoopTest();
    complexTest();

    ifTest(7);
    ifElseChainTest(true, false);

    // Exceptions
    tryCatchTest();

    // Iterators
    forOfTest();
    forInTest();

    // Objects
    objectLiteralTest();
    propertyAccessTest();
    computedPropertyTest();
    optionalChainingTest();

    // Arrays
    arrayTest();
    spreadArrayTest();
    spreadObjectTest();
    spreadFunctionArgsTest();

    // Functions
    arrowFunctionTest();
    closureTest();
    closureLoopTest();
    callDefaultParameterTests();

    // Classes
    classTest();

    console.log("__BC:index/runAllTests/end");
}
