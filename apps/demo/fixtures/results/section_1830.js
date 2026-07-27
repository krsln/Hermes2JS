function collectExtraData(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    // USED → r8 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined;
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → <GetEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 3, UInt8: 0>
    // USED → r0 = getEnvironment(0)[0];
    // CODE → <GetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 21795>  # String: '_extraSources' (Identifier)
    // USED → r0 = getEnvironment(0)[0]._extraSources;
    // CODE → <Mov>: <Reg8: 4, Reg8: 0>
    // USED → r4 = getEnvironment(0)[0]._extraSources;
    // CODE → <IteratorBegin>: <Reg8: 9, Reg8: 4>
    // USED → r9 = GetIterator(getEnvironment(0)[0]._extraSources);
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 1>
    // USED → r0 = getEnvironment(1);
    // CODE → <LoadConstUInt8>: <Reg8: 7, UInt8: 2>
    // USED → r7 = 2;
    // CODE → <LoadConstZero>: <Reg8: 6>
    // USED → r6 = 0;
    // CODE → <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
    // USED → r5 = 1;
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 1 ──────────────── 
            // CODE → <IteratorNext>: <Reg8: 11, Reg8: 9, Reg8: 4>
            // USED → r11 = GetIterator(getEnvironment(0)[0]._extraSources).next();
            // CODE → <Mov>: <Reg8: 10, Reg8: 9>
            // USED → r10 = GetIterator(getEnvironment(0)[0]._extraSources);
            // CODE → <JStrictEqual>: <Addr8: 47, Reg8: 10, Reg8: 8>  # Address: 0000005a
            if (GetIterator(getEnvironment(0)[0]._extraSources) === undefined) goto label_90;
            // ──────────────── Block 2 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 10, Reg8: 0, UInt8: 2>
            // USED → r10 = getEnvironment(1)[2];
            // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 10, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
            // USED → r10 = getEnvironment(1)[2].default;
            // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 8, Reg8: 11, Reg8: 7>
            // USED → r10 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2);
            // CODE → <GetByVal>: <Reg8: 12, Reg8: 10, Reg8: 6>
            // USED → r12 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2)[0];
            // CODE → <GetByVal>: <Reg8: 10, Reg8: 10, Reg8: 5>
            // USED → r10 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2)[1];
            // CODE → <Mov>: <Reg8: 11, Reg8: 2>
            // USED → r11 = {  };
            // CODE → <Call1>: <Reg8: 10, Reg8: 10, Reg8: 8>
            // USED → r10 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2)[1].call(undefined);
            // CODE → <PutByVal>: <Reg8: 11, Reg8: 12, Reg8: 10>
            {  }[getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2)[0]] = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._extraSources).next(), 2)[1].call(undefined);
            // CODE → <Jmp>: <Addr8: -45>  # Address: 00000024
            goto label_36;
        }
        // LOOP → END
    }
    catch (caughtException) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 9, UInt8: 1>
        // Error: IteratorClose at address 85: Invalid arguments: Reg8: 9, UInt8: 1;
        // CODE → <Throw>: <Reg8: 4>
        throw caughtException;
    }
    // ──────────────── Block 4 ──────────────── 
    // CODE → <NewObject>: <Reg8: 1>
    // USED → r1 = {  };
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 0>
    // USED → r3 = getEnvironment(0)[0];
    // CODE → <GetById>: <Reg8: 9, Reg8: 3, UInt8: 3, string_id: 21798>  # String: '_fileSources' (Identifier)
    // USED → r9 = getEnvironment(0)[0]._fileSources;
    // CODE → <Mov>: <Reg8: 3, Reg8: 9>
    // USED → r3 = getEnvironment(0)[0]._fileSources;
    // CODE → <IteratorBegin>: <Reg8: 4, Reg8: 3>
    // USED → r4 = GetIterator(getEnvironment(0)[0]._fileSources);
    try {
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 5 ──────────────── 
            // CODE → <IteratorNext>: <Reg8: 10, Reg8: 4, Reg8: 3>
            // USED → r10 = GetIterator(getEnvironment(0)[0]._fileSources).next();
            // CODE → <Mov>: <Reg8: 9, Reg8: 4>
            // USED → r9 = GetIterator(getEnvironment(0)[0]._fileSources);
            // CODE → <JStrictEqual>: <Addr8: 47, Reg8: 9, Reg8: 8>  # Address: 000000a2
            if (GetIterator(getEnvironment(0)[0]._fileSources) === undefined) goto label_162;
            // ──────────────── Block 6 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 0, UInt8: 2>
            // USED → r9 = getEnvironment(1)[2];
            // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
            // USED → r9 = getEnvironment(1)[2].default;
            // CODE → <Call3>: <Reg8: 9, Reg8: 9, Reg8: 8, Reg8: 10, Reg8: 7>
            // USED → r9 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2);
            // CODE → <GetByVal>: <Reg8: 11, Reg8: 9, Reg8: 6>
            // USED → r11 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2)[0];
            // CODE → <GetByVal>: <Reg8: 9, Reg8: 9, Reg8: 5>
            // USED → r9 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2)[1];
            // CODE → <Mov>: <Reg8: 10, Reg8: 1>
            // USED → r10 = {  };
            // CODE → <Call1>: <Reg8: 9, Reg8: 9, Reg8: 8>
            // USED → r9 = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2)[1].call(undefined);
            // CODE → <PutByVal>: <Reg8: 10, Reg8: 11, Reg8: 9>
            {  }[getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2)[0]] = getEnvironment(1)[2].default.call(undefined, GetIterator(getEnvironment(0)[0]._fileSources).next(), 2)[1].call(undefined);
            // CODE → <Jmp>: <Addr8: -45>  # Address: 0000006c
            goto label_108;
        }
        // LOOP → END
    }
    catch (caughtException) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → <IteratorClose>: <Reg8: 4, UInt8: 1>
        // Error: IteratorClose at address 157: Invalid arguments: Reg8: 4, UInt8: 1;
        // CODE → <Throw>: <Reg8: 3>
        throw caughtException;
    }
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 7>
    // USED → r3 = getEnvironment(1)[7];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(1)[7].default;
    // CODE → <LoadConstNull>: <Reg8: 4>
    // USED → r4 = null;
    if (getEnvironment(1)[7].default != null) {
        // ──────────────── Block 9 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 7>
        // USED → r3 = getEnvironment(1)[7];
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
        // USED → r3 = getEnvironment(1)[7].default;
        // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 13973>  # String: 'setExtraData' (Identifier)
        // USED → r3 = getEnvironment(1)[7].default.setExtraData;
        if (getEnvironment(1)[7].default.setExtraData != null) {
            // ──────────────── Block 10 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 7>
            // USED → r3 = getEnvironment(1)[7];
            // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 3, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
            // USED → r7 = getEnvironment(1)[7].default;
            // CODE → <GetById>: <Reg8: 6, Reg8: 7, UInt8: 4, string_id: 13973>  # String: 'setExtraData' (Identifier)
            // USED → r6 = getEnvironment(1)[7].default.setExtraData;
            // CODE → <Mov>: <Reg8: 5, Reg8: 2>
            // USED → r5 = {  };
            // CODE → <Mov>: <Reg8: 3, Reg8: 1>
            // USED → r3 = {  };
            // CODE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 5, Reg8: 3>
            r3 = getEnvironment(1)[7].default.setExtraData({  }, {  });
        }
    }
    // ──────────────── Block 11 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 6>
    // USED → r3 = getEnvironment(1)[6];
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
    // USED → r3 = getEnvironment(1)[6].default;
    if (getEnvironment(1)[6].default != null) {
        // ──────────────── Block 12 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 0, UInt8: 6>
        // USED → r3 = getEnvironment(1)[6];
        // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 3, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
        // USED → r3 = getEnvironment(1)[6].default;
        // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 13973>  # String: 'setExtraData' (Identifier)
        // USED → r3 = getEnvironment(1)[6].default.setExtraData;
        if (getEnvironment(1)[6].default.setExtraData != null) {
            // ──────────────── Block 13 ──────────────── 
            // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 6>
            // USED → r0 = getEnvironment(1)[6];
            // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 0, UInt8: 2, string_id: 110>  # String: 'default' (Identifier)
            // USED → r5 = getEnvironment(1)[6].default;
            // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 4, string_id: 13973>  # String: 'setExtraData' (Identifier)
            // USED → r4 = getEnvironment(1)[6].default.setExtraData;
            // CODE → <Mov>: <Reg8: 3, Reg8: 2>
            // USED → r3 = {  };
            // CODE → <LoadConstString>: <Reg8: 0, string_id: 5208>  # String: 'From BugReporting.js' (String)
            // USED → r0 = "From BugReporting.js";
            // CODE → <Call3>: <Reg8: 0, Reg8: 4, Reg8: 5, Reg8: 3, Reg8: 0>
            r0 = getEnvironment(1)[6].default.setExtraData({  }, "From BugReporting.js");
        }
    }
    // ──────────────── Block 14 ──────────────── 
    // CODE → <NewObject>: <Reg8: 0>
    // USED → r0 = {  };
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 2, string_id: 11602>  # String: 'extras' (Identifier)
    // USED → r0 = { extras: {  } };
    // CODE → <PutNewOwnById>: <Reg8: 0, Reg8: 1, string_id: 13507>  # String: 'files' (Identifier)
    // USED → r0 = { extras: {  }, files: {  } };
    // CODE → <Ret>: <Reg8: 0>
    return { extras: {  }, files: {  } };
}