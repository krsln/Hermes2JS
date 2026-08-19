function _interopDefault(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  3 | <JmpFalse>: <Addr8: 14, Reg8: 2>  # Address: 00000011
    if (!param1) goto label_17;
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr:  6 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r1 = r2.__esModule;
    // CODE → addr: 11 | <Mov>: <Reg8: 0, Reg8: 2>
    r0 = param1
    // CODE → addr: 14 | <JmpTrue>: <Addr8: 12, Reg8: 1>  # Address: 0000001a
    if (r2.__esModule) goto label_26;
    // ──────────────── Block 2 ──────────────── 
    // CODE → addr: 17 | <NewObject>: <Reg8: 1>
    r1 = {  }
    // CODE → addr: 19 | <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 2, string_id: 107>  # String: 'default' (Identifier)
    r1.default = param1
    // CODE → addr: 23 | <Mov>: <Reg8: 0, Reg8: 1>
    // USED → r0 = r1;
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr: 26 | <Ret>: <Reg8: 0>
    return r1;
}