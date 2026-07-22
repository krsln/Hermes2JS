function _request(param0, param1, param2) {
    // Block 0
    r6 = param1
    r2 = param2
    r8 = this
    r9 = createEnvironment()
    r9[0] = param2;
    r11 = undefined
    r12 = undefined
    r3 = undefined
    r0 = undefined
    r4 = undefined
    r5 = undefined
    r1 = undefined
    r13 = undefined
    r7 = undefined
    r14 = typeof param1
    r10 = "string"
    if (typeof param1 === "string") { /* jump to label_58 */ }
    // Block 1
    r14 = r6
    if (r6) { /* jump to label_52 */ }
    // Block 2
    r14 = {}
    // Block 3
    r9[0] = {};
    goto label_76;
    // Block 4
    if (param2) { /* jump to label_63 */ }
    // Block 5
    r2 = {}
    // Block 6
    r9[0] = {};
    r2 = { url: param1 }
    r14 = r2
    // Block 7
    r6 = getEnvironment(1)
    r2 = r6[7]
    r10 = r2.default
    r2 = this.defaults
    r10 = r2.default(this.defaults)
    r9[0] = r2.default(this.defaults);
    r19 = r2.default(this.defaults).transitional
    r14 = r2.default(this.defaults).paramsSerializer
    r17 = r2.default(this.defaults).headers
    r9[1] = r2.default(this.defaults).headers;
    if (r2.default(this.defaults).transitional === undefined) { /* jump to label_225 */ }
    // Block 8
    r2 = r6[9]
    r18 = r2.default
    r16 = r2.default.assertOptions
    r15 = {}
    r21 = r6[11]
    r20 = r21.transitional
    r2 = r21.boolean
    r2 = r21.transitional(r21.boolean)
    r15 = { silentJSONParsing: r21.transitional(r21.boolean) }
    r20 = r21.transitional
    r2 = r21.boolean
    r2 = r21.transitional(r21.boolean)
    r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean) }
    r20 = r21.transitional
    r2 = r21.boolean
    r2 = r21.transitional(r21.boolean)
    r15 = { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }
    r2 = false
    r2 = r2.default.assertOptions(r2.default(this.defaults).transitional, { silentJSONParsing: r21.transitional(r21.boolean), forcedJSONParsing: r21.transitional(r21.boolean), clarifyTimeoutError: r21.transitional(r21.boolean) }, false)
    // Block 9
    r2 = null
    if (r2.default(this.defaults).paramsSerializer == null) { /* jump to label_321 */ }
    // Block 10
    r2 = r6[3]
    r15 = r2.default
    r2 = r2.default.isFunction
    r2 = r2.default.isFunction(r2.default(this.defaults).paramsSerializer)
    if (r2.default.isFunction(r2.default(this.defaults).paramsSerializer)) { /* jump to label_308 */ }
    // Block 11
    r2 = r6[9]
    r18 = r2.default
    r16 = r2.default.assertOptions
    r15 = {}
    r2 = r6[11]
    r19 = r2.function
    r15 = { encode: r2.function }
    r2 = r2.function
    r15 = { encode: r2.function, serialize: r2.function }
    r2 = true
    r2 = r2.default.assertOptions(r2.default(this.defaults).paramsSerializer, { encode: r2.function, serialize: r2.function }, true)
    goto label_321;
    // Block 12
    r2 = {}
    r2 = { serialize: r2.default(this.defaults).paramsSerializer }
    r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }
    // Block 13
    r2 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }.allowAbsoluteUrls
    if ({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer } }.allowAbsoluteUrls !== undefined) { /* jump to label_375 */ }
    // Block 14
    r2 = this.defaults
    r2 = this.defaults.allowAbsoluteUrls
    if (this.defaults.allowAbsoluteUrls !== undefined) { /* jump to label_357 */ }
    // Block 15
    r2 = true
    r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: true }
    goto label_375;
    // Block 16
    r2 = this.defaults
    r2 = this.defaults.allowAbsoluteUrls
    r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }
    // Block 17
    r2 = r6[9]
    r16 = r2.default
    r15 = r2.default.assertOptions
    r14 = {}
    r19 = r6[11]
    r18 = r19.spelling
    r2 = "baseURL"
    r2 = r19.spelling("baseURL")
    r14 = { baseUrl: r19.spelling("baseURL") }
    r18 = r19.spelling
    r2 = "withXSRFToken"
    r2 = r19.spelling("withXSRFToken")
    r14 = { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }
    r2 = true
    r14 = r2.default.assertOptions({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }, { baseUrl: r19.spelling("baseURL"), withXsrfToken: r19.spelling("withXSRFToken") }, true)
    r15 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }.method
    if ({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls }.method) { /* jump to label_466 */ }
    // Block 18
    r14 = this.defaults
    r15 = this.defaults.method
    // Block 19
    if (this.defaults.method) { /* jump to label_473 */ }
    // Block 20
    r15 = "get"
    // Block 21
    r14 = "get".toLowerCase
    r14 = "get".toLowerCase()
    r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }
    r16 = r17
    if (!r17) { /* jump to label_532 */ }
    // Block 22
    r14 = r6[3]
    r19 = r14.default
    r18 = r14.default.merge
    r15 = r2.default(this.defaults).headers.common
    r14 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase() }.method
    r14 = r17[r14]
    r16 = r14.default.merge(r2.default(this.defaults).headers.common, r17[r14])
    // Block 23
    if (!r2.default(this.defaults).headers) { /* jump to label_568 */ }
    // Block 24
    r14 = r6[3]
    r19 = r14.default
    r18 = r14.default.forEach
    r15 = ["delete", "get", "head", "post", "put", "patch", "common"]
    r14 = function_11949 /* Closure with env r9 = undefined */
    r14 = r14.default.forEach(["delete", "get", "head", "post", "put", "patch", "common"], function_11949 /* Closure with env r9 = undefined */)
    // Block 25
    r14 = r6[10]
    r15 = r14.default
    r14 = r14.default.concat
    r14 = r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers)
    r10 = { paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) }
    r14 = []
    r12 = r14
    r9[2] = [];
    r9[3] = true;
    r2 = this.interceptors
    r15 = this.interceptors.request
    r14 = this.interceptors.request.forEach
    r2 = unshiftRequestInterceptors /* Closure with env r9 = undefined */
    r2 = this.interceptors.request.forEach(unshiftRequestInterceptors /* Closure with env r9 = undefined */)
    r2 = []
    r3 = r2
    r9[4] = [];
    r2 = this.interceptors
    r15 = this.interceptors.response
    r14 = this.interceptors.response.forEach
    r2 = pushResponseInterceptors /* Closure with env r9 = undefined */
    r2 = this.interceptors.response.forEach(pushResponseInterceptors /* Closure with env r9 = undefined */)
    r2 = 0
    r4 = 0
    r9 = r9[3]
    if (r9) { /* jump to label_846 */ }
    // Block 26
    r9 = r6[6]
    r14 = r9.default
    r9 = r9.default.bind
    r9 = r9.default.bind(this)
    r15 = [] /* capacity hint: 2 */
    r15 = [r9.default.bind(this)]
    r15 = [r9.default.bind(this), undefined]
    r16 = [r9.default.bind(this), undefined].unshift
    r14 = [r9.default.bind(this), undefined].unshift.apply
    r9 = r12
    r9 = [r9.default.bind(this), undefined].unshift.apply([r9.default.bind(this), undefined], r12)
    r16 = [r9.default.bind(this), undefined].push
    r14 = [r9.default.bind(this), undefined].push.apply
    r9 = r3
    r9 = [r9.default.bind(this), undefined].push.apply([r9.default.bind(this), undefined], r3)
    r14 = [r9.default.bind(this), undefined].length
    r5 = r14
    r9 = globalThis
    r16 = globalThis.Promise
    r9 = globalThis.Promise.resolve
    r0 = globalThis.Promise.resolve({ paramsSerializer: { serialize: r2.default(this.defaults).paramsSerializer }, allowAbsoluteUrls: this.defaults.allowAbsoluteUrls, method: "get".toLowerCase(), headers: r14.default.concat(r14.default.merge(r2.default(this.defaults).headers.common, r17[r14]), r2.default(this.defaults).headers) })
    r9 = r4
    if (r4 >= [r9.default.bind(this), undefined].length) { /* jump to label_841 */ }
    // Block 27
    r18 = r0
    r17 = r0.then
    r9 = r4
    r14 = +r4
    r9 = +r4 + 1
    r4 = r9
    r16 = r15[r14]
    r9 = ++r4 + 1
    r14 = ++r4 + 1 + 1
    r4 = r14
    r9 = r15[r9]
    r0 = r0.then(r15[r14], r15[r9])
    r9 = r5
    if (++r4 + 1 + 1 < r5) { /* jump to label_791 */ }
    // Block 28
    r9 = r0
    return r0;
    // Block 29
    r9 = r12
    r9 = r12.length
    r5 = r9
    r1 = r10
    r4 = 0
    if (0 >= r12.length) { /* jump to label_934 */ }
    // Block 30
    r10 = r12
    r9 = r4
    r14 = +r4
    r9 = +r4 + 1
    r4 = r9
    r13 = r10[r14]
    r9 = ++r4 + 1
    r4 = ++r4 + 1 + 1
    r7 = r10[r9]
    r10 = r13
    r9 = r1
    r1 = r13(r1)
    r10 = r4
    r9 = r5
    if (r4 < r5) { /* jump to label_866 */ }
    // Block 31
    goto label_934;
    // Block 34
    r8 = r0
    r7 = r0.then
    r9 = r3
    r1 = r4
    r2 = +r4
    r1 = +r4 + 1
    r4 = r1
    r6 = r9[r2]
    r1 = ++r4 + 1
    r2 = ++r4 + 1 + 1
    r4 = r2
    r1 = r9[r1]
    r0 = r0.then(r9[r2], r9[r1])
    r1 = r5
    if (++r4 + 1 + 1 < r5) { /* jump to label_971 */ }
    // Block 35
    return r0.then(r9[r2], r9[r1]);
    r2 = caughtException
    r0 = globalThis
    r1 = globalThis.Promise
    r0 = globalThis.Promise.reject
    r0 = globalThis.Promise.reject(caughtException)
    return globalThis.Promise.reject(caughtException);
    // Loop
        // Block 33
        r6 = r6[6]
        r7 = r6.default
        r6 = r6.default.call
        r0 = r6.default.call(this, r13(r1))
        r4 = 0
        r1 = r3
        r1 = r3.length
        r5 = r1
        if (0 >= r3.length) { /* jump to label_1024 */ }
        // Block 32
        r10 = caughtException
        r9 = r7
        r7 = r7.call
        r7 = r7.call(this, caughtException)
    // EndLoop
}