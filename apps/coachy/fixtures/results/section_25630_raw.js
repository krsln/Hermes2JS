function AcquisitionManager(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 8200>  # String: 'appcenter.ms' (String)
    // USED → r2 = "appcenter.ms";
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 13564>  # String: 'BASE_URL_PART' (Identifier)
    this.BASE_URL_PART = "appcenter.ms"
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 1501>  # String: 'v0.1/public/codepush/' (String)
    // USED → r2 = "v0.1/public/codepush/";
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 22128>  # String: '_publicPrefixUrl' (Identifier)
    this._publicPrefixUrl = "v0.1/public/codepush/"
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 25631>  # Function: [#25631  of 41 bytes]: 2 params @ offset 0x0044ff52
    // USED → r2 = function_25631;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 24002>  # String: 'isRecoverable' (Identifier)
    this.isRecoverable = function_25631
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 20572>  # String: '_httpRequester' (Identifier)
    this._httpRequester = param1
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 22213>  # String: 'serverUrl' (Identifier)
    // USED → r2 = param2.serverUrl;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    this._serverUrl = param2.serverUrl
    // CODE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r4 = this._serverUrl;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r3 = this._serverUrl.slice;
    // CODE → <LoadConstInt>: <Reg8: 2, Imm32: -1>
    // USED → r2 = -1;
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r2 = this._serverUrl.slice(-1);
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 592>  # String: '/' (String)
    // USED → r3 = "/";
    // CODE → <JStrictEqual>: <Addr8: 20, Reg8: 2, Reg8: 3>  # Address: 0000006a
    if (this._serverUrl.slice(-1) === "/") goto label_106;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r2 = this._serverUrl;
    // CODE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // USED → r2 = this._serverUrl + "/";
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    this._serverUrl = this._serverUrl + "/"
    // ──────────────── Block 2 ──────────────── 
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 19645>  # String: 'appVersion' (Identifier)
    // USED → r2 = param2.appVersion;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 19644>  # String: '_appVersion' (Identifier)
    this._appVersion = param2.appVersion
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 21704>  # String: 'clientUniqueId' (Identifier)
    // USED → r2 = param2.clientUniqueId;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 7, string_id: 21703>  # String: '_clientUniqueId' (Identifier)
    this._clientUniqueId = param2.clientUniqueId
    // CODE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 6, string_id: 21751>  # String: 'deploymentKey' (Identifier)
    // USED → r2 = param2.deploymentKey;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 21750>  # String: '_deploymentKey' (Identifier)
    this._deploymentKey = param2.deploymentKey
    // CODE → <GetById>: <Reg8: 0, Reg8: 0, UInt8: 7, string_id: 21903>  # String: 'ignoreAppVersion' (Identifier)
    // USED → r0 = param2.ignoreAppVersion;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 9, string_id: 21902>  # String: '_ignoreAppVersion' (Identifier)
    this._ignoreAppVersion = param2.ignoreAppVersion
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}