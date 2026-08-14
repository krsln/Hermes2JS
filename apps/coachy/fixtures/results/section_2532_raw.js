function describeFiber(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 224>  # String: 'tag' (Identifier)
    // USED → r1 = param1.tag;
    // CODE → <SwitchImm>: <Reg8: 1, UInt32: 193, Addr32: 187, UInt32: 0, UInt32: 27>  # Address: 000000c3  # Jump table: [0000004c, 0000001a, 0000004c, 000000c3, 000000c3, 000000aa, 000000c3, 000000c3, 000000c3, 000000c3, 000000c3, 00000030, 000000c3, 0000007a, 000000c3, 0000004c, 00000092, 000000c3, 000000c3, 00000062, 000000c3, 000000c3, 000000c3, 000000c3, 000000c3, 000000c3, 000000aa, 000000aa]
    // Raw TerminatorSwitch reached Printer. SwitchStructurer should have converted it into a SwitchRegion.
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 1, UInt16: 258>
    // USED → r3 = getEnvironment(0)[258];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 159>  # String: 'type' (Identifier)
    // USED → r2 = param1.type;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 2>
    // USED → r1 = getEnvironment(0)[258].call(undefined, r2);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[258].call(undefined, r2);
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 1, UInt16: 258>
    // USED → r3 = getEnvironment(0)[258];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 159>  # String: 'type' (Identifier)
    // USED → r1 = param1.type;
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 11830>  # String: 'render' (Identifier)
    // USED → r2 = param1.type.render;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 2>
    // USED → r1 = getEnvironment(0)[258].call(undefined, r2);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[258].call(undefined, r2);
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 1, UInt16: 258>
    // USED → r3 = getEnvironment(0)[258];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 159>  # String: 'type' (Identifier)
    // USED → r2 = param1.type;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 1, Reg8: 2>
    // USED → r1 = getEnvironment(0)[258].call(undefined, r2);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[258].call(undefined, r2);
    // ──────────────── Block 4 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 4, Reg8: 1, UInt16: 257>
    // USED → r4 = getEnvironment(0)[257];
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 19812>  # String: 'SuspenseList' (Identifier)
    // USED → r2 = "SuspenseList";
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Call3>: <Reg8: 1, Reg8: 4, Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r1 = getEnvironment(0)[257].call(undefined, "SuspenseList", r1);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[257].call(undefined, "SuspenseList", r1);
    // ──────────────── Block 5 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 4, Reg8: 1, UInt16: 257>
    // USED → r4 = getEnvironment(0)[257];
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 13570>  # String: 'Suspense' (Identifier)
    // USED → r2 = "Suspense";
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Call3>: <Reg8: 1, Reg8: 4, Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r1 = getEnvironment(0)[257].call(undefined, "Suspense", r1);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[257].call(undefined, "Suspense", r1);
    // ──────────────── Block 6 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 4, Reg8: 1, UInt16: 257>
    // USED → r4 = getEnvironment(0)[257];
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    // USED → r3 = undefined;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 13018>  # String: 'Lazy' (Identifier)
    // USED → r2 = "Lazy";
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Call3>: <Reg8: 1, Reg8: 4, Reg8: 3, Reg8: 2, Reg8: 1>
    // USED → r1 = getEnvironment(0)[257].call(undefined, "Lazy", r1);
    // CODE → <Ret>: <Reg8: 1>
    return getEnvironment(0)[257].call(undefined, "Lazy", r1);
    // ──────────────── Block 7 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironmentL>: <Reg8: 3, Reg8: 1, UInt16: 257>
    // USED → r3 = getEnvironment(0)[257];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 2, string_id: 159>  # String: 'type' (Identifier)
    // USED → r2 = param1.type;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <LoadConstNull>: <Reg8: 0>
    // USED → r0 = null;
    // CODE → <Call3>: <Reg8: 0, Reg8: 3, Reg8: 1, Reg8: 2, Reg8: 0>
    // USED → r0 = getEnvironment(0)[257].call(undefined, r2, r0);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[257].call(undefined, r2, r0);
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 11303>  # String: '' (Identifier)
    // USED → r0 = "";
    // CODE → <Ret>: <Reg8: 0>
    return "";
}