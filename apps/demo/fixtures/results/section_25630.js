function AcquisitionManager(param0, param1, param2) {
r0 = param2
r1 = this
r2 = "appcenter.ms"
r1 = { BASE_URL_PART: "appcenter.ms" }
r2 = "v0.1/public/codepush/"
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/" }
r2 = createEnvironment()
r2 = function_25631 /* Closure with env r2 = undefined */
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */ }
r2 = param1
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1 }
r2 = param2.serverUrl
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }
r4 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl
r3 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice
r2 = -1
r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice(-1)
r3 = "/"
if ({ BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl.slice(-1) === "/") { /* jump to label_106 */ }
r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl
r2 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/"
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/" }
r2 = param2.appVersion
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion }
r2 = param2.clientUniqueId
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId }
r2 = param2.deploymentKey
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId, _deploymentKey: param2.deploymentKey }
r0 = param2.ignoreAppVersion
r1 = { BASE_URL_PART: "appcenter.ms", _publicPrefixUrl: "v0.1/public/codepush/", isRecoverable: function_25631 /* Closure with env r2 = undefined */, _httpRequester: param1, _serverUrl: param2.serverUrl }._serverUrl + "/", _appVersion: param2.appVersion, _clientUniqueId: param2.clientUniqueId, _deploymentKey: param2.deploymentKey, _ignoreAppVersion: param2.ignoreAppVersion }
r0 = undefined
return undefined;
}