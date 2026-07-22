function onPress(param0) {
    // Block 0
    r1 = getEnvironment(0)
    r2 = r1[0]
    r0 = getEnvironment(1)
    if (r2) { /* jump to label_123 */ }
    // Block 1
    r2 = r0[10]
    r2 = r2.default
    r3 = r2.default.prototype
    r3 = createThis(prototype=r2.default.prototype, constructor=r2.default)
    r8 = r3
    r2 = new r2.default(r1)
    r3 = r3[r2]
    r2 = r3[r2].trackJoinCompetitionList
    r2 = r3[r2].trackJoinCompetitionList()
    r2 = r0[11]
    r4 = r2.default
    r3 = undefined
    r2 = { message: "You have joined the list", type: "success" }
    r2 = r2.default({ message: "You have joined the list", type: "success" })
    r2 = r0[4]
    r5 = r2.default
    r4 = r2.default.setItem
    r3 = "compjoin"
    r2 = "true"
    r2 = r2.default.setItem("compjoin", "true")
    r2 = r1[3]
    r1 = r2.goBack
    r1 = r2.goBack()
    goto label_153;
    // Block 2
    r0 = r0[12]
    r2 = r0.default
    r1 = r0.default.open
    r0 = { title: "Join Coachify AI Competition", message: "Join Coachify AI Competition", url: "https://coachify.ai/download?ref=compshare", subject: "Join Coachify AI Competition" }
    r0 = r0.default.open({ title: "Join Coachify AI Competition", message: "Join Coachify AI Competition", url: "https://coachify.ai/download?ref=compshare", subject: "Join Coachify AI Competition" })
    // Block 3
    r0 = undefined
    return undefined;
}