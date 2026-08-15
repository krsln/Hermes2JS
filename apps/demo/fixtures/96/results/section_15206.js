function _interopDefault(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    if (!param1) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → <NewObject>: <Reg8: 1>
        r1 = {  }
        // CODE → <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 107>  # String: 'default' (Identifier)
        r1.default = param1
        // CODE → <Mov>: <Reg8: 0, Reg8: 1>
        // USED → r0 = r1;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 48>  # String: '__esModule' (Identifier)
        // USED → r1 = param1.__esModule;
        // CODE → <Mov>: <Reg8: 0, Reg8: 2>
        r0 = param1
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → <Ret>: <Reg8: 0>
    return r1;
}