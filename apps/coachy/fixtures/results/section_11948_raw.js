function _request(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2;
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this;
    // CODE → <CreateEnvironment>: <Reg8: 9>
    // USED → r9 = createEnvironment();
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    createEnvironment()[0] = param2
    // CODE → <LoadConstUndefined>: <Reg8: 11>
    // USED → r11 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 13>
    r13 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <TypeOf>: <Reg8: 14, Reg8: 6>
    // USED → r14 = typeof param1;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 12185>  # String: 'string' (Identifier)
    // USED → r10 = "string";
    // CODE → <JStrictEqual>: <Addr8: 18, Reg8: 14, Reg8: 10>  # Address: 0000003a
    // → r14 = typeof param1
    if (r14 === "string") goto label_58;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 14, Reg8: 6>
    // USED → r14 = param1;
    // CODE → <JmpTrue>: <Addr8: 5, Reg8: 14>  # Address: 00000034
    if (param1) goto label_52;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewObject>: <Reg8: 14>
    r14 = {  }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 14>
    createEnvironment()[0] = r14
    // CODE → <Jmp>: <Addr8: 20>  # Address: 0000004c
    goto label_76;
    // ──────────────── Block 4 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 0000003f
    if (param2) goto label_63;
    // ──────────────── Block 5 ──────────────── 
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    createEnvironment()[0] = r2
    // CODE → <PutById>: <Reg8: 2, Reg8: 6, UInt8: 1, string_id: 14158>  # String: 'url' (Identifier)
    r2.url = param1
    // CODE → <Mov>: <Reg8: 14, Reg8: 2>
    // USED → r14 = r2;
    // ──────────────── Block 7 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 6, UInt8: 1>
    // USED → r6 = getEnvironment(1);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 7>
    // USED → r2 = getEnvironment(1)[7];
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r10 = getEnvironment(1)[7].default;
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults;
    // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 2, Reg8: 14>
    // USED → r10 = getEnvironment(1)[7].default.call(undefined, r2, r14);
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 10>
    createEnvironment()[0] = getEnvironment(1)[7].default.call(undefined, r2, r14)
    // CODE → <GetById>: <Reg8: 19, Reg8: 10, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r19 = getEnvironment(1)[7].default.call(undefined, r2, r14).transitional;
    // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 4, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    // USED → r14 = getEnvironment(1)[7].default.call(undefined, r2, r14).paramsSerializer;
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 10, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    // USED → r17 = getEnvironment(1)[7].default.call(undefined, r2, r14).headers;
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 17>
    createEnvironment()[1] = getEnvironment(1)[7].default.call(undefined, r2, r14).headers
    // CODE → <JStrictEqual>: <Addr8: 100, Reg8: 19, Reg8: 11>  # Address: 000000e1
    // → r19 = getEnvironment(1)[7].default.call(undefined, r2, r14).transitional
    if (r19 === undefined) goto label_225;
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // USED → r2 = getEnvironment(1)[9];
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = getEnvironment(1)[9].default;
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = getEnvironment(1)[9].default.assertOptions;
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  };
    // CODE → <LoadFromEnvironment>: <Reg8: 21, Reg8: 6, UInt8: 11>
    // USED → r21 = getEnvironment(1)[11];
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = getEnvironment(1)[11].transitional;
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = getEnvironment(1)[11].boolean;
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = getEnvironment(1)[11].transitional(r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
    r15.silentJSONParsing = getEnvironment(1)[11].transitional(r2)
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = getEnvironment(1)[11].transitional;
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = getEnvironment(1)[11].boolean;
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = getEnvironment(1)[11].transitional(r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 17756>  # String: 'forcedJSONParsing' (Identifier)
    r15.forcedJSONParsing = getEnvironment(1)[11].transitional(r2)
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = getEnvironment(1)[11].transitional;
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = getEnvironment(1)[11].boolean;
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = getEnvironment(1)[11].transitional(r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 22889>  # String: 'clarifyTimeoutError' (Identifier)
    r15.clarifyTimeoutError = getEnvironment(1)[11].transitional(r2)
    // CODE → <LoadConstFalse>: <Reg8: 2>
    // USED → r2 = false;
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 2>
    r2 = getEnvironment(1)[9].default.assertOptions(r19, r15, r2)
    // ──────────────── Block 9 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null;
    // CODE → <JEqual>: <Addr8: 94, Reg8: 14, Reg8: 2>  # Address: 00000141
    if (r14 == null) goto label_321;
    // ──────────────── Block 10 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 3>
    // USED → r2 = getEnvironment(1)[3];
    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = getEnvironment(1)[3].default;
    // CODE → <GetById>: <Reg8: 2, Reg8: 15, UInt8: 8, string_id: 19853>  # String: 'isFunction' (Identifier)
    // USED → r2 = getEnvironment(1)[3].default.isFunction;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 15, Reg8: 14>
    // USED → r2 = getEnvironment(1)[3].default.isFunction(r14);
    // CODE → <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000134
    if (getEnvironment(1)[3].default.isFunction(r14)) goto label_308;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // USED → r2 = getEnvironment(1)[9];
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = getEnvironment(1)[9].default;
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = getEnvironment(1)[9].default.assertOptions;
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  };
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 11>
    // USED → r2 = getEnvironment(1)[11];
    // CODE → <GetById>: <Reg8: 19, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r19 = getEnvironment(1)[11].function;
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 19, string_id: 13048>  # String: 'encode' (Identifier)
    r15.encode = getEnvironment(1)[11].function
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r2 = getEnvironment(1)[11].function;
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 12525>  # String: 'serialize' (Identifier)
    r15.serialize = getEnvironment(1)[11].function
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = getEnvironment(1)[9].default.assertOptions(r14, r15, r2)
    // CODE → <Jmp>: <Addr8: 15>  # Address: 00000141
    goto label_321;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <NewObject>: <Reg8: 2>
    r2 = {  }
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 14, string_id: 12525>  # String: 'serialize' (Identifier)
    r2.serialize = getEnvironment(1)[7].default.call(undefined, r2, r14).paramsSerializer
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 2, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    getEnvironment(1)[7].default.call(undefined, r2, r14).paramsSerializer = r2
    // ──────────────── Block 13 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 10, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = getEnvironment(1)[7].default.call(undefined, r2, r14).allowAbsoluteUrls;
    // CODE → <JStrictNotEqual>: <Addr8: 48, Reg8: 2, Reg8: 11>  # Address: 00000177
    // → r2 = getEnvironment(1)[7].default.call(undefined, r2, r14).allowAbsoluteUrls
    if (r2 !== undefined) goto label_375;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = this.defaults.allowAbsoluteUrls;
    // CODE → <JStrictNotEqual>: <Addr8: 14, Reg8: 2, Reg8: 11>  # Address: 00000165
    // → r2 = this.defaults.allowAbsoluteUrls
    if (r2 !== undefined) goto label_357;
    // ──────────────── Block 15 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    getEnvironment(1)[7].default.call(undefined, r2, r14).allowAbsoluteUrls = true
    // CODE → <Jmp>: <Addr8: 20>  # Address: 00000177
    goto label_375;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = this.defaults.allowAbsoluteUrls;
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    getEnvironment(1)[7].default.call(undefined, r2, r14).allowAbsoluteUrls = this.defaults.allowAbsoluteUrls
    // ──────────────── Block 17 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // USED → r2 = getEnvironment(1)[9];
    // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r16 = getEnvironment(1)[9].default;
    // CODE → <GetById>: <Reg8: 15, Reg8: 16, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r15 = getEnvironment(1)[9].default.assertOptions;
    // CODE → <NewObject>: <Reg8: 14>
    // USED → r14 = {  };
    // CODE → <LoadFromEnvironment>: <Reg8: 19, Reg8: 6, UInt8: 11>
    // USED → r19 = getEnvironment(1)[11];
    // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED → r18 = getEnvironment(1)[11].spelling;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 15368>  # String: 'baseURL' (Identifier)
    // USED → r2 = "baseURL";
    // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED → r2 = getEnvironment(1)[11].spelling("baseURL");
    // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 22683>  # String: 'baseUrl' (Identifier)
    r14.baseUrl = getEnvironment(1)[11].spelling("baseURL")
    // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED → r18 = getEnvironment(1)[11].spelling;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 24723>  # String: 'withXSRFToken' (Identifier)
    // USED → r2 = "withXSRFToken";
    // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED → r2 = getEnvironment(1)[11].spelling("withXSRFToken");
    // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 24724>  # String: 'withXsrfToken' (Identifier)
    r14.withXsrfToken = getEnvironment(1)[11].spelling("withXSRFToken")
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <Call4>: <Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 10, Reg8: 14, Reg8: 2>
    r14 = getEnvironment(1)[9].default.assertOptions(r10, r14, r2)
    // CODE → <GetById>: <Reg8: 15, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r15 = getEnvironment(1)[7].default.call(undefined, r2, r14).method;
    // CODE → <JmpTrue>: <Addr8: 15, Reg8: 15>  # Address: 000001d2
    // → r14 = getEnvironment(1)[9].default.assertOptions(r10, r14, r2); r2 = true
    if (getEnvironment(1)[7].default.call(undefined, r2, r14).method) goto label_466;
    // ──────────────── Block 18 ──────────────── 
    // CODE → <GetById>: <Reg8: 14, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r14 = this.defaults;
    // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r15 = this.defaults.method;
    // ──────────────── Block 19 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 7, Reg8: 15>  # Address: 000001d9
    if (this.defaults.method) goto label_473;
    // ──────────────── Block 20 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 15, string_id: 137>  # String: 'get' (Identifier)
    // USED → r15 = "get";
    // ──────────────── Block 21 ──────────────── 
    // CODE → <GetById>: <Reg8: 14, Reg8: 15, UInt8: 13, string_id: 20258>  # String: 'toLowerCase' (Identifier)
    // USED → r14 = "get".toLowerCase;
    // CODE → <Call1>: <Reg8: 14, Reg8: 14, Reg8: 15>
    // USED → r14 = "get".toLowerCase();
    // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 4, string_id: 12916>  # String: 'method' (Identifier)
    getEnvironment(1)[7].default.call(undefined, r2, r14).method = "get".toLowerCase()
    // CODE → <Mov>: <Reg8: 16, Reg8: 17>
    // USED → r16 = getEnvironment(1)[7].default.call(undefined, r2, r14).headers;
    // CODE → <JmpFalse>: <Addr8: 40, Reg8: 16>  # Address: 00000214
    // → r14 = "get".toLowerCase()
    if (!getEnvironment(1)[7].default.call(undefined, r2, r14).headers) goto label_532;
    // ──────────────── Block 22 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    // USED → r14 = getEnvironment(1)[3];
    // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = getEnvironment(1)[3].default;
    // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 14, string_id: 12398>  # String: 'merge' (Identifier)
    // USED → r18 = getEnvironment(1)[3].default.merge;
    // CODE → <GetById>: <Reg8: 15, Reg8: 17, UInt8: 15, string_id: 12528>  # String: 'common' (Identifier)
    // USED → r15 = getEnvironment(1)[7].default.call(undefined, r2, r14).headers.common;
    // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r14 = getEnvironment(1)[7].default.call(undefined, r2, r14).method;
    // CODE → <GetByVal>: <Reg8: 14, Reg8: 17, Reg8: 14>
    // USED → r14 = getEnvironment(1)[7].default.call(undefined, r2, r14).headers[getEnvironment(1)[7].default.call(undefined, r2, r14).method];
    // CODE → <Call3>: <Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    // USED → r16 = getEnvironment(1)[3].default.merge(r15, r14);
    // ──────────────── Block 23 ──────────────── 
    // CODE → <JmpFalse>: <Addr8: 36, Reg8: 17>  # Address: 00000238
    if (!getEnvironment(1)[7].default.call(undefined, r2, r14).headers) goto label_568;
    // ──────────────── Block 24 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    // USED → r14 = getEnvironment(1)[3];
    // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = getEnvironment(1)[3].default;
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r18 = getEnvironment(1)[3].default.forEach;
    // CODE → <NewArrayWithBuffer>: <Reg8: 15, UInt16: 7, UInt16: 7, UInt16: 21504>  # Array: ['delete', 'get', 'head', 'post', 'put', 'patch', 'common']
    // USED → r15 = ["delete", "get", "head", "post", "put", "patch", "common"];
    // CODE → <CreateClosure>: <Reg8: 14, Reg8: 9, function_id: 11949>  # Function: [#11949  of 18 bytes]: 2 params @ offset 0x002ba16a
    // USED → r14 = function_11949;
    // CODE → <Call3>: <Reg8: 14, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    r14 = getEnvironment(1)[3].default.forEach(r15, r14)
    // ──────────────── Block 25 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 10>
    // USED → r14 = getEnvironment(1)[10];
    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = getEnvironment(1)[10].default;
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 17, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r14 = getEnvironment(1)[10].default.concat;
    // CODE → <Call3>: <Reg8: 14, Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 17>
    // USED → r14 = getEnvironment(1)[10].default.concat(r16, r17);
    // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    getEnvironment(1)[7].default.call(undefined, r2, r14).headers = getEnvironment(1)[10].default.concat(r16, r17)
    // CODE → <NewArray>: <Reg8: 14, UInt16: 0>
    r14 = []
    // CODE → <Mov>: <Reg8: 12, Reg8: 14>
    // USED → r12 = r14;
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 2, Reg8: 14>
    createEnvironment()[2] = r14
    // CODE → <StoreNPToEnvironment>: <Reg8: 9, UInt8: 3, Reg8: 2>
    createEnvironment()[3] = true
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = this.interceptors;
    // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 19, string_id: 11955>  # String: 'request' (Identifier)
    // USED → r15 = this.interceptors.request;
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = this.interceptors.request.forEach;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11950>  # Function: [#11950 unshiftRequestInterceptors of 100 bytes]: 2 params @ offset 0x002ba17c
    // USED → r2 = unshiftRequestInterceptors;
    // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.request.forEach(r2)
    // CODE → <NewArray>: <Reg8: 2, UInt16: 0>
    r2 = []
    // CODE → <Mov>: <Reg8: 3, Reg8: 2>
    // USED → r3 = r2;
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 4, Reg8: 2>
    createEnvironment()[4] = r2
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = this.interceptors;
    // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 20, string_id: 11767>  # String: 'response' (Identifier)
    // USED → r15 = this.interceptors.response;
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = this.interceptors.response.forEach;
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11951>  # Function: [#11951 pushResponseInterceptors of 37 bytes]: 2 params @ offset 0x002ba1e0
    // USED → r2 = pushResponseInterceptors;
    // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.response.forEach(r2)
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0;
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 9, UInt8: 3>
    // USED → r9 = createEnvironment()[3];
    // CODE → <JmpTrueLong>: <Addr32: 164, Reg8: 9>  # Address: 0000034e
    if (createEnvironment()[3]) goto label_846;
    // ──────────────── Block 26 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 6>
    // USED → r9 = getEnvironment(1)[6];
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 9, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r14 = getEnvironment(1)[6].default;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 14, UInt8: 21, string_id: 87>  # String: 'bind' (Identifier)
    // USED → r9 = getEnvironment(1)[6].default.bind;
    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 14, Reg8: 8>
    // USED → r9 = getEnvironment(1)[6].default.bind(r8);
    // CODE → <NewArray>: <Reg8: 15, UInt16: 2>
    r15 = []
    // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 9, UInt8: 0>
    // USED → r15 = r15[0] = getEnvironment(1)[6].default.bind(r8);
    // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 11, UInt8: 1>
    // USED → r15 = (r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined;
    // CODE → <GetById>: <Reg8: 16, Reg8: 15, UInt8: 22, string_id: 16801>  # String: 'unshift' (Identifier)
    // USED → r16 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).unshift;
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).unshift.apply;
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r14;
    // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).unshift.apply(r15, r9)
    // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 15, UInt8: 24, string_id: 201>  # String: 'push' (Identifier)
    // USED → r16 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).push;
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).push.apply;
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = r2;
    // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).push.apply(r15, r9)
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r14 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).length;
    // CODE → <Mov>: <Reg8: 5, Reg8: 14>
    // USED → r5 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).length;
    // CODE → <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → <TryGetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r16 = globalThis.Promise;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 16, UInt8: 27, string_id: 208>  # String: 'resolve' (Identifier)
    // USED → r9 = globalThis.Promise.resolve;
    // CODE → <Call2>: <Reg8: 0, Reg8: 9, Reg8: 16, Reg8: 10>
    // USED → r0 = globalThis.Promise.resolve(r10);
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = 0;
    // CODE → <JNotLess>: <Addr8: 54, Reg8: 9, Reg8: 14>  # Address: 00000349
    // → r14 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).length; r9 = 0
    if (!(r9 < r14)) goto label_841;
    // ──────────────── Block 27 ──────────────── 
    // CODE → <Mov>: <Reg8: 18, Reg8: 0>
    // USED → r18 = globalThis.Promise.resolve(r10);
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r17 = globalThis.Promise.resolve(r10).then;
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = 0;
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +0;
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = r14 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = r14 + 1
    // CODE → <GetByVal>: <Reg8: 16, Reg8: 15, Reg8: 14>
    // USED → r16 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined)[+0];
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = +(r14 + 1);
    // CODE → <Inc>: <Reg8: 14, Reg8: 9>
    // USED → r14 = r9 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 14>
    r4 = r9 + 1
    // CODE → <GetByVal>: <Reg8: 9, Reg8: 15, Reg8: 9>
    // USED → r9 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined)[+(r14 + 1)];
    // CODE → <Call3>: <Reg8: 0, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 9>
    // USED → r0 = globalThis.Promise.resolve(r10).then(r16, r9);
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).length;
    // CODE → <JLess>: <Addr8: -46, Reg8: 14, Reg8: 9>  # Address: 00000317
    // → r14 = r9 + 1; r9 = ((r15[0] = getEnvironment(1)[6].default.bind(r8))[1] = undefined).length
    if (r14 < r9) goto label_791;
    // ──────────────── Block 28 ──────────────── 
    // CODE → <Mov>: <Reg8: 9, Reg8: 0>
    // USED → r9 = globalThis.Promise.resolve(r10).then(r16, r9);
    // CODE → <Ret>: <Reg8: 9>
    return globalThis.Promise.resolve(r10).then(r16, r9);
    // ──────────────── Block 29 ──────────────── 
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r14;
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r9 = r14.length;
    // CODE → <Mov>: <Reg8: 5, Reg8: 9>
    // USED → r5 = r14.length;
    // CODE → <Mov>: <Reg8: 1, Reg8: 10>
    // USED → r1 = getEnvironment(1)[7].default.call(undefined, r2, r14);
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <JNotLess>: <Addr8: 72, Reg8: 2, Reg8: 9>  # Address: 000003a6
    // → r9 = r14.length
    if (!(0 < r9)) goto label_934;
    // ──────────────── Block 30 ──────────────── 
    // CODE → <Mov>: <Reg8: 10, Reg8: 12>
    // USED → r10 = r14;
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = 0;
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +0;
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = r14 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = r14 + 1
    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 14>
    // USED → r13 = r14[+0];
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = +(r14 + 1);
    // CODE → <Inc>: <Reg8: 4, Reg8: 9>
    // USED → r4 = r9 + 1;
    // CODE → <GetByVal>: <Reg8: 7, Reg8: 10, Reg8: 9>
    // USED → r7 = r14[+(r14 + 1)];
    // CODE → <Mov>: <Reg8: 10, Reg8: 13>
    // USED → r10 = r14[+0];
    // CODE → <Mov>: <Reg8: 9, Reg8: 1>
    // USED → r9 = getEnvironment(1)[7].default.call(undefined, r2, r14);
    // CODE → <Call2>: <Reg8: 1, Reg8: 10, Reg8: 11, Reg8: 9>
    // USED → r1 = r14[+0].call(undefined, r9);
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = r9 + 1;
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r14.length;
    // CODE → <JLess>: <Addr8: -46, Reg8: 10, Reg8: 9>  # Address: 00000362
    // → r10 = r9 + 1; r9 = r14.length
    if (r10 < r9) goto label_866;
    // ──────────────── Block 31 ──────────────── 
    // CODE → <Jmp>: <Addr8: 18>  # Address: 000003a6
    goto label_934;
    // ──────────────── Block 32 ──────────────── 
    // CODE → <Catch>: <Reg8: 10>
    // USED → r10 = caughtException;
    // CODE → <Mov>: <Reg8: 9, Reg8: 7>
    // USED → r9 = r14[+(r14 + 1)];
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
    // USED → r7 = r14[+(r14 + 1)].call;
    // CODE → <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
    r7 = r14[+(r14 + 1)].call(r8, r10)
    // ──────────────── Block 33 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 6>
    // USED → r6 = getEnvironment(1)[6];
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r7 = getEnvironment(1)[6].default;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
    // USED → r6 = getEnvironment(1)[6].default.call;
    // CODE → <Call3>: <Reg8: 0, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1>
    // USED → r0 = getEnvironment(1)[6].default.call(r8, r1);
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0;
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    // USED → r1 = r2;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r1 = r2.length;
    // CODE → <Mov>: <Reg8: 5, Reg8: 1>
    // USED → r5 = r2.length;
    // CODE → <JNotLess>: <Addr8: 57, Reg8: 2, Reg8: 1>  # Address: 00000400
    // → r1 = r2.length
    if (!(0 < r1)) goto label_1024;
    // ──────────────── Block 34 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = getEnvironment(1)[6].default.call(r8, r1);
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r7 = getEnvironment(1)[6].default.call(r8, r1).then;
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = r2;
    // CODE → <Mov>: <Reg8: 1, Reg8: 4>
    // USED → r1 = 0;
    // CODE → <ToNumeric>: <Reg8: 2, Reg8: 1>
    // USED → r2 = +0;
    // CODE → <Inc>: <Reg8: 1, Reg8: 2>
    // USED → r1 = r2 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    r4 = r2 + 1
    // CODE → <GetByVal>: <Reg8: 6, Reg8: 9, Reg8: 2>
    // USED → r6 = r2[+0];
    // CODE → <ToNumeric>: <Reg8: 1, Reg8: 1>
    // USED → r1 = +(r2 + 1);
    // CODE → <Inc>: <Reg8: 2, Reg8: 1>
    // USED → r2 = r1 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    r4 = r1 + 1
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 9, Reg8: 1>
    // USED → r1 = r2[+(r2 + 1)];
    // CODE → <Call3>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 1>
    // USED → r0 = getEnvironment(1)[6].default.call(r8, r1).then(r6, r1);
    // CODE → <Mov>: <Reg8: 1, Reg8: 5>
    // USED → r1 = r2.length;
    // CODE → <JLess>: <Addr8: -49, Reg8: 2, Reg8: 1>  # Address: 000003cb
    // → r1 = r2.length; r2 = r1 + 1
    if (r2 < r1) goto label_971;
    // ──────────────── Block 35 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(1)[6].default.call(r8, r1).then(r6, r1);
    // ──────────────── Block 36 ──────────────── 
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r1 = globalThis.Promise;
    // CODE → <GetById>: <Reg8: 0, Reg8: 1, UInt8: 30, string_id: 13645>  # String: 'reject' (Identifier)
    // USED → r0 = globalThis.Promise.reject;
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 1, Reg8: 2>
    // USED → r0 = globalThis.Promise.reject(r2);
    // CODE → <Ret>: <Reg8: 0>
    return globalThis.Promise.reject(r2);
}