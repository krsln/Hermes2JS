function function_15209(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 5>
    // USED → r5 = createEnvironment();
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15210>  # Function: [#15210 Counter of 148 bytes]: 1 params @ offset 0x0026be26
    // USED → r4 = Counter;
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 4>
    createEnvironment()[0] = Counter
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 3>
    // USED → r0 = getEnvironment(0)[3];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(0)[3].default;
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r1 = "value";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    // USED → r0 = { key: "value" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15211>  # Function: [#15211 get of 59 bytes]: 1 params @ offset 0x0026beba
    // USED → r1 = get;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    // USED → r0 = { key: "value", get: get };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15212>  # Function: [#15212 set of 92 bytes]: 2 params @ offset 0x0026bef5
    // USED → r1 = set;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 185>  # String: 'set' (Identifier)
    // USED → r0 = { key: "value", get: get, set: set };
    // CODE → <NewArray>: <Reg8: 2, UInt16: 3>
    // USED → r2 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = [{ key: "value", get: get, set: set }];
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10830>  # String: 'increment' (Identifier)
    // USED → r1 = "increment";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    // USED → r0 = { key: "increment" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15213>  # Function: [#15213 increment of 66 bytes]: 1 params @ offset 0x0026bf51
    // USED → r1 = increment;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r0 = { key: "increment", value: increment };
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 1>
    // USED → r2 = [{ key: "value", get: get, set: set }, { key: "increment", value: increment }];
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10172>  # String: 'describe' (Identifier)
    // USED → r1 = "describe";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    // USED → r0 = { key: "describe" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15214>  # Function: [#15214 describe of 59 bytes]: 1 params @ offset 0x0026bf93
    // USED → r1 = describe;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r0 = { key: "describe", value: describe };
    // CODE → <PutOwnByIndex>: <Reg8: 2, Reg8: 0, UInt8: 2>
    // USED → r2 = [{ key: "value", get: get, set: set }, { key: "increment", value: increment }, { key: "describe", value: describe }];
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 10838>  # String: 'instanceCount' (Identifier)
    // USED → r1 = "instanceCount";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 117>  # String: 'key' (Identifier)
    // USED → r0 = { key: "instanceCount" };
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 5, function_id: 15215>  # Function: [#15215 get of 59 bytes]: 1 params @ offset 0x0026bfce
    // USED → r1 = get;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 1, string_id: 50>  # String: 'get' (Identifier)
    // USED → r0 = { key: "instanceCount", get: get };
    // CODE → <NewArray>: <Reg8: 1, UInt16: 2>
    // USED → r1 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = [{ key: "instanceCount", get: get }];
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 7840>  # String: 'reset' (Identifier)
    // USED → r6 = "reset";
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 6, string_id: 117>  # String: 'key' (Identifier)
    // USED → r0 = { key: "reset" };
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 5, function_id: 15216>  # Function: [#15216 reset of 61 bytes]: 1 params @ offset 0x0026c009
    // USED → r5 = reset;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 0, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    // USED → r0 = { key: "reset", value: reset };
    // CODE → <PutOwnByIndex>: <Reg8: 1, Reg8: 0, UInt8: 1>
    // USED → r1 = [{ key: "instanceCount", get: get }, { key: "reset", value: reset }];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call4>: <Reg8: 0, Reg8: 3, Reg8: 0, Reg8: 4, Reg8: 2, Reg8: 1>
    // USED → r0 = getEnvironment(0)[3].default.call(undefined, Counter, [{ key: "value", get: get, set: set }, { key: "increment", value: increment }, { key: "describe", value: describe }], [{ key: "instanceCount", get: get }, { key: "reset", value: reset }]);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[3].default.call(undefined, Counter, [{ key: "value", get: get, set: set }, { key: "increment", value: increment }, { key: "describe", value: describe }], [{ key: "instanceCount", get: get }, { key: "reset", value: reset }]);
}