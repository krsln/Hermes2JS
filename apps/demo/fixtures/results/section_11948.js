function _request(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1
    // LINE → <LoadParam>: <Reg8: 2, UInt8: 2>
    // USED → r2 = param2
    // LINE → <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED → r8 = this
    // LINE → <CreateEnvironment>: <Reg8: 9>
    r9 = createEnvironment()
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    r9[0] = param2;
    // LINE → <LoadConstUndefined>: <Reg8: 11>
    // USED → r11 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 12>
    r12 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 3>
    r3 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 4>
    r4 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 5>
    r5 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 1>
    r1 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 13>
    r13 = undefined
    // LINE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // LINE → <TypeOf>: <Reg8: 14, Reg8: 6>
    // USED → r14 = typeof param1
    // LINE → <LoadConstString>: <Reg8: 10, string_id: 12185>  # String: 'string' (Identifier)
    // USED → r10 = "string"
    // LINE → <JStrictEqual>: <Addr8: 18, Reg8: 14, Reg8: 10>  # Address: 0000003a
    if (typeof param1 === "string") { /* jump to label_58 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <Mov>: <Reg8: 14, Reg8: 6>
    // USED → r14 = r6
    // LINE → <JmpTrue>: <Addr8: 5, Reg8: 14>  # Address: 00000034
    if (r6) { /* jump to label_52 */ }
    // ──────────────── Block 2 ──────────────── 
    // LINE → <NewObject>: <Reg8: 14>
    // USED → r14 = {}
    // ──────────────── Block 3 ──────────────── 
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 14>
    r9[0] = {};
    // LINE → <Jmp>: <Addr8: 20>  # Address: 0000004c
    goto label_76;
    // ──────────────── Block 4 ──────────────── 
    // LINE → <JmpTrue>: <Addr8: 5, Reg8: 2>  # Address: 0000003f
    if (param2) { /* jump to label_63 */ }
    // ──────────────── Block 5 ──────────────── 
    // LINE → <NewObject>: <Reg8: 2>
    // USED → r2 = {}
    // ──────────────── Block 6 ──────────────── 
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 2>
    r9[0] = {};
    // LINE → <PutById>: <Reg8: 2, Reg8: 6, UInt8: 1, string_id: 14158>  # String: 'url' (Identifier)
    r2 = { url: param1 }
    // LINE → <Mov>: <Reg8: 14, Reg8: 2>
    // USED → r14 = r2
    // ──────────────── Block 7 ──────────────── 
    // LINE → <GetEnvironment>: <Reg8: 6, UInt8: 1>
    r6 = getEnvironment(1)
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 7>
    r2 = r6[7]
    // LINE → <GetByIdShort>: <Reg8: 10, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r10 = r2.default
    // LINE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults
    // LINE → <Call3>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 2, Reg8: 14>
    // USED → r10 = r2.default(this.defaults)
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 0, Reg8: 10>
    r9[0] = r2.default(this.defaults);
    // LINE → <GetById>: <Reg8: 19, Reg8: 10, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r19 = r2.default(this.defaults).transitional
    // LINE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 4, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    // USED → r14 = r2.default(this.defaults).paramsSerializer
    // LINE → <GetByIdShort>: <Reg8: 17, Reg8: 10, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    // USED → r17 = r2.default(this.defaults).headers
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 17>
    r9[1] = r2.default(this.defaults).headers;
    // LINE → <JStrictEqual>: <Addr8: 100, Reg8: 19, Reg8: 11>  # Address: 000000e1
    if (r2.default(this.defaults).transitional === undefined) { /* jump to label_225 */ }
    // ──────────────── Block 8 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    r2 = r6[9]
    // LINE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = r2.default
    // LINE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = r2.default.assertOptions
    // LINE → <NewObject>: <Reg8: 15>
    // USED → r15 = {}
    // LINE → <LoadFromEnvironment>: <Reg8: 21, Reg8: 6, UInt8: 11>
    r21 = r6[11]
    // LINE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // LINE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // LINE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r21.transitional(r21.boolean)
    // LINE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 19648>  # String: 'silentJSONParsing' (Identifier)
    // USED → r15 = { silentJSONParsing: r21.transitional(r21.boolean) }
    // LINE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // LINE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // LINE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r21.transitional(r21.boolean)
    // LINE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 17756>  # String: 'forcedJSONParsing' (Identifier)
    // USED → r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean) }
    // LINE → <GetById>: <Reg8: 20, Reg8: 21, UInt8: 3, string_id: 17336>  # String: 'transitional' (Identifier)
    // USED → r20 = r21.transitional
    // LINE → <GetById>: <Reg8: 2, Reg8: 21, UInt8: 7, string_id: 12635>  # String: 'boolean' (Identifier)
    // USED → r2 = r21.boolean
    // LINE → <Call2>: <Reg8: 2, Reg8: 20, Reg8: 21, Reg8: 2>
    // USED → r2 = r21.transitional(r21.boolean)
    // LINE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 22889>  # String: 'clarifyTimeoutError' (Identifier)
    // USED → r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }
    // LINE → <LoadConstFalse>: <Reg8: 2>
    // USED → r2 = false
    // LINE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 2>
    r2 = r2.default.assertOptions(r2.default(this.defaults).transitional, { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }, false)
    // ──────────────── Block 9 ──────────────── 
    // LINE → <LoadConstNull>: <Reg8: 2>
    // USED → r2 = null
    // LINE → <JEqual>: <Addr8: 94, Reg8: 14, Reg8: 2>  # Address: 00000141
    if (r2.default(this.defaults).paramsSerializer == null) { /* jump to label_321 */ }
    // ──────────────── Block 10 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 3>
    r2 = r6[3]
    // LINE → <GetByIdShort>: <Reg8: 15, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = r2.default
    // LINE → <GetById>: <Reg8: 2, Reg8: 15, UInt8: 8, string_id: 19853>  # String: 'isFunction' (Identifier)
    // USED → r2 = r2.default.isFunction
    // LINE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 15, Reg8: 14>
    // USED → r2 = r2.default.isFunction(r2.default(this.defaults).paramsSerializer)
    // LINE → <JmpTrue>: <Addr8: 57, Reg8: 2>  # Address: 00000134
    if (r2.default.isFunction(r2.default(this.defaults).paramsSerializer)) { /* jump to label_308 */ }
    // ──────────────── Block 11 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    r2 = r6[9]
    // LINE → <GetByIdShort>: <Reg8: 18, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r18 = r2.default
    // LINE → <GetById>: <Reg8: 16, Reg8: 18, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r16 = r2.default.assertOptions
    // LINE → <NewObject>: <Reg8: 15>
    // USED → r15 = {}
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 11>
    r2 = r6[11]
    // LINE → <GetById>: <Reg8: 19, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r19 = r2.function
    // LINE → <PutNewOwnById>: <Reg8: 15, Reg8: 19, string_id: 13048>  # String: 'encode' (Identifier)
    // USED → r15 = { encode: r2.function }
    // LINE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 9, string_id: 12255>  # String: 'function' (Identifier)
    // USED → r2 = r2.function
    // LINE → <PutNewOwnById>: <Reg8: 15, Reg8: 2, string_id: 12525>  # String: 'serialize' (Identifier)
    // USED → r15 = { encode: r2.function, serialize: r2.function }
    // LINE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // LINE → <Call4>: <Reg8: 2, Reg8: 16, Reg8: 18, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = r2.default.assertOptions(r2.default(this.defaults).paramsSerializer, { encode: r2.function, serialize: r2.function }, true)
    // LINE → <Jmp>: <Addr8: 15>  # Address: 00000141
    goto label_321;
    // ──────────────── Block 12 ──────────────── 
    // LINE → <NewObject>: <Reg8: 2>
    // USED → r2 = {}
    // LINE → <PutNewOwnById>: <Reg8: 2, Reg8: 14, string_id: 12525>  # String: 'serialize' (Identifier)
    // USED → r2 = { serialize: r2.default(this.defaults).paramsSerializer }
    // LINE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 2, string_id: 15117>  # String: 'paramsSerializer' (Identifier)
    // USED → r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }
    // ──────────────── Block 13 ──────────────── 
    // LINE → <GetById>: <Reg8: 2, Reg8: 10, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }.allowAbsoluteUrls
    // LINE → <JStrictNotEqual>: <Addr8: 48, Reg8: 2, Reg8: 11>  # Address: 00000177
    if ({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }.allowAbsoluteUrls !== undefined) { /* jump to label_375 */ }
    // ──────────────── Block 14 ──────────────── 
    // LINE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults
    // LINE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = this.defaults.allowAbsoluteUrls
    // LINE → <JStrictNotEqual>: <Addr8: 14, Reg8: 2, Reg8: 11>  # Address: 00000165
    if (this.defaults.allowAbsoluteUrls !== undefined) { /* jump to label_357 */ }
    // ──────────────── Block 15 ──────────────── 
    // LINE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // LINE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: true }
    // LINE → <Jmp>: <Addr8: 20>  # Address: 00000177
    goto label_375;
    // ──────────────── Block 16 ──────────────── 
    // LINE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r2 = this.defaults
    // LINE → <GetById>: <Reg8: 2, Reg8: 2, UInt8: 10, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r2 = this.defaults.allowAbsoluteUrls
    // LINE → <PutById>: <Reg8: 10, Reg8: 2, UInt8: 3, string_id: 12108>  # String: 'allowAbsoluteUrls' (Identifier)
    // USED → r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }
    // ──────────────── Block 17 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 6, UInt8: 9>
    r2 = r6[9]
    // LINE → <GetByIdShort>: <Reg8: 16, Reg8: 2, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r16 = r2.default
    // LINE → <GetById>: <Reg8: 15, Reg8: 16, UInt8: 6, string_id: 22621>  # String: 'assertOptions' (Identifier)
    // USED → r15 = r2.default.assertOptions
    // LINE → <NewObject>: <Reg8: 14>
    // USED → r14 = {}
    // LINE → <LoadFromEnvironment>: <Reg8: 19, Reg8: 6, UInt8: 11>
    r19 = r6[11]
    // LINE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED → r18 = r19.spelling
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 15368>  # String: 'baseURL' (Identifier)
    // USED → r2 = "baseURL"
    // LINE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED → r2 = r19.spelling("baseURL")
    // LINE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 22683>  # String: 'baseUrl' (Identifier)
    // USED → r14 = { baseUrl: r19.spelling("baseURL") }
    // LINE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 11, string_id: 12544>  # String: 'spelling' (Identifier)
    // USED → r18 = r19.spelling
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 24723>  # String: 'withXSRFToken' (Identifier)
    // USED → r2 = "withXSRFToken"
    // LINE → <Call2>: <Reg8: 2, Reg8: 18, Reg8: 19, Reg8: 2>
    // USED → r2 = r19.spelling("withXSRFToken")
    // LINE → <PutNewOwnById>: <Reg8: 14, Reg8: 2, string_id: 24724>  # String: 'withXsrfToken' (Identifier)
    // USED → r14 = { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }
    // LINE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true
    // LINE → <Call4>: <Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 10, Reg8: 14, Reg8: 2>
    r14 = r2.default.assertOptions({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }, { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }, true)
    // LINE → <GetById>: <Reg8: 15, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r15 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }.method
    // LINE → <JmpTrue>: <Addr8: 15, Reg8: 15>  # Address: 000001d2
    if ({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }.method) { /* jump to label_466 */ }
    // ──────────────── Block 18 ──────────────── 
    // LINE → <GetById>: <Reg8: 14, Reg8: 8, UInt8: 2, string_id: 14042>  # String: 'defaults' (Identifier)
    // USED → r14 = this.defaults
    // LINE → <GetById>: <Reg8: 15, Reg8: 14, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r15 = this.defaults.method
    // ──────────────── Block 19 ──────────────── 
    // LINE → <JmpTrue>: <Addr8: 7, Reg8: 15>  # Address: 000001d9
    if (this.defaults.method) { /* jump to label_473 */ }
    // ──────────────── Block 20 ──────────────── 
    // LINE → <LoadConstString>: <Reg8: 15, string_id: 137>  # String: 'get' (Identifier)
    // USED → r15 = "get"
    // ──────────────── Block 21 ──────────────── 
    // LINE → <GetById>: <Reg8: 14, Reg8: 15, UInt8: 13, string_id: 20258>  # String: 'toLowerCase' (Identifier)
    // USED → r14 = "get".toLowerCase
    // LINE → <Call1>: <Reg8: 14, Reg8: 14, Reg8: 15>
    // USED → r14 = "get".toLowerCase()
    // LINE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 4, string_id: 12916>  # String: 'method' (Identifier)
    // USED → r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }
    // LINE → <Mov>: <Reg8: 16, Reg8: 17>
    // USED → r16 = r17
    // LINE → <JmpFalse>: <Addr8: 40, Reg8: 16>  # Address: 00000214
    if (!r17) { /* jump to label_532 */ }
    // ──────────────── Block 22 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    r14 = r6[3]
    // LINE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = r14.default
    // LINE → <GetById>: <Reg8: 18, Reg8: 19, UInt8: 14, string_id: 12398>  # String: 'merge' (Identifier)
    // USED → r18 = r14.default.merge
    // LINE → <GetById>: <Reg8: 15, Reg8: 17, UInt8: 15, string_id: 12528>  # String: 'common' (Identifier)
    // USED → r15 = r2.default(this.defaults).headers.common
    // LINE → <GetById>: <Reg8: 14, Reg8: 10, UInt8: 12, string_id: 12916>  # String: 'method' (Identifier)
    r14 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }.method
    // LINE → <GetByVal>: <Reg8: 14, Reg8: 17, Reg8: 14>
    // USED → r14 = r17[r14]
    // LINE → <Call3>: <Reg8: 16, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    // USED → r16 = r14.default.merge(r2.default(this.defaults).headers.common, r17[r14])
    // ──────────────── Block 23 ──────────────── 
    // LINE → <JmpFalse>: <Addr8: 36, Reg8: 17>  # Address: 00000238
    if (!r2.default(this.defaults).headers) { /* jump to label_568 */ }
    // ──────────────── Block 24 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 3>
    r14 = r6[3]
    // LINE → <GetByIdShort>: <Reg8: 19, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r19 = r14.default
    // LINE → <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r18 = r14.default.forEach
    // LINE → <NewArrayWithBuffer>: <Reg8: 15, UInt16: 7, UInt16: 7, UInt16: 21504>  # Array: ['delete', 'get', 'head', 'post', 'put', 'patch', 'common']
    // USED → r15 = ["delete", "get", "head", "post", "put", "patch", "common"]
    // LINE → <CreateClosure>: <Reg8: 14, Reg8: 9, function_id: 11949>  # Function: [#11949  of 18 bytes]: 2 params @ offset 0x002ba16a
    // USED → r14 = function_11949 /* Closure with env r9 = undefined */
    // LINE → <Call3>: <Reg8: 14, Reg8: 18, Reg8: 19, Reg8: 15, Reg8: 14>
    r14 = r14.default.forEach(["delete", "get", "head", "post", "put", "patch", "common"], function_11949 /* Closure with env r9 = undefined */)
    // ──────────────── Block 25 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 14, Reg8: 6, UInt8: 10>
    r14 = r6[10]
    // LINE → <GetByIdShort>: <Reg8: 15, Reg8: 14, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r15 = r14.default
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 17, string_id: 98>  # String: 'concat' (Identifier)
    // USED → r14 = r14.default.concat
    // LINE → <Call3>: <Reg8: 14, Reg8: 14, Reg8: 15, Reg8: 16, Reg8: 17>
    // USED → r14 = r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers)
    // LINE → <PutById>: <Reg8: 10, Reg8: 14, UInt8: 5, string_id: 145>  # String: 'headers' (Identifier)
    // USED → r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) }
    // LINE → <NewArray>: <Reg8: 14, UInt16: 0>
    // USED → r14 = []
    // LINE → <Mov>: <Reg8: 12, Reg8: 14>
    r12 = r14
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 2, Reg8: 14>
    r9[2] = [];
    // LINE → <StoreNPToEnvironment>: <Reg8: 9, UInt8: 3, Reg8: 2>
    r9[3] = true;
    // LINE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = this.interceptors
    // LINE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 19, string_id: 11955>  # String: 'request' (Identifier)
    // USED → r15 = this.interceptors.request
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = this.interceptors.request.forEach
    // LINE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11950>  # Function: [#11950 unshiftRequestInterceptors of 100 bytes]: 2 params @ offset 0x002ba17c
    // USED → r2 = unshiftRequestInterceptors /* Closure with env r9 = undefined */
    // LINE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.request.forEach(unshiftRequestInterceptors /* Closure with env r9 = undefined */)
    // LINE → <NewArray>: <Reg8: 2, UInt16: 0>
    // USED → r2 = []
    // LINE → <Mov>: <Reg8: 3, Reg8: 2>
    r3 = r2
    // LINE → <StoreToEnvironment>: <Reg8: 9, UInt8: 4, Reg8: 2>
    r9[4] = [];
    // LINE → <GetById>: <Reg8: 2, Reg8: 8, UInt8: 18, string_id: 19835>  # String: 'interceptors' (Identifier)
    // USED → r2 = this.interceptors
    // LINE → <GetById>: <Reg8: 15, Reg8: 2, UInt8: 20, string_id: 11767>  # String: 'response' (Identifier)
    // USED → r15 = this.interceptors.response
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 16, string_id: 135>  # String: 'forEach' (Identifier)
    // USED → r14 = this.interceptors.response.forEach
    // LINE → <CreateClosure>: <Reg8: 2, Reg8: 9, function_id: 11951>  # Function: [#11951 pushResponseInterceptors of 37 bytes]: 2 params @ offset 0x002ba1e0
    // USED → r2 = pushResponseInterceptors /* Closure with env r9 = undefined */
    // LINE → <Call2>: <Reg8: 2, Reg8: 14, Reg8: 15, Reg8: 2>
    r2 = this.interceptors.response.forEach(pushResponseInterceptors /* Closure with env r9 = undefined */)
    // LINE → <LoadConstZero>: <Reg8: 2>
    // USED → r2 = 0
    // LINE → <LoadConstZero>: <Reg8: 4>
    r4 = 0
    // LINE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 9, UInt8: 3>
    r9 = r9[3]
    // LINE → <JmpTrueLong>: <Addr32: 164, Reg8: 9>  # Address: 0000034e
    if (r9) { /* jump to label_846 */ }
    // ──────────────── Block 26 ──────────────── 
    // LINE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 6, UInt8: 6>
    r9 = r6[6]
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 9, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
    // USED → r14 = r9.default
    // LINE → <GetByIdShort>: <Reg8: 9, Reg8: 14, UInt8: 21, string_id: 87>  # String: 'bind' (Identifier)
    // USED → r9 = r9.default.bind
    // LINE → <Call2>: <Reg8: 9, Reg8: 9, Reg8: 14, Reg8: 8>
    // USED → r9 = r9.default.bind(this)
    // LINE → <NewArray>: <Reg8: 15, UInt16: 2>
    // USED → r15 = [] /* capacity hint: 2 */
    // LINE → <PutOwnByIndex>: <Reg8: 15, Reg8: 9, UInt8: 0>
    // USED → r15 = [r9.default.bind(this)]
    // LINE → <PutOwnByIndex>: <Reg8: 15, Reg8: 11, UInt8: 1>
    // USED → r15 = [r9.default.bind(this), undefined]
    // LINE → <GetById>: <Reg8: 16, Reg8: 15, UInt8: 22, string_id: 16801>  # String: 'unshift' (Identifier)
    // USED → r16 = [r9.default.bind(this), undefined].unshift
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = [r9.default.bind(this), undefined].unshift.apply
    // LINE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r12
    // LINE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = [r9.default.bind(this), undefined].unshift.apply([r9.default.bind(this), undefined], r12)
    // LINE → <GetByIdShort>: <Reg8: 16, Reg8: 15, UInt8: 24, string_id: 201>  # String: 'push' (Identifier)
    // USED → r16 = [r9.default.bind(this), undefined].push
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 16, UInt8: 23, string_id: 86>  # String: 'apply' (Identifier)
    // USED → r14 = [r9.default.bind(this), undefined].push.apply
    // LINE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = r3
    // LINE → <Call3>: <Reg8: 9, Reg8: 14, Reg8: 16, Reg8: 15, Reg8: 9>
    r9 = [r9.default.bind(this), undefined].push.apply([r9.default.bind(this), undefined], r3)
    // LINE → <GetByIdShort>: <Reg8: 14, Reg8: 15, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r14 = [r9.default.bind(this), undefined].length
    // LINE → <Mov>: <Reg8: 5, Reg8: 14>
    r5 = r14
    // LINE → <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis
    // LINE → <TryGetById>: <Reg8: 16, Reg8: 9, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r16 = globalThis.Promise
    // LINE → <GetByIdShort>: <Reg8: 9, Reg8: 16, UInt8: 27, string_id: 208>  # String: 'resolve' (Identifier)
    // USED → r9 = globalThis.Promise.resolve
    // LINE → <Call2>: <Reg8: 0, Reg8: 9, Reg8: 16, Reg8: 10>
    r0 = globalThis.Promise.resolve({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) })
    // LINE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4
    // LINE → <JNotLess>: <Addr8: 54, Reg8: 9, Reg8: 14>  # Address: 00000349
    if (r4 >= [r9.default.bind(this), undefined].length) { /* jump to label_841 */ }
    // ──────────────── Block 27 ──────────────── 
    // LINE → <Mov>: <Reg8: 18, Reg8: 0>
    // USED → r18 = r0
    // LINE → <GetByIdShort>: <Reg8: 17, Reg8: 18, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r17 = r0.then
    // LINE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4
    // LINE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +r4
    // LINE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = +r4 + 1
    // LINE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = r9
    // LINE → <GetByVal>: <Reg8: 16, Reg8: 15, Reg8: 14>
    // USED → r16 = r15[r14]
    // LINE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = ++r4 + 1
    // LINE → <Inc>: <Reg8: 14, Reg8: 9>
    // USED → r14 = ++r4 + 1 + 1
    // LINE → <Mov>: <Reg8: 4, Reg8: 14>
    r4 = r14
    // LINE → <GetByVal>: <Reg8: 9, Reg8: 15, Reg8: 9>
    // USED → r9 = r15[r9]
    // LINE → <Call3>: <Reg8: 0, Reg8: 17, Reg8: 18, Reg8: 16, Reg8: 9>
    r0 = r0.then(r15[r14], r15[r9])
    // LINE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r5
    // LINE → <JLess>: <Addr8: -46, Reg8: 14, Reg8: 9>  # Address: 00000317
    if (++r4 + 1 + 1 < r5) { /* jump to label_791 */ }
    // ──────────────── Block 28 ──────────────── 
    // LINE → <Mov>: <Reg8: 9, Reg8: 0>
    // USED → r9 = r0
    // LINE → <Ret>: <Reg8: 9>
    return r0;
    // ──────────────── Block 29 ──────────────── 
    // LINE → <Mov>: <Reg8: 9, Reg8: 12>
    // USED → r9 = r12
    // LINE → <GetByIdShort>: <Reg8: 9, Reg8: 9, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
    // USED → r9 = r12.length
    // LINE → <Mov>: <Reg8: 5, Reg8: 9>
    r5 = r9
    // LINE → <Mov>: <Reg8: 1, Reg8: 10>
    r1 = r10
    // LINE → <LoadConstZero>: <Reg8: 4>
    r4 = 0
    // LINE → <JNotLess>: <Addr8: 72, Reg8: 2, Reg8: 9>  # Address: 000003a6
    if (0 >= r12.length) { /* jump to label_934 */ }
    // ──────────────── Block 30 ──────────────── 
    // LINE → <Mov>: <Reg8: 10, Reg8: 12>
    r10 = r12
    // LINE → <Mov>: <Reg8: 9, Reg8: 4>
    // USED → r9 = r4
    // LINE → <ToNumeric>: <Reg8: 14, Reg8: 9>
    // USED → r14 = +r4
    // LINE → <Inc>: <Reg8: 9, Reg8: 14>
    // USED → r9 = +r4 + 1
    // LINE → <Mov>: <Reg8: 4, Reg8: 9>
    r4 = r9
    // LINE → <GetByVal>: <Reg8: 13, Reg8: 10, Reg8: 14>
    r13 = r10[r14]
    // LINE → <ToNumeric>: <Reg8: 9, Reg8: 9>
    // USED → r9 = ++r4 + 1
    // LINE → <Inc>: <Reg8: 4, Reg8: 9>
    r4 = ++r4 + 1 + 1
    // LINE → <GetByVal>: <Reg8: 7, Reg8: 10, Reg8: 9>
    r7 = r10[r9]
    // LINE → <Mov>: <Reg8: 10, Reg8: 13>
    // USED → r10 = r13
    // LINE → <Mov>: <Reg8: 9, Reg8: 1>
    // USED → r9 = r1
    // LINE → <Call2>: <Reg8: 1, Reg8: 10, Reg8: 11, Reg8: 9>
    // USED → r1 = r13(r1)
    // LINE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = r4
    // LINE → <Mov>: <Reg8: 9, Reg8: 5>
    // USED → r9 = r5
    // LINE → <JLess>: <Addr8: -46, Reg8: 10, Reg8: 9>  # Address: 00000362
    if (r4 < r5) { /* jump to label_866 */ }
    // ──────────────── Block 31 ──────────────── 
    // LINE → <Jmp>: <Addr8: 18>  # Address: 000003a6
    goto label_934;
    // LOOP → START (while)
    while (0 >= r3.length) {
        // ──────────────── Block 33 ──────────────── 
        // LINE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 6, UInt8: 6>
        r6 = r6[6]
        // LINE → <GetByIdShort>: <Reg8: 7, Reg8: 6, UInt8: 1, string_id: 110>  # String: 'default' (Identifier)
        // USED → r7 = r6.default
        // LINE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // USED → r6 = r6.default.call
        // LINE → <Call3>: <Reg8: 0, Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 1>
        r0 = r6.default.call(this, r13(r1))
        // LINE → <LoadConstZero>: <Reg8: 4>
        r4 = 0
        // LINE → <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = r3
        // LINE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 25, string_id: 139>  # String: 'length' (Identifier)
        // USED → r1 = r3.length
        // LINE → <Mov>: <Reg8: 5, Reg8: 1>
        r5 = r1
        // LINE → <JNotLess>: <Addr8: 57, Reg8: 2, Reg8: 1>  # Address: 00000400
        if (0 >= r3.length) { /* jump to label_1024 */ }
        // ──────────────── Block 32 ──────────────── 
        // LINE → <Catch>: <Reg8: 10>
        // USED → r10 = caughtException
        // LINE → <Mov>: <Reg8: 9, Reg8: 7>
        // USED → r9 = r7
        // LINE → <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 29, string_id: 91>  # String: 'call' (Identifier)
        // USED → r7 = r7.call
        // LINE → <Call3>: <Reg8: 7, Reg8: 7, Reg8: 9, Reg8: 8, Reg8: 10>
        r7 = r7.call(this, caughtException)
    }
    // LOOP → END
    // ──────────────── Block 34 ──────────────── 
    // LINE → <Mov>: <Reg8: 8, Reg8: 0>
    // USED → r8 = r0
    // LINE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 28, string_id: 231>  # String: 'then' (Identifier)
    // USED → r7 = r0.then
    // LINE → <Mov>: <Reg8: 9, Reg8: 3>
    r9 = r3
    // LINE → <Mov>: <Reg8: 1, Reg8: 4>
    // USED → r1 = r4
    // LINE → <ToNumeric>: <Reg8: 2, Reg8: 1>
    // USED → r2 = +r4
    // LINE → <Inc>: <Reg8: 1, Reg8: 2>
    // USED → r1 = +r4 + 1
    // LINE → <Mov>: <Reg8: 4, Reg8: 1>
    r4 = r1
    // LINE → <GetByVal>: <Reg8: 6, Reg8: 9, Reg8: 2>
    // USED → r6 = r9[r2]
    // LINE → <ToNumeric>: <Reg8: 1, Reg8: 1>
    // USED → r1 = ++r4 + 1
    // LINE → <Inc>: <Reg8: 2, Reg8: 1>
    // USED → r2 = ++r4 + 1 + 1
    // LINE → <Mov>: <Reg8: 4, Reg8: 2>
    r4 = r2
    // LINE → <GetByVal>: <Reg8: 1, Reg8: 9, Reg8: 1>
    // USED → r1 = r9[r1]
    // LINE → <Call3>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 1>
    // USED → r0 = r0.then(r9[r2], r9[r1])
    // LINE → <Mov>: <Reg8: 1, Reg8: 5>
    // USED → r1 = r5
    // LINE → <JLess>: <Addr8: -49, Reg8: 2, Reg8: 1>  # Address: 000003cb
    if (++r4 + 1 + 1 < r5) { /* jump to label_971 */ }
    // ──────────────── Block 35 ──────────────── 
    // LINE → <Ret>: <Reg8: 0>
    return r0.then(r9[r2], r9[r1]);
    // LINE → <Catch>: <Reg8: 2>
    // USED → r2 = caughtException
    // LINE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis
    // LINE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 26, string_id: 41>  # String: 'Promise' (Identifier)
    // USED → r1 = globalThis.Promise
    // LINE → <GetById>: <Reg8: 0, Reg8: 1, UInt8: 30, string_id: 13645>  # String: 'reject' (Identifier)
    // USED → r0 = globalThis.Promise.reject
    // LINE → <Call2>: <Reg8: 0, Reg8: 0, Reg8: 1, Reg8: 2>
    // USED → r0 = globalThis.Promise.reject(caughtException)
    // LINE → <Ret>: <Reg8: 0>
    return globalThis.Promise.reject(caughtException);
}