function function_467(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 18, UInt8: 2>
    // USED → r18 = param2;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 6>
    // USED → r3 = param6;
    // CODE → <LoadParam>: <Reg8: 19, UInt8: 7>
    // USED → r19 = param7;
    // CODE → <CreateEnvironment>: <Reg8: 1>
    // USED → r1 = createEnvironment();
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 18>
    createEnvironment()[0] = param2
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 19>
    createEnvironment()[1] = param7
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 468>  # Function: [#468 executeDispatch of 77 bytes]: 4 params @ offset 0x00179753
    // USED → r0 = executeDispatch;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 169, Reg8: 0>
    createEnvironment()[169] = executeDispatch
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 469>  # Function: [#469 executeDirectDispatch of 103 bytes]: 2 params @ offset 0x001797a0
    // USED → r0 = executeDirectDispatch;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 170, Reg8: 0>
    createEnvironment()[170] = executeDirectDispatch
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 470>  # Function: [#470 functionThatReturnsTrue of 4 bytes]: 1 params @ offset 0x00179807
    // USED → r0 = functionThatReturnsTrue;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 171, Reg8: 0>
    createEnvironment()[171] = functionThatReturnsTrue
    // CODE → <CreateClosure>: <Reg8: 42, Reg8: 1, function_id: 471>  # Function: [#471 functionThatReturnsFalse of 4 bytes]: 1 params @ offset 0x00174221
    // USED → r42 = functionThatReturnsFalse;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 172, Reg8: 42>
    createEnvironment()[172] = functionThatReturnsFalse
    // CODE → <CreateClosure>: <Reg8: 39, Reg8: 1, function_id: 472>  # Function: [#472 SyntheticEvent of 213 bytes]: 5 params @ offset 0x0017980b
    // USED → r39 = SyntheticEvent;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 173, Reg8: 39>
    createEnvironment()[173] = SyntheticEvent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 473>  # Function: [#473 createOrGetPooledEvent of 108 bytes]: 5 params @ offset 0x001798e0
    // USED → r0 = createOrGetPooledEvent;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 174, Reg8: 0>
    createEnvironment()[174] = createOrGetPooledEvent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 474>  # Function: [#474 releasePooledEvent of 82 bytes]: 2 params @ offset 0x0017994c
    // USED → r0 = releasePooledEvent;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 175, Reg8: 0>
    createEnvironment()[175] = releasePooledEvent
    // CODE → <CreateClosure>: <Reg8: 17, Reg8: 1, function_id: 475>  # Function: [#475 addEventPoolingTo of 40 bytes]: 2 params @ offset 0x0017999e
    // USED → r17 = addEventPoolingTo;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 176, Reg8: 17>
    createEnvironment()[176] = addEventPoolingTo
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 476>  # Function: [#476 isStartish of 13 bytes]: 2 params @ offset 0x001799c6
    // USED → r0 = isStartish;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 177, Reg8: 0>
    createEnvironment()[177] = isStartish
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 477>  # Function: [#477 isMoveish of 13 bytes]: 2 params @ offset 0x001799d3
    // USED → r0 = isMoveish;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 178, Reg8: 0>
    createEnvironment()[178] = isMoveish
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 478>  # Function: [#478 timestampForTouch of 20 bytes]: 2 params @ offset 0x001799e0
    // USED → r0 = timestampForTouch;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 179, Reg8: 0>
    createEnvironment()[179] = timestampForTouch
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 479>  # Function: [#479 getTouchIdentifier of 38 bytes]: 2 params @ offset 0x001799f4
    // USED → r0 = getTouchIdentifier;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 180, Reg8: 0>
    createEnvironment()[180] = getTouchIdentifier
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 480>  # Function: [#480 recordTouchStart of 283 bytes]: 2 params @ offset 0x00179a1a
    // USED → r0 = recordTouchStart;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 181, Reg8: 0>
    createEnvironment()[181] = recordTouchStart
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 481>  # Function: [#481 recordTouchMove of 128 bytes]: 2 params @ offset 0x00179b35
    // USED → r0 = recordTouchMove;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 182, Reg8: 0>
    createEnvironment()[182] = recordTouchMove
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 482>  # Function: [#482 recordTouchEnd of 128 bytes]: 2 params @ offset 0x00179bb5
    // USED → r0 = recordTouchEnd;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 183, Reg8: 0>
    createEnvironment()[183] = recordTouchEnd
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 483>  # Function: [#483 accumulate of 118 bytes]: 3 params @ offset 0x00179c35
    // USED → r0 = accumulate;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 184, Reg8: 0>
    createEnvironment()[184] = accumulate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 484>  # Function: [#484 accumulateInto of 130 bytes]: 3 params @ offset 0x00179cab
    // USED → r0 = accumulateInto;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 185, Reg8: 0>
    createEnvironment()[185] = accumulateInto
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 485>  # Function: [#485 forEachAccumulated of 62 bytes]: 4 params @ offset 0x00179d2d
    // USED → r0 = forEachAccumulated;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 186, Reg8: 0>
    createEnvironment()[186] = forEachAccumulated
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 486>  # Function: [#486 changeResponder of 60 bytes]: 3 params @ offset 0x00179d6b
    // USED → r0 = changeResponder;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 187, Reg8: 0>
    createEnvironment()[187] = changeResponder
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 487>  # Function: [#487 getParent$1 of 36 bytes]: 2 params @ offset 0x00179da7
    // USED → r0 = getParent$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 188, Reg8: 0>
    createEnvironment()[188] = getParent$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 488>  # Function: [#488 traverseTwoPhase$1 of 128 bytes]: 4 params @ offset 0x00179dcb
    // USED → r0 = traverseTwoPhase$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 189, Reg8: 0>
    createEnvironment()[189] = traverseTwoPhase$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 489>  # Function: [#489 getListener$1 of 102 bytes]: 3 params @ offset 0x00179e4b
    // USED → r0 = getListener$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 190, Reg8: 0>
    createEnvironment()[190] = getListener$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 490>  # Function: [#490 accumulateDirectionalDispatches$1 of 85 bytes]: 4 params @ offset 0x00179eb1
    // USED → r0 = accumulateDirectionalDispatches$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 191, Reg8: 0>
    createEnvironment()[191] = accumulateDirectionalDispatches$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 491>  # Function: [#491 accumulateDirectDispatchesSingle$1 of 119 bytes]: 2 params @ offset 0x00179f06
    // USED → r0 = accumulateDirectDispatchesSingle$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 192, Reg8: 0>
    createEnvironment()[192] = accumulateDirectDispatchesSingle$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 492>  # Function: [#492 accumulateTwoPhaseDispatchesSingleSkipTarget of 70 bytes]: 2 params @ offset 0x00179f7d
    // USED → r0 = accumulateTwoPhaseDispatchesSingleSkipTarget;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 193, Reg8: 0>
    createEnvironment()[193] = accumulateTwoPhaseDispatchesSingleSkipTarget
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 493>  # Function: [#493 accumulateTwoPhaseDispatchesSingle$1 of 54 bytes]: 2 params @ offset 0x00179fc3
    // USED → r0 = accumulateTwoPhaseDispatchesSingle$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 194, Reg8: 0>
    createEnvironment()[194] = accumulateTwoPhaseDispatchesSingle$1
    // CODE → <CreateClosure>: <Reg8: 16, Reg8: 1, function_id: 494>  # Function: [#494 recomputePluginOrdering of 495 bytes]: 1 params @ offset 0x00179ff9
    // USED → r16 = recomputePluginOrdering;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 495>  # Function: [#495 publishRegistrationName of 65 bytes]: 3 params @ offset 0x0017a1e8
    // USED → r0 = publishRegistrationName;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 195, Reg8: 0>
    createEnvironment()[195] = publishRegistrationName
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 496>  # Function: [#496 getListener of 102 bytes]: 3 params @ offset 0x00179e4b
    // USED → r0 = getListener;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 196, Reg8: 0>
    createEnvironment()[196] = getListener
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 497>  # Function: [#497 accumulateDirectionalDispatches of 85 bytes]: 4 params @ offset 0x0017a229
    // USED → r0 = accumulateDirectionalDispatches;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 197, Reg8: 0>
    createEnvironment()[197] = accumulateDirectionalDispatches
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 498>  # Function: [#498 traverseTwoPhase of 176 bytes]: 5 params @ offset 0x0017a27e
    // USED → r0 = traverseTwoPhase;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 198, Reg8: 0>
    createEnvironment()[198] = traverseTwoPhase
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 499>  # Function: [#499 accumulateTwoPhaseDispatchesSingle of 56 bytes]: 2 params @ offset 0x0017a32e
    // USED → r0 = accumulateTwoPhaseDispatchesSingle;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 199, Reg8: 0>
    createEnvironment()[199] = accumulateTwoPhaseDispatchesSingle
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 500>  # Function: [#500 accumulateDirectDispatchesSingle of 119 bytes]: 2 params @ offset 0x0017a366
    // USED → r0 = accumulateDirectDispatchesSingle;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 200, Reg8: 0>
    createEnvironment()[200] = accumulateDirectDispatchesSingle
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 501>  # Function: [#501 defaultDiffer of 71 bytes]: 3 params @ offset 0x0017a3dd
    // USED → r0 = defaultDiffer;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 201, Reg8: 0>
    createEnvironment()[201] = defaultDiffer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 502>  # Function: [#502 restoreDeletedValuesInNestedArray of 316 bytes]: 4 params @ offset 0x0017a424
    // USED → r0 = restoreDeletedValuesInNestedArray;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 202, Reg8: 0>
    createEnvironment()[202] = restoreDeletedValuesInNestedArray
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 503>  # Function: [#503 diffNestedProperty of 416 bytes]: 5 params @ offset 0x0017a560
    // USED → r0 = diffNestedProperty;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 203, Reg8: 0>
    createEnvironment()[203] = diffNestedProperty
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 504>  # Function: [#504 addNestedProperty of 108 bytes]: 4 params @ offset 0x0017a700
    // USED → r0 = addNestedProperty;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 204, Reg8: 0>
    createEnvironment()[204] = addNestedProperty
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 505>  # Function: [#505 clearNestedProperty of 108 bytes]: 4 params @ offset 0x0017a76c
    // USED → r0 = clearNestedProperty;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 205, Reg8: 0>
    createEnvironment()[205] = clearNestedProperty
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 506>  # Function: [#506 diffProperties of 881 bytes]: 5 params @ offset 0x0017a7d8
    // USED → r0 = diffProperties;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 206, Reg8: 0>
    createEnvironment()[206] = diffProperties
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 507>  # Function: [#507 batchedUpdatesImpl of 15 bytes]: 3 params @ offset 0x0017ab49
    // USED → r0 = batchedUpdatesImpl;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 207, Reg8: 0>
    createEnvironment()[207] = batchedUpdatesImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 508>  # Function: [#508 batchedUpdates$1 of 64 bytes]: 3 params @ offset 0x0017ab58
    // USED → r0 = batchedUpdates$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 208, Reg8: 0>
    createEnvironment()[208] = batchedUpdates$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 509>  # Function: [#509 executeDispatchesAndReleaseTopLevel of 174 bytes]: 2 params @ offset 0x0017ab98
    // USED → r0 = executeDispatchesAndReleaseTopLevel;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 209, Reg8: 0>
    createEnvironment()[209] = executeDispatchesAndReleaseTopLevel
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 512>  # Function: [#512 onCommitRoot of 92 bytes]: 2 params @ offset 0x0017adc9
    // USED → r0 = onCommitRoot;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 210, Reg8: 0>
    createEnvironment()[210] = onCommitRoot
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 513>  # Function: [#513 clz32Fallback of 53 bytes]: 2 params @ offset 0x0017ae25
    r9 = clz32Fallback
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 514>  # Function: [#514 getHighestPriorityLanes of 427 bytes]: 2 params @ offset 0x0017ae5a
    // USED → r0 = getHighestPriorityLanes;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 211, Reg8: 0>
    createEnvironment()[211] = getHighestPriorityLanes
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 515>  # Function: [#515 getNextLanes of 233 bytes]: 3 params @ offset 0x0017b005
    // USED → r0 = getNextLanes;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 212, Reg8: 0>
    createEnvironment()[212] = getNextLanes
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 516>  # Function: [#516 computeExpirationTime of 400 bytes]: 3 params @ offset 0x0017b0ee
    // USED → r0 = computeExpirationTime;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 213, Reg8: 0>
    createEnvironment()[213] = computeExpirationTime
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 517>  # Function: [#517 getLanesToRetrySynchronouslyOnError of 69 bytes]: 3 params @ offset 0x0017b27e
    // USED → r0 = getLanesToRetrySynchronouslyOnError;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 214, Reg8: 0>
    createEnvironment()[214] = getLanesToRetrySynchronouslyOnError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 518>  # Function: [#518 claimNextTransitionLane of 43 bytes]: 1 params @ offset 0x0017b2c3
    // USED → r0 = claimNextTransitionLane;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 215, Reg8: 0>
    createEnvironment()[215] = claimNextTransitionLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 519>  # Function: [#519 claimNextRetryLane of 46 bytes]: 1 params @ offset 0x0017b2ee
    // USED → r0 = claimNextRetryLane;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 216, Reg8: 0>
    createEnvironment()[216] = claimNextRetryLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 520>  # Function: [#520 createLaneMap of 31 bytes]: 2 params @ offset 0x0017b31c
    // USED → r0 = createLaneMap;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 217, Reg8: 0>
    createEnvironment()[217] = createLaneMap
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 521>  # Function: [#521 markRootUpdated$1 of 50 bytes]: 3 params @ offset 0x0017b33b
    // USED → r0 = markRootUpdated$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 218, Reg8: 0>
    createEnvironment()[218] = markRootUpdated$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 522>  # Function: [#522 markRootFinished of 281 bytes]: 4 params @ offset 0x0017b36d
    // USED → r0 = markRootFinished;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 219, Reg8: 0>
    createEnvironment()[219] = markRootFinished
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 523>  # Function: [#523 markSpawnedDeferredLane of 127 bytes]: 4 params @ offset 0x0017b486
    // USED → r0 = markSpawnedDeferredLane;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 220, Reg8: 0>
    createEnvironment()[220] = markSpawnedDeferredLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 524>  # Function: [#524 markRootEntangled of 105 bytes]: 3 params @ offset 0x0017b505
    // USED → r0 = markRootEntangled;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 221, Reg8: 0>
    createEnvironment()[221] = markRootEntangled
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 525>  # Function: [#525 lanesToEventPriority of 57 bytes]: 2 params @ offset 0x0017b56e
    // USED → r0 = lanesToEventPriority;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 222, Reg8: 0>
    createEnvironment()[222] = lanesToEventPriority
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 526>  # Function: [#526 shim$1 of 21 bytes]: 1 params @ offset 0x0017b5a7
    // USED → r0 = shim$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 223, Reg8: 0>
    createEnvironment()[223] = shim$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 527>  # Function: [#527 createTextInstance of 62 bytes]: 5 params @ offset 0x0017b5bc
    // USED → r0 = createTextInstance;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 224, Reg8: 0>
    createEnvironment()[224] = createTextInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 528>  # Function: [#528 getPublicInstance of 65 bytes]: 2 params @ offset 0x0017b5fa
    // USED → r0 = getPublicInstance;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 225, Reg8: 0>
    createEnvironment()[225] = getPublicInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 529>  # Function: [#529 cloneHiddenInstance of 97 bytes]: 2 params @ offset 0x0017b63b
    // USED → r0 = cloneHiddenInstance;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 226, Reg8: 0>
    createEnvironment()[226] = cloneHiddenInstance
    // CODE → <CreateClosure>: <Reg8: 8, Reg8: 1, function_id: 530>  # Function: [#530 getInstanceFromNode of 51 bytes]: 2 params @ offset 0x0017b69c
    // USED → r8 = getInstanceFromNode;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 531>  # Function: [#531 getIteratorFn of 67 bytes]: 2 params @ offset 0x0017b6cf
    // USED → r0 = getIteratorFn;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 227, Reg8: 0>
    createEnvironment()[227] = getIteratorFn
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 532>  # Function: [#532 getNearestMountedFiber of 123 bytes]: 2 params @ offset 0x0017b712
    // USED → r0 = getNearestMountedFiber;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 228, Reg8: 0>
    createEnvironment()[228] = getNearestMountedFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 533>  # Function: [#533 assertIsMounted of 42 bytes]: 2 params @ offset 0x0017b78d
    // USED → r0 = assertIsMounted;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 229, Reg8: 0>
    createEnvironment()[229] = assertIsMounted
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 534>  # Function: [#534 findCurrentFiberUsingSlowPath of 534 bytes]: 2 params @ offset 0x0017b7b7
    // USED → r0 = findCurrentFiberUsingSlowPath;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 230, Reg8: 0>
    createEnvironment()[230] = findCurrentFiberUsingSlowPath
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 535>  # Function: [#535 findCurrentHostFiber of 34 bytes]: 2 params @ offset 0x0017b9cd
    // USED → r0 = findCurrentHostFiber;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 231, Reg8: 0>
    createEnvironment()[231] = findCurrentHostFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 536>  # Function: [#536 findCurrentHostFiberImpl of 83 bytes]: 2 params @ offset 0x0017b9ef
    // USED → r0 = findCurrentHostFiberImpl;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 232, Reg8: 0>
    createEnvironment()[232] = findCurrentHostFiberImpl
    // CODE → <CreateClosure>: <Reg8: 15, Reg8: 1, function_id: 537>  # Function: [#537 createCursor of 11 bytes]: 2 params @ offset 0x0017ba42
    // USED → r15 = createCursor;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 538>  # Function: [#538 pop of 63 bytes]: 2 params @ offset 0x0017ba4d
    // USED → r0 = pop;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 233, Reg8: 0>
    createEnvironment()[233] = pop
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 539>  # Function: [#539 push of 43 bytes]: 3 params @ offset 0x0017ba8c
    // USED → r0 = push;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 234, Reg8: 0>
    createEnvironment()[234] = push
    // CODE → <CreateClosure>: <Reg8: 38, Reg8: 1, function_id: 540>  # Function: [#540 is of 59 bytes]: 3 params @ offset 0x0017bab7
    r38 = is
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 541>  # Function: [#541 pushHostContainer of 81 bytes]: 3 params @ offset 0x0017baf2
    // USED → r0 = pushHostContainer;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 235, Reg8: 0>
    createEnvironment()[235] = pushHostContainer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 542>  # Function: [#542 popHostContainer of 38 bytes]: 1 params @ offset 0x0017bb43
    // USED → r0 = popHostContainer;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 236, Reg8: 0>
    createEnvironment()[236] = popHostContainer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 543>  # Function: [#543 pushHostContext of 129 bytes]: 2 params @ offset 0x0017bb69
    // USED → r0 = pushHostContext;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 237, Reg8: 0>
    createEnvironment()[237] = pushHostContext
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 544>  # Function: [#544 popHostContext of 47 bytes]: 2 params @ offset 0x0017bbea
    // USED → r0 = popHostContext;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 238, Reg8: 0>
    createEnvironment()[238] = popHostContext
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 545>  # Function: [#545 finishQueueingConcurrentUpdates of 214 bytes]: 1 params @ offset 0x0017bc19
    // USED → r0 = finishQueueingConcurrentUpdates;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 239, Reg8: 0>
    createEnvironment()[239] = finishQueueingConcurrentUpdates
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 546>  # Function: [#546 enqueueUpdate$1 of 160 bytes]: 5 params @ offset 0x0017bcef
    // USED → r0 = enqueueUpdate$1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 240, Reg8: 0>
    createEnvironment()[240] = enqueueUpdate$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 547>  # Function: [#547 enqueueConcurrentRenderForLane of 39 bytes]: 3 params @ offset 0x0017bd8f
    // USED → r0 = enqueueConcurrentRenderForLane;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 241, Reg8: 0>
    createEnvironment()[241] = enqueueConcurrentRenderForLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 548>  # Function: [#548 markUpdateLaneFromFiberToRoot of 285 bytes]: 4 params @ offset 0x0017bdb6
    // USED → r0 = markUpdateLaneFromFiberToRoot;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 242, Reg8: 0>
    createEnvironment()[242] = markUpdateLaneFromFiberToRoot
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 549>  # Function: [#549 getRootForUpdatedFiber of 97 bytes]: 2 params @ offset 0x0017bed3
    // USED → r0 = getRootForUpdatedFiber;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 243, Reg8: 0>
    createEnvironment()[243] = getRootForUpdatedFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 550>  # Function: [#550 ensureRootIsScheduled of 141 bytes]: 2 params @ offset 0x0017bf34
    // USED → r0 = ensureRootIsScheduled;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 244, Reg8: 0>
    createEnvironment()[244] = ensureRootIsScheduled
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 551>  # Function: [#551 flushSyncWorkAcrossRoots_impl of 657 bytes]: 2 params @ offset 0x0017bfc1
    // USED → r0 = flushSyncWorkAcrossRoots_impl;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 245, Reg8: 0>
    createEnvironment()[245] = flushSyncWorkAcrossRoots_impl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 552>  # Function: [#552 throwError of 5 bytes]: 2 params @ offset 0x0016fa3b
    // USED → r0 = throwError;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 246, Reg8: 0>
    createEnvironment()[246] = throwError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 553>  # Function: [#553 processRootScheduleInMicrotask of 167 bytes]: 1 params @ offset 0x0017c252
    // USED → r0 = processRootScheduleInMicrotask;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 247, Reg8: 0>
    createEnvironment()[247] = processRootScheduleInMicrotask
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 554>  # Function: [#554 scheduleTaskForRootDuringMicrotask of 622 bytes]: 3 params @ offset 0x0017c2f9
    // USED → r0 = scheduleTaskForRootDuringMicrotask;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 248, Reg8: 0>
    createEnvironment()[248] = scheduleTaskForRootDuringMicrotask
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 555>  # Function: [#555 scheduleImmediateTask of 90 bytes]: 2 params @ offset 0x0017c567
    // USED → r0 = scheduleImmediateTask;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 249, Reg8: 0>
    createEnvironment()[249] = scheduleImmediateTask
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 557>  # Function: [#557 initializeUpdateQueue of 50 bytes]: 2 params @ offset 0x0017c620
    // USED → r0 = initializeUpdateQueue;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 250, Reg8: 0>
    createEnvironment()[250] = initializeUpdateQueue
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 558>  # Function: [#558 cloneUpdateQueue of 83 bytes]: 3 params @ offset 0x0017c652
    // USED → r0 = cloneUpdateQueue;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 251, Reg8: 0>
    createEnvironment()[251] = cloneUpdateQueue
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 559>  # Function: [#559 createUpdate of 21 bytes]: 2 params @ offset 0x0017c6a5
    // USED → r0 = createUpdate;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 252, Reg8: 0>
    createEnvironment()[252] = createUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 560>  # Function: [#560 enqueueUpdate of 151 bytes]: 4 params @ offset 0x0017c6ba
    // USED → r0 = enqueueUpdate;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 253, Reg8: 0>
    createEnvironment()[253] = enqueueUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 561>  # Function: [#561 entangleTransitions of 86 bytes]: 4 params @ offset 0x0017c751
    // USED → r0 = entangleTransitions;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 254, Reg8: 0>
    createEnvironment()[254] = entangleTransitions
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 562>  # Function: [#562 enqueueCapturedUpdate of 232 bytes]: 3 params @ offset 0x0017c7a7
    // USED → r0 = enqueueCapturedUpdate;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 255, Reg8: 0>
    createEnvironment()[255] = enqueueCapturedUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 563>  # Function: [#563 processUpdateQueue of 911 bytes]: 5 params @ offset 0x0017c88f
    // USED → r0 = processUpdateQueue;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 256, Reg8: 0>
    createEnvironment()[256] = processUpdateQueue
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 564>  # Function: [#564 callCallback of 56 bytes]: 3 params @ offset 0x0017cc1e
    // USED → r0 = callCallback;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 257, Reg8: 0>
    createEnvironment()[257] = callCallback
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 565>  # Function: [#565 commitCallbacks of 74 bytes]: 3 params @ offset 0x0017cc56
    // USED → r0 = commitCallbacks;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 258, Reg8: 0>
    createEnvironment()[258] = commitCallbacks
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 566>  # Function: [#566 shallowEqual of 207 bytes]: 3 params @ offset 0x0017cca0
    // USED → r0 = shallowEqual;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 259, Reg8: 0>
    createEnvironment()[259] = shallowEqual
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 567>  # Function: [#567 describeComponentFrame of 28 bytes]: 3 params @ offset 0x0017cd6f
    // USED → r0 = describeComponentFrame;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 260, Reg8: 0>
    createEnvironment()[260] = describeComponentFrame
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 568>  # Function: [#568 describeFunctionComponentFrame of 48 bytes]: 2 params @ offset 0x0017cd8b
    // USED → r0 = describeFunctionComponentFrame;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 261, Reg8: 0>
    createEnvironment()[261] = describeFunctionComponentFrame
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 569>  # Function: [#569 describeFiber of 201 bytes]: 2 params @ offset 0x0017cdbb
    // USED → r0 = describeFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 262, Reg8: 0>
    createEnvironment()[262] = describeFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 570>  # Function: [#570 getStackByFiberInDevAndProd of 82 bytes]: 2 params @ offset 0x0017cef4
    // USED → r0 = getStackByFiberInDevAndProd;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 263, Reg8: 0>
    createEnvironment()[263] = getStackByFiberInDevAndProd
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 571>  # Function: [#571 isThenableResolved of 30 bytes]: 2 params @ offset 0x0017cf46
    // USED → r0 = isThenableResolved;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 264, Reg8: 0>
    createEnvironment()[264] = isThenableResolved
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 572>  # Function: [#572 noop of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r0 = noop;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 265, Reg8: 0>
    createEnvironment()[265] = noop
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 573>  # Function: [#573 trackUsedThenable of 298 bytes]: 4 params @ offset 0x0017cf64
    // USED → r0 = trackUsedThenable;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 266, Reg8: 0>
    createEnvironment()[266] = trackUsedThenable
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 576>  # Function: [#576 getSuspendedThenable of 44 bytes]: 1 params @ offset 0x0017d0ee
    // USED → r0 = getSuspendedThenable;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 267, Reg8: 0>
    createEnvironment()[267] = getSuspendedThenable
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 577>  # Function: [#577 checkIfUseWrappedInAsyncCatch of 39 bytes]: 2 params @ offset 0x0017d11a
    // USED → r0 = checkIfUseWrappedInAsyncCatch;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 268, Reg8: 0>
    createEnvironment()[268] = checkIfUseWrappedInAsyncCatch
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 578>  # Function: [#578 unwrapThenable of 59 bytes]: 2 params @ offset 0x0017d141
    // USED → r0 = unwrapThenable;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 269, Reg8: 0>
    createEnvironment()[269] = unwrapThenable
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 579>  # Function: [#579 convertStringRefToCallbackRef of 204 bytes]: 5 params @ offset 0x0017d17c
    // USED → r0 = convertStringRefToCallbackRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 270, Reg8: 0>
    createEnvironment()[270] = convertStringRefToCallbackRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 581>  # Function: [#581 coerceRef of 76 bytes]: 5 params @ offset 0x0017d274
    // USED → r0 = coerceRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 271, Reg8: 0>
    createEnvironment()[271] = coerceRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 582>  # Function: [#582 throwOnInvalidObjectType of 116 bytes]: 3 params @ offset 0x0017d2c0
    // USED → r0 = throwOnInvalidObjectType;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 272, Reg8: 0>
    createEnvironment()[272] = throwOnInvalidObjectType
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 583>  # Function: [#583 resolveLazy of 24 bytes]: 2 params @ offset 0x0017d334
    // USED → r0 = resolveLazy;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 273, Reg8: 0>
    createEnvironment()[273] = resolveLazy
    // CODE → <CreateClosure>: <Reg8: 20, Reg8: 1, function_id: 584>  # Function: [#584 createChildReconciler of 160 bytes]: 2 params @ offset 0x0017d34c
    // USED → r20 = createChildReconciler;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 604>  # Function: [#604 pushHiddenContext of 52 bytes]: 3 params @ offset 0x0017e7c3
    // USED → r0 = pushHiddenContext;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 274, Reg8: 0>
    createEnvironment()[274] = pushHiddenContext
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 605>  # Function: [#605 reuseHiddenContextOnStack of 40 bytes]: 1 params @ offset 0x0017e7f7
    // USED → r0 = reuseHiddenContextOnStack;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 275, Reg8: 0>
    createEnvironment()[275] = reuseHiddenContextOnStack
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 606>  # Function: [#606 popHiddenContext of 42 bytes]: 1 params @ offset 0x0017e81f
    // USED → r0 = popHiddenContext;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 276, Reg8: 0>
    createEnvironment()[276] = popHiddenContext
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 607>  # Function: [#607 pushPrimaryTreeSuspenseHandler of 97 bytes]: 2 params @ offset 0x0017e849
    // USED → r0 = pushPrimaryTreeSuspenseHandler;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 277, Reg8: 0>
    createEnvironment()[277] = pushPrimaryTreeSuspenseHandler
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 608>  # Function: [#608 pushOffscreenSuspenseHandler of 108 bytes]: 2 params @ offset 0x0017e8aa
    // USED → r0 = pushOffscreenSuspenseHandler;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 278, Reg8: 0>
    createEnvironment()[278] = pushOffscreenSuspenseHandler
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 609>  # Function: [#609 reuseSuspenseHandlerOnStack of 41 bytes]: 1 params @ offset 0x0017e916
    // USED → r0 = reuseSuspenseHandlerOnStack;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 279, Reg8: 0>
    createEnvironment()[279] = reuseSuspenseHandlerOnStack
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 610>  # Function: [#610 popSuspenseHandler of 50 bytes]: 2 params @ offset 0x0017e93f
    // USED → r0 = popSuspenseHandler;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 280, Reg8: 0>
    createEnvironment()[280] = popSuspenseHandler
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 611>  # Function: [#611 findFirstSuspended of 269 bytes]: 2 params @ offset 0x0017e971
    // USED → r0 = findFirstSuspended;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 281, Reg8: 0>
    createEnvironment()[281] = findFirstSuspended
    // CODE → <CreateClosure>: <Reg8: 36, Reg8: 1, function_id: 612>  # Function: [#612 throwInvalidHookError of 21 bytes]: 1 params @ offset 0x0017ea7e
    // USED → r36 = throwInvalidHookError;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 613>  # Function: [#613 areHookInputsEqual of 102 bytes]: 3 params @ offset 0x0017ea93
    // USED → r0 = areHookInputsEqual;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 282, Reg8: 0>
    createEnvironment()[282] = areHookInputsEqual
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 614>  # Function: [#614 renderWithHooks of 143 bytes]: 7 params @ offset 0x0017eaf9
    // USED → r0 = renderWithHooks;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 283, Reg8: 0>
    createEnvironment()[283] = renderWithHooks
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 615>  # Function: [#615 finishRenderingHooks of 101 bytes]: 1 params @ offset 0x0017eb88
    // USED → r0 = finishRenderingHooks;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 284, Reg8: 0>
    createEnvironment()[284] = finishRenderingHooks
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 616>  # Function: [#616 renderWithHooksAgain of 127 bytes]: 5 params @ offset 0x0017ebed
    // USED → r0 = renderWithHooksAgain;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 285, Reg8: 0>
    createEnvironment()[285] = renderWithHooksAgain
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 617>  # Function: [#617 bailoutHooks of 63 bytes]: 4 params @ offset 0x0017ec6c
    // USED → r0 = bailoutHooks;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 286, Reg8: 0>
    createEnvironment()[286] = bailoutHooks
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 618>  # Function: [#618 resetHooksOnUnwind of 96 bytes]: 2 params @ offset 0x0017ecab
    // USED → r0 = resetHooksOnUnwind;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 287, Reg8: 0>
    createEnvironment()[287] = resetHooksOnUnwind
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 619>  # Function: [#619 mountWorkInProgressHook of 59 bytes]: 1 params @ offset 0x0017ed0b
    // USED → r0 = mountWorkInProgressHook;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 288, Reg8: 0>
    createEnvironment()[288] = mountWorkInProgressHook
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 620>  # Function: [#620 updateWorkInProgressHook of 259 bytes]: 1 params @ offset 0x0017ed46
    // USED → r0 = updateWorkInProgressHook;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 289, Reg8: 0>
    createEnvironment()[289] = updateWorkInProgressHook
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 621>  # Function: [#621 useThenable of 131 bytes]: 2 params @ offset 0x0017ee49
    // USED → r0 = useThenable;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 290, Reg8: 0>
    createEnvironment()[290] = useThenable
    // CODE → <CreateClosure>: <Reg8: 33, Reg8: 1, function_id: 622>  # Function: [#622 use of 120 bytes]: 2 params @ offset 0x0017eecc
    // USED → r33 = use;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 623>  # Function: [#623 basicStateReducer of 29 bytes]: 3 params @ offset 0x0017ef44
    // USED → r0 = basicStateReducer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 291, Reg8: 0>
    createEnvironment()[291] = basicStateReducer
    // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 624>  # Function: [#624 updateReducer of 610 bytes]: 2 params @ offset 0x0017ef61
    // USED → r34 = updateReducer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 292, Reg8: 34>
    createEnvironment()[292] = updateReducer
    // CODE → <CreateClosure>: <Reg8: 25, Reg8: 1, function_id: 625>  # Function: [#625 rerenderReducer of 188 bytes]: 2 params @ offset 0x0017f1c3
    // USED → r25 = rerenderReducer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 293, Reg8: 25>
    createEnvironment()[293] = rerenderReducer
    // CODE → <CreateClosure>: <Reg8: 22, Reg8: 1, function_id: 626>  # Function: [#626 updateSyncExternalStore of 310 bytes]: 3 params @ offset 0x0017f27f
    // USED → r22 = updateSyncExternalStore;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 627>  # Function: [#627 pushStoreConsistencyCheck of 135 bytes]: 4 params @ offset 0x0017f3b5
    // USED → r0 = pushStoreConsistencyCheck;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 294, Reg8: 0>
    createEnvironment()[294] = pushStoreConsistencyCheck
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 628>  # Function: [#628 updateStoreInstance of 54 bytes]: 5 params @ offset 0x0017f43c
    // USED → r0 = updateStoreInstance;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 295, Reg8: 0>
    createEnvironment()[295] = updateStoreInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 629>  # Function: [#629 subscribeToStore of 33 bytes]: 4 params @ offset 0x0017f472
    // USED → r0 = subscribeToStore;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 296, Reg8: 0>
    createEnvironment()[296] = subscribeToStore
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 631>  # Function: [#631 checkIfSnapshotChanged of 49 bytes]: 2 params @ offset 0x0017f4bc
    // USED → r0 = checkIfSnapshotChanged;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 297, Reg8: 0>
    createEnvironment()[297] = checkIfSnapshotChanged
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 632>  # Function: [#632 forceStoreRerender of 41 bytes]: 2 params @ offset 0x0017f4ed
    // USED → r0 = forceStoreRerender;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 298, Reg8: 0>
    createEnvironment()[298] = forceStoreRerender
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 633>  # Function: [#633 mountStateImpl of 97 bytes]: 2 params @ offset 0x0017f516
    // USED → r0 = mountStateImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 299, Reg8: 0>
    createEnvironment()[299] = mountStateImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 634>  # Function: [#634 pushEffect of 137 bytes]: 5 params @ offset 0x0017f577
    // USED → r0 = pushEffect;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 300, Reg8: 0>
    createEnvironment()[300] = pushEffect
    // CODE → <CreateClosure>: <Reg8: 24, Reg8: 1, function_id: 635>  # Function: [#635 updateRef of 21 bytes]: 1 params @ offset 0x0017f600
    // USED → r24 = updateRef;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 636>  # Function: [#636 mountEffectImpl of 96 bytes]: 5 params @ offset 0x0017f615
    // USED → r0 = mountEffectImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 301, Reg8: 0>
    createEnvironment()[301] = mountEffectImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 637>  # Function: [#637 updateEffectImpl of 174 bytes]: 5 params @ offset 0x0017f675
    // USED → r0 = updateEffectImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 302, Reg8: 0>
    createEnvironment()[302] = updateEffectImpl
    // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 638>  # Function: [#638 mountEffect of 33 bytes]: 3 params @ offset 0x0017f723
    // USED → r35 = mountEffect;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 303, Reg8: 35>
    createEnvironment()[303] = mountEffect
    // CODE → <CreateClosure>: <Reg8: 30, Reg8: 1, function_id: 639>  # Function: [#639 updateEffect of 33 bytes]: 3 params @ offset 0x0017f744
    // USED → r30 = updateEffect;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 304, Reg8: 30>
    createEnvironment()[304] = updateEffect
    // CODE → <CreateClosure>: <Reg8: 28, Reg8: 1, function_id: 640>  # Function: [#640 updateInsertionEffect of 30 bytes]: 3 params @ offset 0x0017f765
    // USED → r28 = updateInsertionEffect;
    // CODE → <CreateClosure>: <Reg8: 27, Reg8: 1, function_id: 641>  # Function: [#641 updateLayoutEffect of 33 bytes]: 3 params @ offset 0x0017f783
    // USED → r27 = updateLayoutEffect;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 642>  # Function: [#642 imperativeHandleEffect of 74 bytes]: 3 params @ offset 0x0017f7a4
    // USED → r0 = imperativeHandleEffect;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 305, Reg8: 0>
    createEnvironment()[305] = imperativeHandleEffect
    // CODE → <CreateClosure>: <Reg8: 29, Reg8: 1, function_id: 645>  # Function: [#645 updateImperativeHandle of 90 bytes]: 4 params @ offset 0x0017f813
    // USED → r29 = updateImperativeHandle;
    // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 646>  # Function: [#646 mountDebugValue of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r23 = mountDebugValue;
    // CODE → <CreateClosure>: <Reg8: 32, Reg8: 1, function_id: 647>  # Function: [#647 updateCallback of 89 bytes]: 3 params @ offset 0x0017f86d
    // USED → r32 = updateCallback;
    // CODE → <CreateClosure>: <Reg8: 26, Reg8: 1, function_id: 648>  # Function: [#648 updateMemo of 104 bytes]: 3 params @ offset 0x0017f8c6
    // USED → r26 = updateMemo;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 649>  # Function: [#649 mountDeferredValueImpl of 97 bytes]: 4 params @ offset 0x0017f92e
    // USED → r0 = mountDeferredValueImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 306, Reg8: 0>
    createEnvironment()[306] = mountDeferredValueImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 650>  # Function: [#650 updateDeferredValueImpl of 156 bytes]: 5 params @ offset 0x0017f98f
    // USED → r0 = updateDeferredValueImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 307, Reg8: 0>
    createEnvironment()[307] = updateDeferredValueImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 651>  # Function: [#651 startTransition of 206 bytes]: 6 params @ offset 0x0017fa2b
    // USED → r0 = startTransition;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 308, Reg8: 0>
    createEnvironment()[308] = startTransition
    // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 652>  # Function: [#652 updateId of 21 bytes]: 1 params @ offset 0x0017f600
    // USED → r21 = updateId;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 653>  # Function: [#653 dispatchReducerAction of 135 bytes]: 4 params @ offset 0x0017faf9
    // USED → r0 = dispatchReducerAction;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 309, Reg8: 0>
    createEnvironment()[309] = dispatchReducerAction
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 654>  # Function: [#654 dispatchSetState of 315 bytes]: 4 params @ offset 0x0017fb80
    // USED → r0 = dispatchSetState;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 310, Reg8: 0>
    createEnvironment()[310] = dispatchSetState
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 655>  # Function: [#655 isRenderPhaseUpdate of 44 bytes]: 2 params @ offset 0x0017fcbb
    // USED → r0 = isRenderPhaseUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 311, Reg8: 0>
    createEnvironment()[311] = isRenderPhaseUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 656>  # Function: [#656 enqueueRenderPhaseUpdate of 66 bytes]: 3 params @ offset 0x0017fce7
    // USED → r0 = enqueueRenderPhaseUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 312, Reg8: 0>
    createEnvironment()[312] = enqueueRenderPhaseUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 657>  # Function: [#657 entangleTransitionUpdate of 69 bytes]: 4 params @ offset 0x0017fd29
    // USED → r0 = entangleTransitionUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 313, Reg8: 0>
    createEnvironment()[313] = entangleTransitionUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 658>  # Function: [#658 resolveDefaultProps of 84 bytes]: 3 params @ offset 0x0017fd6e
    // USED → r0 = resolveDefaultProps;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 314, Reg8: 0>
    createEnvironment()[314] = resolveDefaultProps
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 659>  # Function: [#659 applyDerivedStateFromProps of 84 bytes]: 5 params @ offset 0x0017fdc2
    // USED → r0 = applyDerivedStateFromProps;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 315, Reg8: 0>
    createEnvironment()[315] = applyDerivedStateFromProps
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 660>  # Function: [#660 checkShouldComponentUpdate of 125 bytes]: 8 params @ offset 0x0017fe16
    // USED → r0 = checkShouldComponentUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 316, Reg8: 0>
    createEnvironment()[316] = checkShouldComponentUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 661>  # Function: [#661 constructClassInstance of 141 bytes]: 4 params @ offset 0x0017fe93
    // USED → r0 = constructClassInstance;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 317, Reg8: 0>
    createEnvironment()[317] = constructClassInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 662>  # Function: [#662 callComponentWillReceiveProps of 108 bytes]: 5 params @ offset 0x0017ff20
    // USED → r0 = callComponentWillReceiveProps;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 318, Reg8: 0>
    createEnvironment()[318] = callComponentWillReceiveProps
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 663>  # Function: [#663 mountClassInstance of 380 bytes]: 5 params @ offset 0x0017ff8c
    // USED → r0 = mountClassInstance;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 319, Reg8: 0>
    createEnvironment()[319] = mountClassInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 664>  # Function: [#664 createCapturedValueAtFiber of 125 bytes]: 3 params @ offset 0x00180108
    // USED → r0 = createCapturedValueAtFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 320, Reg8: 0>
    createEnvironment()[320] = createCapturedValueAtFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 665>  # Function: [#665 createCapturedValueFromError of 74 bytes]: 4 params @ offset 0x00180185
    // USED → r0 = createCapturedValueFromError;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 321, Reg8: 0>
    createEnvironment()[321] = createCapturedValueFromError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 666>  # Function: [#666 logCapturedError of 194 bytes]: 3 params @ offset 0x001801cf
    // USED → r0 = logCapturedError;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 322, Reg8: 0>
    createEnvironment()[322] = logCapturedError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 668>  # Function: [#668 createRootErrorUpdate of 79 bytes]: 4 params @ offset 0x0018029a
    // USED → r0 = createRootErrorUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 323, Reg8: 0>
    createEnvironment()[323] = createRootErrorUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 670>  # Function: [#670 createClassErrorUpdate of 142 bytes]: 4 params @ offset 0x0018031e
    // USED → r0 = createClassErrorUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 324, Reg8: 0>
    createEnvironment()[324] = createClassErrorUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 674>  # Function: [#674 throwException of 1387 bytes]: 6 params @ offset 0x00180480
    // USED → r0 = throwException;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 325, Reg8: 0>
    createEnvironment()[325] = throwException
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 675>  # Function: [#675 reconcileChildren of 81 bytes]: 5 params @ offset 0x001809eb
    // USED → r0 = reconcileChildren;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 326, Reg8: 0>
    createEnvironment()[326] = reconcileChildren
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 676>  # Function: [#676 updateForwardRef of 149 bytes]: 6 params @ offset 0x00180a3c
    // USED → r0 = updateForwardRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 327, Reg8: 0>
    createEnvironment()[327] = updateForwardRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 677>  # Function: [#677 updateMemoComponent of 333 bytes]: 6 params @ offset 0x00180ad1
    // USED → r0 = updateMemoComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 328, Reg8: 0>
    createEnvironment()[328] = updateMemoComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 678>  # Function: [#678 updateSimpleMemoComponent of 183 bytes]: 6 params @ offset 0x00180c1e
    // USED → r0 = updateSimpleMemoComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 329, Reg8: 0>
    createEnvironment()[329] = updateSimpleMemoComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 679>  # Function: [#679 updateOffscreenComponent of 463 bytes]: 4 params @ offset 0x00180cd5
    // USED → r0 = updateOffscreenComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 330, Reg8: 0>
    createEnvironment()[330] = updateOffscreenComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 680>  # Function: [#680 deferHiddenOffscreenComponent of 52 bytes]: 4 params @ offset 0x00180ea4
    // USED → r0 = deferHiddenOffscreenComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 331, Reg8: 0>
    createEnvironment()[331] = deferHiddenOffscreenComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 681>  # Function: [#681 markRef of 137 bytes]: 3 params @ offset 0x00180ed8
    // USED → r0 = markRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 332, Reg8: 0>
    createEnvironment()[332] = markRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 682>  # Function: [#682 updateFunctionComponent of 140 bytes]: 6 params @ offset 0x00180f61
    // USED → r0 = updateFunctionComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 333, Reg8: 0>
    createEnvironment()[333] = updateFunctionComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 683>  # Function: [#683 replayFunctionComponent of 144 bytes]: 7 params @ offset 0x00180fed
    // USED → r0 = replayFunctionComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 334, Reg8: 0>
    createEnvironment()[334] = replayFunctionComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 684>  # Function: [#684 updateClassComponent of 1514 bytes]: 6 params @ offset 0x0018107d
    // USED → r0 = updateClassComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 335, Reg8: 0>
    createEnvironment()[335] = updateClassComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 685>  # Function: [#685 finishClassComponent of 240 bytes]: 7 params @ offset 0x00181667
    // USED → r0 = finishClassComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 336, Reg8: 0>
    createEnvironment()[336] = finishClassComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 686>  # Function: [#686 mountSuspenseOffscreenState of 19 bytes]: 2 params @ offset 0x00181757
    // USED → r0 = mountSuspenseOffscreenState;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 337, Reg8: 0>
    createEnvironment()[337] = mountSuspenseOffscreenState
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 687>  # Function: [#687 getRemainingWorkInPrimaryTree of 49 bytes]: 4 params @ offset 0x0018176a
    // USED → r0 = getRemainingWorkInPrimaryTree;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 338, Reg8: 0>
    createEnvironment()[338] = getRemainingWorkInPrimaryTree
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 688>  # Function: [#688 updateSuspenseComponent of 918 bytes]: 4 params @ offset 0x0018179b
    // USED → r0 = updateSuspenseComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 339, Reg8: 0>
    createEnvironment()[339] = updateSuspenseComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 689>  # Function: [#689 mountSuspensePrimaryChildren of 60 bytes]: 3 params @ offset 0x00181b31
    // USED → r0 = mountSuspensePrimaryChildren;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 340, Reg8: 0>
    createEnvironment()[340] = mountSuspensePrimaryChildren
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 690>  # Function: [#690 retrySuspenseComponentWithoutHydrating of 130 bytes]: 5 params @ offset 0x00181b6d
    // USED → r0 = retrySuspenseComponentWithoutHydrating;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 341, Reg8: 0>
    createEnvironment()[341] = retrySuspenseComponentWithoutHydrating
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 691>  # Function: [#691 updateDehydratedSuspenseComponent of 978 bytes]: 9 params @ offset 0x00181bef
    // USED → r0 = updateDehydratedSuspenseComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 342, Reg8: 0>
    createEnvironment()[342] = updateDehydratedSuspenseComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 692>  # Function: [#692 scheduleSuspenseWorkOnFiber of 74 bytes]: 4 params @ offset 0x00181fc1
    // USED → r0 = scheduleSuspenseWorkOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 343, Reg8: 0>
    createEnvironment()[343] = scheduleSuspenseWorkOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 693>  # Function: [#693 initSuspenseListRenderState of 107 bytes]: 6 params @ offset 0x0018200b
    // USED → r0 = initSuspenseListRenderState;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 344, Reg8: 0>
    createEnvironment()[344] = initSuspenseListRenderState
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 694>  # Function: [#694 updateSuspenseListComponent of 689 bytes]: 4 params @ offset 0x00182076
    // USED → r0 = updateSuspenseListComponent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 345, Reg8: 0>
    createEnvironment()[345] = updateSuspenseListComponent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 695>  # Function: [#695 resetSuspendedCurrentOnMountInLegacyMode of 72 bytes]: 3 params @ offset 0x00182327
    // USED → r0 = resetSuspendedCurrentOnMountInLegacyMode;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 346, Reg8: 0>
    createEnvironment()[346] = resetSuspendedCurrentOnMountInLegacyMode
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 696>  # Function: [#696 bailoutOnAlreadyFinishedWork of 240 bytes]: 4 params @ offset 0x0018236f
    // USED → r0 = bailoutOnAlreadyFinishedWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 347, Reg8: 0>
    createEnvironment()[347] = bailoutOnAlreadyFinishedWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 697>  # Function: [#697 attemptEarlyBailoutIfNoScheduledUpdate of 555 bytes]: 4 params @ offset 0x0018245f
    // USED → r0 = attemptEarlyBailoutIfNoScheduledUpdate;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 348, Reg8: 0>
    createEnvironment()[348] = attemptEarlyBailoutIfNoScheduledUpdate
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 698>  # Function: [#698 beginWork of 2529 bytes]: 4 params @ offset 0x0018268a
    // USED → r0 = beginWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 349, Reg8: 0>
    createEnvironment()[349] = beginWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 699>  # Function: [#699 resetContextDependencies of 21 bytes]: 1 params @ offset 0x001830dc
    // USED → r0 = resetContextDependencies;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 350, Reg8: 0>
    createEnvironment()[350] = resetContextDependencies
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 700>  # Function: [#700 popProvider of 38 bytes]: 2 params @ offset 0x001830f1
    // USED → r0 = popProvider;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 351, Reg8: 0>
    createEnvironment()[351] = popProvider
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 701>  # Function: [#701 scheduleContextWorkOnParentPath of 132 bytes]: 4 params @ offset 0x00183117
    // USED → r0 = scheduleContextWorkOnParentPath;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 352, Reg8: 0>
    createEnvironment()[352] = scheduleContextWorkOnParentPath
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 702>  # Function: [#702 prepareToReadContext of 80 bytes]: 3 params @ offset 0x0018319b
    // USED → r0 = prepareToReadContext;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 353, Reg8: 0>
    createEnvironment()[353] = prepareToReadContext
    // CODE → <CreateClosure>: <Reg8: 31, Reg8: 1, function_id: 703>  # Function: [#703 readContext of 25 bytes]: 2 params @ offset 0x001831eb
    // USED → r31 = readContext;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 354, Reg8: 31>
    createEnvironment()[354] = readContext
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 704>  # Function: [#704 readContextDuringReconciliation of 50 bytes]: 4 params @ offset 0x00183204
    // USED → r0 = readContextDuringReconciliation;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 355, Reg8: 0>
    createEnvironment()[355] = readContextDuringReconciliation
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 705>  # Function: [#705 readContextForConsumer of 115 bytes]: 3 params @ offset 0x00183236
    // USED → r0 = readContextForConsumer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 356, Reg8: 0>
    createEnvironment()[356] = readContextForConsumer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 706>  # Function: [#706 handleAsyncAction of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r0 = handleAsyncAction;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 357, Reg8: 0>
    createEnvironment()[357] = handleAsyncAction
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 707>  # Function: [#707 doesRequireClone of 114 bytes]: 3 params @ offset 0x001832a9
    // USED → r0 = doesRequireClone;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 358, Reg8: 0>
    createEnvironment()[358] = doesRequireClone
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 708>  # Function: [#708 appendAllChildren of 396 bytes]: 5 params @ offset 0x0018331b
    // USED → r0 = appendAllChildren;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 359, Reg8: 0>
    createEnvironment()[359] = appendAllChildren
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 709>  # Function: [#709 appendAllChildrenToContainer of 420 bytes]: 5 params @ offset 0x001834a7
    // USED → r0 = appendAllChildrenToContainer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 360, Reg8: 0>
    createEnvironment()[360] = appendAllChildrenToContainer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 710>  # Function: [#710 updateHostContainer of 101 bytes]: 3 params @ offset 0x0018364b
    // USED → r0 = updateHostContainer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 361, Reg8: 0>
    createEnvironment()[361] = updateHostContainer
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 711>  # Function: [#711 scheduleRetryEffect of 100 bytes]: 3 params @ offset 0x001836b0
    // USED → r0 = scheduleRetryEffect;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 362, Reg8: 0>
    createEnvironment()[362] = scheduleRetryEffect
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 712>  # Function: [#712 cutOffTailIfNeeded of 198 bytes]: 3 params @ offset 0x00183714
    // USED → r0 = cutOffTailIfNeeded;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 363, Reg8: 0>
    createEnvironment()[363] = cutOffTailIfNeeded
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 713>  # Function: [#713 bubbleProperties of 232 bytes]: 2 params @ offset 0x001837da
    // USED → r0 = bubbleProperties;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 364, Reg8: 0>
    createEnvironment()[364] = bubbleProperties
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 714>  # Function: [#714 completeWork of 2567 bytes]: 4 params @ offset 0x001838c2
    // USED → r0 = completeWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 365, Reg8: 0>
    createEnvironment()[365] = completeWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 715>  # Function: [#715 unwindWork of 431 bytes]: 3 params @ offset 0x0018433c
    // USED → r0 = unwindWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 366, Reg8: 0>
    createEnvironment()[366] = unwindWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 716>  # Function: [#716 unwindInterruptedWork of 165 bytes]: 3 params @ offset 0x00184558
    // USED → r0 = unwindInterruptedWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 367, Reg8: 0>
    createEnvironment()[367] = unwindInterruptedWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 717>  # Function: [#717 safelyAttachRef of 145 bytes]: 3 params @ offset 0x00184664
    // USED → r0 = safelyAttachRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 368, Reg8: 0>
    createEnvironment()[368] = safelyAttachRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 718>  # Function: [#718 safelyDetachRef of 194 bytes]: 3 params @ offset 0x001846f5
    // USED → r0 = safelyDetachRef;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 369, Reg8: 0>
    createEnvironment()[369] = safelyDetachRef
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 719>  # Function: [#719 safelyCallDestroy of 49 bytes]: 4 params @ offset 0x001847b7
    // USED → r0 = safelyCallDestroy;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 370, Reg8: 0>
    createEnvironment()[370] = safelyCallDestroy
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 720>  # Function: [#720 commitBeforeMutationEffects of 404 bytes]: 3 params @ offset 0x001847e8
    // USED → r0 = commitBeforeMutationEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 371, Reg8: 0>
    createEnvironment()[371] = commitBeforeMutationEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 721>  # Function: [#721 commitHookEffectListUnmount of 136 bytes]: 4 params @ offset 0x001849ec
    // USED → r0 = commitHookEffectListUnmount;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 372, Reg8: 0>
    createEnvironment()[372] = commitHookEffectListUnmount
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 722>  # Function: [#722 commitHookEffectListMount of 89 bytes]: 3 params @ offset 0x00184a74
    // USED → r0 = commitHookEffectListMount;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 373, Reg8: 0>
    createEnvironment()[373] = commitHookEffectListMount
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 723>  # Function: [#723 commitHookLayoutEffects of 61 bytes]: 3 params @ offset 0x00184acd
    // USED → r0 = commitHookLayoutEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 374, Reg8: 0>
    createEnvironment()[374] = commitHookLayoutEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 724>  # Function: [#724 commitClassCallbacks of 77 bytes]: 2 params @ offset 0x00184b0a
    // USED → r0 = commitClassCallbacks;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 375, Reg8: 0>
    createEnvironment()[375] = commitClassCallbacks
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 725>  # Function: [#725 commitHostComponentMount of 53 bytes]: 2 params @ offset 0x00184b57
    // USED → r0 = commitHostComponentMount;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 376, Reg8: 0>
    createEnvironment()[376] = commitHostComponentMount
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 726>  # Function: [#726 commitLayoutEffectOnFiber of 1037 bytes]: 4 params @ offset 0x00184b8c
    // USED → r0 = commitLayoutEffectOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 377, Reg8: 0>
    createEnvironment()[377] = commitLayoutEffectOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 727>  # Function: [#727 detachFiberAfterEffects of 105 bytes]: 2 params @ offset 0x0018500c
    // USED → r0 = detachFiberAfterEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 378, Reg8: 0>
    createEnvironment()[378] = detachFiberAfterEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 728>  # Function: [#728 recursivelyTraverseDeletionEffects of 48 bytes]: 4 params @ offset 0x00185075
    // USED → r0 = recursivelyTraverseDeletionEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 379, Reg8: 0>
    createEnvironment()[379] = recursivelyTraverseDeletionEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 729>  # Function: [#729 commitDeletionEffectsOnFiber of 642 bytes]: 4 params @ offset 0x001850a5
    // USED → r0 = commitDeletionEffectsOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 380, Reg8: 0>
    createEnvironment()[380] = commitDeletionEffectsOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 730>  # Function: [#730 getRetryCache of 171 bytes]: 2 params @ offset 0x00185398
    // USED → r0 = getRetryCache;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 381, Reg8: 0>
    createEnvironment()[381] = getRetryCache
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 731>  # Function: [#731 attachSuspenseRetryListeners of 48 bytes]: 3 params @ offset 0x00185443
    // USED → r0 = attachSuspenseRetryListeners;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 382, Reg8: 0>
    createEnvironment()[382] = attachSuspenseRetryListeners
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 733>  # Function: [#733 recursivelyTraverseMutationEffects of 231 bytes]: 3 params @ offset 0x001854c1
    // USED → r0 = recursivelyTraverseMutationEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 383, Reg8: 0>
    createEnvironment()[383] = recursivelyTraverseMutationEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 734>  # Function: [#734 commitMutationEffectsOnFiber of 1258 bytes]: 3 params @ offset 0x001855a8
    // USED → r0 = commitMutationEffectsOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 384, Reg8: 0>
    createEnvironment()[384] = commitMutationEffectsOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 735>  # Function: [#735 commitReconciliationEffects of 77 bytes]: 2 params @ offset 0x00185b04
    // USED → r0 = commitReconciliationEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 385, Reg8: 0>
    createEnvironment()[385] = commitReconciliationEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 736>  # Function: [#736 recursivelyTraverseLayoutEffects of 71 bytes]: 3 params @ offset 0x00185b51
    // USED → r0 = recursivelyTraverseLayoutEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 386, Reg8: 0>
    createEnvironment()[386] = recursivelyTraverseLayoutEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 737>  # Function: [#737 recursivelyTraverseDisappearLayoutEffects of 394 bytes]: 2 params @ offset 0x00185b98
    // USED → r0 = recursivelyTraverseDisappearLayoutEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 387, Reg8: 0>
    createEnvironment()[387] = recursivelyTraverseDisappearLayoutEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 738>  # Function: [#738 recursivelyTraverseReappearLayoutEffects of 597 bytes]: 4 params @ offset 0x00185d22
    // USED → r0 = recursivelyTraverseReappearLayoutEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 388, Reg8: 0>
    createEnvironment()[388] = recursivelyTraverseReappearLayoutEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 739>  # Function: [#739 commitHookPassiveMountEffects of 61 bytes]: 3 params @ offset 0x00184acd
    // USED → r0 = commitHookPassiveMountEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 389, Reg8: 0>
    createEnvironment()[389] = commitHookPassiveMountEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 740>  # Function: [#740 recursivelyTraversePassiveMountEffects of 65 bytes]: 3 params @ offset 0x00185fe8
    // USED → r0 = recursivelyTraversePassiveMountEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 390, Reg8: 0>
    createEnvironment()[390] = recursivelyTraversePassiveMountEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 741>  # Function: [#741 commitPassiveMountOnFiber of 356 bytes]: 3 params @ offset 0x00186029
    // USED → r0 = commitPassiveMountOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 391, Reg8: 0>
    createEnvironment()[391] = commitPassiveMountOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 742>  # Function: [#742 recursivelyTraverseReconnectPassiveEffects of 305 bytes]: 3 params @ offset 0x0018618d
    // USED → r0 = recursivelyTraverseReconnectPassiveEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 392, Reg8: 0>
    createEnvironment()[392] = recursivelyTraverseReconnectPassiveEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 743>  # Function: [#743 recursivelyAccumulateSuspenseyCommit of 59 bytes]: 2 params @ offset 0x001862be
    // USED → r0 = recursivelyAccumulateSuspenseyCommit;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 393, Reg8: 0>
    createEnvironment()[393] = recursivelyAccumulateSuspenseyCommit
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 744>  # Function: [#744 accumulateSuspenseyCommitOnFiber of 252 bytes]: 2 params @ offset 0x001862f9
    // USED → r0 = accumulateSuspenseyCommitOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 394, Reg8: 0>
    createEnvironment()[394] = accumulateSuspenseyCommitOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 745>  # Function: [#745 detachAlternateSiblings of 51 bytes]: 2 params @ offset 0x001863f5
    // USED → r0 = detachAlternateSiblings;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 395, Reg8: 0>
    createEnvironment()[395] = detachAlternateSiblings
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 746>  # Function: [#746 recursivelyTraversePassiveUnmountEffects of 156 bytes]: 2 params @ offset 0x00186428
    // USED → r0 = recursivelyTraversePassiveUnmountEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 396, Reg8: 0>
    createEnvironment()[396] = recursivelyTraversePassiveUnmountEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 747>  # Function: [#747 commitPassiveUnmountOnFiber of 235 bytes]: 2 params @ offset 0x001864c4
    // USED → r0 = commitPassiveUnmountOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 397, Reg8: 0>
    createEnvironment()[397] = commitPassiveUnmountOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 748>  # Function: [#748 recursivelyTraverseDisconnectPassiveEffects of 287 bytes]: 2 params @ offset 0x001865af
    // USED → r0 = recursivelyTraverseDisconnectPassiveEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 398, Reg8: 0>
    createEnvironment()[398] = recursivelyTraverseDisconnectPassiveEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 749>  # Function: [#749 commitPassiveUnmountEffectsInsideOfDeletedTree_begin of 214 bytes]: 3 params @ offset 0x001866ce
    // USED → r0 = commitPassiveUnmountEffectsInsideOfDeletedTree_begin;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 399, Reg8: 0>
    createEnvironment()[399] = commitPassiveUnmountEffectsInsideOfDeletedTree_begin
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 750>  # Function: [#750 requestUpdateLane of 198 bytes]: 2 params @ offset 0x001867a4
    // USED → r0 = requestUpdateLane;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 400, Reg8: 0>
    createEnvironment()[400] = requestUpdateLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 751>  # Function: [#751 requestDeferredLane of 84 bytes]: 1 params @ offset 0x0018686a
    // USED → r0 = requestDeferredLane;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 401, Reg8: 0>
    createEnvironment()[401] = requestDeferredLane
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 752>  # Function: [#752 scheduleUpdateOnFiber of 284 bytes]: 4 params @ offset 0x001868be
    // USED → r0 = scheduleUpdateOnFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 402, Reg8: 0>
    createEnvironment()[402] = scheduleUpdateOnFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 753>  # Function: [#753 performConcurrentWorkOnRoot of 766 bytes]: 3 params @ offset 0x001869da
    // USED → r0 = performConcurrentWorkOnRoot;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 403, Reg8: 0>
    createEnvironment()[403] = performConcurrentWorkOnRoot
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 754>  # Function: [#754 recoverFromConcurrentError of 158 bytes]: 4 params @ offset 0x00186cd8
    // USED → r0 = recoverFromConcurrentError;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 404, Reg8: 0>
    createEnvironment()[404] = recoverFromConcurrentError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 755>  # Function: [#755 queueRecoverableErrors of 50 bytes]: 2 params @ offset 0x00186d76
    // USED → r0 = queueRecoverableErrors;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 405, Reg8: 0>
    createEnvironment()[405] = queueRecoverableErrors
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 756>  # Function: [#756 commitRootWhenReady of 67 bytes]: 8 params @ offset 0x00186da8
    // USED → r0 = commitRootWhenReady;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 406, Reg8: 0>
    createEnvironment()[406] = commitRootWhenReady
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 757>  # Function: [#757 isRenderConsistentWithExternalStores of 300 bytes]: 2 params @ offset 0x00186deb
    // USED → r0 = isRenderConsistentWithExternalStores;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 407, Reg8: 0>
    createEnvironment()[407] = isRenderConsistentWithExternalStores
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 758>  # Function: [#758 markRootSuspended of 147 bytes]: 4 params @ offset 0x00186f17
    // USED → r0 = markRootSuspended;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 408, Reg8: 0>
    createEnvironment()[408] = markRootSuspended
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 759>  # Function: [#759 resetWorkInProgressStack of 110 bytes]: 1 params @ offset 0x00186faa
    // USED → r0 = resetWorkInProgressStack;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 409, Reg8: 0>
    createEnvironment()[409] = resetWorkInProgressStack
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 760>  # Function: [#760 prepareFreshStack of 289 bytes]: 3 params @ offset 0x00187018
    // USED → r0 = prepareFreshStack;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 410, Reg8: 0>
    createEnvironment()[410] = prepareFreshStack
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 761>  # Function: [#761 handleThrow of 331 bytes]: 3 params @ offset 0x00187139
    // USED → r0 = handleThrow;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 411, Reg8: 0>
    createEnvironment()[411] = handleThrow
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 762>  # Function: [#762 pushDispatcher of 38 bytes]: 1 params @ offset 0x00187284
    // USED → r0 = pushDispatcher;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 412, Reg8: 0>
    createEnvironment()[412] = pushDispatcher
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 763>  # Function: [#763 renderDidSuspendDelayIfPossible of 91 bytes]: 1 params @ offset 0x001872aa
    // USED → r0 = renderDidSuspendDelayIfPossible;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 413, Reg8: 0>
    createEnvironment()[413] = renderDidSuspendDelayIfPossible
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 764>  # Function: [#764 renderRootSync of 346 bytes]: 3 params @ offset 0x00187305
    // USED → r0 = renderRootSync;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 414, Reg8: 0>
    createEnvironment()[414] = renderRootSync
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 765>  # Function: [#765 workLoopSync of 39 bytes]: 1 params @ offset 0x0018745f
    // USED → r0 = workLoopSync;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 415, Reg8: 0>
    createEnvironment()[415] = workLoopSync
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 766>  # Function: [#766 renderRootConcurrent of 729 bytes]: 3 params @ offset 0x00187486
    // USED → r0 = renderRootConcurrent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 416, Reg8: 0>
    createEnvironment()[416] = renderRootConcurrent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 768>  # Function: [#768 workLoopConcurrent of 104 bytes]: 1 params @ offset 0x0018779d
    // USED → r0 = workLoopConcurrent;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 417, Reg8: 0>
    createEnvironment()[417] = workLoopConcurrent
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 769>  # Function: [#769 performUnitOfWork of 75 bytes]: 2 params @ offset 0x00187805
    // USED → r0 = performUnitOfWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 418, Reg8: 0>
    createEnvironment()[418] = performUnitOfWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 770>  # Function: [#770 replaySuspendedUnitOfWork of 349 bytes]: 2 params @ offset 0x00187850
    // USED → r0 = replaySuspendedUnitOfWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 419, Reg8: 0>
    createEnvironment()[419] = replaySuspendedUnitOfWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 771>  # Function: [#771 throwAndUnwindWorkLoop of 304 bytes]: 4 params @ offset 0x001879ad
    // USED → r0 = throwAndUnwindWorkLoop;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 420, Reg8: 0>
    createEnvironment()[420] = throwAndUnwindWorkLoop
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 772>  # Function: [#772 completeUnitOfWork of 94 bytes]: 2 params @ offset 0x00187add
    // USED → r0 = completeUnitOfWork;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 421, Reg8: 0>
    createEnvironment()[421] = completeUnitOfWork
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 773>  # Function: [#773 commitRoot of 113 bytes]: 6 params @ offset 0x00187b3b
    // USED → r0 = commitRoot;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 422, Reg8: 0>
    createEnvironment()[422] = commitRoot
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 774>  # Function: [#774 commitRootImpl of 772 bytes]: 7 params @ offset 0x00187bac
    // USED → r0 = commitRootImpl;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 423, Reg8: 0>
    createEnvironment()[423] = commitRootImpl
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 776>  # Function: [#776 flushPassiveEffects of 305 bytes]: 1 params @ offset 0x00187ec2
    // USED → r0 = flushPassiveEffects;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 424, Reg8: 0>
    createEnvironment()[424] = flushPassiveEffects
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 777>  # Function: [#777 captureCommitPhaseErrorOnRoot of 78 bytes]: 4 params @ offset 0x00187ff3
    // USED → r0 = captureCommitPhaseErrorOnRoot;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 425, Reg8: 0>
    createEnvironment()[425] = captureCommitPhaseErrorOnRoot
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 778>  # Function: [#778 captureCommitPhaseError of 252 bytes]: 4 params @ offset 0x00188041
    // USED → r0 = captureCommitPhaseError;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 426, Reg8: 0>
    createEnvironment()[426] = captureCommitPhaseError
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 779>  # Function: [#779 attachPingListener of 234 bytes]: 4 params @ offset 0x0018813d
    // USED → r0 = attachPingListener;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 427, Reg8: 0>
    createEnvironment()[427] = attachPingListener
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 780>  # Function: [#780 pingSuspendedRoot of 237 bytes]: 4 params @ offset 0x00188227
    // USED → r0 = pingSuspendedRoot;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 428, Reg8: 0>
    createEnvironment()[428] = pingSuspendedRoot
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 781>  # Function: [#781 retryTimedOutBoundary of 89 bytes]: 3 params @ offset 0x00188314
    // USED → r0 = retryTimedOutBoundary;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 429, Reg8: 0>
    createEnvironment()[429] = retryTimedOutBoundary
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 782>  # Function: [#782 resolveRetryWakeable of 141 bytes]: 3 params @ offset 0x0018836d
    // USED → r0 = resolveRetryWakeable;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 430, Reg8: 0>
    createEnvironment()[430] = resolveRetryWakeable
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 783>  # Function: [#783 scheduleCallback of 45 bytes]: 3 params @ offset 0x001883fa
    // USED → r0 = scheduleCallback;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 431, Reg8: 0>
    createEnvironment()[431] = scheduleCallback
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 784>  # Function: [#784 FiberNode of 161 bytes]: 5 params @ offset 0x00188427
    // USED → r0 = FiberNode;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 432, Reg8: 0>
    createEnvironment()[432] = FiberNode
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 785>  # Function: [#785 createFiber of 42 bytes]: 5 params @ offset 0x001884c8
    // USED → r0 = createFiber;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 433, Reg8: 0>
    createEnvironment()[433] = createFiber
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 786>  # Function: [#786 shouldConstruct of 28 bytes]: 2 params @ offset 0x001884f2
    // USED → r0 = shouldConstruct;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 434, Reg8: 0>
    createEnvironment()[434] = shouldConstruct
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 787>  # Function: [#787 resolveLazyComponentTag of 91 bytes]: 2 params @ offset 0x0018850e
    // USED → r0 = resolveLazyComponentTag;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 435, Reg8: 0>
    createEnvironment()[435] = resolveLazyComponentTag
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 788>  # Function: [#788 createWorkInProgress of 316 bytes]: 3 params @ offset 0x00188569
    // USED → r0 = createWorkInProgress;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 436, Reg8: 0>
    createEnvironment()[436] = createWorkInProgress
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 789>  # Function: [#789 resetWorkInProgress of 237 bytes]: 3 params @ offset 0x001886a5
    // USED → r0 = resetWorkInProgress;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 437, Reg8: 0>
    createEnvironment()[437] = resetWorkInProgress
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 790>  # Function: [#790 createFiberFromTypeAndProps of 613 bytes]: 7 params @ offset 0x00188792
    // USED → r0 = createFiberFromTypeAndProps;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 438, Reg8: 0>
    createEnvironment()[438] = createFiberFromTypeAndProps
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 791>  # Function: [#791 createFiberFromFragment of 37 bytes]: 5 params @ offset 0x001889f7
    // USED → r0 = createFiberFromFragment;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 439, Reg8: 0>
    createEnvironment()[439] = createFiberFromFragment
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 792>  # Function: [#792 createFiberFromOffscreen of 89 bytes]: 5 params @ offset 0x00188a1c
    // USED → r0 = createFiberFromOffscreen;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 440, Reg8: 0>
    createEnvironment()[440] = createFiberFromOffscreen
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 795>  # Function: [#795 createFiberFromText of 36 bytes]: 4 params @ offset 0x00188b67
    // USED → r0 = createFiberFromText;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 441, Reg8: 0>
    createEnvironment()[441] = createFiberFromText
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 796>  # Function: [#796 createFiberFromPortal of 99 bytes]: 4 params @ offset 0x00188b8b
    // USED → r0 = createFiberFromPortal;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 442, Reg8: 0>
    createEnvironment()[442] = createFiberFromPortal
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 797>  # Function: [#797 FiberRootNode of 250 bytes]: 7 params @ offset 0x00188bee
    // USED → r0 = FiberRootNode;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 443, Reg8: 0>
    createEnvironment()[443] = FiberRootNode
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 798>  # Function: [#798 createPortal$1 of 90 bytes]: 4 params @ offset 0x00188ce8
    // USED → r0 = createPortal$1;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 444, Reg8: 0>
    createEnvironment()[444] = createPortal$1
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 799>  # Function: [#799 findHostInstance of 138 bytes]: 2 params @ offset 0x00188d42
    // USED → r0 = findHostInstance;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 445, Reg8: 0>
    createEnvironment()[445] = findHostInstance
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 800>  # Function: [#800 updateContainer of 144 bytes]: 5 params @ offset 0x00188dcc
    // USED → r0 = updateContainer;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 446, Reg8: 0>
    createEnvironment()[446] = updateContainer
    // CODE → <CreateClosure>: <Reg8: 13, Reg8: 1, function_id: 801>  # Function: [#801 emptyFindFiberByHostInstance of 4 bytes]: 1 params @ offset 0x00188e5c
    // USED → r13 = emptyFindFiberByHostInstance;
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 1, function_id: 802>  # Function: [#802 findNodeHandle of 199 bytes]: 2 params @ offset 0x00188e60
    // USED → r5 = findNodeHandle;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 803>  # Function: [#803 getInspectorDataForInstance of 21 bytes]: 1 params @ offset 0x00188f27
    // USED → r4 = getInspectorDataForInstance;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 804>  # Function: [#804 onRecoverableError of 25 bytes]: 2 params @ offset 0x00188f3c
    // USED → r0 = onRecoverableError;
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 447, Reg8: 0>
    createEnvironment()[447] = onRecoverableError
    // CODE → <LoadConstZero>: <Reg8: 10>
    // USED → r10 = 0;
    // CODE → <GetByVal>: <Reg8: 0, Reg8: 19, Reg8: 10>
    // USED → r0 = param7[0];
    // CODE → <Call2>: <Reg8: 0, Reg8: 18, Reg8: 2, Reg8: 0>
    r0 = param2.call(undefined, param7[0])
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → <GetByVal>: <Reg8: 0, Reg8: 19, Reg8: 0>
    // USED → r0 = param7[1];
    // CODE → <Call2>: <Reg8: 14, Reg8: 18, Reg8: 2, Reg8: 0>
    // USED → r14 = param2.call(undefined, param7[1]);
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 2>  # String: 'Array' (Identifier)
    // USED → r11 = globalThis.Array;
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 2, string_id: 1>  # String: 'isArray' (Identifier)
    // USED → r11 = globalThis.Array.isArray;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 11>
    createEnvironment()[2] = globalThis.Array.isArray
    // CODE → <LoadConstFalse>: <Reg8: 12>
    // USED → r12 = false;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 12>
    createEnvironment()[3] = false
    // CODE → <LoadConstNull>: <Reg8: 11>
    // USED → r11 = null;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 11>
    createEnvironment()[4] = null
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 11>
    createEnvironment()[5] = null
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 11>
    createEnvironment()[6] = null
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 11>
    createEnvironment()[7] = null
    // CODE → <TryGetById>: <Reg8: 37, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r37 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 37, UInt8: 4, string_id: 62>  # String: 'assign' (Identifier)
    // USED → r41 = globalThis.Object.assign;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 8, Reg8: 41>
    createEnvironment()[8] = globalThis.Object.assign
    // CODE → <GetByIdShort>: <Reg8: 40, Reg8: 39, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r40 = SyntheticEvent.prototype;
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 805>  # Function: [#805 preventDefault of 82 bytes]: 1 params @ offset 0x00188f55
    // USED → r43 = preventDefault;
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 16522>  # String: 'preventDefault' (Identifier)
    // USED → r37 = { preventDefault: preventDefault };
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 806>  # Function: [#806 stopPropagation of 74 bytes]: 1 params @ offset 0x00188fa7
    // USED → r43 = stopPropagation;
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12808>  # String: 'stopPropagation' (Identifier)
    // USED → r37 = { preventDefault: preventDefault, stopPropagation: stopPropagation };
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 807>  # Function: [#807 persist of 20 bytes]: 1 params @ offset 0x00188ff1
    // USED → r43 = persist;
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 16540>  # String: 'persist' (Identifier)
    // USED → r37 = { preventDefault: preventDefault, stopPropagation: stopPropagation, persist: persist };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 23978>  # String: 'isPersistent' (Identifier)
    // USED → r37 = { preventDefault: preventDefault, stopPropagation: stopPropagation, persist: persist, isPersistent: functionThatReturnsFalse };
    // CODE → <CreateClosure>: <Reg8: 42, Reg8: 1, function_id: 808>  # Function: [#808 destructor of 98 bytes]: 1 params @ offset 0x00189005
    // USED → r42 = destructor;
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12543>  # String: 'destructor' (Identifier)
    // USED → r37 = { preventDefault: preventDefault, stopPropagation: stopPropagation, persist: persist, isPersistent: functionThatReturnsFalse, destructor: destructor };
    // CODE → <Call3>: <Reg8: 37, Reg8: 41, Reg8: 2, Reg8: 40, Reg8: 37>
    r37 = globalThis.Object.assign.call(undefined, SyntheticEvent.prototype, { preventDefault: preventDefault, stopPropagation: stopPropagation, persist: persist, isPersistent: functionThatReturnsFalse, destructor: destructor })
    // CODE → <NewObjectWithBuffer>: <Reg8: 37, UInt16: 9, UInt16: 9, UInt16: 194, UInt16: 115>  # Object: {'type': null, 'target': null, 'currentTarget': null, 'eventPhase': null, 'bubbles': null, 'cancelable': null, 'timeStamp': null, 'defaultPrevented': null, 'isTrusted': null}
    // USED → r37 = { "type": null, "target": null, "currentTarget": null, "eventPhase": null, "bubbles": null, "cancelable": null, "timeStamp": null, "defaultPrevented": null, "isTrusted": null };
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 809>  # Function: [#809 currentTarget of 4 bytes]: 1 params @ offset 0x00188e5c
    // USED → r40 = currentTarget;
    // CODE → <PutById>: <Reg8: 37, Reg8: 40, UInt8: 1, string_id: 11848>  # String: 'currentTarget' (Identifier)
    { "type": null, "target": null, "currentTarget": null, "eventPhase": null, "bubbles": null, "cancelable": null, "timeStamp": null, "defaultPrevented": null, "isTrusted": null }.currentTarget = currentTarget
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 810>  # Function: [#810 timeStamp of 31 bytes]: 2 params @ offset 0x00189067
    // USED → r40 = timeStamp;
    // CODE → <PutById>: <Reg8: 37, Reg8: 40, UInt8: 2, string_id: 19393>  # String: 'timeStamp' (Identifier)
    { "type": null, "target": null, "currentTarget": null, "eventPhase": null, "bubbles": null, "cancelable": null, "timeStamp": null, "defaultPrevented": null, "isTrusted": null }.timeStamp = timeStamp
    // CODE → <PutById>: <Reg8: 39, Reg8: 37, UInt8: 3, string_id: 18542>  # String: 'Interface' (Identifier)
    SyntheticEvent.Interface = { "type": null, "target": null, "currentTarget": null, "eventPhase": null, "bubbles": null, "cancelable": null, "timeStamp": null, "defaultPrevented": null, "isTrusted": null }
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 811>  # Function: [#811  of 138 bytes]: 2 params @ offset 0x00189086
    // USED → r37 = function_811;
    // CODE → <PutById>: <Reg8: 39, Reg8: 37, UInt8: 4, string_id: 14224>  # String: 'extend' (Identifier)
    SyntheticEvent.extend = function_811
    // CODE → <Call2>: <Reg8: 17, Reg8: 17, Reg8: 2, Reg8: 39>
    r17 = addEventPoolingTo.call(undefined, SyntheticEvent)
    // CODE → <GetById>: <Reg8: 37, Reg8: 39, UInt8: 6, string_id: 14224>  # String: 'extend' (Identifier)
    // USED → r37 = SyntheticEvent.extend;
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 814>  # Function: [#814 touchHistory of 4 bytes]: 1 params @ offset 0x00188e5c
    // USED → r40 = touchHistory;
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 40, string_id: 21539>  # String: 'touchHistory' (Identifier)
    // USED → r17 = { touchHistory: touchHistory };
    // CODE → <Call2>: <Reg8: 17, Reg8: 37, Reg8: 39, Reg8: 17>
    // USED → r17 = SyntheticEvent.extend({ touchHistory: touchHistory });
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 17>
    createEnvironment()[9] = SyntheticEvent.extend({ touchHistory: touchHistory })
    // CODE → <NewArrayWithBuffer>: <Reg8: 42, UInt16: 1, UInt16: 1, UInt16: 40883>  # Array: ['topTouchStart']
    // USED → r42 = ["topTouchStart"];
    // CODE → <NewArrayWithBuffer>: <Reg8: 41, UInt16: 1, UInt16: 1, UInt16: 40892>  # Array: ['topTouchMove']
    // USED → r41 = ["topTouchMove"];
    // CODE → <NewArrayWithBuffer>: <Reg8: 40, UInt16: 2, UInt16: 2, UInt16: 40895>  # Array: ['topTouchCancel', 'topTouchEnd']
    // USED → r40 = ["topTouchCancel", "topTouchEnd"];
    // CODE → <NewArray>: <Reg8: 17, UInt16: 0>
    // USED → r17 = [];
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 10, Reg8: 17>
    createEnvironment()[10] = []
    // CODE → <NewObjectWithBuffer>: <Reg8: 37, UInt16: 4, UInt16: 4, UInt16: 250, UInt16: 141>  # Object: {'touchBank': null, 'numberActiveTouches': 0, 'indexOfSingleActiveTouch': 4294967295, 'mostRecentTimeStamp': 0}
    // USED → r37 = { "touchBank": null, "numberActiveTouches": 0, "indexOfSingleActiveTouch": 4294967295, "mostRecentTimeStamp": 0 };
    // CODE → <PutById>: <Reg8: 37, Reg8: 17, UInt8: 5, string_id: 21537>  # String: 'touchBank' (Identifier)
    { "touchBank": null, "numberActiveTouches": 0, "indexOfSingleActiveTouch": 4294967295, "mostRecentTimeStamp": 0 }.touchBank = []
    // CODE → <LoadConstInt>: <Reg8: 39, Imm32: -1>
    // USED → r39 = -1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 11, Reg8: 37>
    createEnvironment()[11] = { "touchBank": null, "numberActiveTouches": 0, "indexOfSingleActiveTouch": 4294967295, "mostRecentTimeStamp": 0 }
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 815>  # Function: [#815 instrument of 14 bytes]: 2 params @ offset 0x0018912e
    // USED → r43 = instrument;
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 43, string_id: 23867>  # String: 'instrument' (Identifier)
    // USED → r17 = { instrument: instrument };
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 816>  # Function: [#816 recordTouchTrack of 328 bytes]: 3 params @ offset 0x0018913c
    // USED → r43 = recordTouchTrack;
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 43, string_id: 14419>  # String: 'recordTouchTrack' (Identifier)
    // USED → r17 = { instrument: instrument, recordTouchTrack: recordTouchTrack };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21539>  # String: 'touchHistory' (Identifier)
    // USED → r17 = { instrument: instrument, recordTouchTrack: recordTouchTrack, touchHistory: { "touchBank": null, "numberActiveTouches": 0, "indexOfSingleActiveTouch": 4294967295, "mostRecentTimeStamp": 0 } };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 13, Reg8: 17>
    createEnvironment()[13] = { instrument: instrument, recordTouchTrack: recordTouchTrack, touchHistory: { "touchBank": null, "numberActiveTouches": 0, "indexOfSingleActiveTouch": 4294967295, "mostRecentTimeStamp": 0 } }
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 14, Reg8: 11>
    createEnvironment()[14] = null
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 15, Reg8: 10>
    createEnvironment()[15] = 0
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 159>  # Object: {'bubbled': 'onStartShouldSetResponder', 'captured': 'onStartShouldSetResponderCapture'}
    // USED → r43 = { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" } };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 24007>  # String: 'startShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 164>  # Object: {'bubbled': 'onScrollShouldSetResponder', 'captured': 'onScrollShouldSetResponderCapture'}
    // USED → r43 = { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" } };
    // CODE → <NewArrayWithBuffer>: <Reg8: 43, UInt16: 1, UInt16: 1, UInt16: 40881>  # Array: ['topScroll']
    // USED → r43 = ["topScroll"];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 17673>  # String: 'scrollShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 111>  # Object: {'bubbled': 'onSelectionChangeShouldSetResponder', 'captured': 'onSelectionChangeShouldSetResponderCapture'}
    // USED → r43 = { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" } };
    // CODE → <NewArrayWithBuffer>: <Reg8: 43, UInt16: 1, UInt16: 1, UInt16: 40900>  # Array: ['topSelectionChange']
    // USED → r43 = ["topSelectionChange"];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 22946>  # String: 'selectionChangeShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 184>  # Object: {'bubbled': 'onMoveShouldSetResponder', 'captured': 'onMoveShouldSetResponderCapture'}
    // USED → r43 = { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" } };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 20089>  # String: 'moveShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 43, string_id: 22333>  # String: 'onResponderStart' (Identifier)
    // USED → r43 = "onResponderStart";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 43, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderStart" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderStart", dependencies: ["topTouchStart"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21573>  # String: 'responderStart' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 42, string_id: 22238>  # String: 'onResponderMove' (Identifier)
    // USED → r42 = "onResponderMove";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 42, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderMove" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderMove", dependencies: ["topTouchMove"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21199>  # String: 'responderMove' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 41, string_id: 22198>  # String: 'onResponderEnd' (Identifier)
    // USED → r41 = "onResponderEnd";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 41, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderEnd" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 15364>  # String: 'responderEnd' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 41, string_id: 22319>  # String: 'onResponderRelease' (Identifier)
    // USED → r41 = "onResponderRelease";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 41, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderRelease" };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 14449>  # String: 'responderRelease' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 19872>  # String: 'onResponderTerminationRequest' (Identifier)
    // USED → r40 = "onResponderTerminationRequest";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminationRequest" };
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = [];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminationRequest", dependencies: [] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21593>  # String: 'responderTerminationRequest' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22208>  # String: 'onResponderGrant' (Identifier)
    // USED → r40 = "onResponderGrant";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderGrant" };
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = [];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderGrant", dependencies: [] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 18117>  # String: 'responderGrant' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22270>  # String: 'onResponderReject' (Identifier)
    // USED → r40 = "onResponderReject";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderReject" };
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = [];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderReject", dependencies: [] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21302>  # String: 'responderReject' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22427>  # String: 'onResponderTerminate' (Identifier)
    // USED → r40 = "onResponderTerminate";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminate" };
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = [];
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminate", dependencies: [] };
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21588>  # String: 'responderTerminate' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 16, Reg8: 17>
    createEnvironment()[16] = { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }
    // CODE → <NewObject>: <Reg8: 40>
    // USED → r40 = {  };
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 817>  # Function: [#817 _getResponder of 9 bytes]: 1 params @ offset 0x00189284
    // USED → r37 = _getResponder;
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 37, string_id: 15697>  # String: '_getResponder' (Identifier)
    // USED → r40 = { _getResponder: _getResponder };
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 14917>  # String: 'eventTypes' (Identifier)
    // USED → r40 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } } };
    // CODE → <CreateClosure>: <Reg8: 17, Reg8: 1, function_id: 818>  # Function: [#818 extractEvents of 1750 bytes]: 5 params @ offset 0x0018928d
    // USED → r17 = extractEvents;
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 14577>  # String: 'extractEvents' (Identifier)
    // USED → r40 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents };
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 11, string_id: 21101>  # String: 'GlobalResponderHandler' (Identifier)
    // USED → r40 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null };
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 819>  # Function: [#819 injectGlobalResponderHandler of 20 bytes]: 2 params @ offset 0x00189963
    // USED → r37 = injectGlobalResponderHandler;
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21100>  # String: 'injectGlobalResponderHandler' (Identifier)
    // USED → r17 = { injectGlobalResponderHandler: injectGlobalResponderHandler };
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 15132>  # String: 'injection' (Identifier)
    // USED → r40 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 17, Reg8: 40>
    createEnvironment()[17] = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 18, Reg8: 11>
    createEnvironment()[18] = null
    // CODE → <NewObject>: <Reg8: 51>
    // USED → r51 = {  };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 19, Reg8: 51>
    createEnvironment()[19] = {  }
    // CODE → <NewArray>: <Reg8: 17, UInt16: 0>
    // USED → r17 = [];
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 20, Reg8: 17>
    createEnvironment()[20] = []
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 21, Reg8: 17>
    createEnvironment()[21] = {  }
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {  };
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 22, Reg8: 17>
    createEnvironment()[22] = {  }
    // CODE → <LoadConstUInt8>: <Reg8: 17, UInt8: 2>
    // USED → r17 = 2;
    // CODE → <GetByVal>: <Reg8: 37, Reg8: 19, Reg8: 17>
    // USED → r37 = param7[2];
    // CODE → <Call2>: <Reg8: 37, Reg8: 18, Reg8: 2, Reg8: 37>
    // USED → r37 = param2.call(undefined, param7[2]);
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
    // USED → r37 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry;
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 8, string_id: 22641>  # String: 'customBubblingEventTypes' (Identifier)
    // USED → r37 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.customBubblingEventTypes;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 23, Reg8: 37>
    createEnvironment()[23] = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.customBubblingEventTypes
    // CODE → <GetByVal>: <Reg8: 37, Reg8: 19, Reg8: 17>
    // USED → r37 = param7[2];
    // CODE → <Call2>: <Reg8: 37, Reg8: 18, Reg8: 2, Reg8: 37>
    // USED → r37 = param2.call(undefined, param7[2]);
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
    // USED → r37 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry;
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 9, string_id: 21940>  # String: 'customDirectEventTypes' (Identifier)
    // USED → r37 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.customDirectEventTypes;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 24, Reg8: 37>
    createEnvironment()[24] = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.customDirectEventTypes
    // CODE → <TryGetById>: <Reg8: 37, Reg8: 0, UInt8: 1, string_id: 2>  # String: 'Array' (Identifier)
    // USED → r37 = globalThis.Array;
    // CODE → <GetByIdShort>: <Reg8: 37, Reg8: 37, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r37 = globalThis.Array.prototype;
    // CODE → <GetByIdShort>: <Reg8: 42, Reg8: 37, UInt8: 10, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r42 = globalThis.Array.prototype.slice;
    // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 11, string_id: 91>  # String: 'call' (Identifier)
    // USED → r41 = globalThis.Array.prototype.slice.call;
    // CODE → <NewArrayWithBuffer>: <Reg8: 37, UInt16: 2, UInt16: 2, UInt16: 40903>  # Array: ['ResponderEventPlugin', 'ReactNativeBridgeEventPlugin']
    // USED → r37 = ["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"];
    // CODE → <Call2>: <Reg8: 37, Reg8: 41, Reg8: 42, Reg8: 37>
    // USED → r37 = globalThis.Array.prototype.slice.call(["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"]);
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 18, Reg8: 37>
    createEnvironment()[18] = globalThis.Array.prototype.slice.call(["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"])
    // CODE → <Call1>: <Reg8: 37, Reg8: 16, Reg8: 2>
    r37 = recomputePluginOrdering.call(undefined)
    // CODE → <NewObject>: <Reg8: 50>
    // USED → r50 = {  };
    // CODE → <PutNewOwnById>: <Reg8: 50, Reg8: 40, string_id: 14576>  # String: 'ResponderEventPlugin' (Identifier)
    // USED → r50 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } } };
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {  };
    // CODE → <NewObject>: <Reg8: 41>
    // USED → r41 = {  };
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 14917>  # String: 'eventTypes' (Identifier)
    // USED → r37 = { eventTypes: {  } };
    // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 820>  # Function: [#820 extractEvents of 246 bytes]: 5 params @ offset 0x00189977
    // USED → r41 = extractEvents;
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 14577>  # String: 'extractEvents' (Identifier)
    // USED → r37 = { eventTypes: {  }, extractEvents: extractEvents };
    // CODE → <PutNewOwnById>: <Reg8: 50, Reg8: 37, string_id: 14569>  # String: 'ReactNativeBridgeEventPlugin' (Identifier)
    // USED → r50 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } };
    // CODE → <Mov>: <Reg8: 48, Reg8: 50>
    // USED → r48 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } };
    // CODE → <LoadConstTrue>: <Reg8: 37>
    // USED → r37 = true;
    // CODE → <LoadConstFalse>: <Reg8: 43>
    // USED → r43 = false;
    // CODE → <LoadConstUndefined>: <Reg8: 42>
    r42 = undefined
    // CODE → <LoadConstFalse>: <Reg8: 41>
    r41 = false
    // CODE → <GetPNameList>: <Reg8: 49, Reg8: 48, Reg8: 47, Reg8: 46>
    // USED → r49 = HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } });
    if (HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }) === undefined) {
        if (false) {
            // ──────────────── Block 9 ──────────────── 
            // CODE → <Call1>: <Reg8: 16, Reg8: 16, Reg8: 2>
            r16 = recomputePluginOrdering.call(undefined)
        }
        // ──────────────── Block 10 ──────────────── 
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {  };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 25, Reg8: 16>
        createEnvironment()[25] = {  }
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 26, Reg8: 11>
        createEnvironment()[26] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 27, Reg8: 10>
        createEnvironment()[27] = 0
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {  };
        // CODE → <PutNewOwnById>: <Reg8: 16, Reg8: 37, string_id: 24472>  # String: 'unsafelyIgnoreFunctions' (Identifier)
        // USED → r16 = { unsafelyIgnoreFunctions: true };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 28, Reg8: 16>
        createEnvironment()[28] = { unsafelyIgnoreFunctions: true }
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 29, Reg8: 12>
        createEnvironment()[29] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 30, Reg8: 11>
        createEnvironment()[30] = null
        // CODE → <GetById>: <Reg8: 14, Reg8: 14, UInt8: 14, string_id: 21563>  # String: '__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED' (Identifier)
        // USED → r14 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 31, Reg8: 11>
        createEnvironment()[31] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 32, Reg8: 11>
        createEnvironment()[32] = null
        // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r16 = globalThis.Math;
        // CODE → <GetById>: <Reg8: 16, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
        // USED → r16 = globalThis.Math.clz32;
        if (globalThis.Math.clz32) {
            // ──────────────── Block 11 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
            // USED → r16 = globalThis.Math;
            // CODE → <GetById>: <Reg8: 9, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
            // USED → r9 = globalThis.Math.clz32;
        }
        // ──────────────── Block 12 ──────────────── 
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 33, Reg8: 9>
        createEnvironment()[33] = globalThis.Math.clz32
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math;
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 17, string_id: 171>  # String: 'log' (Identifier)
        // USED → r9 = globalThis.Math.log;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 34, Reg8: 9>
        createEnvironment()[34] = globalThis.Math.log
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math;
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 18, string_id: 21154>  # String: 'LN2' (Identifier)
        // USED → r9 = globalThis.Math.LN2;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 35, Reg8: 9>
        createEnvironment()[35] = globalThis.Math.LN2
        // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 128>
        // USED → r9 = 128;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 36, Reg8: 9>
        createEnvironment()[36] = 128
        // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 4194304>
        // USED → r9 = 4194304;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 37, Reg8: 9>
        createEnvironment()[37] = 4194304
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 38, Reg8: 10>
        createEnvironment()[38] = 0
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 19, string_id: 24093>  # String: 'nativeFabricUIManager' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 20, string_id: 15507>  # String: 'createNode' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createNode;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 39, Reg8: 16>
        createEnvironment()[39] = globalThis.nativeFabricUIManager.createNode
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 21, string_id: 22912>  # String: 'cloneNodeWithNewChildren' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 40, Reg8: 16>
        createEnvironment()[40] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 22, string_id: 22913>  # String: 'cloneNodeWithNewChildrenAndProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 41, Reg8: 16>
        createEnvironment()[41] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 23, string_id: 22914>  # String: 'cloneNodeWithNewProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewProps;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 42, Reg8: 16>
        createEnvironment()[42] = globalThis.nativeFabricUIManager.cloneNodeWithNewProps
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 24, string_id: 23048>  # String: 'createChildSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createChildSet;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 43, Reg8: 16>
        createEnvironment()[43] = globalThis.nativeFabricUIManager.createChildSet
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 25, string_id: 22565>  # String: 'appendChild' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChild;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 44, Reg8: 16>
        createEnvironment()[44] = globalThis.nativeFabricUIManager.appendChild
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 22566>  # String: 'appendChildToSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChildToSet;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 45, Reg8: 16>
        createEnvironment()[45] = globalThis.nativeFabricUIManager.appendChildToSet
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 27, string_id: 22962>  # String: 'completeRoot' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.completeRoot;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 46, Reg8: 16>
        createEnvironment()[46] = globalThis.nativeFabricUIManager.completeRoot
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 28, string_id: 20376>  # String: 'registerEventHandler' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.registerEventHandler;
        // CODE → <GetById>: <Reg8: 41, Reg8: 9, UInt8: 29, string_id: 24474>  # String: 'unstable_DiscreteEventPriority' (Identifier)
        // USED → r41 = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 47, Reg8: 41>
        createEnvironment()[47] = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 30, string_id: 24484>  # String: 'unstable_getCurrentEventPriority' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 48, Reg8: 9>
        createEnvironment()[48] = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority
        // CODE → <GetByVal>: <Reg8: 9, Reg8: 19, Reg8: 17>
        // USED → r9 = param7[2];
        // CODE → <Call2>: <Reg8: 9, Reg8: 18, Reg8: 2, Reg8: 9>
        // USED → r9 = param2.call(undefined, param7[2]);
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
        // USED → r9 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry;
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 31, string_id: 137>  # String: 'get' (Identifier)
        // USED → r9 = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.get;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 49, Reg8: 9>
        createEnvironment()[49] = param2.call(undefined, param7[2]).ReactNativeViewConfigRegistry.get
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 50, Reg8: 17>
        createEnvironment()[50] = 2
        if (globalThis.nativeFabricUIManager.registerEventHandler) {
            // ──────────────── Block 13 ──────────────── 
            // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 510>  # Function: [#510 dispatchEvent of 81 bytes]: 4 params @ offset 0x0017ac46
            // USED → r9 = dispatchEvent;
            // CODE → <Call2>: <Reg8: 9, Reg8: 16, Reg8: 2, Reg8: 9>
            r9 = globalThis.nativeFabricUIManager.registerEventHandler.call(undefined, dispatchEvent)
        }
        // ──────────────── Block 14 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 41, Reg8: 0, UInt8: 32, string_id: 214>  # String: 'setTimeout' (Identifier)
        // USED → r41 = globalThis.setTimeout;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 51, Reg8: 41>
        createEnvironment()[51] = globalThis.setTimeout
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 33, string_id: 12162>  # String: 'clearTimeout' (Identifier)
        // USED → r9 = globalThis.clearTimeout;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 52, Reg8: 9>
        createEnvironment()[52] = globalThis.clearTimeout
        // CODE → <GetById>: <Reg8: 16, Reg8: 0, UInt8: 34, string_id: 15863>  # String: 'RN$enableMicrotasksInReact' (Identifier)
        // USED → r16 = globalThis.RN$enableMicrotasksInReact;
        // CODE → <LoadConstString>: <Reg8: 9, string_id: 610>  # String: 'undefined' (String)
        // USED → r9 = "undefined";
        // CODE → <TypeOf>: <Reg8: 16, Reg8: 16>
        // USED → r16 = typeof globalThis.RN$enableMicrotasksInReact;
        // CODE → <StrictNeq>: <Reg8: 16, Reg8: 9, Reg8: 16>
        // USED → r16 = "undefined" !== typeof globalThis.RN$enableMicrotasksInReact && !!globalThis.RN$enableMicrotasksInReact;
        // ──────────────── Block 16 ──────────────── 
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 53, Reg8: 16>
        createEnvironment()[53] = "undefined" !== typeof globalThis.RN$enableMicrotasksInReact && !!globalThis.RN$enableMicrotasksInReact
        // CODE → <GetById>: <Reg8: 42, Reg8: 0, UInt8: 35, string_id: 16391>  # String: 'queueMicrotask' (Identifier)
        // USED → r42 = globalThis.queueMicrotask;
        // CODE → <LoadConstString>: <Reg8: 16, string_id: 12255>  # String: 'function' (Identifier)
        // USED → r16 = "function";
        // CODE → <TypeOf>: <Reg8: 42, Reg8: 42>
        // USED → r42 = typeof globalThis.queueMicrotask;
        if ("function" === typeof globalThis.queueMicrotask) {
            // ──────────────── Block 17 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 41, Reg8: 0, UInt8: 35, string_id: 16391>  # String: 'queueMicrotask' (Identifier)
            // USED → r41 = globalThis.queueMicrotask;
        }
        // ──────────────── Block 18 ──────────────── 
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 54, Reg8: 41>
        createEnvironment()[54] = globalThis.queueMicrotask
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 821>  # Function: [#821 getFiberCurrentPropsFromNode$1 of 17 bytes]: 2 params @ offset 0x00189a6d
        // USED → r41 = getFiberCurrentPropsFromNode$1;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 41>
        createEnvironment()[5] = getFiberCurrentPropsFromNode$1
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 8>
        createEnvironment()[6] = getInstanceFromNode
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 822>  # Function: [#822 getNodeFromInstance$1 of 49 bytes]: 2 params @ offset 0x00189a7e
        // USED → r41 = getNodeFromInstance$1;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 41>
        createEnvironment()[7] = getNodeFromInstance$1
        // CODE → <GetById>: <Reg8: 42, Reg8: 40, UInt8: 36, string_id: 15132>  # String: 'injection' (Identifier)
        // USED → r42 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }.injection;
        // CODE → <GetById>: <Reg8: 41, Reg8: 42, UInt8: 37, string_id: 21100>  # String: 'injectGlobalResponderHandler' (Identifier)
        // USED → r41 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }.injection.injectGlobalResponderHandler;
        // CODE → <NewObject>: <Reg8: 40>
        // USED → r40 = {  };
        // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 823>  # Function: [#823 onChange of 122 bytes]: 4 params @ offset 0x00189aaf
        // USED → r43 = onChange;
        // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 43, string_id: 15401>  # String: 'onChange' (Identifier)
        // USED → r40 = { onChange: onChange };
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }.injection.injectGlobalResponderHandler({ onChange: onChange })
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 3815>  # String: 'react.element' (String)
        // USED → r40 = "react.element";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.element");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 55, Reg8: 40>
        createEnvironment()[55] = globalThis.Symbol.for("react.element")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5553>  # String: 'react.portal' (String)
        // USED → r40 = "react.portal";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.portal");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 56, Reg8: 40>
        createEnvironment()[56] = globalThis.Symbol.for("react.portal")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5930>  # String: 'react.fragment' (String)
        // USED → r40 = "react.fragment";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.fragment");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 57, Reg8: 40>
        createEnvironment()[57] = globalThis.Symbol.for("react.fragment")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6410>  # String: 'react.strict_mode' (String)
        // USED → r40 = "react.strict_mode";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.strict_mode");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 58, Reg8: 40>
        createEnvironment()[58] = globalThis.Symbol.for("react.strict_mode")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5628>  # String: 'react.profiler' (String)
        // USED → r40 = "react.profiler";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.profiler");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 59, Reg8: 40>
        createEnvironment()[59] = globalThis.Symbol.for("react.profiler")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2499>  # String: 'react.provider' (String)
        // USED → r40 = "react.provider";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.provider");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 60, Reg8: 40>
        createEnvironment()[60] = globalThis.Symbol.for("react.provider")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8244>  # String: 'react.consumer' (String)
        // USED → r40 = "react.consumer";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.consumer");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 61, Reg8: 40>
        createEnvironment()[61] = globalThis.Symbol.for("react.consumer")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4944>  # String: 'react.context' (String)
        // USED → r40 = "react.context";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.context");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 62, Reg8: 40>
        createEnvironment()[62] = globalThis.Symbol.for("react.context")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 7930>  # String: 'react.forward_ref' (String)
        // USED → r40 = "react.forward_ref";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.forward_ref");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 63, Reg8: 40>
        createEnvironment()[63] = globalThis.Symbol.for("react.forward_ref")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6421>  # String: 'react.suspense' (String)
        // USED → r40 = "react.suspense";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 64, Reg8: 40>
        createEnvironment()[64] = globalThis.Symbol.for("react.suspense")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6422>  # String: 'react.suspense_list' (String)
        // USED → r40 = "react.suspense_list";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense_list");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 65, Reg8: 40>
        createEnvironment()[65] = globalThis.Symbol.for("react.suspense_list")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 410>  # String: 'react.memo' (String)
        // USED → r40 = "react.memo";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.memo");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 66, Reg8: 40>
        createEnvironment()[66] = globalThis.Symbol.for("react.memo")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10762>  # String: 'react.lazy' (String)
        // USED → r40 = "react.lazy";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.lazy");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 67, Reg8: 40>
        createEnvironment()[67] = globalThis.Symbol.for("react.lazy")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6222>  # String: 'react.scope' (String)
        // USED → r40 = "react.scope";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.scope")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6531>  # String: 'react.debug_trace_mode' (String)
        // USED → r40 = "react.debug_trace_mode";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.debug_trace_mode")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5577>  # String: 'react.offscreen' (String)
        // USED → r40 = "react.offscreen";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.offscreen");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 68, Reg8: 40>
        createEnvironment()[68] = globalThis.Symbol.for("react.offscreen")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4905>  # String: 'react.legacy_hidden' (String)
        // USED → r40 = "react.legacy_hidden";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.legacy_hidden")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2166>  # String: 'react.cache' (String)
        // USED → r40 = "react.cache";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.cache")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8982>  # String: 'react.tracing_marker' (String)
        // USED → r40 = "react.tracing_marker";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.tracing_marker")
        // CODE → <TryGetById>: <Reg8: 40, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r40 = globalThis.Symbol;
        // CODE → <GetById>: <Reg8: 40, Reg8: 40, UInt8: 40, string_id: 13658>  # String: 'iterator' (Identifier)
        // USED → r40 = globalThis.Symbol.iterator;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 69, Reg8: 40>
        createEnvironment()[69] = globalThis.Symbol.iterator
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol;
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for;
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10511>  # String: 'react.client.reference' (String)
        // USED → r40 = "react.client.reference";
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.client.reference")
        // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
        // USED → r40 = [];
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 70, Reg8: 40>
        createEnvironment()[70] = []
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 71, Reg8: 39>
        createEnvironment()[71] = -1
        // CODE → <NewObject>: <Reg8: 39>
        // USED → r39 = {  };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 72, Reg8: 39>
        createEnvironment()[72] = {  }
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r39 = globalThis.Object;
        // CODE → <GetById>: <Reg8: 39, Reg8: 39, UInt8: 41, string_id: 11558>  # String: 'is' (Identifier)
        // USED → r39 = globalThis.Object.is;
        // CODE → <TypeOf>: <Reg8: 39, Reg8: 39>
        // USED → r39 = typeof globalThis.Object.is;
        if ("function" === typeof globalThis.Object.is) {
            // ──────────────── Block 19 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
            // USED → r39 = globalThis.Object;
            // CODE → <GetById>: <Reg8: 38, Reg8: 39, UInt8: 41, string_id: 11558>  # String: 'is' (Identifier)
            // USED → r38 = globalThis.Object.is;
        }
        // ──────────────── Block 20 ──────────────── 
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 73, Reg8: 38>
        createEnvironment()[73] = globalThis.Object.is
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor.call(undefined, null);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 74, Reg8: 38>
        createEnvironment()[74] = createCursor.call(undefined, null)
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor.call(undefined, null);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 75, Reg8: 38>
        createEnvironment()[75] = createCursor.call(undefined, null)
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor.call(undefined, null);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 76, Reg8: 38>
        createEnvironment()[76] = createCursor.call(undefined, null)
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 77, Reg8: 11>
        createEnvironment()[77] = null
        // CODE → <NewArray>: <Reg8: 38, UInt16: 0>
        // USED → r38 = [];
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 78, Reg8: 38>
        createEnvironment()[78] = []
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 79, Reg8: 10>
        createEnvironment()[79] = 0
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 80, Reg8: 10>
        createEnvironment()[80] = 0
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 81, Reg8: 11>
        createEnvironment()[81] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 82, Reg8: 11>
        createEnvironment()[82] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 83, Reg8: 12>
        createEnvironment()[83] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 84, Reg8: 12>
        createEnvironment()[84] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 85, Reg8: 12>
        createEnvironment()[85] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 86, Reg8: 10>
        createEnvironment()[86] = 0
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 87, Reg8: 12>
        createEnvironment()[87] = false
        // CODE → <TryGetById>: <Reg8: 38, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r38 = globalThis.Object;
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r38 = globalThis.Object.prototype;
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
        // USED → r38 = globalThis.Object.prototype.hasOwnProperty;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 88, Reg8: 38>
        createEnvironment()[88] = globalThis.Object.prototype.hasOwnProperty
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error;
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 3625>  # String: "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\n\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`" (String)
        // USED → r38 = "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\\n\\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`";
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error.call(undefined, "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\\n\\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 89, Reg8: 38>
        createEnvironment()[89] = globalThis.Error.call(undefined, "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\\n\\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`")
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error;
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 6775>  # String: "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React." (String)
        // USED → r38 = "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React.";
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error.call(undefined, "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React.");
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 90, Reg8: 38>
        createEnvironment()[90] = globalThis.Error.call(undefined, "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React.")
        // CODE → <NewObject>: <Reg8: 38>
        // USED → r38 = {  };
        // CODE → <CreateClosure>: <Reg8: 39, Reg8: 1, function_id: 824>  # Function: [#824 then of 4 bytes]: 1 params @ offset 0x0016f98c
        // USED → r39 = then;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 38, Reg8: 39, string_id: 231>  # String: 'then' (Identifier)
        // USED → r38 = { then: then };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 91, Reg8: 38>
        createEnvironment()[91] = { then: then }
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 92, Reg8: 11>
        createEnvironment()[92] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 93, Reg8: 11>
        createEnvironment()[93] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 94, Reg8: 10>
        createEnvironment()[94] = 0
        // CODE → <Call2>: <Reg8: 37, Reg8: 20, Reg8: 2, Reg8: 37>
        // USED → r37 = createChildReconciler.call(undefined, true);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 95, Reg8: 37>
        createEnvironment()[95] = createChildReconciler.call(undefined, true)
        // CODE → <Call2>: <Reg8: 20, Reg8: 20, Reg8: 2, Reg8: 12>
        // USED → r20 = createChildReconciler.call(undefined, false);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 96, Reg8: 20>
        createEnvironment()[96] = createChildReconciler.call(undefined, false)
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor.call(undefined, null);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 97, Reg8: 20>
        createEnvironment()[97] = createCursor.call(undefined, null)
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor.call(undefined, 0);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 98, Reg8: 20>
        createEnvironment()[98] = createCursor.call(undefined, 0)
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor.call(undefined, null);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 99, Reg8: 20>
        createEnvironment()[99] = createCursor.call(undefined, null)
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 100, Reg8: 11>
        createEnvironment()[100] = null
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor.call(undefined, 0);
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 101, Reg8: 20>
        createEnvironment()[101] = createCursor.call(undefined, 0)
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 42, string_id: 21353>  # String: 'ReactCurrentDispatcher' (Identifier)
        // USED → r20 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 102, Reg8: 20>
        createEnvironment()[102] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 43, string_id: 17455>  # String: 'ReactCurrentBatchConfig' (Identifier)
        // USED → r20 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 103, Reg8: 20>
        createEnvironment()[103] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 104, Reg8: 10>
        createEnvironment()[104] = 0
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 105, Reg8: 11>
        createEnvironment()[105] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 106, Reg8: 11>
        createEnvironment()[106] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 107, Reg8: 11>
        createEnvironment()[107] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 108, Reg8: 12>
        createEnvironment()[108] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 109, Reg8: 12>
        createEnvironment()[109] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 110, Reg8: 12>
        createEnvironment()[110] = false
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 111, Reg8: 10>
        createEnvironment()[111] = 0
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 112, Reg8: 11>
        createEnvironment()[112] = null
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 113, Reg8: 10>
        createEnvironment()[113] = 0
        // CODE → <CreateClosure>: <Reg8: 20, Reg8: 1, function_id: 825>  # Function: [#825 createFunctionComponentUpdateQueue of 12 bytes]: 1 params @ offset 0x00189b29
        // USED → r20 = createFunctionComponentUpdateQueue;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 114, Reg8: 20>
        createEnvironment()[114] = createFunctionComponentUpdateQueue
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {  };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext, use: use };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError, useDeferredValue: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError, useDeferredValue: throwInvalidHookError, useTransition: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError, useDeferredValue: throwInvalidHookError, useTransition: throwInvalidHookError, useSyncExternalStore: throwInvalidHookError };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError, useDeferredValue: throwInvalidHookError, useTransition: throwInvalidHookError, useSyncExternalStore: throwInvalidHookError, useId: throwInvalidHookError };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 115, Reg8: 20>
        createEnvironment()[115] = { readContext: readContext, use: use, useCallback: throwInvalidHookError, useContext: throwInvalidHookError, useEffect: throwInvalidHookError, useImperativeHandle: throwInvalidHookError, useInsertionEffect: throwInvalidHookError, useLayoutEffect: throwInvalidHookError, useMemo: throwInvalidHookError, useReducer: throwInvalidHookError, useRef: throwInvalidHookError, useState: throwInvalidHookError, useDebugValue: throwInvalidHookError, useDeferredValue: throwInvalidHookError, useTransition: throwInvalidHookError, useSyncExternalStore: throwInvalidHookError, useId: throwInvalidHookError }
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {  };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext, use: use };
        // CODE → <CreateClosure>: <Reg8: 36, Reg8: 1, function_id: 826>  # Function: [#826 useCallback of 49 bytes]: 3 params @ offset 0x00189b35
        // USED → r36 = useCallback;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 827>  # Function: [#827 useImperativeHandle of 90 bytes]: 4 params @ offset 0x00189b66
        // USED → r35 = useImperativeHandle;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 828>  # Function: [#828 useLayoutEffect of 33 bytes]: 3 params @ offset 0x00189bc0
        // USED → r35 = useLayoutEffect;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 829>  # Function: [#829 useInsertionEffect of 30 bytes]: 3 params @ offset 0x00189be1
        // USED → r35 = useInsertionEffect;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 830>  # Function: [#830 useMemo of 64 bytes]: 3 params @ offset 0x00189bff
        // USED → r35 = useMemo;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 831>  # Function: [#831 useReducer of 139 bytes]: 4 params @ offset 0x00189c3f
        // USED → r35 = useReducer;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 832>  # Function: [#832 useRef of 31 bytes]: 2 params @ offset 0x00189cca
        // USED → r35 = useRef;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 833>  # Function: [#833 useState of 72 bytes]: 2 params @ offset 0x00189ce9
        // USED → r35 = useState;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 834>  # Function: [#834 useDeferredValue of 34 bytes]: 3 params @ offset 0x00189d31
        // USED → r35 = useDeferredValue;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 835>  # Function: [#835 useTransition of 79 bytes]: 1 params @ offset 0x00189d53
        // USED → r35 = useTransition;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 836>  # Function: [#836 useSyncExternalStore of 239 bytes]: 3 params @ offset 0x00189da2
        // USED → r35 = useSyncExternalStore;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: useSyncExternalStore };
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 837>  # Function: [#837 useId of 83 bytes]: 1 params @ offset 0x00189e91
        // USED → r35 = useId;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: useSyncExternalStore, useId: useId };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 116, Reg8: 20>
        createEnvironment()[116] = { readContext: readContext, use: use, useCallback: useCallback, useContext: readContext, useEffect: mountEffect, useImperativeHandle: useImperativeHandle, useLayoutEffect: useLayoutEffect, useInsertionEffect: useInsertionEffect, useMemo: useMemo, useReducer: useReducer, useRef: useRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: useSyncExternalStore, useId: useId }
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {  };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext, use: use };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef };
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 838>  # Function: [#838 useState of 22 bytes]: 1 params @ offset 0x00189ee4
        // USED → r34 = useState;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 34, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue };
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 839>  # Function: [#839 useDeferredValue of 42 bytes]: 3 params @ offset 0x00189efa
        // USED → r34 = useDeferredValue;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue };
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 840>  # Function: [#840 useTransition of 78 bytes]: 1 params @ offset 0x00189f24
        // USED → r34 = useTransition;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore, useId: updateId };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 117, Reg8: 20>
        createEnvironment()[117] = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: updateReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore, useId: updateId }
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {  };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext, use: use };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 25, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer };
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef };
        // CODE → <CreateClosure>: <Reg8: 24, Reg8: 1, function_id: 841>  # Function: [#841 useState of 22 bytes]: 1 params @ offset 0x00189f72
        // USED → r24 = useState;
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue };
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 842>  # Function: [#842 useDeferredValue of 75 bytes]: 3 params @ offset 0x00189f88
        // USED → r23 = useDeferredValue;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue };
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 843>  # Function: [#843 useTransition of 78 bytes]: 1 params @ offset 0x00189fd3
        // USED → r23 = useTransition;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore };
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore, useId: updateId };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 118, Reg8: 20>
        createEnvironment()[118] = { readContext: readContext, use: use, useCallback: updateCallback, useContext: readContext, useEffect: updateEffect, useImperativeHandle: updateImperativeHandle, useInsertionEffect: updateInsertionEffect, useLayoutEffect: updateLayoutEffect, useMemo: updateMemo, useReducer: rerenderReducer, useRef: updateRef, useState: useState, useDebugValue: mountDebugValue, useDeferredValue: useDeferredValue, useTransition: useTransition, useSyncExternalStore: updateSyncExternalStore, useId: updateId }
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {  };
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 844>  # Function: [#844 isMounted of 34 bytes]: 2 params @ offset 0x0018a021
        // USED → r21 = isMounted;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 16785>  # String: 'isMounted' (Identifier)
        // USED → r20 = { isMounted: isMounted };
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 845>  # Function: [#845 enqueueSetState of 109 bytes]: 4 params @ offset 0x0018a043
        // USED → r21 = enqueueSetState;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22773>  # String: 'enqueueSetState' (Identifier)
        // USED → r20 = { isMounted: isMounted, enqueueSetState: enqueueSetState };
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 846>  # Function: [#846 enqueueReplaceState of 118 bytes]: 4 params @ offset 0x0018a0b0
        // USED → r21 = enqueueReplaceState;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22685>  # String: 'enqueueReplaceState' (Identifier)
        // USED → r20 = { isMounted: isMounted, enqueueSetState: enqueueSetState, enqueueReplaceState: enqueueReplaceState };
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 847>  # Function: [#847 enqueueForceUpdate of 109 bytes]: 3 params @ offset 0x0018a126
        // USED → r21 = enqueueForceUpdate;
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 17151>  # String: 'enqueueForceUpdate' (Identifier)
        // USED → r20 = { isMounted: isMounted, enqueueSetState: enqueueSetState, enqueueReplaceState: enqueueReplaceState, enqueueForceUpdate: enqueueForceUpdate };
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 119, Reg8: 20>
        createEnvironment()[119] = { isMounted: isMounted, enqueueSetState: enqueueSetState, enqueueReplaceState: enqueueReplaceState, enqueueForceUpdate: enqueueForceUpdate }
        // CODE → <TryGetById>: <Reg8: 20, Reg8: 0, UInt8: 44, string_id: 24>  # String: 'WeakMap' (Identifier)
        // USED → r20 = globalThis.WeakMap;
        // CODE → <GetByIdShort>: <Reg8: 21, Reg8: 20, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r21 = globalThis.WeakMap.prototype;
        // CODE → <CreateThis>: <Reg8: 21, Reg8: 21, Reg8: 20>
        // USED → r21 = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap);
        // CODE → <Mov>: <Reg8: 57, Reg8: 21>
        r57 = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap)
        // CODE → <Construct>: <Reg8: 20, Reg8: 20, UInt8: 1>
        // USED → r20 = new globalThis.WeakMap(param7);
        // CODE → <SelectObject>: <Reg8: 20, Reg8: 21, Reg8: 20>
        // USED → r20 = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap)[new globalThis.WeakMap(param7)];
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 120, Reg8: 20>
        createEnvironment()[120] = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap)[new globalThis.WeakMap(param7)]
        // CODE → <GetByVal>: <Reg8: 17, Reg8: 19, Reg8: 17>
        // USED → r17 = param7[2];
        // CODE → <Call2>: <Reg8: 17, Reg8: 18, Reg8: 2, Reg8: 17>
        // USED → r17 = param2.call(undefined, param7[2]);
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 45, string_id: 14613>  # String: 'ReactFiberErrorDialog' (Identifier)
        // USED → r17 = param2.call(undefined, param7[2]).ReactFiberErrorDialog;
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 46, string_id: 14615>  # String: 'showErrorDialog' (Identifier)
        // USED → r17 = param2.call(undefined, param7[2]).ReactFiberErrorDialog.showErrorDialog;
        // CODE → <TypeOf>: <Reg8: 17, Reg8: 17>
        // USED → r17 = typeof param2.call(undefined, param7[2]).ReactFiberErrorDialog.showErrorDialog;
        if ("function" !== typeof param2.call(undefined, param7[2]).ReactFiberErrorDialog.showErrorDialog) {
            // ──────────────── Block 35 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
            // USED → r1 = globalThis.Error;
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 4985>  # String: 'Expected ReactFiberErrorDialog.showErrorDialog to be a function.' (String)
            // USED → r0 = "Expected ReactFiberErrorDialog.showErrorDialog to be a function.";
            // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
            // USED → r0 = globalThis.Error.call(undefined, "Expected ReactFiberErrorDialog.showErrorDialog to be a function.");
            // CODE → <Throw>: <Reg8: 0>
            throw globalThis.Error.call(undefined, "Expected ReactFiberErrorDialog.showErrorDialog to be a function.");
        } else {
            // ──────────────── Block 21 ──────────────── 
            // CODE → <GetById>: <Reg8: 17, Reg8: 14, UInt8: 47, string_id: 21355>  # String: 'ReactCurrentOwner' (Identifier)
            // USED → r17 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 121, Reg8: 17>
            createEnvironment()[121] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
            // CODE → <TryGetById>: <Reg8: 18, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
            // USED → r18 = globalThis.Error;
            // CODE → <LoadConstString>: <Reg8: 17, string_id: 6991>  # String: "This is not a real error. It's an implementation detail of React's selective hydration feature. If this leaks into userspace, it's a bug in React. Please file an issue." (String)
            // USED → r17 = "This is not a real error. It's an implementation detail of React's selective hydration feature. If this leaks into userspace, it's a bug in React. Please file an issue.";
            // CODE → <Call2>: <Reg8: 17, Reg8: 18, Reg8: 2, Reg8: 17>
            // USED → r17 = globalThis.Error.call(undefined, "This is not a real error. It's an implementation detail of React's selective hydration feature. If this leaks into userspace, it's a bug in React. Please file an issue.");
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 122, Reg8: 17>
            createEnvironment()[122] = globalThis.Error.call(undefined, "This is not a real error. It's an implementation detail of React's selective hydration feature. If this leaks into userspace, it's a bug in React. Please file an issue.")
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 123, Reg8: 12>
            createEnvironment()[123] = false
            // CODE → <NewObjectWithBuffer>: <Reg8: 17, UInt16: 3, UInt16: 3, UInt16: 64, UInt16: 225>  # Object: {'dehydrated': null, 'treeContext': null, 'retryLane': 0}
            // USED → r17 = { "dehydrated": null, "treeContext": null, "retryLane": 0 };
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 124, Reg8: 17>
            createEnvironment()[124] = { "dehydrated": null, "treeContext": null, "retryLane": 0 }
            // CODE → <Call2>: <Reg8: 15, Reg8: 15, Reg8: 2, Reg8: 11>
            // USED → r15 = createCursor.call(undefined, null);
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 125, Reg8: 15>
            createEnvironment()[125] = createCursor.call(undefined, null)
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 126, Reg8: 11>
            createEnvironment()[126] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 127, Reg8: 11>
            createEnvironment()[127] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 128, Reg8: 11>
            createEnvironment()[128] = null
            // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 43, string_id: 17455>  # String: 'ReactCurrentBatchConfig' (Identifier)
            // USED → r15 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 129, Reg8: 15>
            createEnvironment()[129] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 130, Reg8: 12>
            createEnvironment()[130] = false
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 131, Reg8: 12>
            createEnvironment()[131] = false
            // CODE → <GetById>: <Reg8: 15, Reg8: 0, UInt8: 48, string_id: 16750>  # String: 'WeakSet' (Identifier)
            // USED → r15 = globalThis.WeakSet;
            // CODE → <TypeOf>: <Reg8: 15, Reg8: 15>
            // USED → r15 = typeof globalThis.WeakSet;
            if ("function" === typeof globalThis.WeakSet) {
                // ──────────────── Block 23 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 15, Reg8: 0, UInt8: 48, string_id: 16750>  # String: 'WeakSet' (Identifier)
                // USED → r15 = globalThis.WeakSet;
            } else {
                // ──────────────── Block 22 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 15, Reg8: 0, UInt8: 49, string_id: 12170>  # String: 'Set' (Identifier)
                r15 = globalThis.Set
                // CODE → <Jmp>: <Addr8: 8>  # Address: 0000162b
                goto label_5675;
            }
            // ──────────────── Block 24 ──────────────── 
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 132, Reg8: 15>
            createEnvironment()[132] = globalThis.WeakSet
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 133, Reg8: 11>
            createEnvironment()[133] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 134, Reg8: 12>
            createEnvironment()[134] = false
            // CODE → <LoadConstInt>: <Reg8: 15, Imm32: 8192>
            // USED → r15 = 8192;
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 135, Reg8: 15>
            createEnvironment()[135] = 8192
            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 0, UInt8: 44, string_id: 24>  # String: 'WeakMap' (Identifier)
            // USED → r15 = globalThis.WeakMap;
            // CODE → <TypeOf>: <Reg8: 15, Reg8: 15>
            // USED → r15 = typeof globalThis.WeakMap;
            if ("function" === typeof globalThis.WeakMap) {
                // ──────────────── Block 26 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 15, Reg8: 0, UInt8: 44, string_id: 24>  # String: 'WeakMap' (Identifier)
                // USED → r15 = globalThis.WeakMap;
            } else {
                // ──────────────── Block 25 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 15, Reg8: 0, UInt8: 50, string_id: 26>  # String: 'Map' (Identifier)
                r15 = globalThis.Map
                // CODE → <Jmp>: <Addr8: 8>  # Address: 0000165b
                goto label_5723;
            }
            // ──────────────── Block 27 ──────────────── 
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 136, Reg8: 15>
            createEnvironment()[136] = globalThis.WeakMap
            // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 42, string_id: 21353>  # String: 'ReactCurrentDispatcher' (Identifier)
            // USED → r15 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 137, Reg8: 15>
            createEnvironment()[137] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher
            // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 47, string_id: 21355>  # String: 'ReactCurrentOwner' (Identifier)
            // USED → r15 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 138, Reg8: 15>
            createEnvironment()[138] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
            // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 43, string_id: 17455>  # String: 'ReactCurrentBatchConfig' (Identifier)
            // USED → r15 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 139, Reg8: 15>
            createEnvironment()[139] = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 140, Reg8: 10>
            createEnvironment()[140] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 141, Reg8: 11>
            createEnvironment()[141] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 142, Reg8: 11>
            createEnvironment()[142] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 143, Reg8: 10>
            createEnvironment()[143] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 144, Reg8: 10>
            createEnvironment()[144] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 145, Reg8: 11>
            createEnvironment()[145] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 146, Reg8: 12>
            createEnvironment()[146] = false
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 147, Reg8: 10>
            createEnvironment()[147] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 148, Reg8: 10>
            createEnvironment()[148] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 149, Reg8: 11>
            createEnvironment()[149] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 150, Reg8: 10>
            createEnvironment()[150] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 151, Reg8: 10>
            createEnvironment()[151] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 152, Reg8: 10>
            createEnvironment()[152] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 153, Reg8: 10>
            createEnvironment()[153] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 154, Reg8: 11>
            createEnvironment()[154] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 155, Reg8: 11>
            createEnvironment()[155] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 156, Reg8: 12>
            createEnvironment()[156] = false
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 157, Reg8: 10>
            createEnvironment()[157] = 0
            // CODE → <TryGetById>: <Reg8: 15, Reg8: 0, UInt8: 51, string_id: 21125>  # String: 'Infinity' (Identifier)
            // USED → r15 = globalThis.Infinity;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 158, Reg8: 15>
            createEnvironment()[158] = globalThis.Infinity
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 159, Reg8: 11>
            createEnvironment()[159] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 160, Reg8: 12>
            createEnvironment()[160] = false
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 161, Reg8: 11>
            createEnvironment()[161] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 162, Reg8: 11>
            createEnvironment()[162] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 163, Reg8: 12>
            createEnvironment()[163] = false
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 164, Reg8: 11>
            createEnvironment()[164] = null
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 165, Reg8: 10>
            createEnvironment()[165] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 166, Reg8: 10>
            createEnvironment()[166] = 0
            // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 167, Reg8: 11>
            createEnvironment()[167] = null
            // CODE → <CreateClosure>: <Reg8: 10, Reg8: 1, function_id: 848>  # Function: [#848 batchedUpdatesImpl of 178 bytes]: 3 params @ offset 0x0018a193
            // USED → r10 = batchedUpdatesImpl;
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 207, Reg8: 10>
            createEnvironment()[207] = batchedUpdatesImpl
            // CODE → <TryGetById>: <Reg8: 10, Reg8: 0, UInt8: 50, string_id: 26>  # String: 'Map' (Identifier)
            // USED → r10 = globalThis.Map;
            // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 10, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
            // USED → r12 = globalThis.Map.prototype;
            // CODE → <CreateThis>: <Reg8: 12, Reg8: 12, Reg8: 10>
            // USED → r12 = createThis(globalThis.Map.prototype, globalThis.Map);
            // CODE → <Mov>: <Reg8: 57, Reg8: 12>
            r57 = createThis(globalThis.Map.prototype, globalThis.Map)
            // CODE → <Construct>: <Reg8: 10, Reg8: 10, UInt8: 1>
            // USED → r10 = new globalThis.Map("undefined");
            // CODE → <SelectObject>: <Reg8: 10, Reg8: 12, Reg8: 10>
            // USED → r10 = createThis(globalThis.Map.prototype, globalThis.Map)[new globalThis.Map("undefined")];
            // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 168, Reg8: 10>
            createEnvironment()[168] = createThis(globalThis.Map.prototype, globalThis.Map)[new globalThis.Map("undefined")]
            // CODE → <NewObjectWithBuffer>: <Reg8: 12, UInt16: 5, UInt16: 4, UInt16: 340, UInt16: 302>  # Object: {'findFiberByHostInstance': null, 'bundleType': 0, 'version': '18.3.0-canary-9372c6311-20240315', 'rendererPackageName': 'react-native-renderer'}
            // USED → r12 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer" };
            // CODE → <PutById>: <Reg8: 12, Reg8: 8, UInt8: 6, string_id: 23266>  # String: 'findFiberByHostInstance' (Identifier)
            { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer" }.findFiberByHostInstance = getInstanceFromNode
            // CODE → <LoadConstString>: <Reg8: 10, string_id: 1866>  # String: '18.3.0-canary-9372c6311-20240315' (String)
            // USED → r10 = "18.3.0-canary-9372c6311-20240315";
            // CODE → <NewObject>: <Reg8: 8>
            // USED → r8 = {  };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 4, string_id: 14222>  # String: 'getInspectorDataForInstance' (Identifier)
            // USED → r8 = { getInspectorDataForInstance: getInspectorDataForInstance };
            // CODE → <CreateClosure>: <Reg8: 15, Reg8: 1, function_id: 849>  # Function: [#849 getInspectorDataForViewTag of 21 bytes]: 1 params @ offset 0x0018a245
            // USED → r15 = getInspectorDataForViewTag;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 12857>  # String: 'getInspectorDataForViewTag' (Identifier)
            // USED → r8 = { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag };
            // CODE → <CreateClosure>: <Reg8: 16, Reg8: 1, function_id: 850>  # Function: [#850  of 21 bytes]: 1 params @ offset 0x0018a25a
            // USED → r16 = function_850;
            // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 16, UInt8: 52, string_id: 87>  # String: 'bind' (Identifier)
            // USED → r15 = function_850.bind;
            // CODE → <Call3>: <Reg8: 15, Reg8: 15, Reg8: 16, Reg8: 11, Reg8: 5>
            // USED → r15 = function_850.bind(null, findNodeHandle);
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 11566>  # String: 'getInspectorDataForViewAtPoint' (Identifier)
            // USED → r8 = { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) };
            // CODE → <PutNewOwnById>: <Reg8: 12, Reg8: 8, string_id: 14815>  # String: 'rendererConfig' (Identifier)
            // USED → r12 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } };
            // CODE → <NewObject>: <Reg8: 8>
            // USED → r8 = {  };
            // CODE → <GetById>: <Reg8: 15, Reg8: 12, UInt8: 53, string_id: 18532>  # String: 'bundleType' (Identifier)
            // USED → r15 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 18532>  # String: 'bundleType' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType };
            // CODE → <GetById>: <Reg8: 15, Reg8: 12, UInt8: 54, string_id: 12196>  # String: 'version' (Identifier)
            // USED → r15 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 12196>  # String: 'version' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version };
            // CODE → <GetById>: <Reg8: 15, Reg8: 12, UInt8: 55, string_id: 22187>  # String: 'rendererPackageName' (Identifier)
            // USED → r15 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 22187>  # String: 'rendererPackageName' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName };
            // CODE → <GetById>: <Reg8: 15, Reg8: 12, UInt8: 56, string_id: 14815>  # String: 'rendererConfig' (Identifier)
            // USED → r15 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 15, string_id: 14815>  # String: 'rendererConfig' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 18506>  # String: 'overrideHookState' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 18507>  # String: 'overrideHookStateDeletePath' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 14986>  # String: 'overrideHookStateRenamePath' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 15629>  # String: 'overrideProps' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 15630>  # String: 'overridePropsDeletePath' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 13868>  # String: 'overridePropsRenamePath' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 15428>  # String: 'setErrorHandler' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 14649>  # String: 'setSuspenseHandler' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 17062>  # String: 'scheduleUpdate' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null };
            // CODE → <GetById>: <Reg8: 14, Reg8: 14, UInt8: 42, string_id: 21353>  # String: 'ReactCurrentDispatcher' (Identifier)
            // USED → r14 = param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 14, string_id: 18383>  # String: 'currentDispatcherRef' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher };
            // CODE → <CreateClosure>: <Reg8: 14, Reg8: 1, function_id: 851>  # Function: [#851 findHostInstanceByFiber of 30 bytes]: 2 params @ offset 0x0018a26f
            // USED → r14 = findHostInstanceByFiber;
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 14, string_id: 23271>  # String: 'findHostInstanceByFiber' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber };
            // CODE → <GetById>: <Reg8: 12, Reg8: 12, UInt8: 57, string_id: 23266>  # String: 'findFiberByHostInstance' (Identifier)
            // USED → r12 = { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance;
            // ──────────────── Block 29 ──────────────── 
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 12, string_id: 23266>  # String: 'findFiberByHostInstance' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 20510>  # String: 'findHostInstancesForRefresh' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 17297>  # String: 'scheduleRefresh' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 17366>  # String: 'scheduleRoot' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 20484>  # String: 'setRefreshHandler' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 11, string_id: 17221>  # String: 'getCurrentFiber' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null, getCurrentFiber: null };
            // CODE → <PutNewOwnById>: <Reg8: 8, Reg8: 10, string_id: 19409>  # String: 'reconcilerVersion' (Identifier)
            // USED → r8 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null, getCurrentFiber: null, reconcilerVersion: "18.3.0-canary-9372c6311-20240315" };
            // CODE → <Mov>: <Reg8: 7, Reg8: 8>
            // USED → r7 = { bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null, getCurrentFiber: null, reconcilerVersion: "18.3.0-canary-9372c6311-20240315" };
            // CODE → <GetById>: <Reg8: 8, Reg8: 0, UInt8: 58, string_id: 16819>  # String: '__REACT_DEVTOOLS_GLOBAL_HOOK__' (Identifier)
            // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__;
            // CODE → <TypeOf>: <Reg8: 8, Reg8: 8>
            // USED → r8 = typeof globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__;
            if ("undefined" !== typeof globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__) {
                // ──────────────── Block 30 ──────────────── 
                // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 58, string_id: 16819>  # String: '__REACT_DEVTOOLS_GLOBAL_HOOK__' (Identifier)
                // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__;
                // CODE → <Mov>: <Reg8: 6, Reg8: 8>
                // USED → r6 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__;
                // CODE → <GetById>: <Reg8: 8, Reg8: 8, UInt8: 59, string_id: 23915>  # String: 'isDisabled' (Identifier)
                // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.isDisabled;
                if (!globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.isDisabled) {
                    // ──────────────── Block 31 ──────────────── 
                    // CODE → <Mov>: <Reg8: 8, Reg8: 6>
                    // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__;
                    // CODE → <GetById>: <Reg8: 8, Reg8: 8, UInt8: 60, string_id: 15937>  # String: 'supportsFiber' (Identifier)
                    // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.supportsFiber;
                    if (globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.supportsFiber) {
                        // ──────────────── Block 32 ──────────────── 
                        // CODE → <GetById>: <Reg8: 8, Reg8: 6, UInt8: 61, string_id: 14570>  # String: 'inject' (Identifier)
                        // USED → r8 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.inject;
                        // CODE → <Call2>: <Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 7>
                        // USED → r7 = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.inject({ bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null, getCurrentFiber: null, reconcilerVersion: "18.3.0-canary-9372c6311-20240315" });
                        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 31, Reg8: 7>
                        createEnvironment()[31] = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__.inject({ bundleType: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.bundleType, version: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.version, rendererPackageName: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererPackageName, rendererConfig: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.rendererConfig, overrideHookState: null, overrideHookStateDeletePath: null, overrideHookStateRenamePath: null, overrideProps: null, overridePropsDeletePath: null, overridePropsRenamePath: null, setErrorHandler: null, setSuspenseHandler: null, scheduleUpdate: null, currentDispatcherRef: param2.call(undefined, param7[1]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher, findHostInstanceByFiber: findHostInstanceByFiber, findFiberByHostInstance: { "findFiberByHostInstance": null, "bundleType": 0, "version": "18.3.0-canary-9372c6311-20240315", "rendererPackageName": "react-native-renderer", rendererConfig: { getInspectorDataForInstance: getInspectorDataForInstance, getInspectorDataForViewTag: getInspectorDataForViewTag, getInspectorDataForViewAtPoint: function_850.bind(null, findNodeHandle) } }.findFiberByHostInstance || emptyFindFiberByHostInstance, findHostInstancesForRefresh: null, scheduleRefresh: null, scheduleRoot: null, setRefreshHandler: null, getCurrentFiber: null, reconcilerVersion: "18.3.0-canary-9372c6311-20240315" })
                        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 32, Reg8: 6>
                        createEnvironment()[32] = globalThis.__REACT_DEVTOOLS_GLOBAL_HOOK__
                        // CODE → <Jmp>: <Addr8: 4>  # Address: 0000183d
                        goto label_6205;
                    }
                }
            }
        }
    } else {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <Mov>: <Reg8: 54, Reg8: 43>
            // USED → r54 = false;
            // CODE → <Mov>: <Reg8: 41, Reg8: 54>
            // USED → r41 = false;
            // CODE → <GetNextPName>: <Reg8: 45, Reg8: 49, Reg8: 48, Reg8: 47, Reg8: 46>
            // USED → r45 = HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next();
            // CODE → <JmpUndefined>: <Addr8: 100, Reg8: 45>  # Address: 00000ecd
            if (HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next() === undefined) goto label_3789;
            // ──────────────── Block 2 ──────────────── 
            // CODE → <Mov>: <Reg8: 44, Reg8: 45>
            // USED → r44 = HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next();
            // CODE → <GetByIdShort>: <Reg8: 52, Reg8: 50, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
            // USED → r52 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }.hasOwnProperty;
            // CODE → <Call2>: <Reg8: 52, Reg8: 52, Reg8: 50, Reg8: 44>
            // USED → r52 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }.hasOwnProperty(HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next());
            // CODE → <Mov>: <Reg8: 43, Reg8: 54>
            r43 = false
            // CODE → <JmpFalse>: <Addr8: -31, Reg8: 52>  # Address: 00000e5d
            if (!{ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }.hasOwnProperty(HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next())) goto label_3677;
            // ──────────────── Block 3 ──────────────── 
            // CODE → <GetByVal>: <Reg8: 52, Reg8: 50, Reg8: 44>
            // USED → r52 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()];
            // CODE → <GetByIdShort>: <Reg8: 53, Reg8: 51, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
            // USED → r53 = {  }.hasOwnProperty;
            // CODE → <Call2>: <Reg8: 53, Reg8: 53, Reg8: 51, Reg8: 44>
            // USED → r53 = {  }.hasOwnProperty(HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next());
            if (!{  }.hasOwnProperty(HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next())) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <GetByVal>: <Reg8: 53, Reg8: 51, Reg8: 44>
                // USED → r53 = {  }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()];
                // CODE → <JmpTrue>: <Addr8: 14, Reg8: 53>  # Address: 00000eb0
                if ({  }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()]) goto label_3760;
                // ──────────────── Block 6 ──────────────── 
                // CODE → <PutByVal>: <Reg8: 51, Reg8: 44, Reg8: 52>
                {  }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()] = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()]
                // CODE → <LoadConstTrue>: <Reg8: 43>
                r43 = true
                // CODE → <Mov>: <Reg8: 42, Reg8: 52>
                r42 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()]
                // CODE → <Jmp>: <Addr8: -81>  # Address: 00000e5d
                goto label_3677;
            } else {
                // ──────────────── Block 4 ──────────────── 
                // CODE → <GetByVal>: <Reg8: 53, Reg8: 51, Reg8: 44>
                // USED → r53 = {  }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()];
                // CODE → <Mov>: <Reg8: 43, Reg8: 54>
                r43 = false
                // CODE → <Mov>: <Reg8: 42, Reg8: 52>
                r42 = { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()]
                // CODE → <JStrictEqual>: <Addr8: -61, Reg8: 53, Reg8: 52>  # Address: 00000e5d
                if ({  }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()] === { ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }[HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next()]) goto label_3677;
            }
        }
        // LOOP → END
        // ──────────────── Block 7 ──────────────── 
        // CODE → <TryGetById>: <Reg8: 43, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r43 = globalThis.Error;
        // CODE → <LoadConstString>: <Reg8: 42, string_id: 558>  # String: '`.' (String)
        // USED → r42 = "`.";
        // CODE → <Add>: <Reg8: 44, Reg8: 44, Reg8: 42>
        // USED → r44 = HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next() + "`.";
        // CODE → <LoadConstString>: <Reg8: 42, string_id: 4924>  # String: 'EventPluginRegistry: Cannot inject two different event plugins using the same name, `' (String)
        // USED → r42 = "EventPluginRegistry: Cannot inject two different event plugins using the same name, `";
        // CODE → <Add>: <Reg8: 42, Reg8: 42, Reg8: 44>
        // USED → r42 = "EventPluginRegistry: Cannot inject two different event plugins using the same name, `" + (HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next() + "`.");
        // CODE → <Call2>: <Reg8: 42, Reg8: 43, Reg8: 2, Reg8: 42>
        // USED → r42 = globalThis.Error.call(undefined, "EventPluginRegistry: Cannot inject two different event plugins using the same name, `" + (HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next() + "`."));
        // CODE → <Throw>: <Reg8: 42>
        throw globalThis.Error.call(undefined, "EventPluginRegistry: Cannot inject two different event plugins using the same name, `" + (HermesPropertyIterator({ ResponderEventPlugin: { _getResponder: _getResponder, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onStartShouldSetResponder", "captured": "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onScrollShouldSetResponder", "captured": "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, selectionChangeShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onSelectionChangeShouldSetResponder", "captured": "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, moveShouldSetResponder: { phasedRegistrationNames: { "bubbled": "onMoveShouldSetResponder", "captured": "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }, responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }, responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }, responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] }, responderGrant: { registrationName: "onResponderGrant", dependencies: [] }, responderReject: { registrationName: "onResponderReject", dependencies: [] }, responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }, extractEvents: extractEvents, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler } }, ReactNativeBridgeEventPlugin: { eventTypes: {  }, extractEvents: extractEvents } }).next() + "`."));
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 34 ──────────────── 
            // CODE → <CreateClosure>: <Reg8: 6, Reg8: 1, function_id: 852>  # Function: [#852  of 60 bytes]: 3 params @ offset 0x0018a28d
            // USED → r6 = function_852;
            // CODE → <PutById>: <Reg8: 3, Reg8: 6, UInt8: 7, string_id: 18089>  # String: 'createPortal' (Identifier)
            param6.createPortal = function_852
            // CODE → <CreateClosure>: <Reg8: 6, Reg8: 1, function_id: 853>  # Function: [#853  of 172 bytes]: 4 params @ offset 0x0018a2c9
            // USED → r6 = function_853;
            // CODE → <PutById>: <Reg8: 3, Reg8: 6, UInt8: 8, string_id: 11552>  # String: 'dispatchCommand' (Identifier)
            param6.dispatchCommand = function_853
            // CODE → <CreateClosure>: <Reg8: 6, Reg8: 1, function_id: 854>  # Function: [#854  of 82 bytes]: 2 params @ offset 0x0018a375
            // USED → r6 = function_854;
            // CODE → <PutById>: <Reg8: 3, Reg8: 6, UInt8: 9, string_id: 12842>  # String: 'findHostInstance_DEPRECATED' (Identifier)
            param6.findHostInstance_DEPRECATED = function_854
            // CODE → <PutById>: <Reg8: 3, Reg8: 5, UInt8: 10, string_id: 18319>  # String: 'findNodeHandle' (Identifier)
            param6.findNodeHandle = findNodeHandle
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 11, string_id: 14222>  # String: 'getInspectorDataForInstance' (Identifier)
            param6.getInspectorDataForInstance = getInspectorDataForInstance
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 855>  # Function: [#855  of 30 bytes]: 2 params @ offset 0x0018a3c7
            // USED → r4 = function_855;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 12, string_id: 23506>  # String: 'getNodeFromInternalInstanceHandle' (Identifier)
            param6.getNodeFromInternalInstanceHandle = function_855
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 856>  # Function: [#856  of 115 bytes]: 2 params @ offset 0x0018a3e5
            // USED → r4 = function_856;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 13, string_id: 19508>  # String: 'getPublicInstanceFromInternalInstanceHandle' (Identifier)
            param6.getPublicInstanceFromInternalInstanceHandle = function_856
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 857>  # Function: [#857  of 21 bytes]: 1 params @ offset 0x0018a458
            // USED → r4 = function_857;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 14, string_id: 19860>  # String: 'isChildPublicInstance' (Identifier)
            param6.isChildPublicInstance = function_857
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 858>  # Function: [#858  of 267 bytes]: 5 params @ offset 0x0018a46d
            // USED → r4 = function_858;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 15, string_id: 11830>  # String: 'render' (Identifier)
            param6.render = function_858
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 859>  # Function: [#859  of 161 bytes]: 3 params @ offset 0x0018a578
            // USED → r4 = function_859;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 16, string_id: 13824>  # String: 'sendAccessibilityEvent' (Identifier)
            param6.sendAccessibilityEvent = function_859
            // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 860>  # Function: [#860  of 56 bytes]: 2 params @ offset 0x0018a619
            // USED → r4 = function_860;
            // CODE → <PutById>: <Reg8: 3, Reg8: 4, UInt8: 17, string_id: 17701>  # String: 'stopSurface' (Identifier)
            param6.stopSurface = function_860
            // CODE → <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 862>  # Function: [#862  of 21 bytes]: 2 params @ offset 0x0018a66d
            // USED → r1 = function_862;
            // CODE → <PutById>: <Reg8: 3, Reg8: 1, UInt8: 18, string_id: 24466>  # String: 'unmountComponentAtNode' (Identifier)
            param6.unmountComponentAtNode = function_862
            // CODE → <Ret>: <Reg8: 2>
            return undefined;
            // ──────────────── Block 33 ──────────────── 
            // CODE → <Catch>: <Reg8: 6>
            r6 = caughtException
        }
        // LOOP → END
    }
}