function function_10679(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 3>
    // USED → r3 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 2>
    // USED → r5 = param2;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 6>
    // USED → r2 = param6;
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 7>
    // USED → r6 = param7;
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 5>
    createEnvironment()[0] = param2;
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 1, Reg8: 6>
    createEnvironment()[1] = param7;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 3, function_id: 10680>  # Function: [#10680 processPathConstants of 246 bytes]: 2 params @ offset 0x00294da4
    // USED → r0 = processPathConstants;
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 7, Reg8: 0>
    createEnvironment()[7] = processPathConstants;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 2, string_id: 112>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 0, string_id: 249>  # String: 'value' (Identifier)
    // USED → r1 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 65>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 4, Reg8: 7, Reg8: 2, Reg8: 0, Reg8: 1>
    r0 = globalThis.Object.defineProperty(globalThis.Object, param6, "__esModule", { value: true });
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <PutById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    param6.default = undefined;
    // CODE → <LoadConstZero>: <Reg8: 1>
    // USED → r1 = 0;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 6, Reg8: 1>
    // USED → r1 = param7[0];
    // CODE → <Call2>: <Reg8: 1, Reg8: 5, Reg8: 0, Reg8: 1>
    // USED → r1 = param2(undefined, param7[0]);
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 2, Reg8: 1>
    createEnvironment()[2] = param2(undefined, param7[0]);
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 9, UInt16: 9, UInt16: 43049>  # Array: ['MAIN_BUNDLE', 'CACHES_DIRECTORY', 'DOCUMENT_DIRECTORY', 'EXTERNAL_DIRECTORY', 'EXTERNAL_STORAGE_DIRECTORY', 'TEMP_DIRECTORY', 'LIBRARY_DIRECTORY', 'PICTURES_DIRECTORY', 'MOVIES_DIRECTORY']
    // USED → r1 = ["MAIN_BUNDLE", "CACHES_DIRECTORY", "DOCUMENT_DIRECTORY", "EXTERNAL_DIRECTORY", "EXTERNAL_STORAGE_DIRECTORY", "TEMP_DIRECTORY", "LIBRARY_DIRECTORY", "PICTURES_DIRECTORY", "MOVIES_DIRECTORY"];
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 3, Reg8: 1>
    createEnvironment()[3] = ["MAIN_BUNDLE", "CACHES_DIRECTORY", "DOCUMENT_DIRECTORY", "EXTERNAL_DIRECTORY", "EXTERNAL_STORAGE_DIRECTORY", "TEMP_DIRECTORY", "LIBRARY_DIRECTORY", "PICTURES_DIRECTORY", "MOVIES_DIRECTORY"];
    // CODE → <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 43068>  # Array: ['FILE_TYPE_REGULAR', 'FILE_TYPE_DIRECTORY']
    // USED → r1 = ["FILE_TYPE_REGULAR", "FILE_TYPE_DIRECTORY"];
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 4, Reg8: 1>
    createEnvironment()[4] = ["FILE_TYPE_REGULAR", "FILE_TYPE_DIRECTORY"];
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <StoreToEnvironment>: <Reg8: 3, UInt8: 5, Reg8: 1>
    createEnvironment()[5] = {  };
    // CODE → <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false;
    // CODE → <StoreNPToEnvironment>: <Reg8: 3, UInt8: 6, Reg8: 1>
    createEnvironment()[6] = false;
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    // CODE → <GetByVal>: <Reg8: 4, Reg8: 6, Reg8: 4>
    // USED → r4 = param7[2];
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
    // USED → r4 = param2(undefined, param7[2]);
    // CODE → <PutNewOwnById>: <Reg8: 1, Reg8: 4, string_id: 12734>  # String: 'SDK_VERSION' (Identifier)
    // USED → r1 = { SDK_VERSION: param2(undefined, param7[2]) };
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 10681>  # Function: [#10681 get FilePath of 65 bytes]: 1 params @ offset 0x00294e9a
    // USED → r4 = get FilePath;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 5066>  # String: 'FilePath' (String)
    // USED → r3 = "FilePath";
    // CODE → <PutOwnGetterSetterByVal>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 0, UInt8: 1>
    Object.defineProperty({ SDK_VERSION: param2(undefined, param7[2]) }, "FilePath", { get: get FilePath, set: undefined, enumerable: true, configurable: true });
    // CODE → <PutById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    param6.default = { SDK_VERSION: param2(undefined, param7[2]) };
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}