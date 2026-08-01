// ControlFlow
import { whileTest } from "./ControlFlow/WhileTests";
import { doWhileTest } from "./ControlFlow/DoWhileTests";
import { forTest } from "./ControlFlow/ForTests";
import { forEachTest } from "./ControlFlow/ForEachTests";
import { switchTest } from "./ControlFlow/SwitchTests";
import { nestedLoopTest } from "./ControlFlow/NestedTests";
import { complexTest } from "./ControlFlow/ComplexTests";
import { ifTest, ifElseChainTest } from "./ControlFlow/IfTests";
import {
    labeledBreakTest,
    labeledContinueTest,
    labeledBlockBreakTest,
    tripleNestedLabeledTest,
} from "./ControlFlow/LabeledTests";
import {
    ternaryTest,
    shortCircuitAssignTest,
    logicalShortCircuitTest,
} from "./ControlFlow/TernaryTests";

// Exceptions
import {
    tryCatchTest,
    tryCatchNoFinallyTest,
    tryFinallyNoCatchTest,
    tryFinallyNormalCompletionTest,
    tryCatchRethrowDifferentTest,
    tryLoopMultiReturnTest,
    nestedTryCatchTest,
    nestedTryCatchFinallyTest,
    tryCatchFinallyEarlyReturnTest,
    tryFinallyLoopBreakTest,
    tryCatchInsideLoopTest,
    tryCatchFinallyBranchInFinallyTest,
    tryCatchFinallyImplicitThrowTest,
    loopBreakCrossesTryBoundaryTest,
    switchInsideTryTest,
 } from "./Exceptions/ExceptionTests";

// Iterators
import { forOfTest, forInTest } from "./Iterators/IteratorTests";

// Objects
import { objectLiteralTest } from "./Objects/ObjectLiteralTests";
import {
    propertyAccessTest,
    computedPropertyTest,
    optionalChainingTest,
} from "./Objects/PropertyTests";
import { callDestructuringTests } from "./Objects/DestructuringTests";

// Arrays
import { arrayTest } from "./Arrays/ArrayTests";
import {
    spreadArrayTest,
    spreadObjectTest,
    spreadFunctionArgsTest,
} from "./Arrays/SpreadTests";

// Collections
import { callMapSetTests } from "./Collections/MapSetTests";

// Strings
import {
    basicTemplateTest,
    nestedTemplateTest,
    taggedTemplateTest,
} from "./Strings/TemplateLiteralTests";
import { callRegExpTests } from "./Strings/RegExpTests";

// Functions
import { arrowFunctionTest } from "./Functions/ArrowTests";
import { closureTest, closureLoopTest } from "./Functions/ClosureTests";
import { callDefaultParameterTests } from "./Functions/DefaultParameterTests";
import { callRestParameterTests } from "./Functions/RestParameterTests";
import { callGeneratorTests } from "./Functions/GeneratorTests";
import { callAsyncTests } from "./Functions/AsyncTests";

// Classes
import { classTest } from "./Classes/ClassTests";
import { privateStaticTest } from "./Classes/PrivateStaticTests";

export async function runAllTests() {
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

    labeledBreakTest();
    labeledContinueTest();
    labeledBlockBreakTest();
    tripleNestedLabeledTest();

    ternaryTest(-3);
    shortCircuitAssignTest();
    logicalShortCircuitTest(true, false);

    // Exceptions
    tryCatchTest();
    tryCatchNoFinallyTest();
    tryFinallyNoCatchTest();
    tryFinallyNormalCompletionTest();
    tryCatchRethrowDifferentTest();
    tryLoopMultiReturnTest([1, 0, -1, 2]);
    nestedTryCatchTest();
    nestedTryCatchFinallyTest();
    tryCatchFinallyEarlyReturnTest();
    tryFinallyLoopBreakTest([1, 2, 0, 3]);
    tryCatchInsideLoopTest([1, -2, 3]);
    tryCatchFinallyBranchInFinallyTest(true);
    tryCatchFinallyImplicitThrowTest(5);
    loopBreakCrossesTryBoundaryTest([1, 0, 2, -1, 3]);
    switchInsideTryTest(1);

    // Iterators
    forOfTest();
    forInTest();

    // Objects
    objectLiteralTest();
    propertyAccessTest();
    computedPropertyTest();
    optionalChainingTest();
    callDestructuringTests();

    // Arrays
    arrayTest();
    spreadArrayTest();
    spreadObjectTest();
    spreadFunctionArgsTest();

    // Collections
    callMapSetTests();

    // Strings
    basicTemplateTest("Ada", 30);
    nestedTemplateTest(4, 9);
    taggedTemplateTest(6);
    callRegExpTests();

    // Functions
    arrowFunctionTest();
    closureTest();
    closureLoopTest();
    callDefaultParameterTests();
    callRestParameterTests();
    callGeneratorTests();
    await callAsyncTests();

    // Classes
    classTest();
    privateStaticTest();

    console.log("__BC:index/runAllTests/end");
}
