function processColorsInProps(param0, param1) {
    // CODE → <LoadParam>: <Reg8: 10, UInt8: 1>
    // USED → r10 = param1
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 7>
    r7 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 8>
    r8 = undefined
    // CODE → <LoadConstUndefined>: <Reg8: 9>
    r9 = undefined
    // CODE → <Mov>: <Reg8: 5, Reg8: 10>
    // USED → r5 = r10
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 1>
    r1 = getEnvironment(1)
    // CODE → <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
    // USED → r6 = Object.keys(r10) /* for-in property list */
    // CODE → <JmpUndefinedLong>: <Addr32: 161, Reg8: 6>  # Address: 000000b7
    if (Object.keys(r10) /* for-in property list */ === undefined) {
        goto label_183;  // unstructured control flow, needs review
    } else {
        goto label_28;  // unstructured control flow, needs review
    }
}