function describeFiber(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 195>  # String: 'tag' (Identifier)
    // USED → r4 = param1.tag;
    // CODE → <UIntSwitchImm>: <Reg8: 4, UInt32: 214, Addr32: 208, UInt32: 0, UInt32: 31>  # Address: 000000db
    // Raw TerminatorSwitch reached Printer. SwitchStructurer should have converted it into a SwitchRegion.
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 6>
    // USED → r5 = getParentEnvironment(0)[6];
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 8747>  # String: 'Activity' (Identifier)
    // USED → r4 = "Activity";
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
    // USED → r4 = getParentEnvironment(0)[6].call(0, "Activity");
    // CODE → <Ret>: <Reg8: 4>
    return getParentEnvironment(0)[6].call(0, "Activity");
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 8>
    // USED → r5 = getParentEnvironment(0)[8];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 1>  # String: 'type' (Identifier)
    // USED → r4 = param1.type;
    // CODE → <LoadConstTrue>: <Reg8: 1>
    // USED → r1 = true;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 1>
    // USED → r4 = getParentEnvironment(0)[8].call(0, param1.type, true);
    // CODE → <Ret>: <Reg8: 4>
    return getParentEnvironment(0)[8].call(0, param1.type, true);
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 8>
    // USED → r5 = getParentEnvironment(0)[8];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 1>  # String: 'type' (Identifier)
    // USED → r4 = param1.type;
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 2, string_id: 7445>  # String: 'render' (Identifier)
    // USED → r4 = param1.type.render;
    // CODE → <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 1>
    // USED → r4 = getParentEnvironment(0)[8].call(0, param1.type.render, false);
    // CODE → <Ret>: <Reg8: 4>
    return getParentEnvironment(0)[8].call(0, param1.type.render, false);
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 8>
    // USED → r5 = getParentEnvironment(0)[8];
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 2, UInt8: 1, string_id: 1>  # String: 'type' (Identifier)
    // USED → r4 = param1.type;
    // CODE → <LoadConstFalse>: <Reg8: 1>
    // USED → r1 = false;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call3>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 1>
    // USED → r4 = getParentEnvironment(0)[8].call(0, param1.type, false);
    // CODE → <Ret>: <Reg8: 4>
    return getParentEnvironment(0)[8].call(0, param1.type, false);
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 6>
    // USED → r5 = getParentEnvironment(0)[6];
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 13734>  # String: 'SuspenseList' (Identifier)
    // USED → r4 = "SuspenseList";
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
    // USED → r4 = getParentEnvironment(0)[6].call(0, "SuspenseList");
    // CODE → <Ret>: <Reg8: 4>
    return getParentEnvironment(0)[6].call(0, "SuspenseList");
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 2, UInt8: 3, string_id: 97>  # String: 'child' (Identifier)
    // USED → r5 = param1.child;
    // CODE → <JStrictEqual>: <Addr8: 10, Reg8: 5, Reg8: 4>  # Address: 00000096
    if (param1.child === param2) goto label_150;
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 5 ──────────────── 
        // CODE → <Ret>: <Reg8: 4>
        return getParentEnvironment(0)[6].call(0, "Suspense Fallback");
        // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 6>
        // USED → r5 = getParentEnvironment(0)[6];
        // CODE → <LoadConstString>: <Reg8: 4, string_id: 7829>  # String: 'Lazy' (Identifier)
        // USED → r4 = "Lazy";
        // CODE → <LoadConstZero>: <Reg8: 0>
        // USED → r0 = 0;
        // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
        // USED → r4 = getParentEnvironment(0)[6].call(0, "Lazy");
        // CODE → <Ret>: <Reg8: 4>
        return getParentEnvironment(0)[6].call(0, "Lazy");
        // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 6>
        // USED → r3 = getParentEnvironment(0)[6];
        // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 2, UInt8: 1, string_id: 1>  # String: 'type' (Identifier)
        // USED → r2 = param1.type;
        // CODE → <LoadConstZero>: <Reg8: 0>
        // USED → r0 = 0;
        // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 2>
        // USED → r2 = getParentEnvironment(0)[6].call(0, param1.type);
        // CODE → <Ret>: <Reg8: 2>
        return getParentEnvironment(0)[6].call(0, param1.type);
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 3 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 6>
            // USED → r5 = getParentEnvironment(0)[6];
            // CODE → <LoadConstString>: <Reg8: 4, string_id: 8506>  # String: 'Suspense' (Identifier)
            // USED → r4 = "Suspense";
            // CODE → <LoadConstZero>: <Reg8: 0>
            // USED → r0 = 0;
            // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 0, Reg8: 4>
            r4 = getParentEnvironment(0)[6].call(0, "Suspense")
            // CODE → <Jmp>: <Addr8: 17>  # Address: 000000b6
            goto label_182;
        }
        // LOOP → END
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 4 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 3, UInt8: 6>
            // USED → r6 = getParentEnvironment(0)[6];
            // CODE → <LoadConstString>: <Reg8: 5, string_id: 920>  # String: 'Suspense Fallback' (String)
            // USED → r5 = "Suspense Fallback";
            // CODE → <LoadConstZero>: <Reg8: 0>
            // USED → r0 = 0;
            // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 5>
            // USED → r4 = getParentEnvironment(0)[6].call(0, "Suspense Fallback");
            // ──────────────── Block 2 ──────────────── 
            // CODE → <LoadConstNull>: <Reg8: 1>
            // USED → r1 = null;
            // CODE → <JStrictNotEqual>: <Addr8: 21, Reg8: 1, Reg8: 4>  # Address: 000000a7
            if (null !== param2) goto label_167;
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 6249>  # String: '' (Identifier)
    // USED → r2 = "";
    // CODE → <Ret>: <Reg8: 2>
    return "";
}