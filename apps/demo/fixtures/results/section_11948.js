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
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 11>
    // USED → r11 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 13>
    // USED → r13 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined
    // CODE → <TypeOf>: <Reg8: 14, Reg8: 6>
    // USED → r14 = UnaryExpression(operator=<UnaryOperator.TYPEOF: 'typeof '>, operand=Identifier(name='r6'))
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 12185>  # String: 'string' (Identifier)
    // USED → r10 = "string"
    // CODE → <JStrictEqual>: <Addr8: 18, Reg8: 14, Reg8: 10>  # Address: 0000003a
    if (UnaryExpression(operator=<UnaryOperator.TYPEOF: 'typeof '>, operand=Identifier(name='r6')) === Identifier(name='r10')) { /* jump to label_58 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <Mov>: <Reg8: 14, Reg8: 6>
    // USED → r14 = Identifier(name='r6')
    // CODE → <JmpTrue>: <Addr8: 5, Reg8: 14>  # Address: 00000034
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <NewObject>: <Reg8: 14>
    // USED → r14 = {  }
    // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 14>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Jmp>: <Addr8: 20>  # Address: 0000004c
    goto label_76;
    // LOOP → START (while)
    while (Identifier(name='r19') === Identifier(name='r11')) {
        // ──────────────── Block 3 ──────────────── 
        // CODE → <GetEnvironment>: <Reg8: 6, UInt8: 1>
        // USED → r6 = getEnvironment(1)
        // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 7>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 2, Reg8: 14>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 10>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 19, Reg8: 10, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 4, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 10, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 17>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JStrictEqual>: <Addr8: 100, Reg8: 19, Reg8: 11>  # Address: 000000e1
        if (Identifier(name='r19') === Identifier(name='r11')) { /* jump to label_225 */ }
        // ──────────────── Block 2 ──────────────── 
        // CODE → <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 0000003f
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <NewObject>: <Reg8: 2>
        // USED → r2 = {  }
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <PutById>: <Reg8: 2, Reg8: 6, UInt8: 1, string_id: 14158>  # String: 'url' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 14, Reg8: 2>
        // USED → r14 = Identifier(name='r2')
    }
    // LOOP → END
    // ──────────────── Block 4 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  }
    // CODE → <LoadFromEnvironment>: <Reg8: 21, Reg8: 6, UInt8: 11>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 17756>  # String: 'forcedJSONParsing' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 22889>  # String: 'clarifyTimeoutError' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstFalse>: <Reg8: 2>
    // USED → r2 = false
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // ──────────────── Block 5 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null
    // CODE → <JEqual>: <Addr8: 94, Reg8: 14, Reg8: 2>  # Address: 00000141
    if (Identifier(name='r2') == Identifier(name='r2')) { /* jump to label_321 */ }
    // ──────────────── Block 6 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 3>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 15, UInt8: 8, string_id: 19853>  # String: 'isFunction' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 15, Reg8: 14>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000134
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <NewObject>: <Reg8: 15>
    // USED → r15 = {  }
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 11>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 19, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 19, string_id: 13048>  # String: 'encode' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 12525>  # String: 'serialize' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // CODE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 14, Reg8: 15, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Jmp>: <Addr8: 15>  # Address: 00000141
    goto label_321;
    // LOOP → START (while)
    while (Identifier(name='r2') !== Identifier(name='r11')) {
        // ──────────────── Block 8 ──────────────── 
        // CODE → <GetById>: <Reg8: 2, Reg8: 10, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JStrictNotEqual>: <Addr8: 48, Reg8: 2, Reg8: 11>  # Address: 00000177
        if (Identifier(name='r2') !== Identifier(name='r11')) { /* jump to label_375 */ }
        // ──────────────── Block 7 ──────────────── 
        // CODE → <NewObject>: <Reg8: 2>
        // USED → r2 = {  }
        // CODE → <PutNewOwnById>: <Reg8: 2, Reg8: 14, string_id: 12525>  # String: 'serialize' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 2, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
    }
    // LOOP → END
    // ──────────────── Block 9 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <JStrictNotEqual>: <Addr8: 14, Reg8: 2, Reg8: 11>  # Address: 00000165
    if (Identifier(name='r2') !== Identifier(name='r11')) { /* jump to label_357 */ }
    // ──────────────── Block 10 ──────────────── 
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Jmp>: <Addr8: 20>  # Address: 00000177
    goto label_375;
    // LOOP → START (while)
    while (Identifier(name='r4') >= Identifier(name='r14')) {
        // ──────────────── Block 12 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 15, Reg8: 16, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <NewObject>: <Reg8: 14>
        // USED → r14 = {  }
        // CODE → <LoadFromEnvironment>: <Reg8: 19, Reg8: 6, UInt8: 11>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 15368>  # String: 'baseURL' (Identifier)
        // USED → r2 = "baseURL"
        // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 22683>  # String: 'baseUrl' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstString>: <Reg8: 2, string_id: 24723>  # String: 'withXSRFToken' (Identifier)
        // USED → r2 = "withXSRFToken"
        // CODE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 24724>  # String: 'withXsrfToken' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstTrue>: <Reg8: 2>
        // USED → r2 = true
        // CODE → <Call4>: <Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 10, Reg8: 14, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetById>: <Reg8: 15, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpTrue>: <Addr8: 15, Reg8: 15>  # Address: 000001d2
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 14, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpTrue>: <Addr8: 7, Reg8: 15>  # Address: 000001d9
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadConstString>: <Reg8: 15, string_id: 137>  # String: 'get' (Identifier)
        // USED → r15 = "get"
        // CODE → <GetById>: <Reg8: 14, Reg8: 15, UInt8: 13, string_id: 20258>  # String: 'toLowerCase' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call1>: <Reg8: 14, Reg8: 14, Reg8: 15>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 4, string_id: 12916>  # String: 'method' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 16, Reg8: 17>
        // USED → r16 = Identifier(name='r17')
        // CODE → <JmpFalse>: <Addr8: 40, Reg8: 16>  # Address: 00000214
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 14, string_id: 12398>  # String: 'merge' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 15, Reg8: 17, UInt8: 15, string_id: 12528>  # String: 'common' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByVal>: <Reg8: 14, Reg8: 17, Reg8: 14>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <JmpFalse>: <Addr8: 36, Reg8: 17>  # Address: 00000238
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <NewArrayWithBuffer>: <Reg8: 15, UInt16: 7, UInt16: 7, UInt16: 21504>  # Array: ['delete', 'get', 'head', 'post', 'put', 'patch', 'common']
        // USED → r15 = ["delete", "get", "head", "post", "put", "patch", "common"]
        // CODE → <CreateClosure>: <Reg8: 14, Reg8: 9, function_id: 11949>  # Function: [#11949  of 18 bytes]: 2 params @ offset 0x002ba16a
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 14, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 10>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 17, string_id: 98>  # String: 'concat' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 14, Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 17>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <NewArray>: <Reg8: 14, UInt16: 0>
        // USED → r14 = []
        // CODE → <Mov>: <Reg8: 12, Reg8: 14>
        // USED → r12 = Identifier(name='r14')
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 2, Reg8: 14>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <StoreNPToEnvironment>: <Reg8: 9, UInt8: 3, Reg8: 2>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 19, string_id: 11955>  # String: 'request' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11950>  # Function: [#11950 unshiftRequestInterceptors of 100 bytes]: 2 params @ offset 0x002ba17c
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <NewArray>: <Reg8: 2, UInt16: 0>
        // USED → r2 = []
        // CODE → <Mov>: <Reg8: 3, Reg8: 2>
        // USED → r3 = Identifier(name='r2')
        // CODE → <StoreToEnvironment>: <Reg8: 9, UInt8: 4, Reg8: 2>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 20, string_id: 11767>  # String: 'response' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11951>  # Function: [#11951 pushResponseInterceptors of 37 bytes]: 2 params @ offset 0x002ba1e0
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <LoadConstZero>: <Reg8: 2>
        // USED → r2 = 0
        // CODE → <LoadConstZero>: <Reg8: 4>
        // USED → r4 = 0
        // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 9, UInt8: 3>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <JmpTrueLong>: <Addr32: 164, Reg8: 9>  # Address: 0000034e
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 6>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 9, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 14, UInt8: 21, string_id: 87>  # String: 'bind' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 14, Reg8: 8>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <NewArray>: <Reg8: 15, UInt16: 2>
        // USED → r15 = [] /* capacity hint: 2 */
        // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 9, UInt8: 0>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <PutOwnByIndex>: <Reg8: 15, Reg8: 11, UInt8: 1>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 16, Reg8: 15, UInt8: 22, string_id: 16801>  # String: 'unshift' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 9, Reg8: 12>
        // USED → r9 = Identifier(name='r14')
        // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetByIdShort>: <Reg8: 16, Reg8: 15, UInt8: 24, string_id: 201>  # String: 'push' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 9, Reg8: 3>
        // USED → r9 = Identifier(name='r2')
        // CODE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 5, Reg8: 14>
        // USED → r5 = Identifier(name='r14')
        // CODE → <GetGlobalObject>: <Reg8: 9>
        // USED → r9 = globalThis
        // CODE → <TryGetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 16, UInt8: 27, string_id: 208>  # String: 'resolve' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call2>: <Reg8: 0, Reg8: 9, Reg8: 16, Reg8: 10>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <Mov>: <Reg8: 9, Reg8: 4>
        // USED → r9 = Identifier(name='r4')
        // CODE → <JNotLess>: <Addr8: 54, Reg8: 9, Reg8: 14>  # Address: 00000349
        if (Identifier(name='r4') >= Identifier(name='r14')) { /* jump to label_841 */ }
        // ──────────────── Block 11 ──────────────── 
        // CODE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
    }
    // LOOP → END
    // ──────────────── Block 13 ──────────────── 
    // CODE → <Mov>: <Reg8: 18, Reg8: 0>
    // USED → r18 = Identifier(name='r0')
    // CODE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = Identifier(name='r4')
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4'))
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 16, Reg8: 15, Reg8: 14>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)))
    // CODE → <Inc>: <Reg8: 14, Reg8: 9>
    // USED → r14 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 4, Reg8: 14>
    r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 9, Reg8: 15, Reg8: 9>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call3>: <Reg8: 0, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 9>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = Identifier(name='r14')
    // CODE → <JLess>: <Addr8: -46, Reg8: 14, Reg8: 9>  # Address: 00000317
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r14')) { /* jump to label_791 */ }
    // ──────────────── Block 14 ──────────────── 
    // CODE → <Mov>: <Reg8: 9, Reg8: 0>
    // USED → r9 = Identifier(name='r0')
    // CODE → <Ret>: <Reg8: 9>
    ReturnStatement(argument=Identifier(name='r0'))
    // CODE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = Identifier(name='r14')
    // CODE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 5, Reg8: 9>
    // USED → r5 = Identifier(name='r14')
    // CODE → <Mov>: <Reg8: 1, Reg8: 10>
    // USED → r1 = Identifier(name='r10')
    // CODE → <LoadConstZero>: <Reg8: 4>
    // USED → r4 = 0
    // CODE → <JNotLess>: <Addr8: 72, Reg8: 2, Reg8: 9>  # Address: 000003a6
    if (Identifier(name='r2') >= Identifier(name='r14')) { /* jump to label_934 */ }
    // ──────────────── Block 15 ──────────────── 
    // CODE → <Mov>: <Reg8: 10, Reg8: 12>
    // USED → r10 = Identifier(name='r14')
    // CODE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = Identifier(name='r4')
    // CODE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4'))
    // CODE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 14>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)))
    // CODE → <Inc>: <Reg8: 4, Reg8: 9>
    // USED → r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 7, Reg8: 10, Reg8: 9>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 10, Reg8: 13>
    // USED → r10 = Identifier(name='r13')
    // CODE → <Mov>: <Reg8: 9, Reg8: 1>
    // USED → r9 = Identifier(name='r10')
    // CODE → <Call2>: <Reg8: 1, Reg8: 10, Reg8: 11, Reg8: 9>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = Identifier(name='r14')
    // CODE → <JLess>: <Addr8: -46, Reg8: 10, Reg8: 9>  # Address: 00000362
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r14')) { /* jump to label_866 */ }
    // ──────────────── Block 16 ──────────────── 
    // CODE → <Jmp>: <Addr8: 18>  # Address: 000003a6
    goto label_934;
    // LOOP → START (while)
    while (Identifier(name='r2') >= Identifier(name='r2')) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 6>
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 0, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1>
        // Error: sequence item 0: expected str instance, Identifier found
        // CODE → <LoadConstZero>: <Reg8: 4>
        // USED → r4 = 0
        // CODE → <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = Identifier(name='r2')
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Mov>: <Reg8: 5, Reg8: 1>
        // USED → r5 = Identifier(name='r2')
        // CODE → <JNotLess>: <Addr8: 57, Reg8: 2, Reg8: 1>  # Address: 00000400
        if (Identifier(name='r2') >= Identifier(name='r2')) { /* jump to label_1024 */ }
        // ──────────────── Block 17 ──────────────── 
        // CODE → <Catch>: <Reg8: 10>
        // USED → r10 = caughtException
        // CODE → <Mov>: <Reg8: 9, Reg8: 7>
        // USED → r9 = Identifier(name='r7')
        // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // Error: 'Identifier' object has no attribute 'render'
        // CODE → <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
        // Error: sequence item 0: expected str instance, Identifier found
    }
    // LOOP → END
    // ──────────────── Block 19 ──────────────── 
    // CODE → <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = Identifier(name='r0')
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = Identifier(name='r2')
    // CODE → <Mov>: <Reg8: 1, Reg8: 4>
    // USED → r1 = Identifier(name='r4')
    // CODE → <ToNumeric>: <Reg8: 2, Reg8: 1>
    // USED → r2 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4'))
    // CODE → <Inc>: <Reg8: 1, Reg8: 2>
    // USED → r1 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 4, Reg8: 1>
    r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 6, Reg8: 9, Reg8: 2>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <ToNumeric>: <Reg8: 1, Reg8: 1>
    // USED → r1 = UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)))
    // CODE → <Inc>: <Reg8: 2, Reg8: 1>
    // USED → r2 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <Mov>: <Reg8: 4, Reg8: 2>
    r4 = BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 9, Reg8: 1>
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call3>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 1>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Mov>: <Reg8: 1, Reg8: 5>
    // USED → r1 = Identifier(name='r2')
    // CODE → <JLess>: <Addr8: -49, Reg8: 2, Reg8: 1>  # Address: 000003cb
    if (BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=BinaryExpression(left=UnaryExpression(operator=<UnaryOperator.PLUS: '+'>, operand=Identifier(name='r4')), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1))), operator=<BinaryOperator.ADD: '+'>, right=NumericLiteral(value=1)) < Identifier(name='r2')) { /* jump to label_971 */ }
    // ──────────────── Block 20 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
    // CODE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 0, Reg8: 1, UInt8: 30, string_id: 13645>  # String: 'reject' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 1, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}