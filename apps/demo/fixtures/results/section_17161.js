async function* anon_17161(param0, param1) {
    // Block 0
    // StartGenerator: prepare generator context and jump to next instruction
    r7 = param1
    r0 = await yield
    if (r1) { /* jump to 168 */ }
    // Block 1
    r2 = globalThis
    r3 = globalThis.fetch
    r1 = undefined
    r1 = await globalThis.fetch(param1)
    yield label_32;  // SaveGenerator: suspend and jump to 32
    // Block 2
    return await globalThis.fetch(param1);
    // Block 3
    r1 = await yield
    if (globalThis.fetch) { /* jump to 165 */ }
    // Block 4
    r3 = r1.ok
    if (r1.ok) { /* jump to 140 */ }
    // Block 5
    r4 = r1.status
    r3 = 0
    if (r1.status !== 0) { /* jump to 80 */ }
    // Block 6
    r4 = param1.startsWith
    r3 = "file://"
    r3 = param1.startsWith("file://")
    if (param1.startsWith("file://") { /* jump to 140 */ }
    // Block 7
    r4 = globalThis.Error
    r6 = r1.status
    r2 = globalThis.HermesInternal
    r5 = globalThis.HermesInternal.concat
    r3 = "Fetching "
    r2 = " failed with status "
    r10 = globalThis.HermesInternal.concat.call(this, "Fetching ", param1, " failed with status ", r1.status)
    r3 = globalThis.Error.prototype
    r3 = createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error)
    r11 = r3
    r2 = new globalThis.Error(" failed with status ", createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error))
    r2 = r3[r2]
    r2 = throw r3[r2]
    // Block 8
    r2 = r1.text
    r2 = await r1.text()
    yield label_153;  // SaveGenerator: suspend and jump to 153
    // Block 9
    return await r1.text();
    // Block 10
    r2 = await yield
    if (createThis(prototype=globalThis.Error.prototype, constructor=globalThis.Error) { /* jump to 162 */ }
    // Block 11
    // CompleteGenerator: No output needed
    return undefined_r2;
    // Block 12
    // CompleteGenerator: No output needed
    return undefined_r2;
    // Block 13
    // CompleteGenerator: No output needed
    return undefined_r1;
    // Block 14
    // CompleteGenerator: No output needed
    return undefined_r0;
}