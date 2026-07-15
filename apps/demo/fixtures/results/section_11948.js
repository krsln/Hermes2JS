function _request(param0, param1, param2) {
    // CODE -> <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED -> r6 = param1
    // CODE -> <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED -> r2 = param2
    // CODE -> <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED -> r8 = this
    // CODE -> <CreateEnvironment>: <Reg8: 9>
    r9 = createEnvironment()
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    r9 = setEnvSlot(0, param2)  /*StoreToEnvironment: env=r9, slot=0, value=r2*/
    // CODE -> <LoadConstUndefined>: <Reg8: 11>
    // USED -> r11 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 13>
    r13 = undefined
    // CODE -> <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE -> <TypeOf>: <Reg8: 14, Reg8: 6>
    // USED -> r14 = typeof param1
    // CODE -> <LoadConstString>: <Reg8: 10, string_id: 12185>  # String: 'string' (Identifier)
    // USED -> r10 = "string"
    // CODE -> <JStrictEqual>: <Addr8: 18, Reg8: 14, Reg8: 10>  # Address: 0000003a
    if (typeof param1 === "string") {
        // CODE -> <Mov>: <Reg8: 14, Reg8: 6>
        // USED -> r14 = r6
        // CODE -> <JmpTrue>: <Addr8: 5, Reg8: 14>  # Address: 00000034
        if (r6) {
            // CODE -> <NewObject>: <Reg8: 14>
            // USED -> r14 = {}
        }
        // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 14>
        // label_52:
        r9 = setEnvSlot(0, {})  /*StoreToEnvironment: env=r9, slot=0, value=r14*/
        // CODE -> <Jmp>: <Addr8: 20>  # Address: 0000004c
        goto label_76;
    }
    // CODE -> <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 0000003f
    // label_58:
    if (param2) {
        // CODE -> <NewObject>: <Reg8: 2>
        // USED -> r2 = {}
    }
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    // label_63:
    r9 = setEnvSlot(0, {})  /*StoreToEnvironment: env=r9, slot=0, value=r2*/
    // CODE -> <PutById>: <Reg8: 2, Reg8: 6, UInt8: 1, string_id: 14158>  # String: 'url' (Identifier)
    r2 = { url: param1 }
    // CODE -> <Mov>: <Reg8: 14, Reg8: 2>
    // USED -> r14 = r2
    // CODE -> <GetEnvironment>: <Reg8: 6, UInt8: 1>
    // label_76:
    r6 = getEnvironment(1)
    // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 7>
    r2 = r6[7]
    // CODE -> <GetByIdShort>: <Reg8: 10, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED -> r10 = r2.default
    // CODE -> <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED -> r2 = this.defaults
    // CODE -> <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 2, Reg8: 14>
    // USED -> r10 = r2.default(this.defaults)
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 10>
    r9 = setEnvSlot(0, r2.default(this.defaults))  /*StoreToEnvironment: env=r9, slot=0, value=r10*/
    // CODE -> <GetById>: <Reg8: 19, Reg8: 10, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED -> r19 = r2.default(this.defaults).transitional
    // CODE -> <GetById>: <Reg8: 14, Reg8: 10, UInt8: 4, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    // USED -> r14 = r2.default(this.defaults).paramsSerializer
    // CODE -> <GetByIdShort>: <Reg8: 17, Reg8: 10, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    // USED -> r17 = r2.default(this.defaults).headers
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 17>
    r9 = setEnvSlot(1, r2.default(this.defaults).headers)  /*StoreToEnvironment: env=r9, slot=1, value=r17*/
    // CODE -> <JStrictEqual>: <Addr8: 100, Reg8: 19, Reg8: 11>  # Address: 000000e1
    if (r2.default(this.defaults) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
        r2 = r6[9]
        // CODE -> <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r18 = r2.default
        // CODE -> <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
        // USED -> r16 = r2.default.assertOptions
        // CODE -> <NewObject>: <Reg8: 15>
        // USED -> r15 = {}
        // CODE -> <LoadFromEnvironment>: <Reg8: 21, Reg8: 6, UInt8: 11>
        r21 = r6[11]
        // CODE -> <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
        // USED -> r20 = r21.transitional
        // CODE -> <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
        // USED -> r2 = r21.boolean
        // CODE -> <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
        // USED -> r2 = r21.transitional(r21.boolean)
        // CODE -> <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
        // USED -> r15 = { silentJSONParsing: r21.transitional(r21.boolean) }
        // CODE -> <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
        // USED -> r20 = r21.transitional
        // CODE -> <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
        // USED -> r2 = r21.boolean
        // CODE -> <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
        // USED -> r2 = r21.transitional(r21.boolean)
        // CODE -> <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 17756>  # String: 'forcedJSONParsing' (Identifier)
        // USED -> r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean) }
        // CODE -> <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
        // USED -> r20 = r21.transitional
        // CODE -> <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
        // USED -> r2 = r21.boolean
        // CODE -> <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
        // USED -> r2 = r21.transitional(r21.boolean)
        // CODE -> <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 22889>  # String: 'clarifyTimeoutError' (Identifier)
        // USED -> r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }
        // CODE -> <LoadConstFalse>: <Reg8: 2>
        // USED -> r2 = false
        // CODE -> <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 2>
        r2 = r2.default.assertOptions(r2.default(this.defaults).transitional, { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }, false)
    }
    // CODE -> <LoadConstNull>: <Reg8: 2>
    // label_225:
    // USED -> r2 = null
    // CODE -> <JEqual>: <Addr8: 94, Reg8: 14, Reg8: 2>  # Address: 00000141
    if (r2.default(this.defaults) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 3>
        r2 = r6[3]
        // CODE -> <GetByIdShort>: <Reg8: 15, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r15 = r2.default
        // CODE -> <GetById>: <Reg8: 2, Reg8: 15, UInt8: 8, string_id: 19853>  # String: 'isFunction' (Identifier)
        // USED -> r2 = r2.default.isFunction
        // CODE -> <Call2>: <Reg8: 2, Reg8: 2, Reg8: 15, Reg8: 14>
        // USED -> r2 = r2.default.isFunction(r2.default(this.defaults).paramsSerializer)
        // CODE -> <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000134
        if (r2.default.isFunction(r2.default(this.defaults) {
            // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
            r2 = r6[9]
            // CODE -> <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
            // USED -> r18 = r2.default
            // CODE -> <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
            // USED -> r16 = r2.default.assertOptions
            // CODE -> <NewObject>: <Reg8: 15>
            // USED -> r15 = {}
            // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 11>
            r2 = r6[11]
            // CODE -> <GetById>: <Reg8: 19, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
            // USED -> r19 = r2.function
            // CODE -> <PutNewOwnById>: <Reg8: 15, Reg8: 19, string_id: 13048>  # String: 'encode' (Identifier)
            // USED -> r15 = { encode: r2.function }
            // CODE -> <GetById>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
            // USED -> r2 = r2.function
            // CODE -> <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 12525>  # String: 'serialize' (Identifier)
            // USED -> r15 = { encode: r2.function, serialize: r2.function }
            // CODE -> <LoadConstTrue>: <Reg8: 2>
            // USED -> r2 = true
            // CODE -> <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 14, Reg8: 15, Reg8: 2>
            r2 = r2.default.assertOptions(r2.default(this.defaults).paramsSerializer, { encode: r2.function, serialize: r2.function }, true)
            // CODE -> <Jmp>: <Addr8: 15>  # Address: 00000141
            goto label_321;
        }
        // CODE -> <NewObject>: <Reg8: 2>
        // label_308:
        // USED -> r2 = {}
        // CODE -> <PutNewOwnById>: <Reg8: 2, Reg8: 14, string_id: 12525>  # String: 'serialize' (Identifier)
        // USED -> r2 = { serialize: r2.default(this.defaults).paramsSerializer }
        // CODE -> <PutById>: <Reg8: 10, Reg8: 2, UInt8: 2, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
        // USED -> r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }
    }
    // CODE -> <GetById>: <Reg8: 2, Reg8: 10, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // label_321:
    // USED -> r2 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }.allowAbsoluteUrls
    // CODE -> <JStrictNotEqual>: <Addr8: 48, Reg8: 2, Reg8: 11>  # Address: 00000177
    if ({ paramsSerializer: { serialize: r2.default(this.defaults) {
        // CODE -> <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // USED -> r2 = this.defaults
        // CODE -> <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // USED -> r2 = this.defaults.allowAbsoluteUrls
        // CODE -> <JStrictNotEqual>: <Addr8: 14, Reg8: 2, Reg8: 11>  # Address: 00000165
        if (this.defaults.allowAbsoluteUrls !== undefined) {
            // CODE -> <LoadConstTrue>: <Reg8: 2>
            // USED -> r2 = true
            // CODE -> <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
            // USED -> r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: true }
            // CODE -> <Jmp>: <Addr8: 20>  # Address: 00000177
            goto label_375;
        }
        // CODE -> <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // label_357:
        // USED -> r2 = this.defaults
        // CODE -> <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // USED -> r2 = this.defaults.allowAbsoluteUrls
        // CODE -> <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
        // USED -> r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }
    }
    // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    // label_375:
    r2 = r6[9]
    // CODE -> <GetByIdShort>: <Reg8: 16, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED -> r16 = r2.default
    // CODE -> <GetById>: <Reg8: 15, Reg8: 16, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED -> r15 = r2.default.assertOptions
    // CODE -> <NewObject>: <Reg8: 14>
    // USED -> r14 = {}
    // CODE -> <LoadFromEnvironment>: <Reg8: 19, Reg8: 6, UInt8: 11>
    r19 = r6[11]
    // CODE -> <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED -> r18 = r19.spelling
    // CODE -> <LoadConstString>: <Reg8: 2, string_id: 15368>  # String: 'baseURL' (Identifier)
    // USED -> r2 = "baseURL"
    // CODE -> <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED -> r2 = r19.spelling("baseURL")
    // CODE -> <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 22683>  # String: 'baseUrl' (Identifier)
    // USED -> r14 = { baseUrl: r19.spelling("baseURL") }
    // CODE -> <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED -> r18 = r19.spelling
    // CODE -> <LoadConstString>: <Reg8: 2, string_id: 24723>  # String: 'withXSRFToken' (Identifier)
    // USED -> r2 = "withXSRFToken"
    // CODE -> <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED -> r2 = r19.spelling("withXSRFToken")
    // CODE -> <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 24724>  # String: 'withXsrfToken' (Identifier)
    // USED -> r14 = { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }
    // CODE -> <LoadConstTrue>: <Reg8: 2>
    // USED -> r2 = true
    // CODE -> <Call4>: <Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 10, Reg8: 14, Reg8: 2>
    r14 = r2.default.assertOptions({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }, { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }, true)
    // CODE -> <GetById>: <Reg8: 15, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED -> r15 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }.method
    // CODE -> <JmpTrue>: <Addr8: 15, Reg8: 15>  # Address: 000001d2
    if ({ paramsSerializer: { serialize: r2.default(this.defaults) {
        // CODE -> <GetById>: <Reg8: 14, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
        // USED -> r14 = this.defaults
        // CODE -> <GetById>: <Reg8: 15, Reg8: 14, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        // USED -> r15 = this.defaults.method
    }
    // CODE -> <JmpTrue>: <Addr8: 7, Reg8: 15>  # Address: 000001d9
    // label_466:
    if (this.defaults.method) {
        // CODE -> <LoadConstString>: <Reg8: 15, string_id: 137>  # String: 'get' (Identifier)
        // USED -> r15 = "get"
    }
    // CODE -> <GetById>: <Reg8: 14, Reg8: 15, UInt8: 13, string_id: 20258>  # String: 'toLowerCase' (Identifier)
    // label_473:
    // USED -> r14 = "get".toLowerCase
    // CODE -> <Call1>: <Reg8: 14, Reg8: 14, Reg8: 15>
    // USED -> r14 = "get".toLowerCase()
    // CODE -> <PutById>: <Reg8: 10, Reg8: 14, UInt8: 4, string_id: 12916>  # String: 'method' (Identifier)
    // USED -> r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }
    // CODE -> <Mov>: <Reg8: 16, Reg8: 17>
    // USED -> r16 = r17
    // CODE -> <JmpFalse>: <Addr8: 40, Reg8: 16>  # Address: 00000214
    if (!r17) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
        r14 = r6[3]
        // CODE -> <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r19 = r14.default
        // CODE -> <GetById>: <Reg8: 18, Reg8: 19, UInt8: 14, string_id: 12398>  # String: 'merge' (Identifier)
        // USED -> r18 = r14.default.merge
        // CODE -> <GetById>: <Reg8: 15, Reg8: 17, UInt8: 15, string_id: 12528>  # String: 'common' (Identifier)
        // USED -> r15 = r2.default(this.defaults).headers.common
        // CODE -> <GetById>: <Reg8: 14, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
        r14 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }.method
        // CODE -> <GetByVal>: <Reg8: 14, Reg8: 17, Reg8: 14>
        // USED -> r14 = r17[r14]
        // CODE -> <Call3>: <Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
        // USED -> r16 = r14.default.merge(r2.default(this.defaults).headers.common, r17[r14])
    }
    // CODE -> <JmpFalse>: <Addr8: 36, Reg8: 17>  # Address: 00000238
    // label_532:
    if (!r2.default(this.defaults) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
        r14 = r6[3]
        // CODE -> <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r19 = r14.default
        // CODE -> <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
        // USED -> r18 = r14.default.forEach
        // CODE -> <NewArrayWithBuffer>: <Reg8: 15, UInt16: 7, UInt16: 7, UInt16: 21504>  # Array: ['delete', 'get', 'head', 'post', 'put', 'patch', 'common']
        // USED -> r15 = ["delete", "get", "head", "post", "put", "patch", "common"]
        // CODE -> <CreateClosure>: <Reg8: 14, Reg8: 9, function_id: 11949>  # Function: [#11949  of 18 bytes]: 2 params @ offset 0x002ba16a
        // USED -> r14 = function_11949 /* Closure with env r9 = undefined */
        // CODE -> <Call3>: <Reg8: 14, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
        r14 = r14.default.forEach(["delete", "get", "head", "post", "put", "patch", "common"], function_11949 /* Closure with env r9 = undefined */)
    }
    // CODE -> <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 10>
    // label_568:
    r14 = r6[10]
    // CODE -> <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED -> r15 = r14.default
    // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 17, string_id: 98>  # String: 'concat' (Identifier)
    // USED -> r14 = r14.default.concat
    // CODE -> <Call3>: <Reg8: 14, Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 17>
    // USED -> r14 = r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers)
    // CODE -> <PutById>: <Reg8: 10, Reg8: 14, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    // USED -> r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) }
    // CODE -> <NewArray>: <Reg8: 14, UInt16: 0>
    // USED -> r14 = []
    // CODE -> <Mov>: <Reg8: 12, Reg8: 14>
    r12 = r14
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 2, Reg8: 14>
    r9 = setEnvSlot(2, [])  /*StoreToEnvironment: env=r9, slot=2, value=r14*/
    // CODE -> <StoreNPToEnvironment>: <Reg8: 9, UInt8: 3, Reg8: 2>
    r9 = setEnvSlot(3, true)  /*StoreNPToEnvironment: env=r9, slot=3, value=r2*/
    // CODE -> <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED -> r2 = this.interceptors
    // CODE -> <GetById>: <Reg8: 15, Reg8: 2, UInt8: 19, string_id: 11955>  # String: 'request' (Identifier)
    // USED -> r15 = this.interceptors.request
    // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED -> r14 = this.interceptors.request.forEach
    // CODE -> <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11950>  # Function: [#11950 unshiftRequestInterceptors of 100 bytes]: 2 params @ offset 0x002ba17c
    // USED -> r2 = unshiftRequestInterceptors /* Closure with env r9 = undefined */
    // CODE -> <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.request.forEach(unshiftRequestInterceptors /* Closure with env r9 = undefined */)
    // CODE -> <NewArray>: <Reg8: 2, UInt16: 0>
    // USED -> r2 = []
    // CODE -> <Mov>: <Reg8: 3, Reg8: 2>
    r3 = r2
    // CODE -> <StoreToEnvironment>: <Reg8: 9, UInt8: 4, Reg8: 2>
    r9 = setEnvSlot(4, [])  /*StoreToEnvironment: env=r9, slot=4, value=r2*/
    // CODE -> <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED -> r2 = this.interceptors
    // CODE -> <GetById>: <Reg8: 15, Reg8: 2, UInt8: 20, string_id: 11767>  # String: 'response' (Identifier)
    // USED -> r15 = this.interceptors.response
    // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED -> r14 = this.interceptors.response.forEach
    // CODE -> <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11951>  # Function: [#11951 pushResponseInterceptors of 37 bytes]: 2 params @ offset 0x002ba1e0
    // USED -> r2 = pushResponseInterceptors /* Closure with env r9 = undefined */
    // CODE -> <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.response.forEach(pushResponseInterceptors /* Closure with env r9 = undefined */)
    // CODE -> <LoadConstZero>: <Reg8: 2>
    // USED -> r2 = 0
    // CODE -> <LoadConstZero>: <Reg8: 4>
    r4 = 0
    // CODE -> <LoadFromEnvironment>: <Reg8: 9, Reg8: 9, UInt8: 3>
    r9 = r9[3]
    // CODE -> <JmpTrueLong>: <Addr32: 164, Reg8: 9>  # Address: 0000034e
    if (r9) {
        // CODE -> <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 6>
        r9 = r6[6]
        // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 9, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED -> r14 = r9.default
        // CODE -> <GetByIdShort>: <Reg8: 9, Reg8: 14, UInt8: 21, string_id: 87>  # String: 'bind' (Identifier)
        // USED -> r9 = r9.default.bind
        // CODE -> <Call2>: <Reg8: 9, Reg8: 9, Reg8: 14, Reg8: 8>
        // USED -> r9 = r9.default.bind(this)
        // CODE -> <NewArray>: <Reg8: 15, UInt16: 2>
        // USED -> r15 = [] /* capacity hint: 2 */
        // CODE -> <PutOwnByIndex>: <Reg8: 15, Reg8: 9, UInt8: 0>
        // USED -> r15 = [r9.default.bind(this)]
        // CODE -> <PutOwnByIndex>: <Reg8: 15, Reg8: 11, UInt8: 1>
        // USED -> r15 = [r9.default.bind(this), undefined]
        // CODE -> <GetById>: <Reg8: 16, Reg8: 15, UInt8: 22, string_id: 16801>  # String: 'unshift' (Identifier)
        // USED -> r16 = [r9.default.bind(this), undefined].unshift
        // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
        // USED -> r14 = [r9.default.bind(this), undefined].unshift.apply
        // CODE -> <Mov>: <Reg8: 9, Reg8: 12>
        // USED -> r9 = r12
        // CODE -> <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
        r9 = [r9.default.bind(this), undefined].unshift.apply([r9.default.bind(this), undefined], r12)
        // CODE -> <GetByIdShort>: <Reg8: 16, Reg8: 15, UInt8: 24, string_id: 201>  # String: 'push' (Identifier)
        // USED -> r16 = [r9.default.bind(this), undefined].push
        // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
        // USED -> r14 = [r9.default.bind(this), undefined].push.apply
        // CODE -> <Mov>: <Reg8: 9, Reg8: 3>
        // USED -> r9 = r3
        // CODE -> <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
        r9 = [r9.default.bind(this), undefined].push.apply([r9.default.bind(this), undefined], r3)
        // CODE -> <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // USED -> r14 = [r9.default.bind(this), undefined].length
        // CODE -> <Mov>: <Reg8: 5, Reg8: 14>
        r5 = r14
        // CODE -> <GetGlobalObject>: <Reg8: 9>
        // USED -> r9 = globalThis
        // CODE -> <TryGetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
        // USED -> r16 = globalThis.Promise
        // CODE -> <GetByIdShort>: <Reg8: 9, Reg8: 16, UInt8: 27, string_id: 208>  # String: 'resolve' (Identifier)
        // USED -> r9 = globalThis.Promise.resolve
        // CODE -> <Call2>: <Reg8: 0, Reg8: 9, Reg8: 16, Reg8: 10>
        r0 = globalThis.Promise.resolve({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) })
        // CODE -> <Mov>: <Reg8: 9, Reg8: 4>
        // USED -> r9 = r4
        // CODE -> <JNotLess>: <Addr8: 54, Reg8: 9, Reg8: 14>  # Address: 00000349
        if (r4 >= [r9.default.bind(this) {
            // CODE -> <Mov>: <Reg8: 18, Reg8: 0>
            // label_791:
            // USED -> r18 = r0
            // CODE -> <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
            // USED -> r17 = r0.then
            // CODE -> <Mov>: <Reg8: 9, Reg8: 4>
            // USED -> r9 = r4
            // CODE -> <ToNumeric>: <Reg8: 14, Reg8: 9>
            // USED -> r14 = +r4
            // CODE -> <Inc>: <Reg8: 9, Reg8: 14>
            // USED -> r9 = +r4 + 1
            // CODE -> <Mov>: <Reg8: 4, Reg8: 9>
            r4 = r9
            // CODE -> <GetByVal>: <Reg8: 16, Reg8: 15, Reg8: 14>
            // USED -> r16 = r15[r14]
            // CODE -> <ToNumeric>: <Reg8: 9, Reg8: 9>
            // USED -> r9 = ++r4 + 1
            // CODE -> <Inc>: <Reg8: 14, Reg8: 9>
            // USED -> r14 = ++r4 + 1 + 1
            // CODE -> <Mov>: <Reg8: 4, Reg8: 14>
            r4 = r14
            // CODE -> <GetByVal>: <Reg8: 9, Reg8: 15, Reg8: 9>
            // USED -> r9 = r15[r9]
            // CODE -> <Call3>: <Reg8: 0, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 9>
            r0 = r0.then(r15[r14], r15[r9])
            // CODE -> <Mov>: <Reg8: 9, Reg8: 5>
            // USED -> r9 = r5
            // CODE -> <JLess>: <Addr8: -46, Reg8: 14, Reg8: 9>  # Address: 00000317
            if (++r4 + 1 + 1 < r5) {
            }
            // CODE -> <Mov>: <Reg8: 9, Reg8: 0>
            // label_841:
            // USED -> r9 = r0
            // CODE -> <Ret>: <Reg8: 9>
            return r0;
        }
        // CODE -> <Mov>: <Reg8: 9, Reg8: 12>
        // label_846:
        // USED -> r9 = r12
        // CODE -> <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // USED -> r9 = r12.length
        // CODE -> <Mov>: <Reg8: 5, Reg8: 9>
        r5 = r9
        // CODE -> <Mov>: <Reg8: 1, Reg8: 10>
        r1 = r10
        // CODE -> <LoadConstZero>: <Reg8: 4>
        r4 = 0
        // CODE -> <JNotLess>: <Addr8: 72, Reg8: 2, Reg8: 9>  # Address: 000003a6
        if (0 >= r12.length) {
            // CODE -> <Mov>: <Reg8: 10, Reg8: 12>
            // label_866:
            r10 = r12
            // CODE -> <Mov>: <Reg8: 9, Reg8: 4>
            // USED -> r9 = r4
            // CODE -> <ToNumeric>: <Reg8: 14, Reg8: 9>
            // USED -> r14 = +r4
            // CODE -> <Inc>: <Reg8: 9, Reg8: 14>
            // USED -> r9 = +r4 + 1
            // CODE -> <Mov>: <Reg8: 4, Reg8: 9>
            r4 = r9
            // CODE -> <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 14>
            r13 = r10[r14]
            // CODE -> <ToNumeric>: <Reg8: 9, Reg8: 9>
            // USED -> r9 = ++r4 + 1
            // CODE -> <Inc>: <Reg8: 4, Reg8: 9>
            r4 = ++r4 + 1 + 1
            // CODE -> <GetByVal>: <Reg8: 7, Reg8: 10, Reg8: 9>
            r7 = r10[r9]
            // CODE -> <Mov>: <Reg8: 10, Reg8: 13>
            // USED -> r10 = r13
            // CODE -> <Mov>: <Reg8: 9, Reg8: 1>
            // USED -> r9 = r1
            // CODE -> <Call2>: <Reg8: 1, Reg8: 10, Reg8: 11, Reg8: 9>
            // USED -> r1 = r13(r1)
            // CODE -> <Mov>: <Reg8: 10, Reg8: 4>
            // USED -> r10 = r4
            // CODE -> <Mov>: <Reg8: 9, Reg8: 5>
            // USED -> r9 = r5
            // CODE -> <JLess>: <Addr8: -46, Reg8: 10, Reg8: 9>  # Address: 00000362
            if (r4 < r5) {
                // CODE -> <Jmp>: <Addr8: 18>  # Address: 000003a6
                goto label_934;
                // CODE -> <Catch>: <Reg8: 10>
                // USED -> r10 = caughtException
                // CODE -> <Mov>: <Reg8: 9, Reg8: 7>
                // USED -> r9 = r7
                // CODE -> <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
                // USED -> r7 = r7.call
                // CODE -> <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
                r7 = r7.call(this, caughtException)
            }
            // CODE -> <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 6>
            // label_934:
            r6 = r6[6]
            // CODE -> <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
            // USED -> r7 = r6.default
            // CODE -> <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
            // USED -> r6 = r6.default.call
            // CODE -> <Call3>: <Reg8: 0, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1>
            r0 = r6.default.call(this, r13(r1))
            // CODE -> <LoadConstZero>: <Reg8: 4>
            r4 = 0
            // CODE -> <Mov>: <Reg8: 1, Reg8: 3>
            // USED -> r1 = r3
            // CODE -> <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
            // USED -> r1 = r3.length
            // CODE -> <Mov>: <Reg8: 5, Reg8: 1>
            r5 = r1
            // CODE -> <JNotLess>: <Addr8: 57, Reg8: 2, Reg8: 1>  # Address: 00000400
            if (0 >= r3.length) {
                // CODE -> <Mov>: <Reg8: 8, Reg8: 0>
                // label_971:
                // USED -> r8 = r0
                // CODE -> <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
                // USED -> r7 = r0.then
                // CODE -> <Mov>: <Reg8: 9, Reg8: 3>
                r9 = r3
                // CODE -> <Mov>: <Reg8: 1, Reg8: 4>
                // USED -> r1 = r4
                // CODE -> <ToNumeric>: <Reg8: 2, Reg8: 1>
                // USED -> r2 = +r4
                // CODE -> <Inc>: <Reg8: 1, Reg8: 2>
                // USED -> r1 = +r4 + 1
                // CODE -> <Mov>: <Reg8: 4, Reg8: 1>
                r4 = r1
                // CODE -> <GetByVal>: <Reg8: 6, Reg8: 9, Reg8: 2>
                // USED -> r6 = r9[r2]
                // CODE -> <ToNumeric>: <Reg8: 1, Reg8: 1>
                // USED -> r1 = ++r4 + 1
                // CODE -> <Inc>: <Reg8: 2, Reg8: 1>
                // USED -> r2 = ++r4 + 1 + 1
                // CODE -> <Mov>: <Reg8: 4, Reg8: 2>
                r4 = r2
                // CODE -> <GetByVal>: <Reg8: 1, Reg8: 9, Reg8: 1>
                // USED -> r1 = r9[r1]
                // CODE -> <Call3>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 1>
                // USED -> r0 = r0.then(r9[r2], r9[r1])
                // CODE -> <Mov>: <Reg8: 1, Reg8: 5>
                // USED -> r1 = r5
                // CODE -> <JLess>: <Addr8: -49, Reg8: 2, Reg8: 1>  # Address: 000003cb
                if (++r4 + 1 + 1 < r5) {
                }
                // CODE -> <Ret>: <Reg8: 0>
                // label_1024:
                return r0.then(r9[r2], r9[r1]);
                // CODE -> <Catch>: <Reg8: 2>
                // USED -> r2 = caughtException
                // CODE -> <GetGlobalObject>: <Reg8: 0>
                // USED -> r0 = globalThis
                // CODE -> <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
                // USED -> r1 = globalThis.Promise
                // CODE -> <GetById>: <Reg8: 0, Reg8: 1, UInt8: 30, string_id: 13645>  # String: 'reject' (Identifier)
                // USED -> r0 = globalThis.Promise.reject
                // CODE -> <Call2>: <Reg8: 0, Reg8: 0, Reg8: 1, Reg8: 2>
                // USED -> r0 = globalThis.Promise.reject(caughtException)
                // CODE -> <Ret>: <Reg8: 0>
                return globalThis.Promise.reject(caughtException);
            }
        }
    }
}