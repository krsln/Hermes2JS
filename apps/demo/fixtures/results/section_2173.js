function parseLinearGradientCSSString(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    // USED → r3 = getParentEnvironment(0);
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 1>
    // USED → r6 = param1;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 0, string_id: 230>  # String: 'split' (Identifier)
    // USED → r5 = param1.split;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 559>  # String: ',' (String)
    // USED → r4 = ",";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    // USED → r4 = param1.split(",");
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 3, UInt8: 9>
    r5 = getParentEnvironment(0)[9]
    // CODE → <GetByIndex>: <Reg8: 7, Reg8: 4, UInt8: 0>
    // USED → r7 = param1.split(",")[0];
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 1, string_id: 202>  # String: 'trim' (Identifier)
    // USED → r6 = param1.split(",")[0].trim;
    // CODE → <Call1>: <Reg8: 7, Reg8: 6, Reg8: 7>
    // USED → r7 = param1.split(",")[0].trim();
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 242>  # String: 'toLowerCase' (Identifier)
    // USED → r6 = param1.split(",")[0].trim().toLowerCase;
    // CODE → <Call1>: <Reg8: 7, Reg8: 6, Reg8: 7>
    // USED → r7 = param1.split(",")[0].trim().toLowerCase();
    // CODE → <LoadFromEnvironment>: <Reg8: 8, Reg8: 3, UInt8: 8>
    // USED → r8 = getParentEnvironment(0)[8];
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 8, UInt8: 3, string_id: 45>  # String: 'test' (Identifier)
    // USED → r6 = getParentEnvironment(0)[8].test;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 8, Reg8: 7>
    // USED → r6 = getParentEnvironment(0)[8].test(param1.split(",")[0].trim().toLowerCase());
    // CODE → <JmpTrueLong>: <Addr32: 167, Reg8: 6>  # Address: 000000e3
    if (getParentEnvironment(0)[8].test(param1.split(",")[0].trim().toLowerCase())) goto label_227;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 8, Reg8: 3, UInt8: 7>
    // USED → r8 = getParentEnvironment(0)[7];
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 8, UInt8: 3, string_id: 45>  # String: 'test' (Identifier)
    // USED → r6 = getParentEnvironment(0)[7].test;
    // CODE → <Call2>: <Reg8: 6, Reg8: 6, Reg8: 8, Reg8: 7>
    // USED → r6 = getParentEnvironment(0)[7].test(param1.split(",")[0].trim().toLowerCase());
    // CODE → <JmpFalseLong>: <Addr32: 188, Reg8: 6>  # Address: 0000010c
    if (!getParentEnvironment(0)[7].test(param1.split(",")[0].trim().toLowerCase())) goto label_268;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <Eq>: <Reg8: 2, Reg8: 7, Reg8: 1>
    // USED → r2 = param1.split(",")[0].trim().toLowerCase() == null;
    // CODE → <LoadConstNull>: <Reg8: 6>
    r6 = null
    // CODE → <JmpTrue>: <Addr8: 113, Reg8: 2>  # Address: 000000cf
    if (param1.split(",")[0].trim().toLowerCase() == null) goto label_207;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 10, Reg8: 7, UInt8: 4, string_id: 218>  # String: 'replace' (Identifier)
    // USED → r10 = param1.split(",")[0].trim().toLowerCase().replace;
    // CODE → <LoadFromEnvironment>: <Reg8: 9, Reg8: 3, UInt8: 6>
    // USED → r9 = getParentEnvironment(0)[6];
    // CODE → <LoadConstString>: <Reg8: 8, string_id: 807>  # String: ' ' (String)
    // USED → r8 = " ";
    // CODE → <Call3>: <Reg8: 9, Reg8: 10, Reg8: 7, Reg8: 9, Reg8: 8>
    // USED → r9 = param1.split(",")[0].trim().toLowerCase().replace(getParentEnvironment(0)[6], " ");
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 242>  # String: 'toLowerCase' (Identifier)
    // USED → r8 = param1.split(",")[0].trim().toLowerCase().replace(getParentEnvironment(0)[6], " ").toLowerCase;
    // CODE → <Call1>: <Reg8: 8, Reg8: 8, Reg8: 9>
    // USED → r8 = param1.split(",")[0].trim().toLowerCase().replace(getParentEnvironment(0)[6], " ").toLowerCase();
    // CODE → <LoadConstNull>: <Reg8: 6>
    r6 = null
    // CODE → <StringSwitchImm>: <Reg8: 8, UInt32: 2, UInt32: 176, Addr32: 80, UInt32: 12>  # Address: 000000cf
    // Raw TerminatorSwitch reached Printer. SwitchStructurer should have converted it into a SwitchRegion.
    // LOOP → START (while)
    while ({ "type": "angle", "value": 0 } != null) {
        // ──────────────── Block 12 ──────────────── 
        // CODE → <JNotEqual>: <Addr8: 6, Reg8: 6, Reg8: 1>  # Address: 000000d5
        if ({ "type": "angle", "value": 0 } != null) goto label_213;
        // ──────────────── Block 4 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46187>  # Object: {'type': 'keyword', 'value': 'to bottom left'}
        r6 = { "type": "keyword", "value": "to bottom left" }
        // CODE → <Jmp>: <Addr8: 56>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 5 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46192>  # Object: {'type': 'keyword', 'value': 'to top left'}
        r6 = { "type": "keyword", "value": "to top left" }
        // CODE → <Jmp>: <Addr8: 48>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 6 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46197>  # Object: {'type': 'keyword', 'value': 'to bottom right'}
        r6 = { "type": "keyword", "value": "to bottom right" }
        // CODE → <Jmp>: <Addr8: 40>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 7 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 18917>  # Object: {'type': 'keyword', 'value': 'to top right'}
        r6 = { "type": "keyword", "value": "to top right" }
        // CODE → <Jmp>: <Addr8: 32>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 8 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46202>  # Object: {'type': 'angle', 'value': 270}
        r6 = { "type": "angle", "value": 270 }
        // CODE → <Jmp>: <Addr8: 24>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 9 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 18070>  # Object: {'type': 'angle', 'value': 180}
        r6 = { "type": "angle", "value": 180 }
        // CODE → <Jmp>: <Addr8: 16>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 10 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46210>  # Object: {'type': 'angle', 'value': 90}
        r6 = { "type": "angle", "value": 90 }
        // CODE → <Jmp>: <Addr8: 8>  # Address: 000000cf
        goto label_207;
        // ──────────────── Block 11 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46218>  # Object: {'type': 'angle', 'value': 0}
        // USED → r6 = { "type": "angle", "value": 0 };
    }
    // LOOP → END
    // ──────────────── Block 13 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return null;
    // ──────────────── Block 14 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 4, UInt8: 5, string_id: 228>  # String: 'shift' (Identifier)
    // USED → r8 = param1.split(",").shift;
    // CODE → <Call1>: <Reg8: 8, Reg8: 8, Reg8: 4>
    r8 = param1.split(",").shift()
    // CODE → <Mov>: <Reg8: 5, Reg8: 6>
    r5 = { "type": "angle", "value": 0 }
    // CODE → <Jmp>: <Addr8: 43>  # Address: 0000010c
    goto label_268;
    // ──────────────── Block 15 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 6, Reg8: 3, UInt8: 20>
    // USED → r6 = getParentEnvironment(0)[20];
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call2>: <Reg8: 7, Reg8: 6, Reg8: 0, Reg8: 7>
    // USED → r7 = getParentEnvironment(0)[20].call(0, param1.split(",")[0].trim().toLowerCase());
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <JNotEqual>: <Addr8: 6, Reg8: 7, Reg8: 1>  # Address: 000000f6
    if (getParentEnvironment(0)[20].call(0, param1.split(",")[0].trim().toLowerCase()) != null) goto label_246;
    // ──────────────── Block 16 ──────────────── 
    // CODE → <Ret>: <Reg8: 1>
    return null;
    // ──────────────── Block 17 ──────────────── 
    // CODE → <NewObjectWithBuffer>: <Reg8: 6, UInt16: 53, UInt16: 46156>  # Object: {'type': 'angle', 'value': null}
    // USED → r6 = { "type": "angle", "value": null };
    // CODE → <PutOwnBySlotIdx>: <Reg8: 6, Reg8: 7, UInt8: 1>
    { "type": "angle", "value": null }.slot_1 = getParentEnvironment(0)[20].call(0, param1.split(",")[0].trim().toLowerCase())
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 228>  # String: 'shift' (Identifier)
    // USED → r7 = param1.split(",").shift;
    // CODE → <Call1>: <Reg8: 7, Reg8: 7, Reg8: 4>
    r7 = param1.split(",").shift()
    // CODE → <Mov>: <Reg8: 5, Reg8: 6>
    // USED → r5 = { "type": "angle", "value": null };
    // ──────────────── Block 18 ──────────────── 
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 18>
    // USED → r3 = getParentEnvironment(0)[18];
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <Call2>: <Reg8: 4, Reg8: 3, Reg8: 0, Reg8: 4>
    // USED → r4 = getParentEnvironment(0)[18].call(0, param1.split(","));
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    if (getParentEnvironment(0)[18].call(0, param1.split(",")) == null) {
        // ──────────────── Block 20 ──────────────── 
        // CODE → <Ret>: <Reg8: 1>
        return null;
    } else {
        // ──────────────── Block 19 ──────────────── 
        // CODE → <NewObjectWithBuffer>: <Reg8: 3, UInt16: 927, UInt16: 46152>  # Object: {'type': 'linear-gradient', 'direction': null, 'colorStops': null}
        // USED → r3 = { "type": "linear-gradient", "direction": null, "colorStops": null };
        // CODE → <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 5, UInt8: 1>
        { "type": "linear-gradient", "direction": null, "colorStops": null }.slot_1 = { "type": "angle", "value": null }
        // CODE → <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 4, UInt8: 2>
        { "type": "linear-gradient", "direction": null, "colorStops": null }.slot_2 = getParentEnvironment(0)[18].call(0, param1.split(","))
        // CODE → <Ret>: <Reg8: 3>
        return { "type": "linear-gradient", "direction": null, "colorStops": null };
    }
}