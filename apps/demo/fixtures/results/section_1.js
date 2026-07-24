function function_1(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 1>
    // USED → r8 = param1
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 8>
    createEnvironment()[0] = r8
    // CODE → <CreateClosure>: <Reg8: 7, Reg8: 2, function_id: 2>  # Function: [#2 clear of 37 bytes]: 1 params @ offset 0x0016e004
    // USED → r7 = clear /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 4>  # Function: [#4 metroRequire of 59 bytes]: 2 params @ offset 0x0016e094
    // USED → r4 = metroRequire /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 9, Reg8: 4>
    createEnvironment()[9] = metroRequire /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 5>  # Function: [#5 metroImportDefault of 100 bytes]: 2 params @ offset 0x0016e0cf
    // USED → r6 = metroImportDefault /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 10, Reg8: 6>
    createEnvironment()[10] = metroImportDefault /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 2, function_id: 6>  # Function: [#6 metroImportAll of 157 bytes]: 2 params @ offset 0x0016e133
    // USED → r5 = metroImportAll /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 11, Reg8: 5>
    createEnvironment()[11] = metroImportAll /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 7>  # Function: [#7 guardedLoadModule of 100 bytes]: 3 params @ offset 0x0016e1d0
    // USED → r0 = guardedLoadModule /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 12, Reg8: 0>
    createEnvironment()[12] = guardedLoadModule /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 8>  # Function: [#8 unpackModuleId of 36 bytes]: 2 params @ offset 0x0016e234
    // USED → r3 = unpackModuleId /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 13, Reg8: 3>
    createEnvironment()[13] = unpackModuleId /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 12>  # Function: [#12 loadModuleImplementation of 356 bytes]: 3 params @ offset 0x0016e2ea
    // USED → r0 = loadModuleImplementation /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 14, Reg8: 0>
    createEnvironment()[14] = loadModuleImplementation /* Closure with env r2 = createEnvironment() */
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 13>  # Function: [#13 unknownModuleError of 36 bytes]: 2 params @ offset 0x0016e44e
    // USED → r0 = unknownModuleError /* Closure with env r2 = createEnvironment() */
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 15, Reg8: 0>
    createEnvironment()[15] = unknownModuleError /* Closure with env r2 = createEnvironment() */
    // CODE → <PutById>: <Reg8: 8, Reg8: 4, UInt8: 1, string_id: 14170>  # String: '__r' (Identifier)
    r8.__r = metroRequire /* Closure with env r2 = createEnvironment() */;
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis
    // CODE → <GetById>: <Reg8: 11, Reg8: 1, UInt8: 1, string_id: 13635>  # String: '__METRO_GLOBAL_PREFIX__' (Identifier)
    // USED → r11 = globalThis.__METRO_GLOBAL_PREFIX__
    // CODE → <TryGetById>: <Reg8: 0, Reg8: 1, UInt8: 2, string_id: 21>  # String: 'HermesInternal' (Identifier)
    // USED → r0 = globalThis.HermesInternal
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 0, UInt8: 3, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r10 = globalThis.HermesInternal.concat
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 11303>  # String: '' (Identifier)
    // USED → r9 = ""
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 64>  # String: '__d' (Identifier)
    // USED → r0 = "__d"
    // CODE → <Call3>: <Reg8: 9, Reg8: 10, Reg8: 9, Reg8: 11, Reg8: 0>
    // USED → r9 = globalThis.HermesInternal.concat("", globalThis.__METRO_GLOBAL_PREFIX__, "__d")
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 3>  # Function: [#3 define of 107 bytes]: 4 params @ offset 0x0016e029
    // USED → r0 = define /* Closure with env r2 = createEnvironment() */
    // CODE → <PutByVal>: <Reg8: 8, Reg8: 9, Reg8: 0>
    r8[globalThis.HermesInternal.concat("", globalThis.__METRO_GLOBAL_PREFIX__, "__d")] = define /* Closure with env r2 = createEnvironment() */;
    // CODE → <PutById>: <Reg8: 8, Reg8: 7, UInt8: 2, string_id: 11632>  # String: '__c' (Identifier)
    r8.__c = clear /* Closure with env r2 = createEnvironment() */;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 10>  # Function: [#10 registerSegment of 48 bytes]: 4 params @ offset 0x0016e278
    // USED → r0 = registerSegment /* Closure with env r2 = createEnvironment() */
    // CODE → <PutById>: <Reg8: 8, Reg8: 0, UInt8: 3, string_id: 16001>  # String: '__registerSegment' (Identifier)
    r8.__registerSegment = registerSegment /* Closure with env r2 = createEnvironment() */;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 0>
    // USED → r7 = clear /* Closure with env r2 = createEnvironment() */(undefined)
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 7>
    createEnvironment()[1] = clear /* Closure with env r2 = createEnvironment() */(undefined)
    // CODE → <NewObject>: <Reg8: 7>
    // USED → r7 = {}
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 7>
    createEnvironment()[2] = r7
    // CODE → <NewObject>: <Reg8: 7>
    // USED → r7 = {}
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 7, UInt8: 4, string_id: 143>  # String: 'hasOwnProperty' (Identifier)
    // USED → r7 = r7.hasOwnProperty
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 7>
    createEnvironment()[3] = r7.hasOwnProperty
    // CODE → <PutById>: <Reg8: 4, Reg8: 6, UInt8: 4, string_id: 21604>  # String: 'importDefault' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.importDefault = metroImportDefault /* Closure with env r2 = createEnvironment() */;
    // CODE → <PutById>: <Reg8: 4, Reg8: 5, UInt8: 5, string_id: 23806>  # String: 'importAll' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.importAll = metroImportAll /* Closure with env r2 = createEnvironment() */;
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 2, function_id: 14>  # Function: [#14 fallbackRequireContext of 34 bytes]: 1 params @ offset 0x0016e472
    // USED → r5 = fallbackRequireContext /* Closure with env r2 = createEnvironment() */
    // CODE → <PutById>: <Reg8: 4, Reg8: 5, UInt8: 6, string_id: 11796>  # String: 'context' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.context = fallbackRequireContext /* Closure with env r2 = createEnvironment() */;
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 2, function_id: 15>  # Function: [#15 fallbackRequireResolveWeak of 34 bytes]: 1 params @ offset 0x0016e494
    // USED → r5 = fallbackRequireResolveWeak /* Closure with env r2 = createEnvironment() */
    // CODE → <PutById>: <Reg8: 4, Reg8: 5, UInt8: 7, string_id: 15682>  # String: 'resolveWeak' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.resolveWeak = fallbackRequireResolveWeak /* Closure with env r2 = createEnvironment() */;
    // CODE → <LoadConstFalse>: <Reg8: 5>
    // USED → r5 = false
    // CODE → <StoreNPToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 5>
    createEnvironment()[4] = false
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 16>
    // USED → r5 = 16
    // CODE → <StoreNPToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 5>
    createEnvironment()[5] = 16
    // CODE → <LoadConstInt>: <Reg8: 5, Imm32: 65535>
    // USED → r5 = 65535
    // CODE → <StoreNPToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 5>
    createEnvironment()[6] = 65535
    // CODE → <PutById>: <Reg8: 4, Reg8: 3, UInt8: 8, string_id: 24223>  # String: 'unpackModuleId' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.unpackModuleId = unpackModuleId /* Closure with env r2 = createEnvironment() */;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 9>  # Function: [#9 packModuleId of 32 bytes]: 2 params @ offset 0x0016e258
    // USED → r3 = packModuleId /* Closure with env r2 = createEnvironment() */
    // CODE → <PutById>: <Reg8: 4, Reg8: 3, UInt8: 9, string_id: 24224>  # String: 'packModuleId' (Identifier)
    metroRequire /* Closure with env r2 = createEnvironment() */.packModuleId = packModuleId /* Closure with env r2 = createEnvironment() */;
    // CODE → <NewArray>: <Reg8: 3, UInt16: 0>
    // USED → r3 = []
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 7, Reg8: 3>
    createEnvironment()[7] = []
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 5, string_id: 26>  # String: 'Map' (Identifier)
    // USED → r1 = globalThis.Map
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 6, string_id: 158>  # String: 'prototype' (Identifier)
    // USED → r3 = globalThis.Map.prototype
    // CODE → <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 1>
    // USED → r3 = createThis(prototype=globalThis.Map.prototype, constructor=globalThis.Map)
    // CODE → <Mov>: <Reg8: 14, Reg8: 3>
    r14 = createThis(prototype=globalThis.Map.prototype, constructor=globalThis.Map)
    // CODE → <Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>
    r1 = new globalThis.Map(undefined)
    // CODE → <SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>
    // USED → r1 = r3[r1]
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 8, Reg8: 1>
    createEnvironment()[8] = r1
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}