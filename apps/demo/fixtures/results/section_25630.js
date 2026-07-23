function AcquisitionManager(param0, param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // LINE → <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2
    // LINE → <LoadParam>: <Reg8: 1, UInt8: 0>
    // USED → r1 = this
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 8200>  # String: 'appcenter.ms' (String)
    // USED → r2 = "appcenter.ms"
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 13564>  # String: 'BASE_URL_PART' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms" }
    // LINE → <LoadConstString>: <Reg8: 2, string_id: 1501>  # String: 'v0.1/public/codepush/' (String)
    // USED → r2 = "v0.1/public/codepush/"
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 22128>  # String: '_publicPrefixUrl' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/" }
    // LINE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // LINE → <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 25631>  # Function: [#25631  of 41 bytes]: 2 params @ offset 0x0044ff52
    // USED → r2 = function_25631 /* Closure with env r2 = undefined */
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 24002>  # String: 'isRecoverable' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */ }
    // LINE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 20572>  # String: '_httpRequester' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1 }
    // LINE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 22213>  # String: 'serverUrl' (Identifier)
    // USED → r2 = param2.serverUrl
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }
    // LINE → <GetById>: <Reg8: 4, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r4 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl
    // LINE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 217>  # String: 'slice' (Identifier)
    // USED → r3 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice
    // LINE → <LoadConstInt>: <Reg8: 2, Imm32: -1>
    // USED → r2 = -1
    // LINE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    // USED → r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice(-1)
    // LINE → <LoadConstString>: <Reg8: 3, string_id: 592>  # String: '/' (String)
    // USED → r3 = "/"
    // LINE → <JStrictEqual>: <Addr8: 20, Reg8: 2, Reg8: 3>  # Address: 0000006a
    if ({ BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice(-1) === "/") { /* jump to label_106 */ }
    // ──────────────── Block 1 ──────────────── 
    // LINE → <GetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl
    // LINE → <Add>: <Reg8: 2, Reg8: 2, Reg8: 3>
    // USED → r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/"
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 5, string_id: 22212>  # String: '_serverUrl' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/" }
    // ──────────────── Block 2 ──────────────── 
    // LINE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 4, string_id: 19645>  # String: 'appVersion' (Identifier)
    // USED → r2 = param2.appVersion
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 6, string_id: 19644>  # String: '_appVersion' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion }
    // LINE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 5, string_id: 21704>  # String: 'clientUniqueId' (Identifier)
    // USED → r2 = param2.clientUniqueId
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 7, string_id: 21703>  # String: '_clientUniqueId' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId }
    // LINE → <GetById>: <Reg8: 2, Reg8: 0, UInt8: 6, string_id: 21751>  # String: 'deploymentKey' (Identifier)
    // USED → r2 = param2.deploymentKey
    // LINE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 8, string_id: 21750>  # String: '_deploymentKey' (Identifier)
    // USED → r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId, _deploymentKey: param2.deploymentKey }
    // LINE → <GetById>: <Reg8: 0, Reg8: 0, UInt8: 7, string_id: 21903>  # String: 'ignoreAppVersion' (Identifier)
    // USED → r0 = param2.ignoreAppVersion
    // LINE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 9, string_id: 21902>  # String: '_ignoreAppVersion' (Identifier)
    r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId, _deploymentKey: param2.deploymentKey, _ignoreAppVersion: param2.ignoreAppVersion }
    // LINE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined
    // LINE → <Ret>: <Reg8: 0>
    return undefined;
}