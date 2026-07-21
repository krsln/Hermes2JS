function function_467(param0, param1, param2, param3, param4, param5, param6, param7) {
    // CODE → <LoadParam>: <Reg8: 18, UInt8: 2>
    // USED → r18 = param2
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 6>
    // USED → r3 = param6
    // CODE → <LoadParam>: <Reg8: 19, UInt8: 7>
    // USED → r19 = param7
    // CODE → <CreateEnvironment>: <Reg8: 1>
    r1 = createEnvironment()
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 18>
    r1[0] = param2;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 19>
    r1[1] = param7;
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    // USED → r2 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 468>  # Function: [#468 executeDispatch of 77 bytes]: 4 params @ offset 0x00179753
    // USED → r0 = executeDispatch /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 169, Reg8: 0>
    r1[169] = executeDispatch /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 469>  # Function: [#469 executeDirectDispatch of 103 bytes]: 2 params @ offset 0x001797a0
    // USED → r0 = executeDirectDispatch /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 170, Reg8: 0>
    r1[170] = executeDirectDispatch /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 470>  # Function: [#470 functionThatReturnsTrue of 4 bytes]: 1 params @ offset 0x00179807
    // USED → r0 = functionThatReturnsTrue /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 171, Reg8: 0>
    r1[171] = functionThatReturnsTrue /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 42, Reg8: 1, function_id: 471>  # Function: [#471 functionThatReturnsFalse of 4 bytes]: 1 params @ offset 0x00174221
    // USED → r42 = functionThatReturnsFalse /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 172, Reg8: 42>
    r1[172] = functionThatReturnsFalse /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 39, Reg8: 1, function_id: 472>  # Function: [#472 SyntheticEvent of 213 bytes]: 5 params @ offset 0x0017980b
    // USED → r39 = SyntheticEvent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 173, Reg8: 39>
    r1[173] = SyntheticEvent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 473>  # Function: [#473 createOrGetPooledEvent of 108 bytes]: 5 params @ offset 0x001798e0
    // USED → r0 = createOrGetPooledEvent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 174, Reg8: 0>
    r1[174] = createOrGetPooledEvent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 474>  # Function: [#474 releasePooledEvent of 82 bytes]: 2 params @ offset 0x0017994c
    // USED → r0 = releasePooledEvent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 175, Reg8: 0>
    r1[175] = releasePooledEvent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 17, Reg8: 1, function_id: 475>  # Function: [#475 addEventPoolingTo of 40 bytes]: 2 params @ offset 0x0017999e
    // USED → r17 = addEventPoolingTo /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 176, Reg8: 17>
    r1[176] = addEventPoolingTo /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 476>  # Function: [#476 isStartish of 13 bytes]: 2 params @ offset 0x001799c6
    // USED → r0 = isStartish /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 177, Reg8: 0>
    r1[177] = isStartish /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 477>  # Function: [#477 isMoveish of 13 bytes]: 2 params @ offset 0x001799d3
    // USED → r0 = isMoveish /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 178, Reg8: 0>
    r1[178] = isMoveish /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 478>  # Function: [#478 timestampForTouch of 20 bytes]: 2 params @ offset 0x001799e0
    // USED → r0 = timestampForTouch /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 179, Reg8: 0>
    r1[179] = timestampForTouch /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 479>  # Function: [#479 getTouchIdentifier of 38 bytes]: 2 params @ offset 0x001799f4
    // USED → r0 = getTouchIdentifier /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 180, Reg8: 0>
    r1[180] = getTouchIdentifier /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 480>  # Function: [#480 recordTouchStart of 283 bytes]: 2 params @ offset 0x00179a1a
    // USED → r0 = recordTouchStart /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 181, Reg8: 0>
    r1[181] = recordTouchStart /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 481>  # Function: [#481 recordTouchMove of 128 bytes]: 2 params @ offset 0x00179b35
    // USED → r0 = recordTouchMove /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 182, Reg8: 0>
    r1[182] = recordTouchMove /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 482>  # Function: [#482 recordTouchEnd of 128 bytes]: 2 params @ offset 0x00179bb5
    // USED → r0 = recordTouchEnd /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 183, Reg8: 0>
    r1[183] = recordTouchEnd /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 483>  # Function: [#483 accumulate of 118 bytes]: 3 params @ offset 0x00179c35
    // USED → r0 = accumulate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 184, Reg8: 0>
    r1[184] = accumulate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 484>  # Function: [#484 accumulateInto of 130 bytes]: 3 params @ offset 0x00179cab
    // USED → r0 = accumulateInto /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 185, Reg8: 0>
    r1[185] = accumulateInto /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 485>  # Function: [#485 forEachAccumulated of 62 bytes]: 4 params @ offset 0x00179d2d
    // USED → r0 = forEachAccumulated /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 186, Reg8: 0>
    r1[186] = forEachAccumulated /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 486>  # Function: [#486 changeResponder of 60 bytes]: 3 params @ offset 0x00179d6b
    // USED → r0 = changeResponder /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 187, Reg8: 0>
    r1[187] = changeResponder /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 487>  # Function: [#487 getParent$1 of 36 bytes]: 2 params @ offset 0x00179da7
    // USED → r0 = getParent$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 188, Reg8: 0>
    r1[188] = getParent$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 488>  # Function: [#488 traverseTwoPhase$1 of 128 bytes]: 4 params @ offset 0x00179dcb
    // USED → r0 = traverseTwoPhase$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 189, Reg8: 0>
    r1[189] = traverseTwoPhase$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 489>  # Function: [#489 getListener$1 of 102 bytes]: 3 params @ offset 0x00179e4b
    // USED → r0 = getListener$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 190, Reg8: 0>
    r1[190] = getListener$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 490>  # Function: [#490 accumulateDirectionalDispatches$1 of 85 bytes]: 4 params @ offset 0x00179eb1
    // USED → r0 = accumulateDirectionalDispatches$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 191, Reg8: 0>
    r1[191] = accumulateDirectionalDispatches$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 491>  # Function: [#491 accumulateDirectDispatchesSingle$1 of 119 bytes]: 2 params @ offset 0x00179f06
    // USED → r0 = accumulateDirectDispatchesSingle$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 192, Reg8: 0>
    r1[192] = accumulateDirectDispatchesSingle$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 492>  # Function: [#492 accumulateTwoPhaseDispatchesSingleSkipTarget of 70 bytes]: 2 params @ offset 0x00179f7d
    // USED → r0 = accumulateTwoPhaseDispatchesSingleSkipTarget /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 193, Reg8: 0>
    r1[193] = accumulateTwoPhaseDispatchesSingleSkipTarget /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 493>  # Function: [#493 accumulateTwoPhaseDispatchesSingle$1 of 54 bytes]: 2 params @ offset 0x00179fc3
    // USED → r0 = accumulateTwoPhaseDispatchesSingle$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 194, Reg8: 0>
    r1[194] = accumulateTwoPhaseDispatchesSingle$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 16, Reg8: 1, function_id: 494>  # Function: [#494 recomputePluginOrdering of 495 bytes]: 1 params @ offset 0x00179ff9
    // USED → r16 = recomputePluginOrdering /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 495>  # Function: [#495 publishRegistrationName of 65 bytes]: 3 params @ offset 0x0017a1e8
    // USED → r0 = publishRegistrationName /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 195, Reg8: 0>
    r1[195] = publishRegistrationName /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 496>  # Function: [#496 getListener of 102 bytes]: 3 params @ offset 0x00179e4b
    // USED → r0 = getListener /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 196, Reg8: 0>
    r1[196] = getListener /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 497>  # Function: [#497 accumulateDirectionalDispatches of 85 bytes]: 4 params @ offset 0x0017a229
    // USED → r0 = accumulateDirectionalDispatches /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 197, Reg8: 0>
    r1[197] = accumulateDirectionalDispatches /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 498>  # Function: [#498 traverseTwoPhase of 176 bytes]: 5 params @ offset 0x0017a27e
    // USED → r0 = traverseTwoPhase /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 198, Reg8: 0>
    r1[198] = traverseTwoPhase /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 499>  # Function: [#499 accumulateTwoPhaseDispatchesSingle of 56 bytes]: 2 params @ offset 0x0017a32e
    // USED → r0 = accumulateTwoPhaseDispatchesSingle /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 199, Reg8: 0>
    r1[199] = accumulateTwoPhaseDispatchesSingle /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 500>  # Function: [#500 accumulateDirectDispatchesSingle of 119 bytes]: 2 params @ offset 0x0017a366
    // USED → r0 = accumulateDirectDispatchesSingle /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 200, Reg8: 0>
    r1[200] = accumulateDirectDispatchesSingle /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 501>  # Function: [#501 defaultDiffer of 71 bytes]: 3 params @ offset 0x0017a3dd
    // USED → r0 = defaultDiffer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 201, Reg8: 0>
    r1[201] = defaultDiffer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 502>  # Function: [#502 restoreDeletedValuesInNestedArray of 316 bytes]: 4 params @ offset 0x0017a424
    // USED → r0 = restoreDeletedValuesInNestedArray /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 202, Reg8: 0>
    r1[202] = restoreDeletedValuesInNestedArray /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 503>  # Function: [#503 diffNestedProperty of 416 bytes]: 5 params @ offset 0x0017a560
    // USED → r0 = diffNestedProperty /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 203, Reg8: 0>
    r1[203] = diffNestedProperty /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 504>  # Function: [#504 addNestedProperty of 108 bytes]: 4 params @ offset 0x0017a700
    // USED → r0 = addNestedProperty /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 204, Reg8: 0>
    r1[204] = addNestedProperty /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 505>  # Function: [#505 clearNestedProperty of 108 bytes]: 4 params @ offset 0x0017a76c
    // USED → r0 = clearNestedProperty /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 205, Reg8: 0>
    r1[205] = clearNestedProperty /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 506>  # Function: [#506 diffProperties of 881 bytes]: 5 params @ offset 0x0017a7d8
    // USED → r0 = diffProperties /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 206, Reg8: 0>
    r1[206] = diffProperties /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 507>  # Function: [#507 batchedUpdatesImpl of 15 bytes]: 3 params @ offset 0x0017ab49
    // USED → r0 = batchedUpdatesImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 207, Reg8: 0>
    r1[207] = batchedUpdatesImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 508>  # Function: [#508 batchedUpdates$1 of 64 bytes]: 3 params @ offset 0x0017ab58
    // USED → r0 = batchedUpdates$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 208, Reg8: 0>
    r1[208] = batchedUpdates$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 509>  # Function: [#509 executeDispatchesAndReleaseTopLevel of 174 bytes]: 2 params @ offset 0x0017ab98
    // USED → r0 = executeDispatchesAndReleaseTopLevel /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 209, Reg8: 0>
    r1[209] = executeDispatchesAndReleaseTopLevel /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 512>  # Function: [#512 onCommitRoot of 92 bytes]: 2 params @ offset 0x0017adc9
    // USED → r0 = onCommitRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 210, Reg8: 0>
    r1[210] = onCommitRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 513>  # Function: [#513 clz32Fallback of 53 bytes]: 2 params @ offset 0x0017ae25
    r9 = clz32Fallback /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 514>  # Function: [#514 getHighestPriorityLanes of 427 bytes]: 2 params @ offset 0x0017ae5a
    // USED → r0 = getHighestPriorityLanes /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 211, Reg8: 0>
    r1[211] = getHighestPriorityLanes /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 515>  # Function: [#515 getNextLanes of 233 bytes]: 3 params @ offset 0x0017b005
    // USED → r0 = getNextLanes /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 212, Reg8: 0>
    r1[212] = getNextLanes /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 516>  # Function: [#516 computeExpirationTime of 400 bytes]: 3 params @ offset 0x0017b0ee
    // USED → r0 = computeExpirationTime /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 213, Reg8: 0>
    r1[213] = computeExpirationTime /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 517>  # Function: [#517 getLanesToRetrySynchronouslyOnError of 69 bytes]: 3 params @ offset 0x0017b27e
    // USED → r0 = getLanesToRetrySynchronouslyOnError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 214, Reg8: 0>
    r1[214] = getLanesToRetrySynchronouslyOnError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 518>  # Function: [#518 claimNextTransitionLane of 43 bytes]: 1 params @ offset 0x0017b2c3
    // USED → r0 = claimNextTransitionLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 215, Reg8: 0>
    r1[215] = claimNextTransitionLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 519>  # Function: [#519 claimNextRetryLane of 46 bytes]: 1 params @ offset 0x0017b2ee
    // USED → r0 = claimNextRetryLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 216, Reg8: 0>
    r1[216] = claimNextRetryLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 520>  # Function: [#520 createLaneMap of 31 bytes]: 2 params @ offset 0x0017b31c
    // USED → r0 = createLaneMap /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 217, Reg8: 0>
    r1[217] = createLaneMap /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 521>  # Function: [#521 markRootUpdated$1 of 50 bytes]: 3 params @ offset 0x0017b33b
    // USED → r0 = markRootUpdated$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 218, Reg8: 0>
    r1[218] = markRootUpdated$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 522>  # Function: [#522 markRootFinished of 281 bytes]: 4 params @ offset 0x0017b36d
    // USED → r0 = markRootFinished /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 219, Reg8: 0>
    r1[219] = markRootFinished /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 523>  # Function: [#523 markSpawnedDeferredLane of 127 bytes]: 4 params @ offset 0x0017b486
    // USED → r0 = markSpawnedDeferredLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 220, Reg8: 0>
    r1[220] = markSpawnedDeferredLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 524>  # Function: [#524 markRootEntangled of 105 bytes]: 3 params @ offset 0x0017b505
    // USED → r0 = markRootEntangled /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 221, Reg8: 0>
    r1[221] = markRootEntangled /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 525>  # Function: [#525 lanesToEventPriority of 57 bytes]: 2 params @ offset 0x0017b56e
    // USED → r0 = lanesToEventPriority /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 222, Reg8: 0>
    r1[222] = lanesToEventPriority /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 526>  # Function: [#526 shim$1 of 21 bytes]: 1 params @ offset 0x0017b5a7
    // USED → r0 = shim$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 223, Reg8: 0>
    r1[223] = shim$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 527>  # Function: [#527 createTextInstance of 62 bytes]: 5 params @ offset 0x0017b5bc
    // USED → r0 = createTextInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 224, Reg8: 0>
    r1[224] = createTextInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 528>  # Function: [#528 getPublicInstance of 65 bytes]: 2 params @ offset 0x0017b5fa
    // USED → r0 = getPublicInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 225, Reg8: 0>
    r1[225] = getPublicInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 529>  # Function: [#529 cloneHiddenInstance of 97 bytes]: 2 params @ offset 0x0017b63b
    // USED → r0 = cloneHiddenInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 226, Reg8: 0>
    r1[226] = cloneHiddenInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 8, Reg8: 1, function_id: 530>  # Function: [#530 getInstanceFromNode of 51 bytes]: 2 params @ offset 0x0017b69c
    // USED → r8 = getInstanceFromNode /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 531>  # Function: [#531 getIteratorFn of 67 bytes]: 2 params @ offset 0x0017b6cf
    // USED → r0 = getIteratorFn /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 227, Reg8: 0>
    r1[227] = getIteratorFn /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 532>  # Function: [#532 getNearestMountedFiber of 123 bytes]: 2 params @ offset 0x0017b712
    // USED → r0 = getNearestMountedFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 228, Reg8: 0>
    r1[228] = getNearestMountedFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 533>  # Function: [#533 assertIsMounted of 42 bytes]: 2 params @ offset 0x0017b78d
    // USED → r0 = assertIsMounted /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 229, Reg8: 0>
    r1[229] = assertIsMounted /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 534>  # Function: [#534 findCurrentFiberUsingSlowPath of 534 bytes]: 2 params @ offset 0x0017b7b7
    // USED → r0 = findCurrentFiberUsingSlowPath /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 230, Reg8: 0>
    r1[230] = findCurrentFiberUsingSlowPath /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 535>  # Function: [#535 findCurrentHostFiber of 34 bytes]: 2 params @ offset 0x0017b9cd
    // USED → r0 = findCurrentHostFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 231, Reg8: 0>
    r1[231] = findCurrentHostFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 536>  # Function: [#536 findCurrentHostFiberImpl of 83 bytes]: 2 params @ offset 0x0017b9ef
    // USED → r0 = findCurrentHostFiberImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 232, Reg8: 0>
    r1[232] = findCurrentHostFiberImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 15, Reg8: 1, function_id: 537>  # Function: [#537 createCursor of 11 bytes]: 2 params @ offset 0x0017ba42
    // USED → r15 = createCursor /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 538>  # Function: [#538 pop of 63 bytes]: 2 params @ offset 0x0017ba4d
    // USED → r0 = pop /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 233, Reg8: 0>
    r1[233] = pop /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 539>  # Function: [#539 push of 43 bytes]: 3 params @ offset 0x0017ba8c
    // USED → r0 = push /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 234, Reg8: 0>
    r1[234] = push /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 38, Reg8: 1, function_id: 540>  # Function: [#540 is of 59 bytes]: 3 params @ offset 0x0017bab7
    r38 = is /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 541>  # Function: [#541 pushHostContainer of 81 bytes]: 3 params @ offset 0x0017baf2
    // USED → r0 = pushHostContainer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 235, Reg8: 0>
    r1[235] = pushHostContainer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 542>  # Function: [#542 popHostContainer of 38 bytes]: 1 params @ offset 0x0017bb43
    // USED → r0 = popHostContainer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 236, Reg8: 0>
    r1[236] = popHostContainer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 543>  # Function: [#543 pushHostContext of 129 bytes]: 2 params @ offset 0x0017bb69
    // USED → r0 = pushHostContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 237, Reg8: 0>
    r1[237] = pushHostContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 544>  # Function: [#544 popHostContext of 47 bytes]: 2 params @ offset 0x0017bbea
    // USED → r0 = popHostContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 238, Reg8: 0>
    r1[238] = popHostContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 545>  # Function: [#545 finishQueueingConcurrentUpdates of 214 bytes]: 1 params @ offset 0x0017bc19
    // USED → r0 = finishQueueingConcurrentUpdates /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 239, Reg8: 0>
    r1[239] = finishQueueingConcurrentUpdates /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 546>  # Function: [#546 enqueueUpdate$1 of 160 bytes]: 5 params @ offset 0x0017bcef
    // USED → r0 = enqueueUpdate$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 240, Reg8: 0>
    r1[240] = enqueueUpdate$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 547>  # Function: [#547 enqueueConcurrentRenderForLane of 39 bytes]: 3 params @ offset 0x0017bd8f
    // USED → r0 = enqueueConcurrentRenderForLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 241, Reg8: 0>
    r1[241] = enqueueConcurrentRenderForLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 548>  # Function: [#548 markUpdateLaneFromFiberToRoot of 285 bytes]: 4 params @ offset 0x0017bdb6
    // USED → r0 = markUpdateLaneFromFiberToRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 242, Reg8: 0>
    r1[242] = markUpdateLaneFromFiberToRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 549>  # Function: [#549 getRootForUpdatedFiber of 97 bytes]: 2 params @ offset 0x0017bed3
    // USED → r0 = getRootForUpdatedFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 243, Reg8: 0>
    r1[243] = getRootForUpdatedFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 550>  # Function: [#550 ensureRootIsScheduled of 141 bytes]: 2 params @ offset 0x0017bf34
    // USED → r0 = ensureRootIsScheduled /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 244, Reg8: 0>
    r1[244] = ensureRootIsScheduled /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 551>  # Function: [#551 flushSyncWorkAcrossRoots_impl of 657 bytes]: 2 params @ offset 0x0017bfc1
    // USED → r0 = flushSyncWorkAcrossRoots_impl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 245, Reg8: 0>
    r1[245] = flushSyncWorkAcrossRoots_impl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 552>  # Function: [#552 throwError of 5 bytes]: 2 params @ offset 0x0016fa3b
    // USED → r0 = throwError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 246, Reg8: 0>
    r1[246] = throwError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 553>  # Function: [#553 processRootScheduleInMicrotask of 167 bytes]: 1 params @ offset 0x0017c252
    // USED → r0 = processRootScheduleInMicrotask /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 247, Reg8: 0>
    r1[247] = processRootScheduleInMicrotask /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 554>  # Function: [#554 scheduleTaskForRootDuringMicrotask of 622 bytes]: 3 params @ offset 0x0017c2f9
    // USED → r0 = scheduleTaskForRootDuringMicrotask /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 248, Reg8: 0>
    r1[248] = scheduleTaskForRootDuringMicrotask /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 555>  # Function: [#555 scheduleImmediateTask of 90 bytes]: 2 params @ offset 0x0017c567
    // USED → r0 = scheduleImmediateTask /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 249, Reg8: 0>
    r1[249] = scheduleImmediateTask /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 557>  # Function: [#557 initializeUpdateQueue of 50 bytes]: 2 params @ offset 0x0017c620
    // USED → r0 = initializeUpdateQueue /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 250, Reg8: 0>
    r1[250] = initializeUpdateQueue /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 558>  # Function: [#558 cloneUpdateQueue of 83 bytes]: 3 params @ offset 0x0017c652
    // USED → r0 = cloneUpdateQueue /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 251, Reg8: 0>
    r1[251] = cloneUpdateQueue /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 559>  # Function: [#559 createUpdate of 21 bytes]: 2 params @ offset 0x0017c6a5
    // USED → r0 = createUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 252, Reg8: 0>
    r1[252] = createUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 560>  # Function: [#560 enqueueUpdate of 151 bytes]: 4 params @ offset 0x0017c6ba
    // USED → r0 = enqueueUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 253, Reg8: 0>
    r1[253] = enqueueUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 561>  # Function: [#561 entangleTransitions of 86 bytes]: 4 params @ offset 0x0017c751
    // USED → r0 = entangleTransitions /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 254, Reg8: 0>
    r1[254] = entangleTransitions /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 562>  # Function: [#562 enqueueCapturedUpdate of 232 bytes]: 3 params @ offset 0x0017c7a7
    // USED → r0 = enqueueCapturedUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 255, Reg8: 0>
    r1[255] = enqueueCapturedUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 563>  # Function: [#563 processUpdateQueue of 911 bytes]: 5 params @ offset 0x0017c88f
    // USED → r0 = processUpdateQueue /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 256, Reg8: 0>
    r1[256] = processUpdateQueue /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 564>  # Function: [#564 callCallback of 56 bytes]: 3 params @ offset 0x0017cc1e
    // USED → r0 = callCallback /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 257, Reg8: 0>
    r1[257] = callCallback /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 565>  # Function: [#565 commitCallbacks of 74 bytes]: 3 params @ offset 0x0017cc56
    // USED → r0 = commitCallbacks /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 258, Reg8: 0>
    r1[258] = commitCallbacks /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 566>  # Function: [#566 shallowEqual of 207 bytes]: 3 params @ offset 0x0017cca0
    // USED → r0 = shallowEqual /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 259, Reg8: 0>
    r1[259] = shallowEqual /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 567>  # Function: [#567 describeComponentFrame of 28 bytes]: 3 params @ offset 0x0017cd6f
    // USED → r0 = describeComponentFrame /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 260, Reg8: 0>
    r1[260] = describeComponentFrame /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 568>  # Function: [#568 describeFunctionComponentFrame of 48 bytes]: 2 params @ offset 0x0017cd8b
    // USED → r0 = describeFunctionComponentFrame /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 261, Reg8: 0>
    r1[261] = describeFunctionComponentFrame /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 569>  # Function: [#569 describeFiber of 201 bytes]: 2 params @ offset 0x0017cdbb
    // USED → r0 = describeFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 262, Reg8: 0>
    r1[262] = describeFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 570>  # Function: [#570 getStackByFiberInDevAndProd of 82 bytes]: 2 params @ offset 0x0017cef4
    // USED → r0 = getStackByFiberInDevAndProd /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 263, Reg8: 0>
    r1[263] = getStackByFiberInDevAndProd /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 571>  # Function: [#571 isThenableResolved of 30 bytes]: 2 params @ offset 0x0017cf46
    // USED → r0 = isThenableResolved /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 264, Reg8: 0>
    r1[264] = isThenableResolved /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 572>  # Function: [#572 noop of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r0 = noop /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 265, Reg8: 0>
    r1[265] = noop /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 573>  # Function: [#573 trackUsedThenable of 298 bytes]: 4 params @ offset 0x0017cf64
    // USED → r0 = trackUsedThenable /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 266, Reg8: 0>
    r1[266] = trackUsedThenable /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 576>  # Function: [#576 getSuspendedThenable of 44 bytes]: 1 params @ offset 0x0017d0ee
    // USED → r0 = getSuspendedThenable /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 267, Reg8: 0>
    r1[267] = getSuspendedThenable /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 577>  # Function: [#577 checkIfUseWrappedInAsyncCatch of 39 bytes]: 2 params @ offset 0x0017d11a
    // USED → r0 = checkIfUseWrappedInAsyncCatch /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 268, Reg8: 0>
    r1[268] = checkIfUseWrappedInAsyncCatch /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 578>  # Function: [#578 unwrapThenable of 59 bytes]: 2 params @ offset 0x0017d141
    // USED → r0 = unwrapThenable /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 269, Reg8: 0>
    r1[269] = unwrapThenable /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 579>  # Function: [#579 convertStringRefToCallbackRef of 204 bytes]: 5 params @ offset 0x0017d17c
    // USED → r0 = convertStringRefToCallbackRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 270, Reg8: 0>
    r1[270] = convertStringRefToCallbackRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 581>  # Function: [#581 coerceRef of 76 bytes]: 5 params @ offset 0x0017d274
    // USED → r0 = coerceRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 271, Reg8: 0>
    r1[271] = coerceRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 582>  # Function: [#582 throwOnInvalidObjectType of 116 bytes]: 3 params @ offset 0x0017d2c0
    // USED → r0 = throwOnInvalidObjectType /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 272, Reg8: 0>
    r1[272] = throwOnInvalidObjectType /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 583>  # Function: [#583 resolveLazy of 24 bytes]: 2 params @ offset 0x0017d334
    // USED → r0 = resolveLazy /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 273, Reg8: 0>
    r1[273] = resolveLazy /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 20, Reg8: 1, function_id: 584>  # Function: [#584 createChildReconciler of 160 bytes]: 2 params @ offset 0x0017d34c
    // USED → r20 = createChildReconciler /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 604>  # Function: [#604 pushHiddenContext of 52 bytes]: 3 params @ offset 0x0017e7c3
    // USED → r0 = pushHiddenContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 274, Reg8: 0>
    r1[274] = pushHiddenContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 605>  # Function: [#605 reuseHiddenContextOnStack of 40 bytes]: 1 params @ offset 0x0017e7f7
    // USED → r0 = reuseHiddenContextOnStack /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 275, Reg8: 0>
    r1[275] = reuseHiddenContextOnStack /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 606>  # Function: [#606 popHiddenContext of 42 bytes]: 1 params @ offset 0x0017e81f
    // USED → r0 = popHiddenContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 276, Reg8: 0>
    r1[276] = popHiddenContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 607>  # Function: [#607 pushPrimaryTreeSuspenseHandler of 97 bytes]: 2 params @ offset 0x0017e849
    // USED → r0 = pushPrimaryTreeSuspenseHandler /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 277, Reg8: 0>
    r1[277] = pushPrimaryTreeSuspenseHandler /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 608>  # Function: [#608 pushOffscreenSuspenseHandler of 108 bytes]: 2 params @ offset 0x0017e8aa
    // USED → r0 = pushOffscreenSuspenseHandler /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 278, Reg8: 0>
    r1[278] = pushOffscreenSuspenseHandler /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 609>  # Function: [#609 reuseSuspenseHandlerOnStack of 41 bytes]: 1 params @ offset 0x0017e916
    // USED → r0 = reuseSuspenseHandlerOnStack /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 279, Reg8: 0>
    r1[279] = reuseSuspenseHandlerOnStack /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 610>  # Function: [#610 popSuspenseHandler of 50 bytes]: 2 params @ offset 0x0017e93f
    // USED → r0 = popSuspenseHandler /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 280, Reg8: 0>
    r1[280] = popSuspenseHandler /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 611>  # Function: [#611 findFirstSuspended of 269 bytes]: 2 params @ offset 0x0017e971
    // USED → r0 = findFirstSuspended /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 281, Reg8: 0>
    r1[281] = findFirstSuspended /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 36, Reg8: 1, function_id: 612>  # Function: [#612 throwInvalidHookError of 21 bytes]: 1 params @ offset 0x0017ea7e
    // USED → r36 = throwInvalidHookError /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 613>  # Function: [#613 areHookInputsEqual of 102 bytes]: 3 params @ offset 0x0017ea93
    // USED → r0 = areHookInputsEqual /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 282, Reg8: 0>
    r1[282] = areHookInputsEqual /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 614>  # Function: [#614 renderWithHooks of 143 bytes]: 7 params @ offset 0x0017eaf9
    // USED → r0 = renderWithHooks /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 283, Reg8: 0>
    r1[283] = renderWithHooks /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 615>  # Function: [#615 finishRenderingHooks of 101 bytes]: 1 params @ offset 0x0017eb88
    // USED → r0 = finishRenderingHooks /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 284, Reg8: 0>
    r1[284] = finishRenderingHooks /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 616>  # Function: [#616 renderWithHooksAgain of 127 bytes]: 5 params @ offset 0x0017ebed
    // USED → r0 = renderWithHooksAgain /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 285, Reg8: 0>
    r1[285] = renderWithHooksAgain /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 617>  # Function: [#617 bailoutHooks of 63 bytes]: 4 params @ offset 0x0017ec6c
    // USED → r0 = bailoutHooks /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 286, Reg8: 0>
    r1[286] = bailoutHooks /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 618>  # Function: [#618 resetHooksOnUnwind of 96 bytes]: 2 params @ offset 0x0017ecab
    // USED → r0 = resetHooksOnUnwind /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 287, Reg8: 0>
    r1[287] = resetHooksOnUnwind /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 619>  # Function: [#619 mountWorkInProgressHook of 59 bytes]: 1 params @ offset 0x0017ed0b
    // USED → r0 = mountWorkInProgressHook /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 288, Reg8: 0>
    r1[288] = mountWorkInProgressHook /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 620>  # Function: [#620 updateWorkInProgressHook of 259 bytes]: 1 params @ offset 0x0017ed46
    // USED → r0 = updateWorkInProgressHook /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 289, Reg8: 0>
    r1[289] = updateWorkInProgressHook /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 621>  # Function: [#621 useThenable of 131 bytes]: 2 params @ offset 0x0017ee49
    // USED → r0 = useThenable /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 290, Reg8: 0>
    r1[290] = useThenable /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 33, Reg8: 1, function_id: 622>  # Function: [#622 use of 120 bytes]: 2 params @ offset 0x0017eecc
    // USED → r33 = use /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 623>  # Function: [#623 basicStateReducer of 29 bytes]: 3 params @ offset 0x0017ef44
    // USED → r0 = basicStateReducer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 291, Reg8: 0>
    r1[291] = basicStateReducer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 624>  # Function: [#624 updateReducer of 610 bytes]: 2 params @ offset 0x0017ef61
    // USED → r34 = updateReducer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 292, Reg8: 34>
    r1[292] = updateReducer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 25, Reg8: 1, function_id: 625>  # Function: [#625 rerenderReducer of 188 bytes]: 2 params @ offset 0x0017f1c3
    // USED → r25 = rerenderReducer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 293, Reg8: 25>
    r1[293] = rerenderReducer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 22, Reg8: 1, function_id: 626>  # Function: [#626 updateSyncExternalStore of 310 bytes]: 3 params @ offset 0x0017f27f
    // USED → r22 = updateSyncExternalStore /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 627>  # Function: [#627 pushStoreConsistencyCheck of 135 bytes]: 4 params @ offset 0x0017f3b5
    // USED → r0 = pushStoreConsistencyCheck /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 294, Reg8: 0>
    r1[294] = pushStoreConsistencyCheck /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 628>  # Function: [#628 updateStoreInstance of 54 bytes]: 5 params @ offset 0x0017f43c
    // USED → r0 = updateStoreInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 295, Reg8: 0>
    r1[295] = updateStoreInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 629>  # Function: [#629 subscribeToStore of 33 bytes]: 4 params @ offset 0x0017f472
    // USED → r0 = subscribeToStore /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 296, Reg8: 0>
    r1[296] = subscribeToStore /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 631>  # Function: [#631 checkIfSnapshotChanged of 49 bytes]: 2 params @ offset 0x0017f4bc
    // USED → r0 = checkIfSnapshotChanged /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 297, Reg8: 0>
    r1[297] = checkIfSnapshotChanged /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 632>  # Function: [#632 forceStoreRerender of 41 bytes]: 2 params @ offset 0x0017f4ed
    // USED → r0 = forceStoreRerender /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 298, Reg8: 0>
    r1[298] = forceStoreRerender /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 633>  # Function: [#633 mountStateImpl of 97 bytes]: 2 params @ offset 0x0017f516
    // USED → r0 = mountStateImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 299, Reg8: 0>
    r1[299] = mountStateImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 634>  # Function: [#634 pushEffect of 137 bytes]: 5 params @ offset 0x0017f577
    // USED → r0 = pushEffect /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 300, Reg8: 0>
    r1[300] = pushEffect /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 24, Reg8: 1, function_id: 635>  # Function: [#635 updateRef of 21 bytes]: 1 params @ offset 0x0017f600
    // USED → r24 = updateRef /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 636>  # Function: [#636 mountEffectImpl of 96 bytes]: 5 params @ offset 0x0017f615
    // USED → r0 = mountEffectImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 301, Reg8: 0>
    r1[301] = mountEffectImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 637>  # Function: [#637 updateEffectImpl of 174 bytes]: 5 params @ offset 0x0017f675
    // USED → r0 = updateEffectImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 302, Reg8: 0>
    r1[302] = updateEffectImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 638>  # Function: [#638 mountEffect of 33 bytes]: 3 params @ offset 0x0017f723
    // USED → r35 = mountEffect /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 303, Reg8: 35>
    r1[303] = mountEffect /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 30, Reg8: 1, function_id: 639>  # Function: [#639 updateEffect of 33 bytes]: 3 params @ offset 0x0017f744
    // USED → r30 = updateEffect /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 304, Reg8: 30>
    r1[304] = updateEffect /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 28, Reg8: 1, function_id: 640>  # Function: [#640 updateInsertionEffect of 30 bytes]: 3 params @ offset 0x0017f765
    // USED → r28 = updateInsertionEffect /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 27, Reg8: 1, function_id: 641>  # Function: [#641 updateLayoutEffect of 33 bytes]: 3 params @ offset 0x0017f783
    // USED → r27 = updateLayoutEffect /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 642>  # Function: [#642 imperativeHandleEffect of 74 bytes]: 3 params @ offset 0x0017f7a4
    // USED → r0 = imperativeHandleEffect /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 305, Reg8: 0>
    r1[305] = imperativeHandleEffect /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 29, Reg8: 1, function_id: 645>  # Function: [#645 updateImperativeHandle of 90 bytes]: 4 params @ offset 0x0017f813
    // USED → r29 = updateImperativeHandle /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 646>  # Function: [#646 mountDebugValue of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r23 = mountDebugValue /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 32, Reg8: 1, function_id: 647>  # Function: [#647 updateCallback of 89 bytes]: 3 params @ offset 0x0017f86d
    // USED → r32 = updateCallback /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 26, Reg8: 1, function_id: 648>  # Function: [#648 updateMemo of 104 bytes]: 3 params @ offset 0x0017f8c6
    // USED → r26 = updateMemo /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 649>  # Function: [#649 mountDeferredValueImpl of 97 bytes]: 4 params @ offset 0x0017f92e
    // USED → r0 = mountDeferredValueImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 306, Reg8: 0>
    r1[306] = mountDeferredValueImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 650>  # Function: [#650 updateDeferredValueImpl of 156 bytes]: 5 params @ offset 0x0017f98f
    // USED → r0 = updateDeferredValueImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 307, Reg8: 0>
    r1[307] = updateDeferredValueImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 651>  # Function: [#651 startTransition of 206 bytes]: 6 params @ offset 0x0017fa2b
    // USED → r0 = startTransition /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 308, Reg8: 0>
    r1[308] = startTransition /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 652>  # Function: [#652 updateId of 21 bytes]: 1 params @ offset 0x0017f600
    // USED → r21 = updateId /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 653>  # Function: [#653 dispatchReducerAction of 135 bytes]: 4 params @ offset 0x0017faf9
    // USED → r0 = dispatchReducerAction /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 309, Reg8: 0>
    r1[309] = dispatchReducerAction /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 654>  # Function: [#654 dispatchSetState of 315 bytes]: 4 params @ offset 0x0017fb80
    // USED → r0 = dispatchSetState /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 310, Reg8: 0>
    r1[310] = dispatchSetState /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 655>  # Function: [#655 isRenderPhaseUpdate of 44 bytes]: 2 params @ offset 0x0017fcbb
    // USED → r0 = isRenderPhaseUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 311, Reg8: 0>
    r1[311] = isRenderPhaseUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 656>  # Function: [#656 enqueueRenderPhaseUpdate of 66 bytes]: 3 params @ offset 0x0017fce7
    // USED → r0 = enqueueRenderPhaseUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 312, Reg8: 0>
    r1[312] = enqueueRenderPhaseUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 657>  # Function: [#657 entangleTransitionUpdate of 69 bytes]: 4 params @ offset 0x0017fd29
    // USED → r0 = entangleTransitionUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 313, Reg8: 0>
    r1[313] = entangleTransitionUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 658>  # Function: [#658 resolveDefaultProps of 84 bytes]: 3 params @ offset 0x0017fd6e
    // USED → r0 = resolveDefaultProps /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 314, Reg8: 0>
    r1[314] = resolveDefaultProps /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 659>  # Function: [#659 applyDerivedStateFromProps of 84 bytes]: 5 params @ offset 0x0017fdc2
    // USED → r0 = applyDerivedStateFromProps /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 315, Reg8: 0>
    r1[315] = applyDerivedStateFromProps /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 660>  # Function: [#660 checkShouldComponentUpdate of 125 bytes]: 8 params @ offset 0x0017fe16
    // USED → r0 = checkShouldComponentUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 316, Reg8: 0>
    r1[316] = checkShouldComponentUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 661>  # Function: [#661 constructClassInstance of 141 bytes]: 4 params @ offset 0x0017fe93
    // USED → r0 = constructClassInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 317, Reg8: 0>
    r1[317] = constructClassInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 662>  # Function: [#662 callComponentWillReceiveProps of 108 bytes]: 5 params @ offset 0x0017ff20
    // USED → r0 = callComponentWillReceiveProps /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 318, Reg8: 0>
    r1[318] = callComponentWillReceiveProps /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 663>  # Function: [#663 mountClassInstance of 380 bytes]: 5 params @ offset 0x0017ff8c
    // USED → r0 = mountClassInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 319, Reg8: 0>
    r1[319] = mountClassInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 664>  # Function: [#664 createCapturedValueAtFiber of 125 bytes]: 3 params @ offset 0x00180108
    // USED → r0 = createCapturedValueAtFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 320, Reg8: 0>
    r1[320] = createCapturedValueAtFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 665>  # Function: [#665 createCapturedValueFromError of 74 bytes]: 4 params @ offset 0x00180185
    // USED → r0 = createCapturedValueFromError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 321, Reg8: 0>
    r1[321] = createCapturedValueFromError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 666>  # Function: [#666 logCapturedError of 194 bytes]: 3 params @ offset 0x001801cf
    // USED → r0 = logCapturedError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 322, Reg8: 0>
    r1[322] = logCapturedError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 668>  # Function: [#668 createRootErrorUpdate of 79 bytes]: 4 params @ offset 0x0018029a
    // USED → r0 = createRootErrorUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 323, Reg8: 0>
    r1[323] = createRootErrorUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 670>  # Function: [#670 createClassErrorUpdate of 142 bytes]: 4 params @ offset 0x0018031e
    // USED → r0 = createClassErrorUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 324, Reg8: 0>
    r1[324] = createClassErrorUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 674>  # Function: [#674 throwException of 1387 bytes]: 6 params @ offset 0x00180480
    // USED → r0 = throwException /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 325, Reg8: 0>
    r1[325] = throwException /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 675>  # Function: [#675 reconcileChildren of 81 bytes]: 5 params @ offset 0x001809eb
    // USED → r0 = reconcileChildren /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 326, Reg8: 0>
    r1[326] = reconcileChildren /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 676>  # Function: [#676 updateForwardRef of 149 bytes]: 6 params @ offset 0x00180a3c
    // USED → r0 = updateForwardRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 327, Reg8: 0>
    r1[327] = updateForwardRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 677>  # Function: [#677 updateMemoComponent of 333 bytes]: 6 params @ offset 0x00180ad1
    // USED → r0 = updateMemoComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 328, Reg8: 0>
    r1[328] = updateMemoComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 678>  # Function: [#678 updateSimpleMemoComponent of 183 bytes]: 6 params @ offset 0x00180c1e
    // USED → r0 = updateSimpleMemoComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 329, Reg8: 0>
    r1[329] = updateSimpleMemoComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 679>  # Function: [#679 updateOffscreenComponent of 463 bytes]: 4 params @ offset 0x00180cd5
    // USED → r0 = updateOffscreenComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 330, Reg8: 0>
    r1[330] = updateOffscreenComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 680>  # Function: [#680 deferHiddenOffscreenComponent of 52 bytes]: 4 params @ offset 0x00180ea4
    // USED → r0 = deferHiddenOffscreenComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 331, Reg8: 0>
    r1[331] = deferHiddenOffscreenComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 681>  # Function: [#681 markRef of 137 bytes]: 3 params @ offset 0x00180ed8
    // USED → r0 = markRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 332, Reg8: 0>
    r1[332] = markRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 682>  # Function: [#682 updateFunctionComponent of 140 bytes]: 6 params @ offset 0x00180f61
    // USED → r0 = updateFunctionComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 333, Reg8: 0>
    r1[333] = updateFunctionComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 683>  # Function: [#683 replayFunctionComponent of 144 bytes]: 7 params @ offset 0x00180fed
    // USED → r0 = replayFunctionComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 334, Reg8: 0>
    r1[334] = replayFunctionComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 684>  # Function: [#684 updateClassComponent of 1514 bytes]: 6 params @ offset 0x0018107d
    // USED → r0 = updateClassComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 335, Reg8: 0>
    r1[335] = updateClassComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 685>  # Function: [#685 finishClassComponent of 240 bytes]: 7 params @ offset 0x00181667
    // USED → r0 = finishClassComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 336, Reg8: 0>
    r1[336] = finishClassComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 686>  # Function: [#686 mountSuspenseOffscreenState of 19 bytes]: 2 params @ offset 0x00181757
    // USED → r0 = mountSuspenseOffscreenState /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 337, Reg8: 0>
    r1[337] = mountSuspenseOffscreenState /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 687>  # Function: [#687 getRemainingWorkInPrimaryTree of 49 bytes]: 4 params @ offset 0x0018176a
    // USED → r0 = getRemainingWorkInPrimaryTree /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 338, Reg8: 0>
    r1[338] = getRemainingWorkInPrimaryTree /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 688>  # Function: [#688 updateSuspenseComponent of 918 bytes]: 4 params @ offset 0x0018179b
    // USED → r0 = updateSuspenseComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 339, Reg8: 0>
    r1[339] = updateSuspenseComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 689>  # Function: [#689 mountSuspensePrimaryChildren of 60 bytes]: 3 params @ offset 0x00181b31
    // USED → r0 = mountSuspensePrimaryChildren /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 340, Reg8: 0>
    r1[340] = mountSuspensePrimaryChildren /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 690>  # Function: [#690 retrySuspenseComponentWithoutHydrating of 130 bytes]: 5 params @ offset 0x00181b6d
    // USED → r0 = retrySuspenseComponentWithoutHydrating /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 341, Reg8: 0>
    r1[341] = retrySuspenseComponentWithoutHydrating /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 691>  # Function: [#691 updateDehydratedSuspenseComponent of 978 bytes]: 9 params @ offset 0x00181bef
    // USED → r0 = updateDehydratedSuspenseComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 342, Reg8: 0>
    r1[342] = updateDehydratedSuspenseComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 692>  # Function: [#692 scheduleSuspenseWorkOnFiber of 74 bytes]: 4 params @ offset 0x00181fc1
    // USED → r0 = scheduleSuspenseWorkOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 343, Reg8: 0>
    r1[343] = scheduleSuspenseWorkOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 693>  # Function: [#693 initSuspenseListRenderState of 107 bytes]: 6 params @ offset 0x0018200b
    // USED → r0 = initSuspenseListRenderState /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 344, Reg8: 0>
    r1[344] = initSuspenseListRenderState /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 694>  # Function: [#694 updateSuspenseListComponent of 689 bytes]: 4 params @ offset 0x00182076
    // USED → r0 = updateSuspenseListComponent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 345, Reg8: 0>
    r1[345] = updateSuspenseListComponent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 695>  # Function: [#695 resetSuspendedCurrentOnMountInLegacyMode of 72 bytes]: 3 params @ offset 0x00182327
    // USED → r0 = resetSuspendedCurrentOnMountInLegacyMode /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 346, Reg8: 0>
    r1[346] = resetSuspendedCurrentOnMountInLegacyMode /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 696>  # Function: [#696 bailoutOnAlreadyFinishedWork of 240 bytes]: 4 params @ offset 0x0018236f
    // USED → r0 = bailoutOnAlreadyFinishedWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 347, Reg8: 0>
    r1[347] = bailoutOnAlreadyFinishedWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 697>  # Function: [#697 attemptEarlyBailoutIfNoScheduledUpdate of 555 bytes]: 4 params @ offset 0x0018245f
    // USED → r0 = attemptEarlyBailoutIfNoScheduledUpdate /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 348, Reg8: 0>
    r1[348] = attemptEarlyBailoutIfNoScheduledUpdate /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 698>  # Function: [#698 beginWork of 2529 bytes]: 4 params @ offset 0x0018268a
    // USED → r0 = beginWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 349, Reg8: 0>
    r1[349] = beginWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 699>  # Function: [#699 resetContextDependencies of 21 bytes]: 1 params @ offset 0x001830dc
    // USED → r0 = resetContextDependencies /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 350, Reg8: 0>
    r1[350] = resetContextDependencies /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 700>  # Function: [#700 popProvider of 38 bytes]: 2 params @ offset 0x001830f1
    // USED → r0 = popProvider /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 351, Reg8: 0>
    r1[351] = popProvider /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 701>  # Function: [#701 scheduleContextWorkOnParentPath of 132 bytes]: 4 params @ offset 0x00183117
    // USED → r0 = scheduleContextWorkOnParentPath /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 352, Reg8: 0>
    r1[352] = scheduleContextWorkOnParentPath /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 702>  # Function: [#702 prepareToReadContext of 80 bytes]: 3 params @ offset 0x0018319b
    // USED → r0 = prepareToReadContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 353, Reg8: 0>
    r1[353] = prepareToReadContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 31, Reg8: 1, function_id: 703>  # Function: [#703 readContext of 25 bytes]: 2 params @ offset 0x001831eb
    // USED → r31 = readContext /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 354, Reg8: 31>
    r1[354] = readContext /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 704>  # Function: [#704 readContextDuringReconciliation of 50 bytes]: 4 params @ offset 0x00183204
    // USED → r0 = readContextDuringReconciliation /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 355, Reg8: 0>
    r1[355] = readContextDuringReconciliation /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 705>  # Function: [#705 readContextForConsumer of 115 bytes]: 3 params @ offset 0x00183236
    // USED → r0 = readContextForConsumer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 356, Reg8: 0>
    r1[356] = readContextForConsumer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 706>  # Function: [#706 handleAsyncAction of 4 bytes]: 1 params @ offset 0x0016f98c
    // USED → r0 = handleAsyncAction /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 357, Reg8: 0>
    r1[357] = handleAsyncAction /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 707>  # Function: [#707 doesRequireClone of 114 bytes]: 3 params @ offset 0x001832a9
    // USED → r0 = doesRequireClone /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 358, Reg8: 0>
    r1[358] = doesRequireClone /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 708>  # Function: [#708 appendAllChildren of 396 bytes]: 5 params @ offset 0x0018331b
    // USED → r0 = appendAllChildren /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 359, Reg8: 0>
    r1[359] = appendAllChildren /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 709>  # Function: [#709 appendAllChildrenToContainer of 420 bytes]: 5 params @ offset 0x001834a7
    // USED → r0 = appendAllChildrenToContainer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 360, Reg8: 0>
    r1[360] = appendAllChildrenToContainer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 710>  # Function: [#710 updateHostContainer of 101 bytes]: 3 params @ offset 0x0018364b
    // USED → r0 = updateHostContainer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 361, Reg8: 0>
    r1[361] = updateHostContainer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 711>  # Function: [#711 scheduleRetryEffect of 100 bytes]: 3 params @ offset 0x001836b0
    // USED → r0 = scheduleRetryEffect /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 362, Reg8: 0>
    r1[362] = scheduleRetryEffect /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 712>  # Function: [#712 cutOffTailIfNeeded of 198 bytes]: 3 params @ offset 0x00183714
    // USED → r0 = cutOffTailIfNeeded /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 363, Reg8: 0>
    r1[363] = cutOffTailIfNeeded /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 713>  # Function: [#713 bubbleProperties of 232 bytes]: 2 params @ offset 0x001837da
    // USED → r0 = bubbleProperties /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 364, Reg8: 0>
    r1[364] = bubbleProperties /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 714>  # Function: [#714 completeWork of 2567 bytes]: 4 params @ offset 0x001838c2
    // USED → r0 = completeWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 365, Reg8: 0>
    r1[365] = completeWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 715>  # Function: [#715 unwindWork of 431 bytes]: 3 params @ offset 0x0018433c
    // USED → r0 = unwindWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 366, Reg8: 0>
    r1[366] = unwindWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 716>  # Function: [#716 unwindInterruptedWork of 165 bytes]: 3 params @ offset 0x00184558
    // USED → r0 = unwindInterruptedWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 367, Reg8: 0>
    r1[367] = unwindInterruptedWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 717>  # Function: [#717 safelyAttachRef of 145 bytes]: 3 params @ offset 0x00184664
    // USED → r0 = safelyAttachRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 368, Reg8: 0>
    r1[368] = safelyAttachRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 718>  # Function: [#718 safelyDetachRef of 194 bytes]: 3 params @ offset 0x001846f5
    // USED → r0 = safelyDetachRef /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 369, Reg8: 0>
    r1[369] = safelyDetachRef /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 719>  # Function: [#719 safelyCallDestroy of 49 bytes]: 4 params @ offset 0x001847b7
    // USED → r0 = safelyCallDestroy /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 370, Reg8: 0>
    r1[370] = safelyCallDestroy /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 720>  # Function: [#720 commitBeforeMutationEffects of 404 bytes]: 3 params @ offset 0x001847e8
    // USED → r0 = commitBeforeMutationEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 371, Reg8: 0>
    r1[371] = commitBeforeMutationEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 721>  # Function: [#721 commitHookEffectListUnmount of 136 bytes]: 4 params @ offset 0x001849ec
    // USED → r0 = commitHookEffectListUnmount /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 372, Reg8: 0>
    r1[372] = commitHookEffectListUnmount /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 722>  # Function: [#722 commitHookEffectListMount of 89 bytes]: 3 params @ offset 0x00184a74
    // USED → r0 = commitHookEffectListMount /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 373, Reg8: 0>
    r1[373] = commitHookEffectListMount /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 723>  # Function: [#723 commitHookLayoutEffects of 61 bytes]: 3 params @ offset 0x00184acd
    // USED → r0 = commitHookLayoutEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 374, Reg8: 0>
    r1[374] = commitHookLayoutEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 724>  # Function: [#724 commitClassCallbacks of 77 bytes]: 2 params @ offset 0x00184b0a
    // USED → r0 = commitClassCallbacks /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 375, Reg8: 0>
    r1[375] = commitClassCallbacks /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 725>  # Function: [#725 commitHostComponentMount of 53 bytes]: 2 params @ offset 0x00184b57
    // USED → r0 = commitHostComponentMount /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 376, Reg8: 0>
    r1[376] = commitHostComponentMount /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 726>  # Function: [#726 commitLayoutEffectOnFiber of 1037 bytes]: 4 params @ offset 0x00184b8c
    // USED → r0 = commitLayoutEffectOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 377, Reg8: 0>
    r1[377] = commitLayoutEffectOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 727>  # Function: [#727 detachFiberAfterEffects of 105 bytes]: 2 params @ offset 0x0018500c
    // USED → r0 = detachFiberAfterEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 378, Reg8: 0>
    r1[378] = detachFiberAfterEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 728>  # Function: [#728 recursivelyTraverseDeletionEffects of 48 bytes]: 4 params @ offset 0x00185075
    // USED → r0 = recursivelyTraverseDeletionEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 379, Reg8: 0>
    r1[379] = recursivelyTraverseDeletionEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 729>  # Function: [#729 commitDeletionEffectsOnFiber of 642 bytes]: 4 params @ offset 0x001850a5
    // USED → r0 = commitDeletionEffectsOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 380, Reg8: 0>
    r1[380] = commitDeletionEffectsOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 730>  # Function: [#730 getRetryCache of 171 bytes]: 2 params @ offset 0x00185398
    // USED → r0 = getRetryCache /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 381, Reg8: 0>
    r1[381] = getRetryCache /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 731>  # Function: [#731 attachSuspenseRetryListeners of 48 bytes]: 3 params @ offset 0x00185443
    // USED → r0 = attachSuspenseRetryListeners /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 382, Reg8: 0>
    r1[382] = attachSuspenseRetryListeners /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 733>  # Function: [#733 recursivelyTraverseMutationEffects of 231 bytes]: 3 params @ offset 0x001854c1
    // USED → r0 = recursivelyTraverseMutationEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 383, Reg8: 0>
    r1[383] = recursivelyTraverseMutationEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 734>  # Function: [#734 commitMutationEffectsOnFiber of 1258 bytes]: 3 params @ offset 0x001855a8
    // USED → r0 = commitMutationEffectsOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 384, Reg8: 0>
    r1[384] = commitMutationEffectsOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 735>  # Function: [#735 commitReconciliationEffects of 77 bytes]: 2 params @ offset 0x00185b04
    // USED → r0 = commitReconciliationEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 385, Reg8: 0>
    r1[385] = commitReconciliationEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 736>  # Function: [#736 recursivelyTraverseLayoutEffects of 71 bytes]: 3 params @ offset 0x00185b51
    // USED → r0 = recursivelyTraverseLayoutEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 386, Reg8: 0>
    r1[386] = recursivelyTraverseLayoutEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 737>  # Function: [#737 recursivelyTraverseDisappearLayoutEffects of 394 bytes]: 2 params @ offset 0x00185b98
    // USED → r0 = recursivelyTraverseDisappearLayoutEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 387, Reg8: 0>
    r1[387] = recursivelyTraverseDisappearLayoutEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 738>  # Function: [#738 recursivelyTraverseReappearLayoutEffects of 597 bytes]: 4 params @ offset 0x00185d22
    // USED → r0 = recursivelyTraverseReappearLayoutEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 388, Reg8: 0>
    r1[388] = recursivelyTraverseReappearLayoutEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 739>  # Function: [#739 commitHookPassiveMountEffects of 61 bytes]: 3 params @ offset 0x00184acd
    // USED → r0 = commitHookPassiveMountEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 389, Reg8: 0>
    r1[389] = commitHookPassiveMountEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 740>  # Function: [#740 recursivelyTraversePassiveMountEffects of 65 bytes]: 3 params @ offset 0x00185fe8
    // USED → r0 = recursivelyTraversePassiveMountEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 390, Reg8: 0>
    r1[390] = recursivelyTraversePassiveMountEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 741>  # Function: [#741 commitPassiveMountOnFiber of 356 bytes]: 3 params @ offset 0x00186029
    // USED → r0 = commitPassiveMountOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 391, Reg8: 0>
    r1[391] = commitPassiveMountOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 742>  # Function: [#742 recursivelyTraverseReconnectPassiveEffects of 305 bytes]: 3 params @ offset 0x0018618d
    // USED → r0 = recursivelyTraverseReconnectPassiveEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 392, Reg8: 0>
    r1[392] = recursivelyTraverseReconnectPassiveEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 743>  # Function: [#743 recursivelyAccumulateSuspenseyCommit of 59 bytes]: 2 params @ offset 0x001862be
    // USED → r0 = recursivelyAccumulateSuspenseyCommit /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 393, Reg8: 0>
    r1[393] = recursivelyAccumulateSuspenseyCommit /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 744>  # Function: [#744 accumulateSuspenseyCommitOnFiber of 252 bytes]: 2 params @ offset 0x001862f9
    // USED → r0 = accumulateSuspenseyCommitOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 394, Reg8: 0>
    r1[394] = accumulateSuspenseyCommitOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 745>  # Function: [#745 detachAlternateSiblings of 51 bytes]: 2 params @ offset 0x001863f5
    // USED → r0 = detachAlternateSiblings /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 395, Reg8: 0>
    r1[395] = detachAlternateSiblings /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 746>  # Function: [#746 recursivelyTraversePassiveUnmountEffects of 156 bytes]: 2 params @ offset 0x00186428
    // USED → r0 = recursivelyTraversePassiveUnmountEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 396, Reg8: 0>
    r1[396] = recursivelyTraversePassiveUnmountEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 747>  # Function: [#747 commitPassiveUnmountOnFiber of 235 bytes]: 2 params @ offset 0x001864c4
    // USED → r0 = commitPassiveUnmountOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 397, Reg8: 0>
    r1[397] = commitPassiveUnmountOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 748>  # Function: [#748 recursivelyTraverseDisconnectPassiveEffects of 287 bytes]: 2 params @ offset 0x001865af
    // USED → r0 = recursivelyTraverseDisconnectPassiveEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 398, Reg8: 0>
    r1[398] = recursivelyTraverseDisconnectPassiveEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 749>  # Function: [#749 commitPassiveUnmountEffectsInsideOfDeletedTree_begin of 214 bytes]: 3 params @ offset 0x001866ce
    // USED → r0 = commitPassiveUnmountEffectsInsideOfDeletedTree_begin /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 399, Reg8: 0>
    r1[399] = commitPassiveUnmountEffectsInsideOfDeletedTree_begin /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 750>  # Function: [#750 requestUpdateLane of 198 bytes]: 2 params @ offset 0x001867a4
    // USED → r0 = requestUpdateLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 400, Reg8: 0>
    r1[400] = requestUpdateLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 751>  # Function: [#751 requestDeferredLane of 84 bytes]: 1 params @ offset 0x0018686a
    // USED → r0 = requestDeferredLane /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 401, Reg8: 0>
    r1[401] = requestDeferredLane /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 752>  # Function: [#752 scheduleUpdateOnFiber of 284 bytes]: 4 params @ offset 0x001868be
    // USED → r0 = scheduleUpdateOnFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 402, Reg8: 0>
    r1[402] = scheduleUpdateOnFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 753>  # Function: [#753 performConcurrentWorkOnRoot of 766 bytes]: 3 params @ offset 0x001869da
    // USED → r0 = performConcurrentWorkOnRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 403, Reg8: 0>
    r1[403] = performConcurrentWorkOnRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 754>  # Function: [#754 recoverFromConcurrentError of 158 bytes]: 4 params @ offset 0x00186cd8
    // USED → r0 = recoverFromConcurrentError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 404, Reg8: 0>
    r1[404] = recoverFromConcurrentError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 755>  # Function: [#755 queueRecoverableErrors of 50 bytes]: 2 params @ offset 0x00186d76
    // USED → r0 = queueRecoverableErrors /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 405, Reg8: 0>
    r1[405] = queueRecoverableErrors /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 756>  # Function: [#756 commitRootWhenReady of 67 bytes]: 8 params @ offset 0x00186da8
    // USED → r0 = commitRootWhenReady /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 406, Reg8: 0>
    r1[406] = commitRootWhenReady /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 757>  # Function: [#757 isRenderConsistentWithExternalStores of 300 bytes]: 2 params @ offset 0x00186deb
    // USED → r0 = isRenderConsistentWithExternalStores /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 407, Reg8: 0>
    r1[407] = isRenderConsistentWithExternalStores /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 758>  # Function: [#758 markRootSuspended of 147 bytes]: 4 params @ offset 0x00186f17
    // USED → r0 = markRootSuspended /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 408, Reg8: 0>
    r1[408] = markRootSuspended /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 759>  # Function: [#759 resetWorkInProgressStack of 110 bytes]: 1 params @ offset 0x00186faa
    // USED → r0 = resetWorkInProgressStack /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 409, Reg8: 0>
    r1[409] = resetWorkInProgressStack /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 760>  # Function: [#760 prepareFreshStack of 289 bytes]: 3 params @ offset 0x00187018
    // USED → r0 = prepareFreshStack /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 410, Reg8: 0>
    r1[410] = prepareFreshStack /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 761>  # Function: [#761 handleThrow of 331 bytes]: 3 params @ offset 0x00187139
    // USED → r0 = handleThrow /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 411, Reg8: 0>
    r1[411] = handleThrow /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 762>  # Function: [#762 pushDispatcher of 38 bytes]: 1 params @ offset 0x00187284
    // USED → r0 = pushDispatcher /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 412, Reg8: 0>
    r1[412] = pushDispatcher /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 763>  # Function: [#763 renderDidSuspendDelayIfPossible of 91 bytes]: 1 params @ offset 0x001872aa
    // USED → r0 = renderDidSuspendDelayIfPossible /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 413, Reg8: 0>
    r1[413] = renderDidSuspendDelayIfPossible /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 764>  # Function: [#764 renderRootSync of 346 bytes]: 3 params @ offset 0x00187305
    // USED → r0 = renderRootSync /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 414, Reg8: 0>
    r1[414] = renderRootSync /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 765>  # Function: [#765 workLoopSync of 39 bytes]: 1 params @ offset 0x0018745f
    // USED → r0 = workLoopSync /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 415, Reg8: 0>
    r1[415] = workLoopSync /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 766>  # Function: [#766 renderRootConcurrent of 729 bytes]: 3 params @ offset 0x00187486
    // USED → r0 = renderRootConcurrent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 416, Reg8: 0>
    r1[416] = renderRootConcurrent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 768>  # Function: [#768 workLoopConcurrent of 104 bytes]: 1 params @ offset 0x0018779d
    // USED → r0 = workLoopConcurrent /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 417, Reg8: 0>
    r1[417] = workLoopConcurrent /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 769>  # Function: [#769 performUnitOfWork of 75 bytes]: 2 params @ offset 0x00187805
    // USED → r0 = performUnitOfWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 418, Reg8: 0>
    r1[418] = performUnitOfWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 770>  # Function: [#770 replaySuspendedUnitOfWork of 349 bytes]: 2 params @ offset 0x00187850
    // USED → r0 = replaySuspendedUnitOfWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 419, Reg8: 0>
    r1[419] = replaySuspendedUnitOfWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 771>  # Function: [#771 throwAndUnwindWorkLoop of 304 bytes]: 4 params @ offset 0x001879ad
    // USED → r0 = throwAndUnwindWorkLoop /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 420, Reg8: 0>
    r1[420] = throwAndUnwindWorkLoop /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 772>  # Function: [#772 completeUnitOfWork of 94 bytes]: 2 params @ offset 0x00187add
    // USED → r0 = completeUnitOfWork /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 421, Reg8: 0>
    r1[421] = completeUnitOfWork /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 773>  # Function: [#773 commitRoot of 113 bytes]: 6 params @ offset 0x00187b3b
    // USED → r0 = commitRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 422, Reg8: 0>
    r1[422] = commitRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 774>  # Function: [#774 commitRootImpl of 772 bytes]: 7 params @ offset 0x00187bac
    // USED → r0 = commitRootImpl /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 423, Reg8: 0>
    r1[423] = commitRootImpl /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 776>  # Function: [#776 flushPassiveEffects of 305 bytes]: 1 params @ offset 0x00187ec2
    // USED → r0 = flushPassiveEffects /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 424, Reg8: 0>
    r1[424] = flushPassiveEffects /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 777>  # Function: [#777 captureCommitPhaseErrorOnRoot of 78 bytes]: 4 params @ offset 0x00187ff3
    // USED → r0 = captureCommitPhaseErrorOnRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 425, Reg8: 0>
    r1[425] = captureCommitPhaseErrorOnRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 778>  # Function: [#778 captureCommitPhaseError of 252 bytes]: 4 params @ offset 0x00188041
    // USED → r0 = captureCommitPhaseError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 426, Reg8: 0>
    r1[426] = captureCommitPhaseError /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 779>  # Function: [#779 attachPingListener of 234 bytes]: 4 params @ offset 0x0018813d
    // USED → r0 = attachPingListener /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 427, Reg8: 0>
    r1[427] = attachPingListener /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 780>  # Function: [#780 pingSuspendedRoot of 237 bytes]: 4 params @ offset 0x00188227
    // USED → r0 = pingSuspendedRoot /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 428, Reg8: 0>
    r1[428] = pingSuspendedRoot /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 781>  # Function: [#781 retryTimedOutBoundary of 89 bytes]: 3 params @ offset 0x00188314
    // USED → r0 = retryTimedOutBoundary /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 429, Reg8: 0>
    r1[429] = retryTimedOutBoundary /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 782>  # Function: [#782 resolveRetryWakeable of 141 bytes]: 3 params @ offset 0x0018836d
    // USED → r0 = resolveRetryWakeable /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 430, Reg8: 0>
    r1[430] = resolveRetryWakeable /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 783>  # Function: [#783 scheduleCallback of 45 bytes]: 3 params @ offset 0x001883fa
    // USED → r0 = scheduleCallback /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 431, Reg8: 0>
    r1[431] = scheduleCallback /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 784>  # Function: [#784 FiberNode of 161 bytes]: 5 params @ offset 0x00188427
    // USED → r0 = FiberNode /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 432, Reg8: 0>
    r1[432] = FiberNode /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 785>  # Function: [#785 createFiber of 42 bytes]: 5 params @ offset 0x001884c8
    // USED → r0 = createFiber /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 433, Reg8: 0>
    r1[433] = createFiber /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 786>  # Function: [#786 shouldConstruct of 28 bytes]: 2 params @ offset 0x001884f2
    // USED → r0 = shouldConstruct /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 434, Reg8: 0>
    r1[434] = shouldConstruct /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 787>  # Function: [#787 resolveLazyComponentTag of 91 bytes]: 2 params @ offset 0x0018850e
    // USED → r0 = resolveLazyComponentTag /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 435, Reg8: 0>
    r1[435] = resolveLazyComponentTag /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 788>  # Function: [#788 createWorkInProgress of 316 bytes]: 3 params @ offset 0x00188569
    // USED → r0 = createWorkInProgress /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 436, Reg8: 0>
    r1[436] = createWorkInProgress /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 789>  # Function: [#789 resetWorkInProgress of 237 bytes]: 3 params @ offset 0x001886a5
    // USED → r0 = resetWorkInProgress /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 437, Reg8: 0>
    r1[437] = resetWorkInProgress /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 790>  # Function: [#790 createFiberFromTypeAndProps of 613 bytes]: 7 params @ offset 0x00188792
    // USED → r0 = createFiberFromTypeAndProps /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 438, Reg8: 0>
    r1[438] = createFiberFromTypeAndProps /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 791>  # Function: [#791 createFiberFromFragment of 37 bytes]: 5 params @ offset 0x001889f7
    // USED → r0 = createFiberFromFragment /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 439, Reg8: 0>
    r1[439] = createFiberFromFragment /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 792>  # Function: [#792 createFiberFromOffscreen of 89 bytes]: 5 params @ offset 0x00188a1c
    // USED → r0 = createFiberFromOffscreen /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 440, Reg8: 0>
    r1[440] = createFiberFromOffscreen /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 795>  # Function: [#795 createFiberFromText of 36 bytes]: 4 params @ offset 0x00188b67
    // USED → r0 = createFiberFromText /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 441, Reg8: 0>
    r1[441] = createFiberFromText /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 796>  # Function: [#796 createFiberFromPortal of 99 bytes]: 4 params @ offset 0x00188b8b
    // USED → r0 = createFiberFromPortal /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 442, Reg8: 0>
    r1[442] = createFiberFromPortal /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 797>  # Function: [#797 FiberRootNode of 250 bytes]: 7 params @ offset 0x00188bee
    // USED → r0 = FiberRootNode /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 443, Reg8: 0>
    r1[443] = FiberRootNode /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 798>  # Function: [#798 createPortal$1 of 90 bytes]: 4 params @ offset 0x00188ce8
    // USED → r0 = createPortal$1 /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 444, Reg8: 0>
    r1[444] = createPortal$1 /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 799>  # Function: [#799 findHostInstance of 138 bytes]: 2 params @ offset 0x00188d42
    // USED → r0 = findHostInstance /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 445, Reg8: 0>
    r1[445] = findHostInstance /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 800>  # Function: [#800 updateContainer of 144 bytes]: 5 params @ offset 0x00188dcc
    // USED → r0 = updateContainer /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 446, Reg8: 0>
    r1[446] = updateContainer /* Closure with env r1 = undefined */;
    // CODE → <CreateClosure>: <Reg8: 13, Reg8: 1, function_id: 801>  # Function: [#801 emptyFindFiberByHostInstance of 4 bytes]: 1 params @ offset 0x00188e5c
    r13 = emptyFindFiberByHostInstance /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 1, function_id: 802>  # Function: [#802 findNodeHandle of 199 bytes]: 2 params @ offset 0x00188e60
    // USED → r5 = findNodeHandle /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 1, function_id: 803>  # Function: [#803 getInspectorDataForInstance of 21 bytes]: 1 params @ offset 0x00188f27
    // USED → r4 = getInspectorDataForInstance /* Closure with env r1 = undefined */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 1, function_id: 804>  # Function: [#804 onRecoverableError of 25 bytes]: 2 params @ offset 0x00188f3c
    // USED → r0 = onRecoverableError /* Closure with env r1 = undefined */
    // CODE → <StoreToEnvironmentL>: <Reg8: 1, UInt16: 447, Reg8: 0>
    r1[447] = onRecoverableError /* Closure with env r1 = undefined */;
    // CODE → <LoadConstZero>: <Reg8: 10>
    // USED → r10 = 0
    // CODE → <GetByVal>: <Reg8: 0, Reg8: 19, Reg8: 10>
    // USED → r0 = r19[r10]
    // CODE → <Call2>: <Reg8: 0, Reg8: 18, Reg8: 2, Reg8: 0>
    r0 = param2(r19[r10])
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    r0 = 1
    // CODE → <GetByVal>: <Reg8: 0, Reg8: 19, Reg8: 0>
    // USED → r0 = r19[r0]
    // CODE → <Call2>: <Reg8: 14, Reg8: 18, Reg8: 2, Reg8: 0>
    // USED → r14 = param2(r19[r0])
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis
    // CODE → <TryGetById>: <Reg8: 11, Reg8: 0, UInt8: 1, string_id: 2>  # String: 'Array' (Identifier)
    // USED → r11 = globalThis.Array
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 11, UInt8: 2, string_id: 1>  # String: 'isArray' (Identifier)
    // USED → r11 = globalThis.Array.isArray
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 11>
    r1[2] = globalThis.Array.isArray;
    // CODE → <LoadConstFalse>: <Reg8: 12>
    // USED → r12 = false
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 12>
    r1[3] = false;
    // CODE → <LoadConstNull>: <Reg8: 11>
    // USED → r11 = null
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 11>
    r1[4] = null;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 11>
    r1[5] = null;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 11>
    r1[6] = null;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 11>
    r1[7] = null;
    // CODE → <TryGetById>: <Reg8: 37, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r37 = globalThis.Object
    // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 37, UInt8: 4, string_id: 62>  # String: 'assign' (Identifier)
    // USED → r41 = globalThis.Object.assign
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 8, Reg8: 41>
    r1[8] = globalThis.Object.assign;
    // CODE → <GetByIdShort>: <Reg8: 40, Reg8: 39, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r40 = SyntheticEvent /* Closure with env r1 = undefined */.prototype
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 805>  # Function: [#805 preventDefault of 82 bytes]: 1 params @ offset 0x00188f55
    // USED → r43 = preventDefault /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 16522>  # String: 'preventDefault' (Identifier)
    // USED → r37 = { preventDefault: preventDefault /* Closure with env r1 = undefined */ }
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 806>  # Function: [#806 stopPropagation of 74 bytes]: 1 params @ offset 0x00188fa7
    // USED → r43 = stopPropagation /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12808>  # String: 'stopPropagation' (Identifier)
    // USED → r37 = { preventDefault: preventDefault /* Closure with env r1 = undefined */, stopPropagation: stopPropagation /* Closure with env r1 = undefined */ }
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 807>  # Function: [#807 persist of 20 bytes]: 1 params @ offset 0x00188ff1
    // USED → r43 = persist /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 16540>  # String: 'persist' (Identifier)
    // USED → r37 = { preventDefault: preventDefault /* Closure with env r1 = undefined */, stopPropagation: stopPropagation /* Closure with env r1 = undefined */, persist: persist /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 23978>  # String: 'isPersistent' (Identifier)
    // USED → r37 = { preventDefault: preventDefault /* Closure with env r1 = undefined */, stopPropagation: stopPropagation /* Closure with env r1 = undefined */, persist: persist /* Closure with env r1 = undefined */, isPersistent: functionThatReturnsFalse /* Closure with env r1 = undefined */ }
    // CODE → <CreateClosure>: <Reg8: 42, Reg8: 1, function_id: 808>  # Function: [#808 destructor of 98 bytes]: 1 params @ offset 0x00189005
    // USED → r42 = destructor /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12543>  # String: 'destructor' (Identifier)
    // USED → r37 = { preventDefault: preventDefault /* Closure with env r1 = undefined */, stopPropagation: stopPropagation /* Closure with env r1 = undefined */, persist: persist /* Closure with env r1 = undefined */, isPersistent: functionThatReturnsFalse /* Closure with env r1 = undefined */, destructor: destructor /* Closure with env r1 = undefined */ }
    // CODE → <Call3>: <Reg8: 37, Reg8: 41, Reg8: 2, Reg8: 40, Reg8: 37>
    r37 = globalThis.Object.assign(SyntheticEvent /* Closure with env r1 = undefined */.prototype, { preventDefault: preventDefault /* Closure with env r1 = undefined */, stopPropagation: stopPropagation /* Closure with env r1 = undefined */, persist: persist /* Closure with env r1 = undefined */, isPersistent: functionThatReturnsFalse /* Closure with env r1 = undefined */, destructor: destructor /* Closure with env r1 = undefined */ })
    // CODE → <NewObjectWithBuffer>: <Reg8: 37, UInt16: 9, UInt16: 9, UInt16: 194, UInt16: 115>  # Object: {'type': null, 'target': null, 'currentTarget': null, 'eventPhase': null, 'bubbles': null, 'cancelable': null, 'timeStamp': null, 'defaultPrevented': null, 'isTrusted': null}
    // USED → r37 = { type: null, target: null, currentTarget: null, eventPhase: null, bubbles: null, cancelable: null, timeStamp: null, defaultPrevented: null, isTrusted: null }
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 809>  # Function: [#809 currentTarget of 4 bytes]: 1 params @ offset 0x00188e5c
    // USED → r40 = currentTarget /* Closure with env r1 = undefined */
    // CODE → <PutById>: <Reg8: 37, Reg8: 40, UInt8: 1, string_id: 11848>  # String: 'currentTarget' (Identifier)
    // USED → r37 = { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: null, defaultPrevented: null, isTrusted: null }
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 810>  # Function: [#810 timeStamp of 31 bytes]: 2 params @ offset 0x00189067
    // USED → r40 = timeStamp /* Closure with env r1 = undefined */
    // CODE → <PutById>: <Reg8: 37, Reg8: 40, UInt8: 2, string_id: 19393>  # String: 'timeStamp' (Identifier)
    // USED → r37 = { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }
    // CODE → <PutById>: <Reg8: 39, Reg8: 37, UInt8: 3, string_id: 18542>  # String: 'Interface' (Identifier)
    // USED → r39 = { Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null } }
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 811>  # Function: [#811  of 138 bytes]: 2 params @ offset 0x00189086
    // USED → r37 = function_811 /* Closure with env r1 = undefined */
    // CODE → <PutById>: <Reg8: 39, Reg8: 37, UInt8: 4, string_id: 14224>  # String: 'extend' (Identifier)
    // USED → r39 = { Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }, extend: function_811 /* Closure with env r1 = undefined */ }
    // CODE → <Call2>: <Reg8: 17, Reg8: 17, Reg8: 2, Reg8: 39>
    r17 = addEventPoolingTo /* Closure with env r1 = undefined */({ Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }, extend: function_811 /* Closure with env r1 = undefined */ })
    // CODE → <GetById>: <Reg8: 37, Reg8: 39, UInt8: 6, string_id: 14224>  # String: 'extend' (Identifier)
    // USED → r37 = { Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }, extend: function_811 /* Closure with env r1 = undefined */ }.extend
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <CreateClosure>: <Reg8: 40, Reg8: 1, function_id: 814>  # Function: [#814 touchHistory of 4 bytes]: 1 params @ offset 0x00188e5c
    // USED → r40 = touchHistory /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 40, string_id: 21539>  # String: 'touchHistory' (Identifier)
    // USED → r17 = { touchHistory: touchHistory /* Closure with env r1 = undefined */ }
    // CODE → <Call2>: <Reg8: 17, Reg8: 37, Reg8: 39, Reg8: 17>
    // USED → r17 = { Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }, extend: function_811 /* Closure with env r1 = undefined */ }.extend({ touchHistory: touchHistory /* Closure with env r1 = undefined */ })
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 17>
    r1[9] = { Interface: { type: null, target: null, currentTarget: currentTarget /* Closure with env r1 = undefined */, eventPhase: null, bubbles: null, cancelable: null, timeStamp: timeStamp /* Closure with env r1 = undefined */, defaultPrevented: null, isTrusted: null }, extend: function_811 /* Closure with env r1 = undefined */ }.extend({ touchHistory: touchHistory /* Closure with env r1 = undefined */ });
    // CODE → <NewArrayWithBuffer>: <Reg8: 42, UInt16: 1, UInt16: 1, UInt16: 40883>  # Array: ['topTouchStart']
    // USED → r42 = ["topTouchStart"]
    // CODE → <NewArrayWithBuffer>: <Reg8: 41, UInt16: 1, UInt16: 1, UInt16: 40892>  # Array: ['topTouchMove']
    // USED → r41 = ["topTouchMove"]
    // CODE → <NewArrayWithBuffer>: <Reg8: 40, UInt16: 2, UInt16: 2, UInt16: 40895>  # Array: ['topTouchCancel', 'topTouchEnd']
    // USED → r40 = ["topTouchCancel", "topTouchEnd"]
    // CODE → <NewArray>: <Reg8: 17, UInt16: 0>
    // USED → r17 = []
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 10, Reg8: 17>
    r1[10] = [];
    // CODE → <NewObjectWithBuffer>: <Reg8: 37, UInt16: 4, UInt16: 4, UInt16: 250, UInt16: 141>  # Object: {'touchBank': null, 'numberActiveTouches': 0, 'indexOfSingleActiveTouch': 4294967295, 'mostRecentTimeStamp': 0}
    // USED → r37 = { touchBank: null, numberActiveTouches: 0, indexOfSingleActiveTouch: 4294967295, mostRecentTimeStamp: 0 }
    // CODE → <PutById>: <Reg8: 37, Reg8: 17, UInt8: 5, string_id: 21537>  # String: 'touchBank' (Identifier)
    // USED → r37 = { touchBank: [], numberActiveTouches: 0, indexOfSingleActiveTouch: 4294967295, mostRecentTimeStamp: 0 }
    // CODE → <LoadConstInt>: <Reg8: 39, Imm32: -1>
    // USED → r39 = -1
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 11, Reg8: 37>
    r1[11] = { touchBank: [], numberActiveTouches: 0, indexOfSingleActiveTouch: 4294967295, mostRecentTimeStamp: 0 };
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 815>  # Function: [#815 instrument of 14 bytes]: 2 params @ offset 0x0018912e
    // USED → r43 = instrument /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 43, string_id: 23867>  # String: 'instrument' (Identifier)
    // USED → r17 = { instrument: instrument /* Closure with env r1 = undefined */ }
    // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 816>  # Function: [#816 recordTouchTrack of 328 bytes]: 3 params @ offset 0x0018913c
    // USED → r43 = recordTouchTrack /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 43, string_id: 14419>  # String: 'recordTouchTrack' (Identifier)
    // USED → r17 = { instrument: instrument /* Closure with env r1 = undefined */, recordTouchTrack: recordTouchTrack /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21539>  # String: 'touchHistory' (Identifier)
    // USED → r17 = { instrument: instrument /* Closure with env r1 = undefined */, recordTouchTrack: recordTouchTrack /* Closure with env r1 = undefined */, touchHistory: { touchBank: [], numberActiveTouches: 0, indexOfSingleActiveTouch: 4294967295, mostRecentTimeStamp: 0 } }
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 13, Reg8: 17>
    r1[13] = { instrument: instrument /* Closure with env r1 = undefined */, recordTouchTrack: recordTouchTrack /* Closure with env r1 = undefined */, touchHistory: { touchBank: [], numberActiveTouches: 0, indexOfSingleActiveTouch: 4294967295, mostRecentTimeStamp: 0 } };
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 14, Reg8: 11>
    r1[14] = null;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 15, Reg8: 10>
    r1[15] = 0;
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 159>  # Object: {'bubbled': 'onStartShouldSetResponder', 'captured': 'onStartShouldSetResponderCapture'}
    // USED → r43 = { bubbled: "onStartShouldSetResponder", captured: "onStartShouldSetResponderCapture" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onStartShouldSetResponderCapture" } }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 24007>  # String: 'startShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 164>  # Object: {'bubbled': 'onScrollShouldSetResponder', 'captured': 'onScrollShouldSetResponderCapture'}
    // USED → r43 = { bubbled: "onScrollShouldSetResponder", captured: "onScrollShouldSetResponderCapture" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", captured: "onScrollShouldSetResponderCapture" } }
    // CODE → <NewArrayWithBuffer>: <Reg8: 43, UInt16: 1, UInt16: 1, UInt16: 40881>  # Array: ['topScroll']
    // USED → r43 = ["topScroll"]
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", captured: "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 17673>  # String: 'scrollShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onStartShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", captured: "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 111>  # Object: {'bubbled': 'onSelectionChangeShouldSetResponder', 'captured': 'onSelectionChangeShouldSetResponderCapture'}
    // USED → r43 = { bubbled: "onSelectionChangeShouldSetResponder", captured: "onSelectionChangeShouldSetResponderCapture" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", captured: "onSelectionChangeShouldSetResponderCapture" } }
    // CODE → <NewArrayWithBuffer>: <Reg8: 43, UInt16: 1, UInt16: 1, UInt16: 40900>  # Array: ['topSelectionChange']
    // USED → r43 = ["topSelectionChange"]
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", captured: "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 22946>  # String: 'selectionChangeShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onScrollShouldSetResponderCapture" }, dependencies: ["topScroll"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", captured: "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <NewObjectWithBuffer>: <Reg8: 43, UInt16: 2, UInt16: 2, UInt16: 263, UInt16: 184>  # Object: {'bubbled': 'onMoveShouldSetResponder', 'captured': 'onMoveShouldSetResponderCapture'}
    // USED → r43 = { bubbled: "onMoveShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 43, string_id: 20186>  # String: 'phasedRegistrationNames' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", captured: "onMoveShouldSetResponderCapture" } }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 20089>  # String: 'moveShouldSetResponder' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onSelectionChangeShouldSetResponderCapture" }, dependencies: ["topSelectionChange"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 43, string_id: 22333>  # String: 'onResponderStart' (Identifier)
    // USED → r43 = "onResponderStart"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 43, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderStart" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 42, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderStart", dependencies: ["topTouchStart"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21573>  # String: 'responderStart' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", dependencies: ["topTouchStart"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 42, string_id: 22238>  # String: 'onResponderMove' (Identifier)
    // USED → r42 = "onResponderMove"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 42, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderMove" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderMove", dependencies: ["topTouchMove"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21199>  # String: 'responderMove' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchStart"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", dependencies: ["topTouchMove"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 41, string_id: 22198>  # String: 'onResponderEnd' (Identifier)
    // USED → r41 = "onResponderEnd"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 41, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderEnd" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 15364>  # String: 'responderEnd' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchMove"] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", dependencies: ["topTouchCancel", "topTouchEnd"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 41, string_id: 22319>  # String: 'onResponderRelease' (Identifier)
    // USED → r41 = "onResponderRelease"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 41, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderRelease" }
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 14449>  # String: 'responderRelease' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchCancel", scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", dependencies: ["topTouchCancel", "topTouchEnd"] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 19872>  # String: 'onResponderTerminationRequest' (Identifier)
    // USED → r40 = "onResponderTerminationRequest"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminationRequest" }
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = []
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminationRequest", dependencies: [] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21593>  # String: 'responderTerminationRequest' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: ["topTouchCancel", scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", dependencies: [] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22208>  # String: 'onResponderGrant' (Identifier)
    // USED → r40 = "onResponderGrant"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderGrant" }
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = []
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderGrant", dependencies: [] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 18117>  # String: 'responderGrant' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", dependencies: [] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22270>  # String: 'onResponderReject' (Identifier)
    // USED → r40 = "onResponderReject"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderReject" }
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = []
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderReject", dependencies: [] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21302>  # String: 'responderReject' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", dependencies: [] } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <LoadConstString>: <Reg8: 40, string_id: 22427>  # String: 'onResponderTerminate' (Identifier)
    // USED → r40 = "onResponderTerminate"
    // CODE → <PutNewOwnByIdShort>: <Reg8: 37, Reg8: 40, string_id: 204>  # String: 'registrationName' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminate" }
    // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
    // USED → r40 = []
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 40, string_id: 12219>  # String: 'dependencies' (Identifier)
    // USED → r37 = { registrationName: "onResponderTerminate", dependencies: [] }
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21588>  # String: 'responderTerminate' (Identifier)
    // USED → r17 = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } }
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 16, Reg8: 17>
    r1[16] = { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } };
    // CODE → <NewObject>: <Reg8: 40>
    // USED → r40 = {}
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 817>  # Function: [#817 _getResponder of 9 bytes]: 1 params @ offset 0x00189284
    // USED → r37 = _getResponder /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 37, string_id: 15697>  # String: '_getResponder' (Identifier)
    // USED → r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 14917>  # String: 'eventTypes' (Identifier)
    // USED → r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", dependencies: [] } } }
    // CODE → <CreateClosure>: <Reg8: 17, Reg8: 1, function_id: 818>  # Function: [#818 extractEvents of 1750 bytes]: 5 params @ offset 0x0018928d
    // USED → r17 = extractEvents /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 14577>  # String: 'extractEvents' (Identifier)
    // USED → r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 11, string_id: 21101>  # String: 'GlobalResponderHandler' (Identifier)
    // USED → r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null }
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <CreateClosure>: <Reg8: 37, Reg8: 1, function_id: 819>  # Function: [#819 injectGlobalResponderHandler of 20 bytes]: 2 params @ offset 0x00189963
    // USED → r37 = injectGlobalResponderHandler /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 17, Reg8: 37, string_id: 21100>  # String: 'injectGlobalResponderHandler' (Identifier)
    // USED → r17 = { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 17, string_id: 15132>  # String: 'injection' (Identifier)
    // USED → r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 17, Reg8: 40>
    r1[17] = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } };
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 18, Reg8: 11>
    r1[18] = null;
    // CODE → <NewObject>: <Reg8: 51>
    // USED → r51 = {}
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 19, Reg8: 51>
    r1[19] = {};
    // CODE → <NewArray>: <Reg8: 17, UInt16: 0>
    // USED → r17 = []
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 20, Reg8: 17>
    r1[20] = [];
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 21, Reg8: 17>
    r1[21] = {};
    // CODE → <NewObject>: <Reg8: 17>
    // USED → r17 = {}
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 22, Reg8: 17>
    r1[22] = {};
    // CODE → <LoadConstUInt8>: <Reg8: 17, UInt8: 2>
    // USED → r17 = 2
    // CODE → <GetByVal>: <Reg8: 37, Reg8: 19, Reg8: 17>
    // USED → r37 = r19[r17]
    // CODE → <Call2>: <Reg8: 37, Reg8: 18, Reg8: 2, Reg8: 37>
    // USED → r37 = param2(r19[r17])
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
    // USED → r37 = param2(r19[r17]).ReactNativeViewConfigRegistry
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 8, string_id: 22641>  # String: 'customBubblingEventTypes' (Identifier)
    // USED → r37 = param2(r19[r17]).ReactNativeViewConfigRegistry.customBubblingEventTypes
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 23, Reg8: 37>
    r1[23] = param2(r19[r17]).ReactNativeViewConfigRegistry.customBubblingEventTypes;
    // CODE → <GetByVal>: <Reg8: 37, Reg8: 19, Reg8: 17>
    // USED → r37 = r19[r17]
    // CODE → <Call2>: <Reg8: 37, Reg8: 18, Reg8: 2, Reg8: 37>
    // USED → r37 = param2(r19[r17])
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
    // USED → r37 = param2(r19[r17]).ReactNativeViewConfigRegistry
    // CODE → <GetById>: <Reg8: 37, Reg8: 37, UInt8: 9, string_id: 21940>  # String: 'customDirectEventTypes' (Identifier)
    // USED → r37 = param2(r19[r17]).ReactNativeViewConfigRegistry.customDirectEventTypes
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 24, Reg8: 37>
    r1[24] = param2(r19[r17]).ReactNativeViewConfigRegistry.customDirectEventTypes;
    // CODE → <TryGetById>: <Reg8: 37, Reg8: 0, UInt8: 1, string_id: 2>  # String: 'Array' (Identifier)
    // USED → r37 = globalThis.Array
    // CODE → <GetByIdShort>: <Reg8: 37, Reg8: 37, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r37 = globalThis.Array.prototype
    // CODE → <GetByIdShort>: <Reg8: 42, Reg8: 37, UInt8: 10, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r42 = globalThis.Array.prototype.slice
    // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 11, string_id: 91>  # String: 'call' (Identifier)
    // USED → r41 = globalThis.Array.prototype.slice.call
    // CODE → <NewArrayWithBuffer>: <Reg8: 37, UInt16: 2, UInt16: 2, UInt16: 40903>  # Array: ['ResponderEventPlugin', 'ReactNativeBridgeEventPlugin']
    // USED → r37 = ["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"]
    // CODE → <Call2>: <Reg8: 37, Reg8: 41, Reg8: 42, Reg8: 37>
    // USED → r37 = globalThis.Array.prototype.slice.call(["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"])
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 18, Reg8: 37>
    r1[18] = globalThis.Array.prototype.slice.call(["ResponderEventPlugin", "ReactNativeBridgeEventPlugin"]);
    // CODE → <Call1>: <Reg8: 37, Reg8: 16, Reg8: 2>
    r37 = recomputePluginOrdering /* Closure with env r1 = undefined */()
    // CODE → <NewObject>: <Reg8: 50>
    // USED → r50 = {}
    // CODE → <PutNewOwnById>: <Reg8: 50, Reg8: 40, string_id: 14576>  # String: 'ResponderEventPlugin' (Identifier)
    // USED → r50 = { ResponderEventPlugin: { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } } }
    // CODE → <NewObject>: <Reg8: 37>
    // USED → r37 = {}
    // CODE → <NewObject>: <Reg8: 41>
    // USED → r41 = {}
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 14917>  # String: 'eventTypes' (Identifier)
    // USED → r37 = { eventTypes: {} }
    // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 820>  # Function: [#820 extractEvents of 246 bytes]: 5 params @ offset 0x00189977
    // USED → r41 = extractEvents /* Closure with env r1 = undefined */
    // CODE → <PutNewOwnById>: <Reg8: 37, Reg8: 41, string_id: 14577>  # String: 'extractEvents' (Identifier)
    // USED → r37 = { eventTypes: {}, extractEvents: extractEvents /* Closure with env r1 = undefined */ }
    // CODE → <PutNewOwnById>: <Reg8: 50, Reg8: 37, string_id: 14569>  # String: 'ReactNativeBridgeEventPlugin' (Identifier)
    // USED → r50 = { ResponderEventPlugin: { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }, ReactNativeBridgeEventPlugin: { eventTypes: {}, extractEvents: extractEvents /* Closure with env r1 = undefined */ } }
    // CODE → <Mov>: <Reg8: 48, Reg8: 50>
    // USED → r48 = r50
    // CODE → <LoadConstTrue>: <Reg8: 37>
    // USED → r37 = true
    // CODE → <LoadConstFalse>: <Reg8: 43>
    r43 = false
    // CODE → <LoadConstUndefined>: <Reg8: 42>
    r42 = undefined
    // CODE → <LoadConstFalse>: <Reg8: 41>
    r41 = false
    // CODE → <GetPNameList>: <Reg8: 49, Reg8: 48, Reg8: 47, Reg8: 46>
    // USED → r49 = Object.keys(r50) /* for-in property list */
    // CODE → <JmpUndefined>: <Addr8: 115, Reg8: 49>  # Address: 00000ecd
    if (Object.keys(r50) /* for-in property list */ === undefined) {
        // CODE → <JmpFalse>: <Addr8: 7, Reg8: 41>  # Address: 00000ed4
        if (!r54) {
        } else {
            // CODE → <Call1>: <Reg8: 16, Reg8: 16, Reg8: 2>
            r16 = recomputePluginOrdering /* Closure with env r1 = undefined */()
        }
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {}
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 25, Reg8: 16>
        r1[25] = {};
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 26, Reg8: 11>
        r1[26] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 27, Reg8: 10>
        r1[27] = 0;
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {}
        // CODE → <PutNewOwnById>: <Reg8: 16, Reg8: 37, string_id: 24472>  # String: 'unsafelyIgnoreFunctions' (Identifier)
        // USED → r16 = { unsafelyIgnoreFunctions: true }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 28, Reg8: 16>
        r1[28] = { unsafelyIgnoreFunctions: true };
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 29, Reg8: 12>
        r1[29] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 30, Reg8: 11>
        r1[30] = null;
        // CODE → <GetById>: <Reg8: 14, Reg8: 14, UInt8: 14, string_id: 21563>  # String: '__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED' (Identifier)
        // USED → r14 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 31, Reg8: 11>
        r1[31] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 32, Reg8: 11>
        r1[32] = null;
        // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r16 = globalThis.Math
        // CODE → <GetById>: <Reg8: 16, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
        // USED → r16 = globalThis.Math.clz32
        // CODE → <JmpFalse>: <Addr8: 15, Reg8: 16>  # Address: 00000f1e
        if (!globalThis.Math.clz32) {
        } else {
            // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
            // USED → r16 = globalThis.Math
            // CODE → <GetById>: <Reg8: 9, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
            // USED → r9 = globalThis.Math.clz32
        }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 33, Reg8: 9>
        r1[33] = globalThis.Math.clz32;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 17, string_id: 171>  # String: 'log' (Identifier)
        // USED → r9 = globalThis.Math.log
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 34, Reg8: 9>
        r1[34] = globalThis.Math.log;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 18, string_id: 21154>  # String: 'LN2' (Identifier)
        // USED → r9 = globalThis.Math.LN2
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 35, Reg8: 9>
        r1[35] = globalThis.Math.LN2;
        // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 128>
        // USED → r9 = 128
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 36, Reg8: 9>
        r1[36] = 128;
        // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 4194304>
        // USED → r9 = 4194304
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 37, Reg8: 9>
        r1[37] = 4194304;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 38, Reg8: 10>
        r1[38] = 0;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 19, string_id: 24093>  # String: 'nativeFabricUIManager' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 20, string_id: 15507>  # String: 'createNode' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createNode
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 39, Reg8: 16>
        r1[39] = globalThis.nativeFabricUIManager.createNode;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 21, string_id: 22912>  # String: 'cloneNodeWithNewChildren' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 40, Reg8: 16>
        r1[40] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 22, string_id: 22913>  # String: 'cloneNodeWithNewChildrenAndProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 41, Reg8: 16>
        r1[41] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 23, string_id: 22914>  # String: 'cloneNodeWithNewProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewProps
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 42, Reg8: 16>
        r1[42] = globalThis.nativeFabricUIManager.cloneNodeWithNewProps;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 24, string_id: 23048>  # String: 'createChildSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createChildSet
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 43, Reg8: 16>
        r1[43] = globalThis.nativeFabricUIManager.createChildSet;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 25, string_id: 22565>  # String: 'appendChild' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChild
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 44, Reg8: 16>
        r1[44] = globalThis.nativeFabricUIManager.appendChild;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 22566>  # String: 'appendChildToSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChildToSet
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 45, Reg8: 16>
        r1[45] = globalThis.nativeFabricUIManager.appendChildToSet;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 27, string_id: 22962>  # String: 'completeRoot' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.completeRoot
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 46, Reg8: 16>
        r1[46] = globalThis.nativeFabricUIManager.completeRoot;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 28, string_id: 20376>  # String: 'registerEventHandler' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.registerEventHandler
        // CODE → <GetById>: <Reg8: 41, Reg8: 9, UInt8: 29, string_id: 24474>  # String: 'unstable_DiscreteEventPriority' (Identifier)
        // USED → r41 = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 47, Reg8: 41>
        r1[47] = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority;
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 30, string_id: 24484>  # String: 'unstable_getCurrentEventPriority' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 48, Reg8: 9>
        r1[48] = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority;
        // CODE → <GetByVal>: <Reg8: 9, Reg8: 19, Reg8: 17>
        // USED → r9 = r19[r17]
        // CODE → <Call2>: <Reg8: 9, Reg8: 18, Reg8: 2, Reg8: 9>
        // USED → r9 = param2(r19[r17])
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
        // USED → r9 = param2(r19[r17]).ReactNativeViewConfigRegistry
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 31, string_id: 137>  # String: 'get' (Identifier)
        // USED → r9 = param2(r19[r17]).ReactNativeViewConfigRegistry.get
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 49, Reg8: 9>
        r1[49] = param2(r19[r17]).ReactNativeViewConfigRegistry.get;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 50, Reg8: 17>
        r1[50] = 2;
        // CODE → <JmpFalse>: <Addr8: 13, Reg8: 16>  # Address: 00000fef
        if (!globalThis.nativeFabricUIManager.registerEventHandler) {
        } else {
            // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 510>  # Function: [#510 dispatchEvent of 81 bytes]: 4 params @ offset 0x0017ac46
            // USED → r9 = dispatchEvent /* Closure with env r1 = undefined */
            // CODE → <Call2>: <Reg8: 9, Reg8: 16, Reg8: 2, Reg8: 9>
            r9 = globalThis.nativeFabricUIManager.registerEventHandler(dispatchEvent /* Closure with env r1 = undefined */)
        }
        // CODE → <TryGetById>: <Reg8: 41, Reg8: 0, UInt8: 32, string_id: 214>  # String: 'setTimeout' (Identifier)
        // USED → r41 = globalThis.setTimeout
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 51, Reg8: 41>
        r1[51] = globalThis.setTimeout;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 33, string_id: 12162>  # String: 'clearTimeout' (Identifier)
        // USED → r9 = globalThis.clearTimeout
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 52, Reg8: 9>
        r1[52] = globalThis.clearTimeout;
        // CODE → <GetById>: <Reg8: 16, Reg8: 0, UInt8: 34, string_id: 15863>  # String: 'RN$enableMicrotasksInReact' (Identifier)
        // USED → r16 = globalThis.RN$enableMicrotasksInReact
        // CODE → <LoadConstString>: <Reg8: 9, string_id: 610>  # String: 'undefined' (String)
        // USED → r9 = "undefined"
        // CODE → <TypeOf>: <Reg8: 16, Reg8: 16>
        // USED → r16 = typeof globalThis.RN$enableMicrotasksInReact
        // CODE → <StrictNeq>: <Reg8: 16, Reg8: 9, Reg8: 16>
        // USED → r16 = "undefined" !== typeof globalThis.RN$enableMicrotasksInReact
        // CODE → <JmpFalse>: <Addr8: 15, Reg8: 16>  # Address: 00001023
        if (!"undefined" !== typeof globalThis.RN$enableMicrotasksInReact) {
        } else {
            // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 34, string_id: 15863>  # String: 'RN$enableMicrotasksInReact' (Identifier)
            // USED → r42 = globalThis.RN$enableMicrotasksInReact
            // CODE → <Not>: <Reg8: 42, Reg8: 42>
            // USED → r42 = !globalThis.RN$enableMicrotasksInReact
            // CODE → <Not>: <Reg8: 16, Reg8: 42>
            // USED → r16 = !!globalThis.RN$enableMicrotasksInReact
        }
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 53, Reg8: 16>
        r1[53] = !!globalThis.RN$enableMicrotasksInReact;
        // CODE → <GetById>: <Reg8: 42, Reg8: 0, UInt8: 35, string_id: 16391>  # String: 'queueMicrotask' (Identifier)
        // USED → r42 = globalThis.queueMicrotask
        // CODE → <LoadConstString>: <Reg8: 16, string_id: 12255>  # String: 'function' (Identifier)
        // USED → r16 = "function"
        // CODE → <TypeOf>: <Reg8: 42, Reg8: 42>
        // USED → r42 = typeof globalThis.queueMicrotask
        // CODE → <JStrictNotEqual>: <Addr8: 10, Reg8: 16, Reg8: 42>  # Address: 0000103e
        if ("function" !== typeof globalThis.queueMicrotask) { /* jump to label_4158 */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 54, Reg8: 41>
        r1[54] = globalThis.queueMicrotask;
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 821>  # Function: [#821 getFiberCurrentPropsFromNode$1 of 17 bytes]: 2 params @ offset 0x00189a6d
        // USED → r41 = getFiberCurrentPropsFromNode$1 /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 41>
        r1[5] = getFiberCurrentPropsFromNode$1 /* Closure with env r1 = undefined */;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 8>
        r1[6] = getInstanceFromNode /* Closure with env r1 = undefined */;
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 822>  # Function: [#822 getNodeFromInstance$1 of 49 bytes]: 2 params @ offset 0x00189a7e
        // USED → r41 = getNodeFromInstance$1 /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 41>
        r1[7] = getNodeFromInstance$1 /* Closure with env r1 = undefined */;
        // CODE → <GetById>: <Reg8: 42, Reg8: 40, UInt8: 36, string_id: 15132>  # String: 'injection' (Identifier)
        // USED → r42 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection
        // CODE → <GetById>: <Reg8: 41, Reg8: 42, UInt8: 37, string_id: 21100>  # String: 'injectGlobalResponderHandler' (Identifier)
        // USED → r41 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection.injectGlobalResponderHandler
        // CODE → <NewObject>: <Reg8: 40>
        // USED → r40 = {}
        // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 823>  # Function: [#823 onChange of 122 bytes]: 4 params @ offset 0x00189aaf
        // USED → r43 = onChange /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 43, string_id: 15401>  # String: 'onChange' (Identifier)
        // USED → r40 = { onChange: onChange /* Closure with env r1 = undefined */ }
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection.injectGlobalResponderHandler({ onChange: onChange /* Closure with env r1 = undefined */ })
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 3815>  # String: 'react.element' (String)
        // USED → r40 = "react.element"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.element")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 55, Reg8: 40>
        r1[55] = globalThis.Symbol.for("react.element");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5553>  # String: 'react.portal' (String)
        // USED → r40 = "react.portal"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.portal")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 56, Reg8: 40>
        r1[56] = globalThis.Symbol.for("react.portal");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5930>  # String: 'react.fragment' (String)
        // USED → r40 = "react.fragment"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.fragment")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 57, Reg8: 40>
        r1[57] = globalThis.Symbol.for("react.fragment");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6410>  # String: 'react.strict_mode' (String)
        // USED → r40 = "react.strict_mode"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.strict_mode")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 58, Reg8: 40>
        r1[58] = globalThis.Symbol.for("react.strict_mode");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5628>  # String: 'react.profiler' (String)
        // USED → r40 = "react.profiler"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.profiler")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 59, Reg8: 40>
        r1[59] = globalThis.Symbol.for("react.profiler");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2499>  # String: 'react.provider' (String)
        // USED → r40 = "react.provider"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.provider")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 60, Reg8: 40>
        r1[60] = globalThis.Symbol.for("react.provider");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8244>  # String: 'react.consumer' (String)
        // USED → r40 = "react.consumer"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.consumer")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 61, Reg8: 40>
        r1[61] = globalThis.Symbol.for("react.consumer");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4944>  # String: 'react.context' (String)
        // USED → r40 = "react.context"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.context")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 62, Reg8: 40>
        r1[62] = globalThis.Symbol.for("react.context");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 7930>  # String: 'react.forward_ref' (String)
        // USED → r40 = "react.forward_ref"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.forward_ref")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 63, Reg8: 40>
        r1[63] = globalThis.Symbol.for("react.forward_ref");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6421>  # String: 'react.suspense' (String)
        // USED → r40 = "react.suspense"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 64, Reg8: 40>
        r1[64] = globalThis.Symbol.for("react.suspense");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6422>  # String: 'react.suspense_list' (String)
        // USED → r40 = "react.suspense_list"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense_list")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 65, Reg8: 40>
        r1[65] = globalThis.Symbol.for("react.suspense_list");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 410>  # String: 'react.memo' (String)
        // USED → r40 = "react.memo"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.memo")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 66, Reg8: 40>
        r1[66] = globalThis.Symbol.for("react.memo");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10762>  # String: 'react.lazy' (String)
        // USED → r40 = "react.lazy"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.lazy")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 67, Reg8: 40>
        r1[67] = globalThis.Symbol.for("react.lazy");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6222>  # String: 'react.scope' (String)
        // USED → r40 = "react.scope"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.scope")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6531>  # String: 'react.debug_trace_mode' (String)
        // USED → r40 = "react.debug_trace_mode"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.debug_trace_mode")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5577>  # String: 'react.offscreen' (String)
        // USED → r40 = "react.offscreen"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.offscreen")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 68, Reg8: 40>
        r1[68] = globalThis.Symbol.for("react.offscreen");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4905>  # String: 'react.legacy_hidden' (String)
        // USED → r40 = "react.legacy_hidden"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.legacy_hidden")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2166>  # String: 'react.cache' (String)
        // USED → r40 = "react.cache"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.cache")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8982>  # String: 'react.tracing_marker' (String)
        // USED → r40 = "react.tracing_marker"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.tracing_marker")
        // CODE → <TryGetById>: <Reg8: 40, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r40 = globalThis.Symbol
        // CODE → <GetById>: <Reg8: 40, Reg8: 40, UInt8: 40, string_id: 13658>  # String: 'iterator' (Identifier)
        // USED → r40 = globalThis.Symbol.iterator
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 69, Reg8: 40>
        r1[69] = globalThis.Symbol.iterator;
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10511>  # String: 'react.client.reference' (String)
        // USED → r40 = "react.client.reference"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.client.reference")
        // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
        // USED → r40 = []
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 70, Reg8: 40>
        r1[70] = [];
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 71, Reg8: 39>
        r1[71] = -1;
        // CODE → <NewObject>: <Reg8: 39>
        // USED → r39 = {}
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 72, Reg8: 39>
        r1[72] = {};
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r39 = globalThis.Object
        // CODE → <GetById>: <Reg8: 39, Reg8: 39, UInt8: 41, string_id: 11558>  # String: 'is' (Identifier)
        // USED → r39 = globalThis.Object.is
        // CODE → <TypeOf>: <Reg8: 39, Reg8: 39>
        // USED → r39 = typeof globalThis.Object.is
        // CODE → <JStrictNotEqual>: <Addr8: 16, Reg8: 16, Reg8: 39>  # Address: 0000127e
        if ("function" !== typeof globalThis.Object.is) { /* jump to label_4734 */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 73, Reg8: 38>
        r1[73] = globalThis.Object.is;
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 74, Reg8: 38>
        r1[74] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 75, Reg8: 38>
        r1[75] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 76, Reg8: 38>
        r1[76] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 77, Reg8: 11>
        r1[77] = null;
        // CODE → <NewArray>: <Reg8: 38, UInt16: 0>
        // USED → r38 = []
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 78, Reg8: 38>
        r1[78] = [];
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 79, Reg8: 10>
        r1[79] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 80, Reg8: 10>
        r1[80] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 81, Reg8: 11>
        r1[81] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 82, Reg8: 11>
        r1[82] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 83, Reg8: 12>
        r1[83] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 84, Reg8: 12>
        r1[84] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 85, Reg8: 12>
        r1[85] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 86, Reg8: 10>
        r1[86] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 87, Reg8: 12>
        r1[87] = false;
        // CODE → <TryGetById>: <Reg8: 38, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r38 = globalThis.Object
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r38 = globalThis.Object.prototype
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
        // USED → r38 = globalThis.Object.prototype.hasOwnProperty
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 88, Reg8: 38>
        r1[88] = globalThis.Object.prototype.hasOwnProperty;
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 3625>  # String: "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\n\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`" (String)
        // USED → r38 = "str_3625"
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error("str_3625")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 89, Reg8: 38>
        r1[89] = globalThis.Error("str_3625");
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 6775>  # String: "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React." (String)
        // USED → r38 = "str_6775"
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error("str_6775")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 90, Reg8: 38>
        r1[90] = globalThis.Error("str_6775");
        // CODE → <NewObject>: <Reg8: 38>
        // USED → r38 = {}
        // CODE → <CreateClosure>: <Reg8: 39, Reg8: 1, function_id: 824>  # Function: [#824 then of 4 bytes]: 1 params @ offset 0x0016f98c
        // USED → r39 = then /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 38, Reg8: 39, string_id: 231>  # String: 'then' (Identifier)
        // USED → r38 = { then: then /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 91, Reg8: 38>
        r1[91] = { then: then /* Closure with env r1 = undefined */ };
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 92, Reg8: 11>
        r1[92] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 93, Reg8: 11>
        r1[93] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 94, Reg8: 10>
        r1[94] = 0;
        // CODE → <Call2>: <Reg8: 37, Reg8: 20, Reg8: 2, Reg8: 37>
        // USED → r37 = createChildReconciler /* Closure with env r1 = undefined */(true)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 95, Reg8: 37>
        r1[95] = createChildReconciler /* Closure with env r1 = undefined */(true);
        // CODE → <Call2>: <Reg8: 20, Reg8: 20, Reg8: 2, Reg8: 12>
        // USED → r20 = createChildReconciler /* Closure with env r1 = undefined */(false)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 96, Reg8: 20>
        r1[96] = createChildReconciler /* Closure with env r1 = undefined */(false);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 97, Reg8: 20>
        r1[97] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(0)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 98, Reg8: 20>
        r1[98] = createCursor /* Closure with env r1 = undefined */(0);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 99, Reg8: 20>
        r1[99] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 100, Reg8: 11>
        r1[100] = null;
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(0)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 101, Reg8: 20>
        r1[101] = createCursor /* Closure with env r1 = undefined */(0);
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 42, string_id: 21353>  # String: 'ReactCurrentDispatcher' (Identifier)
        // USED → r20 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 102, Reg8: 20>
        r1[102] = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher;
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 43, string_id: 17455>  # String: 'ReactCurrentBatchConfig' (Identifier)
        // USED → r20 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 103, Reg8: 20>
        r1[103] = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 104, Reg8: 10>
        r1[104] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 105, Reg8: 11>
        r1[105] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 106, Reg8: 11>
        r1[106] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 107, Reg8: 11>
        r1[107] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 108, Reg8: 12>
        r1[108] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 109, Reg8: 12>
        r1[109] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 110, Reg8: 12>
        r1[110] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 111, Reg8: 10>
        r1[111] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 112, Reg8: 11>
        r1[112] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 113, Reg8: 10>
        r1[113] = 0;
        // CODE → <CreateClosure>: <Reg8: 20, Reg8: 1, function_id: 825>  # Function: [#825 createFunctionComponentUpdateQueue of 12 bytes]: 1 params @ offset 0x00189b29
        // USED → r20 = createFunctionComponentUpdateQueue /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 114, Reg8: 20>
        r1[114] = createFunctionComponentUpdateQueue /* Closure with env r1 = undefined */;
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */, useId: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 115, Reg8: 20>
        r1[115] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */, useId: throwInvalidHookError /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 36, Reg8: 1, function_id: 826>  # Function: [#826 useCallback of 49 bytes]: 3 params @ offset 0x00189b35
        // USED → r36 = useCallback /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 827>  # Function: [#827 useImperativeHandle of 90 bytes]: 4 params @ offset 0x00189b66
        // USED → r35 = useImperativeHandle /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 828>  # Function: [#828 useLayoutEffect of 33 bytes]: 3 params @ offset 0x00189bc0
        // USED → r35 = useLayoutEffect /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 829>  # Function: [#829 useInsertionEffect of 30 bytes]: 3 params @ offset 0x00189be1
        // USED → r35 = useInsertionEffect /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 830>  # Function: [#830 useMemo of 64 bytes]: 3 params @ offset 0x00189bff
        // USED → r35 = useMemo /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 831>  # Function: [#831 useReducer of 139 bytes]: 4 params @ offset 0x00189c3f
        // USED → r35 = useReducer /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 832>  # Function: [#832 useRef of 31 bytes]: 2 params @ offset 0x00189cca
        // USED → r35 = useRef /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 833>  # Function: [#833 useState of 72 bytes]: 2 params @ offset 0x00189ce9
        // USED → r35 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 834>  # Function: [#834 useDeferredValue of 34 bytes]: 3 params @ offset 0x00189d31
        // USED → r35 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 835>  # Function: [#835 useTransition of 79 bytes]: 1 params @ offset 0x00189d53
        // USED → r35 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 836>  # Function: [#836 useSyncExternalStore of 239 bytes]: 3 params @ offset 0x00189da2
        // USED → r35 = useSyncExternalStore /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 837>  # Function: [#837 useId of 83 bytes]: 1 params @ offset 0x00189e91
        // USED → r35 = useId /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */, useId: useId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 116, Reg8: 20>
        r1[116] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */, useId: useId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 838>  # Function: [#838 useState of 22 bytes]: 1 params @ offset 0x00189ee4
        // USED → r34 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 34, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 839>  # Function: [#839 useDeferredValue of 42 bytes]: 3 params @ offset 0x00189efa
        // USED → r34 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 840>  # Function: [#840 useTransition of 78 bytes]: 1 params @ offset 0x00189f24
        // USED → r34 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 117, Reg8: 20>
        r1[117] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 25, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 24, Reg8: 1, function_id: 841>  # Function: [#841 useState of 22 bytes]: 1 params @ offset 0x00189f72
        // USED → r24 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 842>  # Function: [#842 useDeferredValue of 75 bytes]: 3 params @ offset 0x00189f88
        // USED → r23 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 843>  # Function: [#843 useTransition of 78 bytes]: 1 params @ offset 0x00189fd3
        // USED → r23 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 118, Reg8: 20>
        r1[118] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 844>  # Function: [#844 isMounted of 34 bytes]: 2 params @ offset 0x0018a021
        // USED → r21 = isMounted /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 16785>  # String: 'isMounted' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 845>  # Function: [#845 enqueueSetState of 109 bytes]: 4 params @ offset 0x0018a043
        // USED → r21 = enqueueSetState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22773>  # String: 'enqueueSetState' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 846>  # Function: [#846 enqueueReplaceState of 118 bytes]: 4 params @ offset 0x0018a0b0
        // USED → r21 = enqueueReplaceState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22685>  # String: 'enqueueReplaceState' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 847>  # Function: [#847 enqueueForceUpdate of 109 bytes]: 3 params @ offset 0x0018a126
        // USED → r21 = enqueueForceUpdate /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 17151>  # String: 'enqueueForceUpdate' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */, enqueueForceUpdate: enqueueForceUpdate /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 119, Reg8: 20>
        r1[119] = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */, enqueueForceUpdate: enqueueForceUpdate /* Closure with env r1 = undefined */ };
        // CODE → <TryGetById>: <Reg8: 20, Reg8: 0, UInt8: 44, string_id: 24>  # String: 'WeakMap' (Identifier)
        // USED → r20 = globalThis.WeakMap
        // CODE → <GetByIdShort>: <Reg8: 21, Reg8: 20, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r21 = globalThis.WeakMap.prototype
        // CODE → <CreateThis>: <Reg8: 21, Reg8: 21, Reg8: 20>
        r21 = createThis(prototype=globalThis.WeakMap.prototype, constructor=globalThis.WeakMap)
        // CODE → <Mov>: <Reg8: 57, Reg8: 21>
        r57 = r21
        // CODE → <Construct>: <Reg8: 20, Reg8: 20, UInt8: 1>
        r20 = new globalThis.WeakMap(param7)
        // CODE → <SelectObject>: <Reg8: 20, Reg8: 21, Reg8: 20>
        // USED → r20 = r21[r20]
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 120, Reg8: 20>
        r1[120] = r21[r20];
        // CODE → <GetByVal>: <Reg8: 17, Reg8: 19, Reg8: 17>
        // USED → r17 = r19[r17]
        // CODE → <Call2>: <Reg8: 17, Reg8: 18, Reg8: 2, Reg8: 17>
        // USED → r17 = param2(r19[r17])
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 45, string_id: 14613>  # String: 'ReactFiberErrorDialog' (Identifier)
        // USED → r17 = param2(r19[r17]).ReactFiberErrorDialog
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 46, string_id: 14615>  # String: 'showErrorDialog' (Identifier)
        // USED → r17 = param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog
        // CODE → <TypeOf>: <Reg8: 17, Reg8: 17>
        // USED → r17 = typeof param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog
        // CODE → <JStrictNotEqualLong>: <Addr32: 774, Reg8: 16, Reg8: 17>  # Address: 000018b9
        if ("function" !== typeof param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog) { /* jump to label_6329 */ }
        // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r1 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4985>  # String: 'Expected ReactFiberErrorDialog.showErrorDialog to be a function.' (String)
        // USED → r0 = "Expected ReactFiberErrorDialog.showErrorDialog to be a function."
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        // USED → r0 = globalThis.Error("Expected ReactFiberErrorDialog.showErrorDialog to be a function.")
        // CODE → <Throw>: <Reg8: 0>
        r0 = throw globalThis.Error("Expected ReactFiberErrorDialog.showErrorDialog to be a function.")
    } else {
        while (Object.keys(r50) /* for-in property list */.next() /* for-in step */ === undefined) {
            // CODE → <Mov>: <Reg8: 44, Reg8: 45>
            // USED → r44 = r45
            // CODE → <GetByIdShort>: <Reg8: 52, Reg8: 50, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
            // USED → r52 = { ResponderEventPlugin: { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }, ReactNativeBridgeEventPlugin: { eventTypes: {}, extractEvents: extractEvents /* Closure with env r1 = undefined */ } }.hasOwnProperty
            // CODE → <Call2>: <Reg8: 52, Reg8: 52, Reg8: 50, Reg8: 44>
            // USED → r52 = { ResponderEventPlugin: { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }, ReactNativeBridgeEventPlugin: { eventTypes: {}, extractEvents: extractEvents /* Closure with env r1 = undefined */ } }.hasOwnProperty(r45)
            // CODE → <Mov>: <Reg8: 43, Reg8: 54>
            r43 = r54
            // CODE → <JmpFalse>: <Addr8: -31, Reg8: 52>  # Address: 00000e5d
            if (!{ ResponderEventPlugin: { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }, ReactNativeBridgeEventPlugin: { eventTypes: {}, extractEvents: extractEvents /* Closure with env r1 = undefined */ } }.hasOwnProperty(r45)) {
                continue;
            } else {
                // CODE → <GetByVal>: <Reg8: 52, Reg8: 50, Reg8: 44>
                // USED → r52 = r50[r44]
                // CODE → <GetByIdShort>: <Reg8: 53, Reg8: 51, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
                // USED → r53 = {}.hasOwnProperty
                // CODE → <Call2>: <Reg8: 53, Reg8: 53, Reg8: 51, Reg8: 44>
                // USED → r53 = {}.hasOwnProperty(r45)
                // CODE → <JmpFalse>: <Addr8: 17, Reg8: 53>  # Address: 00000e9e
                if (!{}.hasOwnProperty(r45)) {
                    // CODE → <GetByVal>: <Reg8: 53, Reg8: 51, Reg8: 44>
                    // USED → r53 = r51[r44]
                    // CODE → <JmpTrue>: <Addr8: 14, Reg8: 53>  # Address: 00000eb0
                    if (r51[r44]) {
                        break;
                    } else {
                        // CODE → <PutByVal>: <Reg8: 51, Reg8: 44, Reg8: 52>
                        {}[r45] = r50[r44]
                        // CODE → <LoadConstTrue>: <Reg8: 43>
                        r43 = true
                        // CODE → <Mov>: <Reg8: 42, Reg8: 52>
                        r42 = r52
                        // CODE → <Jmp>: <Addr8: -81>  # Address: 00000e5d
                        continue;
                    }
                } else {
                    // CODE → <GetByVal>: <Reg8: 53, Reg8: 51, Reg8: 44>
                    // USED → r53 = r51[r44]
                    // CODE → <Mov>: <Reg8: 43, Reg8: 54>
                    r43 = r54
                    // CODE → <Mov>: <Reg8: 42, Reg8: 52>
                    r42 = r52
                    // CODE → <JStrictEqual>: <Addr8: -61, Reg8: 53, Reg8: 52>  # Address: 00000e5d
                    if (r51[r44] === r50[r44]) { /* jump to label_3677 */ }
                    continue;
                }
            }
        }
        // CODE → <JmpFalse>: <Addr8: 7, Reg8: 41>  # Address: 00000ed4
        if (!r54) {
        } else {
            // CODE → <Call1>: <Reg8: 16, Reg8: 16, Reg8: 2>
            r16 = recomputePluginOrdering /* Closure with env r1 = undefined */()
        }
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {}
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 25, Reg8: 16>
        r1[25] = {};
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 26, Reg8: 11>
        r1[26] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 27, Reg8: 10>
        r1[27] = 0;
        // CODE → <NewObject>: <Reg8: 16>
        // USED → r16 = {}
        // CODE → <PutNewOwnById>: <Reg8: 16, Reg8: 37, string_id: 24472>  # String: 'unsafelyIgnoreFunctions' (Identifier)
        // USED → r16 = { unsafelyIgnoreFunctions: true }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 28, Reg8: 16>
        r1[28] = { unsafelyIgnoreFunctions: true };
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 29, Reg8: 12>
        r1[29] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 30, Reg8: 11>
        r1[30] = null;
        // CODE → <GetById>: <Reg8: 14, Reg8: 14, UInt8: 14, string_id: 21563>  # String: '__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED' (Identifier)
        // USED → r14 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 31, Reg8: 11>
        r1[31] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 32, Reg8: 11>
        r1[32] = null;
        // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r16 = globalThis.Math
        // CODE → <GetById>: <Reg8: 16, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
        // USED → r16 = globalThis.Math.clz32
        // CODE → <JmpFalse>: <Addr8: 15, Reg8: 16>  # Address: 00000f1e
        if (!globalThis.Math.clz32) {
        } else {
            // CODE → <TryGetById>: <Reg8: 16, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
            // USED → r16 = globalThis.Math
            // CODE → <GetById>: <Reg8: 9, Reg8: 16, UInt8: 16, string_id: 12352>  # String: 'clz32' (Identifier)
            // USED → r9 = globalThis.Math.clz32
        }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 33, Reg8: 9>
        r1[33] = globalThis.Math.clz32;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 17, string_id: 171>  # String: 'log' (Identifier)
        // USED → r9 = globalThis.Math.log
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 34, Reg8: 9>
        r1[34] = globalThis.Math.log;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 15, string_id: 33>  # String: 'Math' (Identifier)
        // USED → r9 = globalThis.Math
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 18, string_id: 21154>  # String: 'LN2' (Identifier)
        // USED → r9 = globalThis.Math.LN2
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 35, Reg8: 9>
        r1[35] = globalThis.Math.LN2;
        // CODE → <LoadConstUInt8>: <Reg8: 9, UInt8: 128>
        // USED → r9 = 128
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 36, Reg8: 9>
        r1[36] = 128;
        // CODE → <LoadConstInt>: <Reg8: 9, Imm32: 4194304>
        // USED → r9 = 4194304
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 37, Reg8: 9>
        r1[37] = 4194304;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 38, Reg8: 10>
        r1[38] = 0;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 19, string_id: 24093>  # String: 'nativeFabricUIManager' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 20, string_id: 15507>  # String: 'createNode' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createNode
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 39, Reg8: 16>
        r1[39] = globalThis.nativeFabricUIManager.createNode;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 21, string_id: 22912>  # String: 'cloneNodeWithNewChildren' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 40, Reg8: 16>
        r1[40] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildren;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 22, string_id: 22913>  # String: 'cloneNodeWithNewChildrenAndProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 41, Reg8: 16>
        r1[41] = globalThis.nativeFabricUIManager.cloneNodeWithNewChildrenAndProps;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 23, string_id: 22914>  # String: 'cloneNodeWithNewProps' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.cloneNodeWithNewProps
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 42, Reg8: 16>
        r1[42] = globalThis.nativeFabricUIManager.cloneNodeWithNewProps;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 24, string_id: 23048>  # String: 'createChildSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.createChildSet
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 43, Reg8: 16>
        r1[43] = globalThis.nativeFabricUIManager.createChildSet;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 25, string_id: 22565>  # String: 'appendChild' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChild
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 44, Reg8: 16>
        r1[44] = globalThis.nativeFabricUIManager.appendChild;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 22566>  # String: 'appendChildToSet' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.appendChildToSet
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 45, Reg8: 16>
        r1[45] = globalThis.nativeFabricUIManager.appendChildToSet;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 27, string_id: 22962>  # String: 'completeRoot' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.completeRoot
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 46, Reg8: 16>
        r1[46] = globalThis.nativeFabricUIManager.completeRoot;
        // CODE → <GetById>: <Reg8: 16, Reg8: 9, UInt8: 28, string_id: 20376>  # String: 'registerEventHandler' (Identifier)
        // USED → r16 = globalThis.nativeFabricUIManager.registerEventHandler
        // CODE → <GetById>: <Reg8: 41, Reg8: 9, UInt8: 29, string_id: 24474>  # String: 'unstable_DiscreteEventPriority' (Identifier)
        // USED → r41 = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 47, Reg8: 41>
        r1[47] = globalThis.nativeFabricUIManager.unstable_DiscreteEventPriority;
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 30, string_id: 24484>  # String: 'unstable_getCurrentEventPriority' (Identifier)
        // USED → r9 = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 48, Reg8: 9>
        r1[48] = globalThis.nativeFabricUIManager.unstable_getCurrentEventPriority;
        // CODE → <GetByVal>: <Reg8: 9, Reg8: 19, Reg8: 17>
        // USED → r9 = r19[r17]
        // CODE → <Call2>: <Reg8: 9, Reg8: 18, Reg8: 2, Reg8: 9>
        // USED → r9 = param2(r19[r17])
        // CODE → <GetById>: <Reg8: 9, Reg8: 9, UInt8: 7, string_id: 13517>  # String: 'ReactNativeViewConfigRegistry' (Identifier)
        // USED → r9 = param2(r19[r17]).ReactNativeViewConfigRegistry
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 31, string_id: 137>  # String: 'get' (Identifier)
        // USED → r9 = param2(r19[r17]).ReactNativeViewConfigRegistry.get
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 49, Reg8: 9>
        r1[49] = param2(r19[r17]).ReactNativeViewConfigRegistry.get;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 50, Reg8: 17>
        r1[50] = 2;
        // CODE → <JmpFalse>: <Addr8: 13, Reg8: 16>  # Address: 00000fef
        if (!globalThis.nativeFabricUIManager.registerEventHandler) {
        } else {
            // CODE → <CreateClosure>: <Reg8: 9, Reg8: 1, function_id: 510>  # Function: [#510 dispatchEvent of 81 bytes]: 4 params @ offset 0x0017ac46
            // USED → r9 = dispatchEvent /* Closure with env r1 = undefined */
            // CODE → <Call2>: <Reg8: 9, Reg8: 16, Reg8: 2, Reg8: 9>
            r9 = globalThis.nativeFabricUIManager.registerEventHandler(dispatchEvent /* Closure with env r1 = undefined */)
        }
        // CODE → <TryGetById>: <Reg8: 41, Reg8: 0, UInt8: 32, string_id: 214>  # String: 'setTimeout' (Identifier)
        // USED → r41 = globalThis.setTimeout
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 51, Reg8: 41>
        r1[51] = globalThis.setTimeout;
        // CODE → <TryGetById>: <Reg8: 9, Reg8: 0, UInt8: 33, string_id: 12162>  # String: 'clearTimeout' (Identifier)
        // USED → r9 = globalThis.clearTimeout
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 52, Reg8: 9>
        r1[52] = globalThis.clearTimeout;
        // CODE → <GetById>: <Reg8: 16, Reg8: 0, UInt8: 34, string_id: 15863>  # String: 'RN$enableMicrotasksInReact' (Identifier)
        // USED → r16 = globalThis.RN$enableMicrotasksInReact
        // CODE → <LoadConstString>: <Reg8: 9, string_id: 610>  # String: 'undefined' (String)
        // USED → r9 = "undefined"
        // CODE → <TypeOf>: <Reg8: 16, Reg8: 16>
        // USED → r16 = typeof globalThis.RN$enableMicrotasksInReact
        // CODE → <StrictNeq>: <Reg8: 16, Reg8: 9, Reg8: 16>
        // USED → r16 = "undefined" !== typeof globalThis.RN$enableMicrotasksInReact
        // CODE → <JmpFalse>: <Addr8: 15, Reg8: 16>  # Address: 00001023
        if (!"undefined" !== typeof globalThis.RN$enableMicrotasksInReact) {
        } else {
            // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 34, string_id: 15863>  # String: 'RN$enableMicrotasksInReact' (Identifier)
            // USED → r42 = globalThis.RN$enableMicrotasksInReact
            // CODE → <Not>: <Reg8: 42, Reg8: 42>
            // USED → r42 = !globalThis.RN$enableMicrotasksInReact
            // CODE → <Not>: <Reg8: 16, Reg8: 42>
            // USED → r16 = !!globalThis.RN$enableMicrotasksInReact
        }
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 53, Reg8: 16>
        r1[53] = !!globalThis.RN$enableMicrotasksInReact;
        // CODE → <GetById>: <Reg8: 42, Reg8: 0, UInt8: 35, string_id: 16391>  # String: 'queueMicrotask' (Identifier)
        // USED → r42 = globalThis.queueMicrotask
        // CODE → <LoadConstString>: <Reg8: 16, string_id: 12255>  # String: 'function' (Identifier)
        // USED → r16 = "function"
        // CODE → <TypeOf>: <Reg8: 42, Reg8: 42>
        // USED → r42 = typeof globalThis.queueMicrotask
        // CODE → <JStrictNotEqual>: <Addr8: 10, Reg8: 16, Reg8: 42>  # Address: 0000103e
        if ("function" !== typeof globalThis.queueMicrotask) { /* jump to label_4158 */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 54, Reg8: 41>
        r1[54] = globalThis.queueMicrotask;
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 821>  # Function: [#821 getFiberCurrentPropsFromNode$1 of 17 bytes]: 2 params @ offset 0x00189a6d
        // USED → r41 = getFiberCurrentPropsFromNode$1 /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 41>
        r1[5] = getFiberCurrentPropsFromNode$1 /* Closure with env r1 = undefined */;
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 8>
        r1[6] = getInstanceFromNode /* Closure with env r1 = undefined */;
        // CODE → <CreateClosure>: <Reg8: 41, Reg8: 1, function_id: 822>  # Function: [#822 getNodeFromInstance$1 of 49 bytes]: 2 params @ offset 0x00189a7e
        // USED → r41 = getNodeFromInstance$1 /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 41>
        r1[7] = getNodeFromInstance$1 /* Closure with env r1 = undefined */;
        // CODE → <GetById>: <Reg8: 42, Reg8: 40, UInt8: 36, string_id: 15132>  # String: 'injection' (Identifier)
        // USED → r42 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection
        // CODE → <GetById>: <Reg8: 41, Reg8: 42, UInt8: 37, string_id: 21100>  # String: 'injectGlobalResponderHandler' (Identifier)
        // USED → r41 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection.injectGlobalResponderHandler
        // CODE → <NewObject>: <Reg8: 40>
        // USED → r40 = {}
        // CODE → <CreateClosure>: <Reg8: 43, Reg8: 1, function_id: 823>  # Function: [#823 onChange of 122 bytes]: 4 params @ offset 0x00189aaf
        // USED → r43 = onChange /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 40, Reg8: 43, string_id: 15401>  # String: 'onChange' (Identifier)
        // USED → r40 = { onChange: onChange /* Closure with env r1 = undefined */ }
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = { _getResponder: _getResponder /* Closure with env r1 = undefined */, eventTypes: { startShouldSetResponder: { phasedRegistrationNames: { bubbled: "onStartShouldSetResponder", captured: "onMoveShouldSetResponderCapture" }, dependencies: [] } }, scrollShouldSetResponder: { phasedRegistrationNames: { bubbled: "onScrollShouldSetResponder", selectionChangeShouldSetResponder: { phasedRegistrationNames: { bubbled: "onSelectionChangeShouldSetResponder", moveShouldSetResponder: { phasedRegistrationNames: { bubbled: "onMoveShouldSetResponder", responderStart: { registrationName: "onResponderStart", responderMove: { registrationName: "onResponderMove", responderEnd: { registrationName: "onResponderEnd", responderRelease: { registrationName: "onResponderRelease", responderTerminationRequest: { registrationName: "onResponderTerminationRequest", responderGrant: { registrationName: "onResponderGrant", responderReject: { registrationName: "onResponderReject", responderTerminate: { registrationName: "onResponderTerminate", extractEvents: extractEvents /* Closure with env r1 = undefined */, GlobalResponderHandler: null, injection: { injectGlobalResponderHandler: injectGlobalResponderHandler /* Closure with env r1 = undefined */ } }.injection.injectGlobalResponderHandler({ onChange: onChange /* Closure with env r1 = undefined */ })
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 3815>  # String: 'react.element' (String)
        // USED → r40 = "react.element"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.element")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 55, Reg8: 40>
        r1[55] = globalThis.Symbol.for("react.element");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5553>  # String: 'react.portal' (String)
        // USED → r40 = "react.portal"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.portal")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 56, Reg8: 40>
        r1[56] = globalThis.Symbol.for("react.portal");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5930>  # String: 'react.fragment' (String)
        // USED → r40 = "react.fragment"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.fragment")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 57, Reg8: 40>
        r1[57] = globalThis.Symbol.for("react.fragment");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6410>  # String: 'react.strict_mode' (String)
        // USED → r40 = "react.strict_mode"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.strict_mode")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 58, Reg8: 40>
        r1[58] = globalThis.Symbol.for("react.strict_mode");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5628>  # String: 'react.profiler' (String)
        // USED → r40 = "react.profiler"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.profiler")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 59, Reg8: 40>
        r1[59] = globalThis.Symbol.for("react.profiler");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2499>  # String: 'react.provider' (String)
        // USED → r40 = "react.provider"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.provider")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 60, Reg8: 40>
        r1[60] = globalThis.Symbol.for("react.provider");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8244>  # String: 'react.consumer' (String)
        // USED → r40 = "react.consumer"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.consumer")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 61, Reg8: 40>
        r1[61] = globalThis.Symbol.for("react.consumer");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4944>  # String: 'react.context' (String)
        // USED → r40 = "react.context"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.context")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 62, Reg8: 40>
        r1[62] = globalThis.Symbol.for("react.context");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 7930>  # String: 'react.forward_ref' (String)
        // USED → r40 = "react.forward_ref"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.forward_ref")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 63, Reg8: 40>
        r1[63] = globalThis.Symbol.for("react.forward_ref");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6421>  # String: 'react.suspense' (String)
        // USED → r40 = "react.suspense"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 64, Reg8: 40>
        r1[64] = globalThis.Symbol.for("react.suspense");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6422>  # String: 'react.suspense_list' (String)
        // USED → r40 = "react.suspense_list"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.suspense_list")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 65, Reg8: 40>
        r1[65] = globalThis.Symbol.for("react.suspense_list");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 410>  # String: 'react.memo' (String)
        // USED → r40 = "react.memo"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.memo")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 66, Reg8: 40>
        r1[66] = globalThis.Symbol.for("react.memo");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10762>  # String: 'react.lazy' (String)
        // USED → r40 = "react.lazy"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.lazy")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 67, Reg8: 40>
        r1[67] = globalThis.Symbol.for("react.lazy");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6222>  # String: 'react.scope' (String)
        // USED → r40 = "react.scope"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.scope")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 6531>  # String: 'react.debug_trace_mode' (String)
        // USED → r40 = "react.debug_trace_mode"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.debug_trace_mode")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 5577>  # String: 'react.offscreen' (String)
        // USED → r40 = "react.offscreen"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        // USED → r40 = globalThis.Symbol.for("react.offscreen")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 68, Reg8: 40>
        r1[68] = globalThis.Symbol.for("react.offscreen");
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 4905>  # String: 'react.legacy_hidden' (String)
        // USED → r40 = "react.legacy_hidden"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.legacy_hidden")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 2166>  # String: 'react.cache' (String)
        // USED → r40 = "react.cache"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.cache")
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 8982>  # String: 'react.tracing_marker' (String)
        // USED → r40 = "react.tracing_marker"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.tracing_marker")
        // CODE → <TryGetById>: <Reg8: 40, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r40 = globalThis.Symbol
        // CODE → <GetById>: <Reg8: 40, Reg8: 40, UInt8: 40, string_id: 13658>  # String: 'iterator' (Identifier)
        // USED → r40 = globalThis.Symbol.iterator
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 69, Reg8: 40>
        r1[69] = globalThis.Symbol.iterator;
        // CODE → <TryGetById>: <Reg8: 42, Reg8: 0, UInt8: 38, string_id: 52>  # String: 'Symbol' (Identifier)
        // USED → r42 = globalThis.Symbol
        // CODE → <GetByIdShort>: <Reg8: 41, Reg8: 42, UInt8: 39, string_id: 39>  # String: 'for' (Identifier)
        // USED → r41 = globalThis.Symbol.for
        // CODE → <LoadConstString>: <Reg8: 40, string_id: 10511>  # String: 'react.client.reference' (String)
        // USED → r40 = "react.client.reference"
        // CODE → <Call2>: <Reg8: 40, Reg8: 41, Reg8: 42, Reg8: 40>
        r40 = globalThis.Symbol.for("react.client.reference")
        // CODE → <NewArray>: <Reg8: 40, UInt16: 0>
        // USED → r40 = []
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 70, Reg8: 40>
        r1[70] = [];
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 71, Reg8: 39>
        r1[71] = -1;
        // CODE → <NewObject>: <Reg8: 39>
        // USED → r39 = {}
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 72, Reg8: 39>
        r1[72] = {};
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r39 = globalThis.Object
        // CODE → <GetById>: <Reg8: 39, Reg8: 39, UInt8: 41, string_id: 11558>  # String: 'is' (Identifier)
        // USED → r39 = globalThis.Object.is
        // CODE → <TypeOf>: <Reg8: 39, Reg8: 39>
        // USED → r39 = typeof globalThis.Object.is
        // CODE → <JStrictNotEqual>: <Addr8: 16, Reg8: 16, Reg8: 39>  # Address: 0000127e
        if ("function" !== typeof globalThis.Object.is) { /* jump to label_4734 */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 73, Reg8: 38>
        r1[73] = globalThis.Object.is;
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 74, Reg8: 38>
        r1[74] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 75, Reg8: 38>
        r1[75] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 38, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r38 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 76, Reg8: 38>
        r1[76] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 77, Reg8: 11>
        r1[77] = null;
        // CODE → <NewArray>: <Reg8: 38, UInt16: 0>
        // USED → r38 = []
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 78, Reg8: 38>
        r1[78] = [];
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 79, Reg8: 10>
        r1[79] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 80, Reg8: 10>
        r1[80] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 81, Reg8: 11>
        r1[81] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 82, Reg8: 11>
        r1[82] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 83, Reg8: 12>
        r1[83] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 84, Reg8: 12>
        r1[84] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 85, Reg8: 12>
        r1[85] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 86, Reg8: 10>
        r1[86] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 87, Reg8: 12>
        r1[87] = false;
        // CODE → <TryGetById>: <Reg8: 38, Reg8: 0, UInt8: 3, string_id: 37>  # String: 'Object' (Identifier)
        // USED → r38 = globalThis.Object
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r38 = globalThis.Object.prototype
        // CODE → <GetByIdShort>: <Reg8: 38, Reg8: 38, UInt8: 12, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
        // USED → r38 = globalThis.Object.prototype.hasOwnProperty
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 88, Reg8: 38>
        r1[88] = globalThis.Object.prototype.hasOwnProperty;
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 3625>  # String: "Suspense Exception: This is not a real error! It's an implementation detail of `use` to interrupt the current render. You must either rethrow it immediately, or move the `use` call outside of the `try/catch` block. Capturing without rethrowing will lead to unexpected behavior.\n\nTo handle async errors, wrap your component in an error boundary, or call the promise's `.catch` method and pass the result to `use`" (String)
        // USED → r38 = "str_3625"
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error("str_3625")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 89, Reg8: 38>
        r1[89] = globalThis.Error("str_3625");
        // CODE → <TryGetById>: <Reg8: 39, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r39 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 38, string_id: 6775>  # String: "Suspense Exception: This is not a real error, and should not leak into userspace. If you're seeing this, it's likely a bug in React." (String)
        // USED → r38 = "str_6775"
        // CODE → <Call2>: <Reg8: 38, Reg8: 39, Reg8: 2, Reg8: 38>
        // USED → r38 = globalThis.Error("str_6775")
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 90, Reg8: 38>
        r1[90] = globalThis.Error("str_6775");
        // CODE → <NewObject>: <Reg8: 38>
        // USED → r38 = {}
        // CODE → <CreateClosure>: <Reg8: 39, Reg8: 1, function_id: 824>  # Function: [#824 then of 4 bytes]: 1 params @ offset 0x0016f98c
        // USED → r39 = then /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 38, Reg8: 39, string_id: 231>  # String: 'then' (Identifier)
        // USED → r38 = { then: then /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 91, Reg8: 38>
        r1[91] = { then: then /* Closure with env r1 = undefined */ };
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 92, Reg8: 11>
        r1[92] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 93, Reg8: 11>
        r1[93] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 94, Reg8: 10>
        r1[94] = 0;
        // CODE → <Call2>: <Reg8: 37, Reg8: 20, Reg8: 2, Reg8: 37>
        // USED → r37 = createChildReconciler /* Closure with env r1 = undefined */(true)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 95, Reg8: 37>
        r1[95] = createChildReconciler /* Closure with env r1 = undefined */(true);
        // CODE → <Call2>: <Reg8: 20, Reg8: 20, Reg8: 2, Reg8: 12>
        // USED → r20 = createChildReconciler /* Closure with env r1 = undefined */(false)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 96, Reg8: 20>
        r1[96] = createChildReconciler /* Closure with env r1 = undefined */(false);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 97, Reg8: 20>
        r1[97] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(0)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 98, Reg8: 20>
        r1[98] = createCursor /* Closure with env r1 = undefined */(0);
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 11>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(null)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 99, Reg8: 20>
        r1[99] = createCursor /* Closure with env r1 = undefined */(null);
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 100, Reg8: 11>
        r1[100] = null;
        // CODE → <Call2>: <Reg8: 20, Reg8: 15, Reg8: 2, Reg8: 10>
        // USED → r20 = createCursor /* Closure with env r1 = undefined */(0)
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 101, Reg8: 20>
        r1[101] = createCursor /* Closure with env r1 = undefined */(0);
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 42, string_id: 21353>  # String: 'ReactCurrentDispatcher' (Identifier)
        // USED → r20 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 102, Reg8: 20>
        r1[102] = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentDispatcher;
        // CODE → <GetById>: <Reg8: 20, Reg8: 14, UInt8: 43, string_id: 17455>  # String: 'ReactCurrentBatchConfig' (Identifier)
        // USED → r20 = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 103, Reg8: 20>
        r1[103] = param2(r19[r0]).__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentBatchConfig;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 104, Reg8: 10>
        r1[104] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 105, Reg8: 11>
        r1[105] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 106, Reg8: 11>
        r1[106] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 107, Reg8: 11>
        r1[107] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 108, Reg8: 12>
        r1[108] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 109, Reg8: 12>
        r1[109] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 110, Reg8: 12>
        r1[110] = false;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 111, Reg8: 10>
        r1[111] = 0;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 112, Reg8: 11>
        r1[112] = null;
        // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 113, Reg8: 10>
        r1[113] = 0;
        // CODE → <CreateClosure>: <Reg8: 20, Reg8: 1, function_id: 825>  # Function: [#825 createFunctionComponentUpdateQueue of 12 bytes]: 1 params @ offset 0x00189b29
        // USED → r20 = createFunctionComponentUpdateQueue /* Closure with env r1 = undefined */
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 114, Reg8: 20>
        r1[114] = createFunctionComponentUpdateQueue /* Closure with env r1 = undefined */;
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 36, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */, useId: throwInvalidHookError /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 115, Reg8: 20>
        r1[115] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: throwInvalidHookError /* Closure with env r1 = undefined */, useContext: throwInvalidHookError /* Closure with env r1 = undefined */, useEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useImperativeHandle: throwInvalidHookError /* Closure with env r1 = undefined */, useInsertionEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useLayoutEffect: throwInvalidHookError /* Closure with env r1 = undefined */, useMemo: throwInvalidHookError /* Closure with env r1 = undefined */, useReducer: throwInvalidHookError /* Closure with env r1 = undefined */, useRef: throwInvalidHookError /* Closure with env r1 = undefined */, useState: throwInvalidHookError /* Closure with env r1 = undefined */, useDebugValue: throwInvalidHookError /* Closure with env r1 = undefined */, useDeferredValue: throwInvalidHookError /* Closure with env r1 = undefined */, useTransition: throwInvalidHookError /* Closure with env r1 = undefined */, useSyncExternalStore: throwInvalidHookError /* Closure with env r1 = undefined */, useId: throwInvalidHookError /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 36, Reg8: 1, function_id: 826>  # Function: [#826 useCallback of 49 bytes]: 3 params @ offset 0x00189b35
        // USED → r36 = useCallback /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 36, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 827>  # Function: [#827 useImperativeHandle of 90 bytes]: 4 params @ offset 0x00189b66
        // USED → r35 = useImperativeHandle /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 828>  # Function: [#828 useLayoutEffect of 33 bytes]: 3 params @ offset 0x00189bc0
        // USED → r35 = useLayoutEffect /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 829>  # Function: [#829 useInsertionEffect of 30 bytes]: 3 params @ offset 0x00189be1
        // USED → r35 = useInsertionEffect /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 830>  # Function: [#830 useMemo of 64 bytes]: 3 params @ offset 0x00189bff
        // USED → r35 = useMemo /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 831>  # Function: [#831 useReducer of 139 bytes]: 4 params @ offset 0x00189c3f
        // USED → r35 = useReducer /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 832>  # Function: [#832 useRef of 31 bytes]: 2 params @ offset 0x00189cca
        // USED → r35 = useRef /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 833>  # Function: [#833 useState of 72 bytes]: 2 params @ offset 0x00189ce9
        // USED → r35 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 35, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 834>  # Function: [#834 useDeferredValue of 34 bytes]: 3 params @ offset 0x00189d31
        // USED → r35 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 835>  # Function: [#835 useTransition of 79 bytes]: 1 params @ offset 0x00189d53
        // USED → r35 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 836>  # Function: [#836 useSyncExternalStore of 239 bytes]: 3 params @ offset 0x00189da2
        // USED → r35 = useSyncExternalStore /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 35, Reg8: 1, function_id: 837>  # Function: [#837 useId of 83 bytes]: 1 params @ offset 0x00189e91
        // USED → r35 = useId /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 35, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */, useId: useId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 116, Reg8: 20>
        r1[116] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: useCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: mountEffect /* Closure with env r1 = undefined */, useImperativeHandle: useImperativeHandle /* Closure with env r1 = undefined */, useLayoutEffect: useLayoutEffect /* Closure with env r1 = undefined */, useInsertionEffect: useInsertionEffect /* Closure with env r1 = undefined */, useMemo: useMemo /* Closure with env r1 = undefined */, useReducer: useReducer /* Closure with env r1 = undefined */, useRef: useRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: useSyncExternalStore /* Closure with env r1 = undefined */, useId: useId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 838>  # Function: [#838 useState of 22 bytes]: 1 params @ offset 0x00189ee4
        // USED → r34 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 34, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 839>  # Function: [#839 useDeferredValue of 42 bytes]: 3 params @ offset 0x00189efa
        // USED → r34 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 34, Reg8: 1, function_id: 840>  # Function: [#840 useTransition of 78 bytes]: 1 params @ offset 0x00189f24
        // USED → r34 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 34, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 117, Reg8: 20>
        r1[117] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: updateReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 31, string_id: 20330>  # String: 'readContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 33, string_id: 12261>  # String: 'use' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 32, string_id: 242>  # String: 'useCallback' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 31, string_id: 228>  # String: 'useContext' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 30, string_id: 243>  # String: 'useEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 29, string_id: 24596>  # String: 'useImperativeHandle' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 28, string_id: 24597>  # String: 'useInsertionEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 27, string_id: 24614>  # String: 'useLayoutEffect' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 26, string_id: 230>  # String: 'useMemo' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 25, string_id: 12216>  # String: 'useReducer' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 244>  # String: 'useRef' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 24, Reg8: 1, function_id: 841>  # Function: [#841 useState of 22 bytes]: 1 params @ offset 0x00189f72
        // USED → r24 = useState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnByIdShort>: <Reg8: 20, Reg8: 24, string_id: 246>  # String: 'useState' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24567>  # String: 'useDebugValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 842>  # Function: [#842 useDeferredValue of 75 bytes]: 3 params @ offset 0x00189f88
        // USED → r23 = useDeferredValue /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24568>  # String: 'useDeferredValue' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 23, Reg8: 1, function_id: 843>  # Function: [#843 useTransition of 78 bytes]: 1 params @ offset 0x00189fd3
        // USED → r23 = useTransition /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 23, string_id: 24665>  # String: 'useTransition' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 22, string_id: 20645>  # String: 'useSyncExternalStore' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */ }
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 24594>  # String: 'useId' (Identifier)
        // USED → r20 = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 118, Reg8: 20>
        r1[118] = { readContext: readContext /* Closure with env r1 = undefined */, use: use /* Closure with env r1 = undefined */, useCallback: updateCallback /* Closure with env r1 = undefined */, useContext: readContext /* Closure with env r1 = undefined */, useEffect: updateEffect /* Closure with env r1 = undefined */, useImperativeHandle: updateImperativeHandle /* Closure with env r1 = undefined */, useInsertionEffect: updateInsertionEffect /* Closure with env r1 = undefined */, useLayoutEffect: updateLayoutEffect /* Closure with env r1 = undefined */, useMemo: updateMemo /* Closure with env r1 = undefined */, useReducer: rerenderReducer /* Closure with env r1 = undefined */, useRef: updateRef /* Closure with env r1 = undefined */, useState: useState /* Closure with env r1 = undefined */, useDebugValue: mountDebugValue /* Closure with env r1 = undefined */, useDeferredValue: useDeferredValue /* Closure with env r1 = undefined */, useTransition: useTransition /* Closure with env r1 = undefined */, useSyncExternalStore: updateSyncExternalStore /* Closure with env r1 = undefined */, useId: updateId /* Closure with env r1 = undefined */ };
        // CODE → <NewObject>: <Reg8: 20>
        // USED → r20 = {}
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 844>  # Function: [#844 isMounted of 34 bytes]: 2 params @ offset 0x0018a021
        // USED → r21 = isMounted /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 16785>  # String: 'isMounted' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 845>  # Function: [#845 enqueueSetState of 109 bytes]: 4 params @ offset 0x0018a043
        // USED → r21 = enqueueSetState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22773>  # String: 'enqueueSetState' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 846>  # Function: [#846 enqueueReplaceState of 118 bytes]: 4 params @ offset 0x0018a0b0
        // USED → r21 = enqueueReplaceState /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 22685>  # String: 'enqueueReplaceState' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */ }
        // CODE → <CreateClosure>: <Reg8: 21, Reg8: 1, function_id: 847>  # Function: [#847 enqueueForceUpdate of 109 bytes]: 3 params @ offset 0x0018a126
        // USED → r21 = enqueueForceUpdate /* Closure with env r1 = undefined */
        // CODE → <PutNewOwnById>: <Reg8: 20, Reg8: 21, string_id: 17151>  # String: 'enqueueForceUpdate' (Identifier)
        // USED → r20 = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */, enqueueForceUpdate: enqueueForceUpdate /* Closure with env r1 = undefined */ }
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 119, Reg8: 20>
        r1[119] = { isMounted: isMounted /* Closure with env r1 = undefined */, enqueueSetState: enqueueSetState /* Closure with env r1 = undefined */, enqueueReplaceState: enqueueReplaceState /* Closure with env r1 = undefined */, enqueueForceUpdate: enqueueForceUpdate /* Closure with env r1 = undefined */ };
        // CODE → <TryGetById>: <Reg8: 20, Reg8: 0, UInt8: 44, string_id: 24>  # String: 'WeakMap' (Identifier)
        // USED → r20 = globalThis.WeakMap
        // CODE → <GetByIdShort>: <Reg8: 21, Reg8: 20, UInt8: 5, string_id: 158>  # String: 'prototype' (Identifier)
        // USED → r21 = globalThis.WeakMap.prototype
        // CODE → <CreateThis>: <Reg8: 21, Reg8: 21, Reg8: 20>
        r21 = createThis(prototype=globalThis.WeakMap.prototype, constructor=globalThis.WeakMap)
        // CODE → <Mov>: <Reg8: 57, Reg8: 21>
        r57 = r21
        // CODE → <Construct>: <Reg8: 20, Reg8: 20, UInt8: 1>
        r20 = new globalThis.WeakMap(param7)
        // CODE → <SelectObject>: <Reg8: 20, Reg8: 21, Reg8: 20>
        // USED → r20 = r21[r20]
        // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 120, Reg8: 20>
        r1[120] = r21[r20];
        // CODE → <GetByVal>: <Reg8: 17, Reg8: 19, Reg8: 17>
        // USED → r17 = r19[r17]
        // CODE → <Call2>: <Reg8: 17, Reg8: 18, Reg8: 2, Reg8: 17>
        // USED → r17 = param2(r19[r17])
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 45, string_id: 14613>  # String: 'ReactFiberErrorDialog' (Identifier)
        // USED → r17 = param2(r19[r17]).ReactFiberErrorDialog
        // CODE → <GetById>: <Reg8: 17, Reg8: 17, UInt8: 46, string_id: 14615>  # String: 'showErrorDialog' (Identifier)
        // USED → r17 = param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog
        // CODE → <TypeOf>: <Reg8: 17, Reg8: 17>
        // USED → r17 = typeof param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog
        // CODE → <JStrictNotEqualLong>: <Addr32: 774, Reg8: 16, Reg8: 17>  # Address: 000018b9
        if ("function" !== typeof param2(r19[r17]).ReactFiberErrorDialog.showErrorDialog) { /* jump to label_6329 */ }
        // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 13, string_id: 14>  # String: 'Error' (Identifier)
        // USED → r1 = globalThis.Error
        // CODE → <LoadConstString>: <Reg8: 0, string_id: 4985>  # String: 'Expected ReactFiberErrorDialog.showErrorDialog to be a function.' (String)
        // USED → r0 = "Expected ReactFiberErrorDialog.showErrorDialog to be a function."
        // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
        // USED → r0 = globalThis.Error("Expected ReactFiberErrorDialog.showErrorDialog to be a function.")
        // CODE → <Throw>: <Reg8: 0>
        r0 = throw globalThis.Error("Expected ReactFiberErrorDialog.showErrorDialog to be a function.")
    }
}