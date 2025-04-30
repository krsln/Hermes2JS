function func_11944(param0) {
    // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0);
    // CODE -> <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 0>
    r1 = r1[0]
    // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 131>  # String: 'default' (Identifier)
    // USED -> r3 = r1.default
    // CODE -> <LoadConstUndefined>: <Reg8: 2>
    // USED -> r2 = undefined
    // CODE -> <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
    r1 = r1.default.call(this, undefined, r1)
    // CODE -> <Ret>: <Reg8: 0>
    return r0;
}