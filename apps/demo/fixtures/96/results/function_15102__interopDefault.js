function _interopDefault(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    if (param1 && param1.__esModule) {
        // ──────────────── Block 4 ──────────────── 
        // CODE → addr: 11 | <Mov>: <Reg8: 0, Reg8: 2>
        r0 = param1;
    } else {
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr: 17 | <NewObject>: <Reg8: 1>
        // USED → r1 = {  };
        // CODE → addr: 19 | <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 107>  # String: 'default' (Identifier)
        r1 = { "default": param1 };
        // CODE → addr: 23 | <Mov>: <Reg8: 0, Reg8: 1>
        r0 = r1;
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 26 | <Ret>: <Reg8: 0>
    return r0;
}