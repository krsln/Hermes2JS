function describeFiber(param0, param1) {
    switch (param1.tag) {
        case 1:
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
            // USED → r1 = getEnvironment(0)[258].call(undefined, param1.type);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[258].call(undefined, param1.type);
        case 11:
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
            // USED → r1 = getEnvironment(0)[258].call(undefined, param1.type.render);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[258].call(undefined, param1.type.render);
        case 0:
        case 2:
        case 15:
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
            // USED → r1 = getEnvironment(0)[258].call(undefined, param1.type);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[258].call(undefined, param1.type);
        case 19:
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
            // USED → r1 = getEnvironment(0)[257].call(undefined, "SuspenseList", null);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[257].call(undefined, "SuspenseList", null);
        case 13:
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
            // USED → r1 = getEnvironment(0)[257].call(undefined, "Suspense", null);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[257].call(undefined, "Suspense", null);
        case 16:
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
            // USED → r1 = getEnvironment(0)[257].call(undefined, "Lazy", null);
            // CODE → <Ret>: <Reg8: 1>
            return getEnvironment(0)[257].call(undefined, "Lazy", null);
        case 5:
        case 26:
        case 27:
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
            // USED → r0 = getEnvironment(0)[257].call(undefined, param1.type, null);
            // CODE → <Ret>: <Reg8: 0>
            return getEnvironment(0)[257].call(undefined, param1.type, null);
        default:
            // ──────────────── Block 8 ──────────────── 
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 11303>  # String: '' (Identifier)
            // USED → r0 = "";
            // CODE → <Ret>: <Reg8: 0>
            return "";
    }
}