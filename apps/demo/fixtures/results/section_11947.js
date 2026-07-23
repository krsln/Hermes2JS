async function* anon_11947(param0, param1, param2) {
    // Block 0
    // StartGenerator: prepare generator context and jump to next instruction
    r8 = this
    r0 = await yield
    if (r5) { /* jump to label_318 */ }
    // Block 1
    r4 = param1
    r3 = param2
    r5 = undefined
    r6 = undefined
    r2 = undefined
    r7 = this._request
    r3 = await this._request(param1, param2)
    yield label_41;  // SaveGenerator: suspend and jump to 41
    // Block 2
    return await this._request(param1, param2);
    // Block 3
    r3 = await yield
    if (param1) { /* jump to label_50 */ }
    // Block 4
    // CompleteGenerator: No output needed
    return undefined_r3;
    // Block 5
    // CompleteGenerator: No output needed
    return undefined_r3;
    r7 = caughtException
    r1 = r7
    r3 = globalThis
    r4 = globalThis.Error
    r4 = caughtException instanceof globalThis.Error
    if (!caughtException instanceof globalThis.Error) { /* jump to label_316 */ }
    // Block 6
    r6 = {}
    r4 = globalThis.Error
    r4 = globalThis.Error.captureStackTrace
    r8 = globalThis.Error
    if (globalThis.Error.captureStackTrace) { /* jump to label_121 */ }
    // Block 7
    r4 = globalThis.Error.prototype
    r7 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
    r12 = r7
    r4 = new globalThis.Error(createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
    r6 = r7[r4]
    goto label_135;
    // Block 8
    r7 = globalThis.Error.captureStackTrace
    r4 = r6
    r4 = globalThis.Error.captureStackTrace(r6)
    // Block 9
    r4 = r6
    r7 = r6.stack
    r8 = ""
    r4 = r8
    if (!r6.stack) { /* jump to label_185 */ }
    // Block 10
    r9 = r7[r4].stack
    r7 = r7[r4].stack.replace
    r6 = /^.+\\n/
    r4 = r7[r4].stack.replace(/^.+\\n/, "")
    // Block 11
    r2 = r4
    r4 = r1
    r4 = r1.stack
    if (r1.stack) { /* jump to label_214 */ }
    // Block 12
    r6 = r1
    r4 = r2
    r6 = { stack: r2 }
    goto label_312;
    // Block 13
    r4 = r2
    if (!r2) { /* jump to label_312 */ }
    // Block 14
    r4 = globalThis.String
    r3 = r1
    r3 = r1.stack
    r5 = globalThis.String(r1.stack)
    r4 = globalThis.String(r1.stack).endsWith
    r7 = r2
    r6 = r2.replace
    r3 = /^.+\\n.+\\n/
    r3 = r2.replace(/^.+\\n.+\\n/, "")
    r3 = globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, ""))
    if (globalThis.String(r1.stack).endsWith(r2.replace(/^.+\\n.+\\n/, ""))) { /* jump to label_312 */ }
    // Block 15
    r3 = r1
    r4 = r1.stack
    r5 = r2
    r2 = "\n"
    r2 = "\n" + r2
    r2 = r1.stack + "\n" + r2
    r3 = { stack: r1.stack + "\n" + r2 }
    // Block 16
    goto label_316;
    // Loop (LoopKind.WHILE)
    while (true) {
        // Block 18
        r1 = throw r7
        // Block 17
        r2 = caughtException
    } /* EndLoop */
    // Block 19
    // CompleteGenerator: No output needed
    return undefined_r0;
}