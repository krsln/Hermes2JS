function _request(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this
    // CODE → <CreateEnvironment>: <Reg8: 9>
    // USED → r9 = createEnvironment()
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    r9[0] = r2
    // CODE → <LoadConstUndefined>: <Reg8: 11>
    // USED → r11 = undefined
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
    // USED → r14 = typeof r6;
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 12185>  # String: 'string' (Identifier)
    // USED → r10 = "string"
    // CODE → <JStrictEqual>: <Addr8: 18, Reg8: 14, Reg8: 10>  # Address: 0000003a
    if (UnaryExpression(operator=<UnaryOperator.TYPEOF: 'typeof '>, operand=Identifier(name='r6')) === Identifier(name='r10')) { /* jump to label_58 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 14, Reg8: 6>
    // USED → r14 = r6;
    // CODE → <JmpTrue>: <Addr8: 5, Reg8: 14>  # Address: 00000034
    if (r6) goto label_52;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewObject>: <Reg8: 14>
    // USED → r14 = {  }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 14>
    r9[0] = r14
    // CODE → <Jmp>: <Addr8: 20>  # Address: 0000004c
    goto label_76;
    // LOOP → START (while)
    while (Identifier(name='r19') === Identifier(name='r11')) {
        // ──────────────── Block 7 ──────────────── 
        // CODE → <GetEnvironment>: <Reg8: 6, UInt8: 1>
        // USED → r6 = getEnvironment(1)
        // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 7>
        // USED → r2 = r6[7]
        // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED → r10 = r2.default
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // USED → r2 = r8.defaults
        // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 2, Reg8: 14>
        // USED → r10 = r10(r11, r2, r2);
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 10>
        r9[0] = r10(r11, r2, r2)
        // CODE → <GetById>: <Reg8: 19, Reg8: 10, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
        // USED → r19 = r10(r11, r2, r2).transitional
        // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 4, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
        // USED → r14 = r10(r11, r2, r2).paramsSerializer
        // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 10, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
        // USED → r17 = r10(r11, r2, r2).headers
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 17>
        r9[1] = r17
        // CODE → <JStrictEqual>: <Addr8: 100, Reg8: 19, Reg8: 11>  # Address: 000000e1
        if (Identifier(name='r19') === Identifier(name='r11')) { /* jump to label_225 */ }
        // LOOP → START (while)
        while (true) {
            // ──────────────── Block 6 ──────────────── 
            // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
            r9[0] = r2
            // CODE → <PutById>: <Reg8: 2, Reg8: 6, UInt8: 1, string_id: 14158>  # String: 'url' (Identifier)
            r2.url = r6;
            // CODE → <Mov>: <Reg8: 14, Reg8: 2>
            // USED → r14 = r2;
            // LOOP → START (while)
            while (true) {
                // ──────────────── Block 5 ──────────────── 
                // CODE → <NewObject>: <Reg8: 2>
                // USED → r2 = {  }
                // ──────────────── Block 4 ──────────────── 
                // CODE → <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 0000003f
                if (r2) goto label_63;
            }
            // LOOP → END
        }
        // LOOP → END
    }
    // LOOP → END
    // ──────────────── Block 8 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // USED → r2 = r6[9]
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = r2.default
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = r18.assertOptions
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  }
    // CODE → <LoadFromEnvironment>: <Reg8: 21, Reg8: 6, UInt8: 11>
    // USED → r21 = r6[11]
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r20(r21, r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
    r15."silentJSONParsing" = r20(r21, r2);
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r20(r21, r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 17756>  # String: 'forcedJSONParsing' (Identifier)
    r15."forcedJSONParsing" = r20(r21, r2);
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r20(r21, r2);
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 22889>  # String: 'clarifyTimeoutError' (Identifier)
    r15."clarifyTimeoutError" = r20(r21, r2);
    // CODE → <LoadConstFalse>: <Reg8: 2>
    // USED → r2 = false
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 2>
    r2 = r16(r18, r19, r15, r2);
    // ──────────────── Block 9 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null
    // CODE → <JEqual>: <Addr8: 94, Reg8: 14, Reg8: 2>  # Address: 00000141
    if (Identifier(name='r14') == Identifier(name='r2')) { /* jump to label_321 */ }
    // ──────────────── Block 10 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 3>
    // USED → r2 = r6[3]
    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = r2.default
    // CODE → <GetById>: <Reg8: 2, Reg8: 15, UInt8: 8, string_id: 19853>  # String: 'isFunction' (Identifier)
    // USED → r2 = r15.isFunction
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 15, Reg8: 14>
    // USED → r2 = r2(r15, r14);
    // CODE → <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000134
    if (r2(r15, r14)) goto label_308;
    // ──────────────── Block 11 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // USED → r2 = r6[9]
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = r2.default
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = r18.assertOptions
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  }
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 11>
    // USED → r2 = r6[11]
    // CODE → <GetById>: <Reg8: 19, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r19 = r2.function
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 19, string_id: 13048>  # String: 'encode' (Identifier)
    r15."encode" = r19;
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r2 = r2.function
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 12525>  # String: 'serialize' (Identifier)
    r15."serialize" = r2;
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = r16(r18, r14, r15, r2);
    // CODE → <Jmp>: <Addr8: 15>  # Address: 00000141
    goto label_321;
    // ──────────────── Block 12 ──────────────── 
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  }
    // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 14, string_id: 12525>  # String: 'serialize' (Identifier)
    r2."serialize" = r14;
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 2, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    r10(r11, r2, r2).paramsSerializer = r2;
    // ──────────────── Block 13 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 10, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = r10(r11, r2, r2).allowAbsoluteUrls
    // CODE → <JStrictNotEqual>: <Addr8: 48, Reg8: 2, Reg8: 11>  # Address: 00000177
    if (Identifier(name='r2') !== Identifier(name='r11')) { /* jump to label_375 */ }
    // ──────────────── Block 14 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = r8.defaults
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = r2.allowAbsoluteUrls
    // CODE → <JStrictNotEqual>: <Addr8: 14, Reg8: 2, Reg8: 11>  # Address: 00000165
    if (Identifier(name='r2') !== Identifier(name='r11')) { /* jump to label_357 */ }
    // ──────────────── Block 15 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    r10(r11, r2, r2).allowAbsoluteUrls = r2;
    // CODE → <Jmp>: <Addr8: 20>  # Address: 00000177
    goto label_375;
    // LOOP → START (while)
    while (r15) {
        // ──────────────── Block 17 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
        // USED → r2 = r6[9]
        // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED → r16 = r2.default
        // CODE → <GetById>: <Reg8: 15, Reg8: 16, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
        // USED → r15 = r16.assertOptions
        // CODE → <NewObject>: <Reg8: 14>
        // USED → r14 = {  }
        // CODE → <LoadFromEnvironment>: <Reg8: 19, Reg8: 6, UInt8: 11>
        // USED → r19 = r6[11]
        // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
        // USED → r18 = r19.spelling
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 15368>  # String: 'baseURL' (Identifier)
        // USED → r2 = "baseURL"
        // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
        // USED → r2 = r18(r19, r2);
        // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 22683>  # String: 'baseUrl' (Identifier)
        r14."baseUrl" = r18(r19, r2);
        // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
        // USED → r18 = r19.spelling
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 24723>  # String: 'withXSRFToken' (Identifier)
        // USED → r2 = "withXSRFToken"
        // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
        // USED → r2 = r18(r19, r2);
        // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 24724>  # String: 'withXsrfToken' (Identifier)
        r14."withXsrfToken" = r18(r19, r2);
        // CODE → <LoadConstTrue>: <Reg8: 2>
        // USED → r2 = true
        // CODE → <Call4>: <Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 10, Reg8: 14, Reg8: 2>
        r14 = r15(r16, r10(r11, r2, r2), r14, r2);
        // CODE → <GetById>: <Reg8: 15, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        // USED → r15 = r10(r11, r2, r2).method
        // CODE → <JmpTrue>: <Addr8: 15, Reg8: 15>  # Address: 000001d2
        if (r15) goto label_466;
        // ──────────────── Block 16 ──────────────── 
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // USED → r2 = r8.defaults
        // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // USED → r2 = r2.allowAbsoluteUrls
        // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        r10(r11, r2, r2).allowAbsoluteUrls = r2;
    }
    // LOOP → END
    // ──────────────── Block 18 ──────────────── 
    // CODE → <GetById>: <Reg8: 14, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r14 = r8.defaults
    // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r15 = r14.method
    // ──────────────── Block 19 ──────────────── 
    // CODE → <JmpTrue>: <Addr8: 7, Reg8: 15>  # Address: 000001d9
    if (r15) goto label_473;
    // ──────────────── Block 20 ──────────────── 
    // CODE → <LoadConstString>: <Reg8: 15, string_id: 137>  # String: 'get' (Identifier)
    // USED → r15 = "get"
    // ──────────────── Block 21 ──────────────── 
    // CODE → <GetById>: <Reg8: 14, Reg8: 15, UInt8: 13, string_id: 20258>  # String: 'toLowerCase' (Identifier)
    // USED → r14 = r15.toLowerCase
    // CODE → <Call1>: <Reg8: 14, Reg8: 14, Reg8: 15>
    // USED → r14 = r14(r15);
    // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 4, string_id: 12916>  # String: 'method' (Identifier)
    r10(r11, r2, r2).method = r14(r15);
    // CODE → <Mov>: <Reg8: 16, Reg8: 17>
    // USED → r16 = r17;
    // CODE → <JmpFalse>: <Addr8: 40, Reg8: 16>  # Address: 00000214
    if (!r17) goto label_532;
    // ──────────────── Block 22 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    // USED → r14 = r6[3]
    // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = r14.default
    // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 14, string_id: 12398>  # String: 'merge' (Identifier)
    // USED → r18 = r19.merge
    // CODE → <GetById>: <Reg8: 15, Reg8: 17, UInt8: 15, string_id: 12528>  # String: 'common' (Identifier)
    // USED → r15 = r17.common
    // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r14 = r10(r11, r2, r2).method
    // CODE → <GetByVal>: <Reg8: 14, Reg8: 17, Reg8: 14>
    // USED → r14 = r17[r14]
    // CODE → <Call3>: <Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    // USED → r16 = r18(r19, r15, r14);
    // ──────────────── Block 23 ──────────────── 
    // CODE → <JmpFalse>: <Addr8: 36, Reg8: 17>  # Address: 00000238
    if (!r17) goto label_568;
    // ──────────────── Block 24 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    // USED → r14 = r6[3]
    // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = r14.default
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r18 = r19.forEach
    // CODE → <NewArrayWithBuffer>: <Reg8: 15, UInt16: 7, UInt16: 7, UInt16: 21504>  # Array: ['delete', 'get', 'head', 'post', 'put', 'patch', 'common']
    // USED → r15 = ["delete", "get", "head", "post", "put", "patch", "common"];
    // CODE → <CreateClosure>: <Reg8: 14, Reg8: 9, function_id: 11949>  # Function: [#11949  of 18 bytes]: 2 params @ offset 0x002ba16a
    // USED → r14 = function_11949 /* Closure with env r9 = r9 */
    // CODE → <Call3>: <Reg8: 14, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    r14 = r18(r19, ["delete", "get", "head", "post", "put", "patch", "common"], r14);
    // ──────────────── Block 25 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 10>
    // USED → r14 = r6[10]
    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = r14.default
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 17, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r14 = r15.concat
    // CODE → <Call3>: <Reg8: 14, Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 17>
    // USED → r14 = r14(r15, r18(r19, r15, r14), r17);
    // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    r10(r11, r2, r2).headers = r14(r15, r18(r19, r15, r14), r17);
    // CODE → <NewArray>: <Reg8: 14, UInt16: 0>
    // USED → r14 = [];
    // CODE → <Mov>: <Reg8: 12, Reg8: 14>
    // USED → r12 = [];
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 2, Reg8: 14>
    r9[2] = []
    // CODE → <StoreNPToEnvironment>: <Reg8: 9, UInt8: 3, Reg8: 2>
    r9[3] = r2
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = r8.interceptors
    // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 19, string_id: 11955>  # String: 'request' (Identifier)
    // USED → r15 = r2.request
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = r15.forEach
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11950>  # Function: [#11950 unshiftRequestInterceptors of 100 bytes]: 2 params @ offset 0x002ba17c
    // USED → r2 = unshiftRequestInterceptors /* Closure with env r9 = r9 */
    // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = r14(r15, r2);
    // CODE → <NewArray>: <Reg8: 2, UInt16: 0>
    // USED → r2 = [];
    // CODE → <Mov>: <Reg8: 3, Reg8: 2>
    // USED → r3 = [];
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 4, Reg8: 2>
    r9[4] = []
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = r8.interceptors
    // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 20, string_id: 11767>  # String: 'response' (Identifier)
    // USED → r15 = r2.response
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = r15.forEach
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11951>  # Function: [#11951 pushResponseInterceptors of 37 bytes]: 2 params @ offset 0x002ba1e0
    // USED → r2 = pushResponseInterceptors /* Closure with env r9 = r9 */
    // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = r14(r15, r2);
    // CODE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 9, UInt8: 3>
    // USED → r9 = r9[3]
    // CODE → <JmpTrueLong>: <Addr32: 164, Reg8: 9>  # Address: 0000034e
    if (r9) goto label_846;
    // ──────────────── Block 26 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 6>
    // USED → r9 = r6[6]
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 9, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r14 = r9.default
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 14, UInt8: 21, string_id: 87>  # String: 'bind' (Identifier)
    // USED → r9 = r14.bind
    // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 14, Reg8: 8>
    // USED → r9 = r9(r14, r8);
    // CODE → <NewArray>: <Reg8: 15, UInt16: 2>
    // USED → r15 = [];
    // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 9, UInt8: 0>
    // USED → r15 = [r9(r14, r8)];
    // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 11, UInt8: 1>
    // USED → r15 = [r9(r14, r8), r11];
    // CODE → <GetById>: <Reg8: 16, Reg8: 15, UInt8: 22, string_id: 16801>  # String: 'unshift' (Identifier)
    // USED → r16 = [r9(r14, r8), r11].unshift
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = r16.apply
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = [];
    // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = r14(r16, [r9(r14, r8), r11], []);
    // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 15, UInt8: 24, string_id: 201>  # String: 'push' (Identifier)
    // USED → r16 = [r9(r14, r8), r11].push
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = r16.apply
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = [];
    // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = r14(r16, [r9(r14, r8), r11], []);
    // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r14 = [r9(r14, r8), r11].length
    // CODE → <Mov>: <Reg8: 5, Reg8: 14>
    // USED → r5 = r14;
    // CODE → <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → <TryGetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r16 = globalThis.Promise
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 16, UInt8: 27, string_id: 208>  # String: 'resolve' (Identifier)
    // USED → r9 = r16.resolve
    // CODE → <Call2>: <Reg8: 0, Reg8: 9, Reg8: 16, Reg8: 10>
    // USED → r0 = r9(r16, r10(r11, r2, r2));
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4;
    // CODE → <JNotLess>: <Addr8: 54, Reg8: 9, Reg8: 14>  # Address: 00000349
    if (Identifier(name='r4') >= Identifier(name='r14')) { /* jump to label_841 */ }
    // ──────────────── Block 27 ──────────────── 
    // CODE → <Mov>: <Reg8: 18, Reg8: 0>
    // USED → r18 = r9(r16, r10(r11, r2, r2));
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r17 = r9(r16, r10(r11, r2, r2)).then
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4;
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +r4;
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = +r4 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = +r4 + 1;
    // CODE → <GetByVal>: <Reg8: 16, Reg8: 15, Reg8: 14>
    // USED → r16 = [r9(r14, r8), r11][+r4]
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = +(+r4 + 1);
    // CODE → <Inc>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +(+r4 + 1) + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 14>
    r4 = +(+r4 + 1) + 1;
    // CODE → <GetByVal>: <Reg8: 9, Reg8: 15, Reg8: 9>
    // USED → r9 = [r9(r14, r8), r11][+(+r4 + 1)]
    // CODE → <Call3>: <Reg8: 0, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 9>
    // USED → r0 = r17(r9(r16, r10(r11, r2, r2)), r16, r9);
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r14;
    // CODE → <JLess>: <Addr8: -46, Reg8: 14, Reg8: 9>  # Address: 00000317
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r14')) { /* jump to label_791 */ }
    // ──────────────── Block 28 ──────────────── 
    // CODE → <Mov>: <Reg8: 9, Reg8: 0>
    r9 = r17(r9(r16, r10(r11, r2, r2)), r16, r9);
    // CODE → <Ret>: <Reg8: 9>
    // Unhandled opcode: Ret
    // ──────────────── Block 29 ──────────────── 
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = [];
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r9 = [].length
    // CODE → <Mov>: <Reg8: 5, Reg8: 9>
    // USED → r5 = r9;
    // CODE → <Mov>: <Reg8: 1, Reg8: 10>
    // USED → r1 = r10(r11, r2, r2);
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0
    // CODE → <JNotLess>: <Addr8: 72, Reg8: 2, Reg8: 9>  # Address: 000003a6
    if (Identifier(name='r2') >= Identifier(name='r9')) { /* jump to label_934 */ }
    // ──────────────── Block 30 ──────────────── 
    // CODE → <Mov>: <Reg8: 10, Reg8: 12>
    // USED → r10 = [];
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4;
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +r4;
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = +r4 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = +r4 + 1;
    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 14>
    // USED → r13 = [][+r4]
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = +(+r4 + 1);
    // CODE → <Inc>: <Reg8: 4, Reg8: 9>
    // USED → r4 = +(+r4 + 1) + 1;
    // CODE → <GetByVal>: <Reg8: 7, Reg8: 10, Reg8: 9>
    // USED → r7 = [][+(+r4 + 1)]
    // CODE → <Mov>: <Reg8: 10, Reg8: 13>
    // USED → r10 = r13;
    // CODE → <Mov>: <Reg8: 9, Reg8: 1>
    // USED → r9 = r10(r11, r2, r2);
    // CODE → <Call2>: <Reg8: 1, Reg8: 10, Reg8: 11, Reg8: 9>
    // USED → r1 = r13(r11, r10(r11, r2, r2));
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = +(+r4 + 1) + 1;
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r9;
    // CODE → <JLess>: <Addr8: -46, Reg8: 10, Reg8: 9>  # Address: 00000362
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r9')) { /* jump to label_866 */ }
    // ──────────────── Block 31 ──────────────── 
    // CODE → <Jmp>: <Addr8: 18>  # Address: 000003a6
    goto label_934;
    // LOOP → START (while)
    while (Identifier(name='r2') >= Identifier(name='r1')) {
        // ──────────────── Block 33 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 6>
        // USED → r6 = r6[6]
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED → r7 = r6.default
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // USED → r6 = r7.call
        // CODE → <Call3>: <Reg8: 0, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1>
        // USED → r0 = r6(r7, r8, r13(r11, r10(r11, r2, r2)));
        // CODE → <LoadConstZero>: <Reg8: 4>
        // USED → r4 = 0
        // CODE → <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = [];
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // USED → r1 = [].length
        // CODE → <Mov>: <Reg8: 5, Reg8: 1>
        // USED → r5 = r1;
        // CODE → <JNotLess>: <Addr8: 57, Reg8: 2, Reg8: 1>  # Address: 00000400
        if (Identifier(name='r2') >= Identifier(name='r1')) { /* jump to label_1024 */ }
        // ──────────────── Block 32 ──────────────── 
        // CODE → <Catch>: <Reg8: 10>
        // USED → r10 = caughtException
        // CODE → <Mov>: <Reg8: 9, Reg8: 7>
        // USED → r9 = r7;
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // USED → r7 = r7.call
        // CODE → <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
        r7 = r7(r7, r8, r10);
    }
    // LOOP → END
    // ──────────────── Block 34 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = r6(r7, r8, r13(r11, r10(r11, r2, r2)));
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r7 = r6(r7, r8, r13(r11, r10(r11, r2, r2))).then
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = [];
    // CODE → <Mov>: <Reg8: 1, Reg8: 4>
    // USED → r1 = r4;
    // CODE → <ToNumeric>: <Reg8: 2, Reg8: 1>
    // USED → r2 = +r4;
    // CODE → <Inc>: <Reg8: 1, Reg8: 2>
    // USED → r1 = +r4 + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    r4 = +r4 + 1;
    // CODE → <GetByVal>: <Reg8: 6, Reg8: 9, Reg8: 2>
    // USED → r6 = [][+r4]
    // CODE → <ToNumeric>: <Reg8: 1, Reg8: 1>
    // USED → r1 = +(+r4 + 1);
    // CODE → <Inc>: <Reg8: 2, Reg8: 1>
    // USED → r2 = +(+r4 + 1) + 1;
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    r4 = +(+r4 + 1) + 1;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 9, Reg8: 1>
    // USED → r1 = [][+(+r4 + 1)]
    // CODE → <Call3>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 1>
    r0 = r7(r6(r7, r8, r13(r11, r10(r11, r2, r2))), r6, r1);
    // CODE → <Mov>: <Reg8: 1, Reg8: 5>
    // USED → r1 = r1;
    // CODE → <JLess>: <Addr8: -49, Reg8: 2, Reg8: 1>  # Address: 000003cb
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r1')) { /* jump to label_971 */ }
    // ──────────────── Block 35 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r1 = globalThis.Promise
    // CODE → <GetById>: <Reg8: 0, Reg8: 1, UInt8: 30, string_id: 13645>  # String: 'reject' (Identifier)
    // USED → r0 = r1.reject
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 1, Reg8: 2>
    r0 = r0(r1, r2);
    // CODE → <Ret>: <Reg8: 0>
    // Unhandled opcode: Ret
}