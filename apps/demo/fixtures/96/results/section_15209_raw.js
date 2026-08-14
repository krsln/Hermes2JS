function function_15209() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 5>
    // USED → r5 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15210>  # Function: [#15210 Counter of 148 bytes]: 1 params @ offset 0x0026be26
    // USED → r4 = Counter();
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = Counter()
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 3>
    // USED → r0 = getEnvironment(0)[3];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(0)[3].default;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r1 = "value";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "value"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15211>  # Function: [#15211 get of 59 bytes]: 1 params @ offset 0x0026beba
    // USED → r1 = get();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15212>  # Function: [#15212 set of 92 bytes]: 2 params @ offset 0x0026bef5
    // USED → r1 = set(param1);
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 185>  # String: 'set' (Identifier)
    r0.set = set(param1)
    // CODE → <NewArray>: <Reg8: 2, UInt16: 3>
    r2 = []
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r2[0] = r0;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r1 = "increment";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "increment"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15213>  # Function: [#15213 increment of 66 bytes]: 1 params @ offset 0x0026bf51
    // USED → r1 = increment();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = increment()
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 1>
    // USED → r2 = (r2[0] = r0)[1] = r0;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10172>  # String: 'describe' (Identifier)
    // USED → r1 = "describe";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "describe"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15214>  # Function: [#15214 describe of 59 bytes]: 1 params @ offset 0x0026bf93
    // USED → r1 = describe();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = describe()
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 2>
    // USED → r2 = ((r2[0] = r0)[1] = r0)[2] = r0;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r1 = "instanceCount";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "instanceCount"
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15215>  # Function: [#15215 get of 59 bytes]: 1 params @ offset 0x0026bfce
    // USED → r1 = get();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
    r1 = []
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = r1[0] = r0;
    // CODE → <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 7840>  # String: 'reset' (Identifier)
    // USED → r6 = "reset";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 6, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "reset"
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 5, function_id: 15216>  # Function: [#15216 reset of 61 bytes]: 1 params @ offset 0x0026c009
    // USED → r5 = reset();
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r0.value = reset()
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = (r1[0] = r0)[1] = r0;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call4>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r0 = getEnvironment(0)[3].default.call(undefined, Counter(), r2, r1);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[3].default.call(undefined, Counter(), r2, r1);
}