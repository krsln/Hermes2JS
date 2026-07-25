function AcquisitionManager(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 8200>  # String: 'appcenter.ms' (String)
    // USED → r2 = "appcenter.ms"
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 13564>  # String: 'BASE_URL_PART' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1501>  # String: 'v0.1/public/codepush/' (String)
    // USED → r2 = "v0.1/public/codepush/"
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 22128>  # String: '_publicPrefixUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 25631>  # Function: [#25631  of 41 bytes]: 2 params @ offset 0x0044ff52
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 24002>  # String: 'isRecoverable' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 20572>  # String: '_httpRequester' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 22213>  # String: 'serverUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 217>  # String: 'slice' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstInt>: <Reg8: 2, Imm32: -1>
    // USED → r2 = -1
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    // Error: sequence item 0: expected str instance, Identifier found
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 592>  # String: '/' (String)
    // USED → r3 = "/"
    // CODE → <JStrictEqual>: <Addr8: 20, Reg8: 2, Reg8: 3>  # Address: 0000006a
    if (Identifier(name='r2') === Identifier(name='r3')) { /* jump to label_106 */ }
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // USED → r2 = BinaryExpression(left=Identifier(name='r2'), operator=<BinaryOperator.ADD: '+'>, right=Identifier(name='r3'))
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 19645>  # String: 'appVersion' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 19644>  # String: '_appVersion' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 21704>  # String: 'clientUniqueId' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 7, string_id: 21703>  # String: '_clientUniqueId' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 6, string_id: 21751>  # String: 'deploymentKey' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 21750>  # String: '_deploymentKey' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <GetById>: <Reg8: 0, Reg8: 0, UInt8: 7, string_id: 21903>  # String: 'ignoreAppVersion' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 9, string_id: 21902>  # String: '_ignoreAppVersion' (Identifier)
    // Error: 'Identifier' object has no attribute 'render'
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // CODE → <Ret>: <Reg8: 0>
    ReturnStatement(argument=Identifier(name='r0'))
}