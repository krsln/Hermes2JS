async function* anon_11947(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <StartGenerator>: <>
    // StartGenerator
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    // USED → r0 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    // USED → r5 = __resumeIsReturn;
    // CODE → <JmpTrueLong>: <Addr32: 311, Reg8: 5>  # Address: 0000013e
    if (__resumeIsReturn) goto label_318;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 1>
    // USED → r4 = param1;
    // CODE → <LoadParam>: <Reg8: 3, UInt8: 2>
    // USED → r3 = param2;
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    r6 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 2>
    r2 = undefined
    // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 17057>  # String: '_request' (Identifier)
    // USED → r7 = this._request;
    // CODE → <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 4, Reg8: 3>
    // USED → r3 = await this._request(r4, r3);
    // CODE → <SaveGenerator>: <Addr8: 4>  # Address: 00000029
    goto label_41;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <Ret>: <Reg8: 3>
    return await this._request(r4, r3);
    // ──────────────── Block 3 ──────────────── 
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r3 = await yield;
    // CODE → <ResumeGenerator>: <Reg8: 3, Reg8: 4>
    // USED → r4 = __resumeIsReturn;
    // CODE → <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 00000032
    if (__resumeIsReturn) goto label_50;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    return await yield;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 3>
    return await yield;
    // ──────────────── Block 6 ──────────────── 
    // CODE → <Catch>: <Reg8: 7>
    // USED → r7 = caughtException;
    // CODE → <Mov>: <Reg8: 1, Reg8: 7>
    // USED → r1 = caughtException;
    // CODE → <GetGlobalObject>: <Reg8: 3>
    // USED → r3 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error;
    // CODE → <InstanceOf>: <Reg8: 4, Reg8: 7, Reg8: 4>
    // USED → r4 = caughtException instanceof globalThis.Error;
    // CODE → <JmpFalseLong>: <Addr32: 246, Reg8: 4>  # Address: 0000013c
    if (!(caughtException instanceof globalThis.Error)) goto label_316;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r4 = globalThis.Error;
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r4 = globalThis.Error.captureStackTrace;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
    // USED → r8 = globalThis.Error;
    // CODE → <JmpTrue>: <Addr8: 25, Reg8: 4>  # Address: 00000079
    if (globalThis.Error.captureStackTrace) goto label_121;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 4, string_id: 158>  # String: 'prototype' (Identifier)
    r4 = globalThis.Error.prototype
    // CODE → <CreateThis>: <Reg8: 7, Reg8: 4, Reg8: 8>
    // USED → r7 = CreateThis(r4);
    // CODE → <Mov>: <Reg8: 12, Reg8: 7>
    // USED → r12 = CreateThis(r4);
    // CODE → <Construct>: <Reg8: 4, Reg8: 8, UInt8: 1>
    // USED → r4 = new globalThis.Error();
    // CODE → <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
    // USED → r6 = new globalThis.Error();
    // CODE → <Jmp>: <Addr8: 16>  # Address: 00000087
    goto label_135;
    // ──────────────── Block 9 ──────────────── 
    // CODE → <GetById>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
    // USED → r7 = globalThis.Error.captureStackTrace;
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = new globalThis.Error();
    // CODE → <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
    r4 = globalThis.Error.captureStackTrace(r4)
    // ──────────────── Block 10 ──────────────── 
    // CODE → <Mov>: <Reg8: 4, Reg8: 6>
    // USED → r4 = new globalThis.Error();
    // CODE → <GetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r7 = new globalThis.Error().stack;
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 11303>  # String: '' (Identifier)
    // USED → r8 = "";
    // CODE → <Mov>: <Reg8: 4, Reg8: 8>
    r4 = ""
    // CODE → <JmpFalse>: <Addr8: 34, Reg8: 7>  # Address: 000000b9
    if (!new globalThis.Error().stack) goto label_185;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <GetById>: <Reg8: 9, Reg8: 6, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r9 = new globalThis.Error().stack;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
    // USED → r7 = new globalThis.Error().stack.replace;
    // CODE → <CreateRegExp>: <Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168>  # String: '^.+\\n' (String)  # String: '' (Identifier)
    // USED → r6 = /^.+\\n/;
    // CODE → <Call3>: <Reg8: 4, Reg8: 7, Reg8: 9, Reg8: 6, Reg8: 8>
    // USED → r4 = new globalThis.Error().stack.replace(r6, "");
    // ──────────────── Block 12 ──────────────── 
    // CODE → <Mov>: <Reg8: 2, Reg8: 4>
    // USED → r2 = new globalThis.Error().stack.replace(r6, "");
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    // USED → r4 = caughtException;
    // CODE → <GetById>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r4 = caughtException.stack;
    // CODE → <JmpTrue>: <Addr8: 17, Reg8: 4>  # Address: 000000d6
    if (caughtException.stack) goto label_214;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <Mov>: <Reg8: 6, Reg8: 1>
    // USED → r6 = caughtException;
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = new globalThis.Error().stack.replace(r6, "");
    // CODE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
    caughtException.stack = new globalThis.Error().stack.replace(r6, "")
    // CODE → <Jmp>: <Addr8: 100>  # Address: 00000138
    goto label_312;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    // USED → r4 = new globalThis.Error().stack.replace(r6, "");
    // CODE → <JmpFalse>: <Addr8: 95, Reg8: 4>  # Address: 00000138
    if (!new globalThis.Error().stack.replace(r6, "")) goto label_312;
    // ──────────────── Block 15 ──────────────── 
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 7, string_id: 50>  # String: 'String' (Identifier)
    // USED → r4 = globalThis.String;
    // CODE → <Mov>: <Reg8: 3, Reg8: 1>
    // USED → r3 = caughtException;
    // CODE → <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r3 = caughtException.stack;
    // CODE → <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
    // USED → r5 = globalThis.String.call(undefined, r3);
    // CODE → <GetById>: <Reg8: 4, Reg8: 5, UInt8: 8, string_id: 19080>  # String: 'endsWith' (Identifier)
    // USED → r4 = globalThis.String.call(undefined, r3).endsWith;
    // CODE → <Mov>: <Reg8: 7, Reg8: 2>
    // USED → r7 = new globalThis.Error().stack.replace(r6, "");
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
    // USED → r6 = new globalThis.Error().stack.replace(r6, "").replace;
    // CODE → <CreateRegExp>: <Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169>  # String: '^.+\\n.+\\n' (String)  # String: '' (Identifier)
    // USED → r3 = /^.+\\n.+\\n/;
    // CODE → <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 8>
    // USED → r3 = new globalThis.Error().stack.replace(r6, "").replace(r3, "");
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    // USED → r3 = globalThis.String.call(undefined, r3).endsWith(r3);
    // CODE → <JmpTrue>: <Addr8: 33, Reg8: 3>  # Address: 00000138
    // → r3 = globalThis.String.call(undefined, r3).endsWith(r3)
    if (globalThis.String.call(undefined, r3).endsWith(r3)) goto label_312;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <Mov>: <Reg8: 3, Reg8: 1>
    // USED → r3 = caughtException;
    // CODE → <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
    // USED → r4 = caughtException.stack;
    // CODE → <Mov>: <Reg8: 5, Reg8: 2>
    // USED → r5 = new globalThis.Error().stack.replace(r6, "");
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 12321>  # String: '\n' (Identifier)
    // USED → r2 = "\\n";
    // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 5>
    // USED → r2 = "\\n" + new globalThis.Error().stack.replace(r6, "");
    // CODE → <Add>: <Reg8: 2, Reg8: 4, Reg8: 2>
    // USED → r2 = caughtException.stack + ("\\n" + new globalThis.Error().stack.replace(r6, ""));
    // CODE → <PutById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
    caughtException.stack = caughtException.stack + ("\\n" + new globalThis.Error().stack.replace(r6, ""))
    // ──────────────── Block 17 ──────────────── 
    // CODE → <Jmp>: <Addr8: 4>  # Address: 0000013c
    goto label_316;
    // ──────────────── Block 18 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    r2 = caughtException
    // ──────────────── Block 19 ──────────────── 
    // CODE → <Throw>: <Reg8: 1>
    throw caughtException;
    // ──────────────── Block 20 ──────────────── 
    // CODE → <CompleteGenerator>: <>
    // CompleteGenerator
    // CODE → <Ret>: <Reg8: 0>
    return await yield;
}