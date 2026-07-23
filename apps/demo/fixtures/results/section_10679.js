function function_10679(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <CreateEnvironment>: <Reg8: 3>
    r3 = createEnvironment()
    // LINE → <LoadParam>: <Reg8: 5, UInt8: 2>
    // USED → r5 = param2
    // LINE → <LoadParam>: <Reg8: 2, UInt8: 6>
    // USED → r2 = param6
    // LINE → <LoadParam>: <Reg8: 6, UInt8: 7>
    // USED → r6 = param7
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 5>
    r3[0] = param2;
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 1, Reg8: 6>
    r3[1] = param7;
    // LINE → <CreateClosure>: <Reg8: 0, Reg8: 3, function_id: 10680>  # Function: [#10680 processPathConstants of 246 bytes]: 2 params @ offset 0x00294da4
    // USED → r0 = processPathConstants /* Closure with env r3 = undefined */
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 7, Reg8: 0>
    r3[7] = processPathConstants /* Closure with env r3 = undefined */;
    // LINE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis
    // LINE → <TryGetById>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object
    // LINE → <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 2, string_id: 112>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty
    // LINE → <NewObject>: <Reg8: 1>
    // USED → r1 = {}
    // LINE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true
    // LINE → <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 0, string_id: 249>  # String: 'value' (Identifier)
    // USED → r1 = { value: true }
    // LINE → <LoadConstString>: <Reg8: 0, string_id: 65>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule"
    // LINE → <Call4>: <Reg8: 0, Reg8: 4, Reg8: 7, Reg8: 2, Reg8: 0, Reg8: 1>
    r0 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // LINE → <PutById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r2 = { default: undefined }
    // LINE → <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // LINE → <GetByVal>: <Reg8: 1, Reg8: 6, Reg8: 1>
    // USED → r1 = r6[r1]
    // LINE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 0, Reg8: 1>
    // USED → r1 = param2(r6[r1])
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 2, Reg8: 1>
    r3[2] = param2(r6[r1]);
    // LINE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 9, UInt16: 9, UInt16: 43049>  # Array: ['MAIN_BUNDLE', 'CACHES_DIRECTORY', 'DOCUMENT_DIRECTORY', 'EXTERNAL_DIRECTORY', 'EXTERNAL_STORAGE_DIRECTORY', 'TEMP_DIRECTORY', 'LIBRARY_DIRECTORY', 'PICTURES_DIRECTORY', 'MOVIES_DIRECTORY']
    // USED → r1 = ["MAIN_BUNDLE", "CACHES_DIRECTORY", "DOCUMENT_DIRECTORY", "EXTERNAL_DIRECTORY", "EXTERNAL_STORAGE_DIRECTORY", "TEMP_DIRECTORY", "LIBRARY_DIRECTORY", "PICTURES_DIRECTORY", "MOVIES_DIRECTORY"]
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 3, Reg8: 1>
    r3[3] = ["MAIN_BUNDLE", "CACHES_DIRECTORY", "DOCUMENT_DIRECTORY", "EXTERNAL_DIRECTORY", "EXTERNAL_STORAGE_DIRECTORY", "TEMP_DIRECTORY", "LIBRARY_DIRECTORY", "PICTURES_DIRECTORY", "MOVIES_DIRECTORY"];
    // LINE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 43068>  # Array: ['FILE_TYPE_REGULAR', 'FILE_TYPE_DIRECTORY']
    // USED → r1 = ["FILE_TYPE_REGULAR", "FILE_TYPE_DIRECTORY"]
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 4, Reg8: 1>
    r3[4] = ["FILE_TYPE_REGULAR", "FILE_TYPE_DIRECTORY"];
    // LINE → <NewObject>: <Reg8: 1>
    // USED → r1 = {}
    // LINE → <StoreToEnvironment>: <Reg8: 3, UInt8: 5, Reg8: 1>
    r3[5] = {};
    // LINE → <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false
    // LINE → <StoreNPToEnvironment>: <Reg8: 3, UInt8: 6, Reg8: 1>
    r3[6] = false;
    // LINE → <NewObject>: <Reg8: 1>
    // USED → r1 = {}
    // LINE → <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    r4 = 2
    // LINE → <GetByVal>: <Reg8: 4, Reg8: 6, Reg8: 4>
    // USED → r4 = r6[r4]
    // LINE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
    // USED → r4 = param2(r6[r4])
    // LINE → <PutNewOwnById>: <Reg8: 1, Reg8: 4, string_id: 12734>  # String: 'SDK_VERSION' (Identifier)
    // USED → r1 = { SDK_VERSION: param2(r6[r4]) }
    // LINE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 10681>  # Function: [#10681 get FilePath of 65 bytes]: 1 params @ offset 0x00294e9a
    // USED → r4 = get FilePath /* Closure with env r3 = undefined */
    // LINE → <LoadConstString>: <Reg8: 3, string_id: 5066>  # String: 'FilePath' (String)
    // USED → r3 = "FilePath"
    // LINE → <PutOwnGetterSetterByVal>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 0, UInt8: 1>
    // USED → r1 = Object.defineProperty({ SDK_VERSION: param2(r6[r4]) }, "FilePath", { get: get FilePath /* Closure with env r3 = undefined */, set: undefined, enumerable: true, configurable: true })
    // LINE → <PutById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    r2 = { default: Object.defineProperty({ SDK_VERSION: param2(r6[r4]) }, "FilePath", { get: get FilePath /* Closure with env r3 = undefined */, set: undefined, enumerable: true, configurable: true }) }
    // LINE → <Ret>: <Reg8: 0>
    return undefined;
}