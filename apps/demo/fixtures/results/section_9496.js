function setTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4745>  # String: '__BC:Collections/MapSetTests/setTest/start' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/setTest/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/setTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 2, string_id: 31>  # String: 'Set' (Identifier)
    // USED → r3 = globalThis.Set;
    // CODE → <CreateThisForNew>: <Reg8: 2, Reg8: 3, UInt8: 3>
    // USED → r2 = __uninitialized_this_for_new__;
    // CODE → <NewArrayWithBuffer>: <Reg8: 10, UInt16: 6, UInt16: 6, UInt16: 48500>  # Array: [1, 2, 2, 3, 3, 3]
    // USED → r10 = [1, 2, 2, 3, 3, 3];
    // CODE → <Mov>: <Reg8: 11, Reg8: 2>
    // USED → r11 = __uninitialized_this_for_new__;
    // CODE → <Construct>: <Reg8: 0, Reg8: 3, UInt8: 2>
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__);
    // CODE → <SelectObject>: <Reg8: 3, Reg8: 2, Reg8: 0>
    // USED → r3 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 0, Reg8: 3, UInt8: 4, string_id: 69>  # String: 'size' (Identifier)
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).size;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(new Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).size)
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 5, string_id: 79>  # String: 'add' (Identifier)
    // USED → r2 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).add;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 4>
    // USED → r0 = 4;
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    r0 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).add(4)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 6, string_id: 11>  # String: 'has' (Identifier)
    // USED → r5 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).has;
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → <Call2>: <Reg8: 0, Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r0 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).has(2);
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
    console.log(new Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__).has(2))
    // CODE → <Mov>: <Reg8: 2, Reg8: 3>
    // USED → r2 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__);
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 2>
    // USED → r4 = GetIterator(r2);
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 5, Reg8: 2>
        r5 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__)
        // CODE → <IteratorNext>: <Reg8: 7, Reg8: 4, Reg8: 5>
        // USED → r7 = GetIterator(r2).next();
        // CODE → <Mov>: <Reg8: 5, Reg8: 4>
        // USED → r5 = GetIterator(r2);
        if (GetIterator(r2) !== undefined) {
            // ──────────────── Block 2 ──────────────── 
            // CODE → <TryGetById>: <Reg8: 6, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r6 = globalThis.console;
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r5 = globalThis.console.log;
            // CODE → <Call2>: <Reg8: 5, Reg8: 5, Reg8: 6, Reg8: 7>
            console.log(GetIterator(r2).next())
            // CODE → <Jmp>: <Addr8: -30>  # Address: 0000007a
            goto label_122;
        }
    }
    // LOOP → END
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
    GetIterator(r2).return()
    // CODE → <Throw>: <Reg8: 2>
    throw caughtException;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <NewArray>: <Reg8: 4, UInt16: 0>
    r4 = []
    // CODE → <LoadConstZero>: <Reg8: 8>
    r8 = 0
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    r10 = r4
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = new globalThis.Set([1, 2, 2, 3, 3, 3], __uninitialized_this_for_new__)
    // CODE → <CallBuiltin>: <Reg8: 2, UInt8: 48, UInt8: 4>  # Built-in function: [#48 applyArguments]
    r2 = applyArguments(r-2, r-1, r0, r1)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
    console.log(r4)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4741>  # String: '__BC:Collections/MapSetTests/setTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/setTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/setTest/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}