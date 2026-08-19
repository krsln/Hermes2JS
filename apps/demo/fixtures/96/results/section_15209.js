function function_15209() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 5>
    r5 = createEnvironment()
    // CODE → addr:  2 | <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15210>  # Function: [#15210 Counter of 148 bytes]: 1 params @ offset 0x0026be26
    // USED → r4 = Counter();
    // CODE → addr:  7 | <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 4>
    r5[0] = Counter()
    // CODE → addr: 11 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 14 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 3>
    r0 = r0[3]
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r0.default;
    // CODE → addr: 23 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 25 | <LoadConstString>: <Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r1 = "value";
    // CODE → addr: 29 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "value"
    // CODE → addr: 33 | <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15211>  # Function: [#15211 get of 59 bytes]: 1 params @ offset 0x0026beba
    // USED → r1 = get();
    // CODE → addr: 38 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → addr: 42 | <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15212>  # Function: [#15212 set of 92 bytes]: 2 params @ offset 0x0026bef5
    // USED → r1 = set(param1);
    // CODE → addr: 47 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 185>  # String: 'set' (Identifier)
    r0.set = set(param1)
    // CODE → addr: 51 | <NewArray>: <Reg8: 2, UInt16: 3>
    r2 = []
    // CODE → addr: 55 | <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r2[0] = r0;
    // CODE → addr: 59 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 61 | <LoadConstString>: <Reg8: 1, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r1 = "increment";
    // CODE → addr: 65 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "increment"
    // CODE → addr: 69 | <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15213>  # Function: [#15213 increment of 66 bytes]: 1 params @ offset 0x0026bf51
    // USED → r1 = increment();
    // CODE → addr: 74 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = increment()
    // CODE → addr: 78 | <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 1>
    // USED → r2 = (r2[0] = r0)[1] = r0;
    // CODE → addr: 82 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr: 84 | <LoadConstString>: <Reg8: 1, string_id: 10172>  # String: 'describe' (Identifier)
    // USED → r1 = "describe";
    // CODE → addr: 88 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "describe"
    // CODE → addr: 92 | <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15214>  # Function: [#15214 describe of 59 bytes]: 1 params @ offset 0x0026bf93
    // USED → r1 = describe();
    // CODE → addr: 97 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    r0.value = describe()
    // CODE → addr:101 | <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 2>
    // USED → r2 = ((r2[0] = r0)[1] = r0)[2] = r0;
    // CODE → addr:105 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr:107 | <LoadConstString>: <Reg8: 1, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r1 = "instanceCount";
    // CODE → addr:111 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "instanceCount"
    // CODE → addr:115 | <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15215>  # Function: [#15215 get of 59 bytes]: 1 params @ offset 0x0026bfce
    // USED → r1 = get();
    // CODE → addr:120 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    r0.get = get()
    // CODE → addr:124 | <NewArray>: <Reg8: 1, UInt16: 2>
    r1 = []
    // CODE → addr:128 | <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = r1[0] = r0;
    // CODE → addr:132 | <NewObject>: <Reg8: 0>
    r0 = {  }
    // CODE → addr:134 | <LoadConstString>: <Reg8: 6, string_id: 7840>  # String: 'reset' (Identifier)
    // USED → r6 = "reset";
    // CODE → addr:138 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 6, string_id: 117>  # String: 'key' (Identifier)
    r0.key = "reset"
    // CODE → addr:142 | <CreateClosure>: <Reg8: 5, Reg8: 5, function_id: 15216>  # Function: [#15216 reset of 61 bytes]: 1 params @ offset 0x0026c009
    // USED → r5 = reset();
    // CODE → addr:147 | <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r0.value = reset()
    // CODE → addr:151 | <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = (r1[0] = r0)[1] = r0;
    // CODE → addr:155 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:157 | <Call4>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 4, Reg8: 2, Reg8: 1>
    r0 = r0.default(Counter(), r2, r1)
    // CODE → addr:164 | <Ret>: <Reg8: 0>
    return r0;
}