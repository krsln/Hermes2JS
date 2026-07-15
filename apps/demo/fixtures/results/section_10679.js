function function_10679(param0, param1, param2, param3, param4, param5, param6, param7) {
    // CODE -> <CreateEnvironment>: <Reg8: 3>
    r3 = // Create new environment
    // CODE -> <LoadParam>: <Reg8: 5, UInt8: 2>
    // USED -> r5 = param2
    // CODE -> <LoadParam>: <Reg8: 2, UInt8: 6>
    // USED -> r2 = param6
    // CODE -> <LoadParam>: <Reg8: 6, UInt8: 7>
    r6 = param7
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 0, Reg8: 5>
    r3 = setEnvSlot(0, r5)  // StoreToEnvironment: env=r3, slot=0, value=r5
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 1, Reg8: 6>
    r3 = setEnvSlot(1, r6)  // StoreToEnvironment: env=r3, slot=1, value=r6
    // CODE -> <CreateClosure>: <Reg8: 0, Reg8: 3, function_id: 10680>  # Function: [#10680 processPathConstants of 246 bytes]: 2 params @ offset 0x00294da4
    r0 = processPathConstants /* Closure with env r3 = undefined */
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 7, Reg8: 0>
    r3 = setEnvSlot(7, r0)  // StoreToEnvironment: env=r3, slot=7, value=r0
    // CODE -> <GetGlobalObject>: <Reg8: 0>
    // USED -> r0 = this
    // CODE -> <TryGetById>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 37>  # String: 'Object' (Identifier)
    // USED -> r7 = this.Object
    // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 2, string_id: 112>  # String: 'defineProperty' (Identifier)
    // USED -> r4 = this.Object.defineProperty
    // CODE -> <NewObject>: <Reg8: 1>
    // USED -> r1 = {}
    // CODE -> <LoadConstTrue>: <Reg8: 0>
    // USED -> r0 = true
    // CODE -> <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 0, string_id: 249>  # String: 'value' (Identifier)
    // USED -> r1 = { value: true }
    // CODE -> <LoadConstString>: <Reg8: 0, string_id: 65>  # String: '__esModule' (Identifier)
    // USED -> r0 = "__esModule"
    // CODE -> <Call4>: <Reg8: 0, Reg8: 4, Reg8: 7, Reg8: 2, Reg8: 0, Reg8: 1>
    r0 = this.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE -> <LoadConstUndefined>: <Reg8: 0>
    // USED -> r0 = undefined
    // CODE -> <PutById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED -> r2 = { default: undefined }
    // CODE -> <LoadConstZero>: <Reg8: 1>
    r1 = 0
    // CODE -> <GetByVal>: <Reg8: 1, Reg8: 6, Reg8: 1>
    // USED -> r1 = r6[r1]
    // CODE -> <Call2>: <Reg8: 1, Reg8: 5, Reg8: 0, Reg8: 1>
    r1 = param2(r6[r1])
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 2, Reg8: 1>
    r3 = setEnvSlot(2, r1)  // StoreToEnvironment: env=r3, slot=2, value=r1
    // CODE -> <NewArrayWithBuffer>: <Reg8: 1, UInt16: 9, UInt16: 9, UInt16: 43049>  # Array: ['MAIN_BUNDLE', 'CACHES_DIRECTORY', 'DOCUMENT_DIRECTORY', 'EXTERNAL_DIRECTORY', 'EXTERNAL_STORAGE_DIRECTORY', 'TEMP_DIRECTORY', 'LIBRARY_DIRECTORY', 'PICTURES_DIRECTORY', 'MOVIES_DIRECTORY']
    r1 = ["MAIN_BUNDLE", "CACHES_DIRECTORY", "DOCUMENT_DIRECTORY", "EXTERNAL_DIRECTORY", "EXTERNAL_STORAGE_DIRECTORY", "TEMP_DIRECTORY", "LIBRARY_DIRECTORY", "PICTURES_DIRECTORY", "MOVIES_DIRECTORY"]
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 3, Reg8: 1>
    r3 = setEnvSlot(3, r1)  // StoreToEnvironment: env=r3, slot=3, value=r1
    // CODE -> <NewArrayWithBuffer>: <Reg8: 1, UInt16: 2, UInt16: 2, UInt16: 43068>  # Array: ['FILE_TYPE_REGULAR', 'FILE_TYPE_DIRECTORY']
    r1 = ["FILE_TYPE_REGULAR", "FILE_TYPE_DIRECTORY"]
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 4, Reg8: 1>
    r3 = setEnvSlot(4, r1)  // StoreToEnvironment: env=r3, slot=4, value=r1
    // CODE -> <NewObject>: <Reg8: 1>
    r1 = {}
    // CODE -> <StoreToEnvironment>: <Reg8: 3, UInt8: 5, Reg8: 1>
    r3 = setEnvSlot(5, r1)  // StoreToEnvironment: env=r3, slot=5, value=r1
    // CODE -> <LoadConstFalse>: <Reg8: 1>
    r1 = false
    // CODE -> <StoreNPToEnvironment>: <Reg8: 3, UInt8: 6, Reg8: 1>
    r3 = setEnvSlot(6, r1)  // StoreNPToEnvironment: env=r3, slot=6, value=r1
    // CODE -> <NewObject>: <Reg8: 1>
    // USED -> r1 = {}
    // CODE -> <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    r4 = 2
    // CODE -> <GetByVal>: <Reg8: 4, Reg8: 6, Reg8: 4>
    // USED -> r4 = r6[r4]
    // CODE -> <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
    // USED -> r4 = param2(r6[r4])
    // CODE -> <PutNewOwnById>: <Reg8: 1, Reg8: 4, string_id: 12734>  # String: 'SDK_VERSION' (Identifier)
    // USED -> r1 = { SDK_VERSION: param2(r6[r4]) }
    // CODE -> <CreateClosure>: <Reg8: 4, Reg8: 3, function_id: 10681>  # Function: [#10681 get FilePath of 65 bytes]: 1 params @ offset 0x00294e9a
    r4 = function_10681 /* Closure with env r3 = undefined */
    // CODE -> <LoadConstString>: <Reg8: 3, string_id: 5066>  # String: 'FilePath' (String)
    r3 = "FilePath"
    // CODE -> <PutById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    r2 = { default: { SDK_VERSION: param2(r6[r4]) } }
    // CODE -> <Ret>: <Reg8: 0>
    return undefined;
}