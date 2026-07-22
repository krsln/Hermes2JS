async function* anon_9594(param0, param1) {
// StartGenerator: prepare generator context and jump to next instruction
r0 = await yield
if (r1) { /* jump to label_102 */ }
r1 = getEnvironment(4)
r1 = r1[16]
r4 = r1.default
r3 = r1.default.get
r2 = globalThis
r1 = globalThis.HermesInternal
r6 = globalThis.HermesInternal.concat
r5 = "https://coachify.ai/api/checkUsernameAvailable?username="
r1 = param1
r1 = globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1)
r1 = await r1.default.get(globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1))
yield label_58;  // SaveGenerator: suspend and jump to 58
return await r1.default.get(globalThis.HermesInternal.concat.call(this, "https://coachify.ai/api/checkUsernameAvailable?username=", param1));
r1 = await yield
if (r1.default.get) { /* jump to label_99 */ }
r4 = globalThis.console
r3 = globalThis.console.log
r2 = r1.data
r2 = globalThis.console.log(r1.data)
r2 = r1.data
r2 = r1.data.available
// CompleteGenerator: No output needed
return r1.data.available;
// CompleteGenerator: No output needed
return undefined_r1;
// CompleteGenerator: No output needed
return undefined_r0;
}