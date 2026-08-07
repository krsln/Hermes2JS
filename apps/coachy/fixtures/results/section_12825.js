function function_12825(param0, param1, param2, param3, param4) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 2>
    // USED → r7 = param2;
    // CODE → <LoadParam>: <Reg8: 8, UInt8: 3>
    // USED → r8 = param3;
    // CODE → <LoadParam>: <Reg8: 9, UInt8: 4>
    // USED → r9 = param4;
    // CODE → <LoadConstUndefined>: <Reg8: 6>
    // USED → r6 = undefined;
    // CODE → <LoadConstUndefined>: <Reg8: 10>
    r10 = undefined
    // CODE → <LoadConstFalse>: <Reg8: 5>
    // USED → r5 = false;
    // CODE → <LoadConstFalse>: <Reg8: 0>
    r0 = false
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r1 = param1.slice;
    // CODE → <Call1>: <Reg8: 10, Reg8: 1, Reg8: 2>
    // USED → r10 = param1.slice();
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3614>  # String: 'Error occurred in ' (String)
    // USED → r3 = "Error occurred in ";
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 11214>  # String: ' callback, continuing anyway…' (String)
    // USED → r2 = " callback, continuing anyway\u2026";
    // LOOP → START (while)
    while (true) {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <Mov>: <Reg8: 1, Reg8: 10>
        // USED → r1 = param1.slice();
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 139>  # String: 'length' (Identifier)
        // USED → r1 = param1.slice().length;
        if (param1.slice().length) {
            try {
                // ──────────────── Block 2 ──────────────── 
                // CODE → <Mov>: <Reg8: 11, Reg8: 10>
                // USED → r11 = param1.slice();
                // CODE → <GetById>: <Reg8: 1, Reg8: 11, UInt8: 3, string_id: 16799>  # String: 'pop' (Identifier)
                // USED → r1 = param1.slice().pop;
                // CODE → <Call1>: <Reg8: 11, Reg8: 1, Reg8: 11>
                // USED → r11 = param1.slice().pop();
                // CODE → <Mov>: <Reg8: 1, Reg8: 7>
                // USED → r1 = param2;
                // CODE → <Call2>: <Reg8: 1, Reg8: 11, Reg8: 6, Reg8: 1>
                // USED → r1 = param1.slice().pop().call(undefined, param2);
                // CODE → <StrictEq>: <Reg8: 0, Reg8: 1, Reg8: 5>
                // USED → r0 = param1.slice().pop().call(undefined, param2) === false;
                // CODE → <Jmp>: <Addr8: 47>  # Address: 0000007a
                goto label_122;
            } catch (caughtException) {
                // LOOP → START (while)
                while (true) {
                    // ──────────────── Block 4 ──────────────── 
                    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
                    // USED → r1 = param1.slice().pop().call(undefined, param2) === false && param4.error(caughtException);
                }
                // LOOP → END
            }
        }
    }
    // LOOP → END
    // ──────────────── Block 5 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    return param1.slice().pop().call(undefined, param2) === false;
}