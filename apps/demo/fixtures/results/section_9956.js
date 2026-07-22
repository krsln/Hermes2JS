async function* anon_9956(param0, param1) {
// Block 0
// StartGenerator: prepare generator context and jump to next instruction
r0 = await yield
if (r1) { /* jump to label_61 */ }
// Block 1
r1 = getEnvironment(3)
r1 = r1[16]
r3 = r1.default
r2 = r1.default.get
r4 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr="
r1 = param1
r1 = "https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1
r1 = await r1.default.get("https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1)
yield label_44;  // SaveGenerator: suspend and jump to 44
// Block 2
return await r1.default.get("https://api.edamam.com/api/food-database/v2/parser?app_id=3ac995c0&app_key=86e23e190bd9559f728aeb1010a73765&nutrition-type=logging&ingr=" + param1);
// Block 3
r1 = await yield
if (r1.default.get) { /* jump to label_58 */ }
// Block 4
r2 = r1.data
// CompleteGenerator: No output needed
return r1.data;
// Block 5
// CompleteGenerator: No output needed
return undefined_r1;
// Block 6
// CompleteGenerator: No output needed
return undefined_r0;
}