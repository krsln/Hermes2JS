async function* anon_11947(param0, param1, param2) {
    // CODE -> <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE -> <LoadParam>: <Reg8: 8, UInt8: 0>
    // USED -> r8 = param0
    // CODE -> <ResumeGenerator>: <Reg8: 0, Reg8: 5>
    // label_4:
    r0 = await yield; // Resume generator
    // CODE -> <JmpTrueLong>: <Addr32: 311, Reg8: 5>  # Address: 0000013e
    if (r5) {
        // CODE -> <LoadParam>: <Reg8: 4, UInt8: 1>
        // USED -> r4 = param1
        // CODE -> <LoadParam>: <Reg8: 3, UInt8: 2>
        // USED -> r3 = param2
        // CODE -> <LoadConstUndefined>: <Reg8: 5>
        // USED -> r5 = undefined
        // CODE -> <LoadConstUndefined>: <Reg8: 6>
        r6 = undefined
        // CODE -> <LoadConstUndefined>: <Reg8: 2>
        r2 = undefined
        // CODE -> <GetById>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 17057>  # String: '_request' (Identifier)
        // USED -> r7 = param0._request
        // CODE -> <Call3>: <Reg8: 3, Reg8: 7, Reg8: 8, Reg8: 4, Reg8: 3>
        // USED -> r3 = await param0._request(param1, param2)
        // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 00000029
        // await yield; // check: JSConverter.Dispatcher // Resume at label_4
        // CODE -> <Ret>: <Reg8: 3>
        return await param0._request(param1, param2);
        // CODE -> <ResumeGenerator>: <Reg8: 3, Reg8: 4>
        r3 = await yield; // Resume generator
        // CODE -> <JmpTrue>: <Addr8: 6, Reg8: 4>  # Address: 00000032
        if (param1) {
            // CODE -> <CompleteGenerator>: <>
            // CODE -> <Ret>: <Reg8: 3>
            return r3;
        }
        // CODE -> <CompleteGenerator>: <>
        // label_50:
        // CODE -> <Ret>: <Reg8: 3>
        return r3;
        // CODE -> <Catch>: <Reg8: 7>
        // USED -> r7 = caughtException
        // CODE -> <Mov>: <Reg8: 1, Reg8: 7>
        // USED -> r1 = r7
        // CODE -> <GetGlobalObject>: <Reg8: 3>
        // USED -> r3 = this
        // CODE -> <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
        // USED -> r4 = this.Error
        // CODE -> <InstanceOf>: <Reg8: 4, Reg8: 7, Reg8: 4>
        // USED -> r4 = caughtException instanceof this.Error
        // CODE -> <JmpFalseLong>: <Addr32: 246, Reg8: 4>  # Address: 0000013c
        if (!caughtException instanceof this.Error) {
            // CODE -> <NewObject>: <Reg8: 6>
            r6 = {}
            // CODE -> <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
            // USED -> r4 = this.Error
            // CODE -> <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
            // USED -> r4 = this.Error.captureStackTrace
            // CODE -> <TryGetById>: <Reg8: 8, Reg8: 3, UInt8: 2, string_id: 14>  # String: 'Error' (Identifier)
            // USED -> r8 = this.Error
            // CODE -> <JmpTrue>: <Addr8: 25, Reg8: 4>  # Address: 00000079
            if (this.Error.captureStackTrace) {
                // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 8, UInt8: 4, string_id: 158>  # String: 'prototype' (Identifier)
                // USED -> r4 = this.Error.prototype
                // CODE -> <CreateThis>: <Reg8: 7, Reg8: 4, Reg8: 8>
                r7 = createThis(prototype=this.Error.prototype, constructor=this.Error)
                // CODE -> <Mov>: <Reg8: 12, Reg8: 7>
                r12 = r7
                // CODE -> <Construct>: <Reg8: 4, Reg8: 8, UInt8: 1>
                r4 = new this.Error(arg0);
                // CODE -> <SelectObject>: <Reg8: 6, Reg8: 7, Reg8: 4>
                // USED -> r6 = r7[r4]
                // CODE -> <Jmp>: <Addr8: 16>  # Address: 00000087
                goto label_135;
            }
            // CODE -> <GetById>: <Reg8: 7, Reg8: 8, UInt8: 3, string_id: 22838>  # String: 'captureStackTrace' (Identifier)
            // label_121:
            // USED -> r7 = this.Error.captureStackTrace
            // CODE -> <Mov>: <Reg8: 4, Reg8: 6>
            // USED -> r4 = r6
            // CODE -> <Call2>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 4>
            r4 = this.Error.captureStackTrace(r6)
            // CODE -> <Mov>: <Reg8: 4, Reg8: 6>
            // label_135:
            // USED -> r4 = r6
            // CODE -> <GetById>: <Reg8: 7, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
            // USED -> r7 = r6.stack
            // CODE -> <LoadConstString>: <Reg8: 8, string_id: 11303>  # String: '' (Identifier)
            // USED -> r8 = ""
            // CODE -> <Mov>: <Reg8: 4, Reg8: 8>
            r4 = r8
            // CODE -> <JmpFalse>: <Addr8: 34, Reg8: 7>  # Address: 000000b9
            if (!r6.stack) {
                // CODE -> <GetById>: <Reg8: 9, Reg8: 6, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
                // USED -> r9 = r7[r4].stack
                // CODE -> <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
                // USED -> r7 = r7[r4].stack.replace
                // CODE -> <CreateRegExp>: <Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168>  # String: '^.+\\n' (String)  # String: '' (Identifier)
                // Error: CreateRegExp at address 165: Expected Reg8 and three UInt32 arguments: Reg8: 6, string_id: 7558, string_id: 11303, UInt32: 168
                // CODE -> <Call3>: <Reg8: 4, Reg8: 7, Reg8: 9, Reg8: 6, Reg8: 8>
                r4 = r7[r4].stack.replace(r7[r4], "")
            }
            // CODE -> <Mov>: <Reg8: 2, Reg8: 4>
            // label_185:
            r2 = r4
            // CODE -> <Mov>: <Reg8: 4, Reg8: 1>
            // USED -> r4 = r1
            // CODE -> <GetById>: <Reg8: 4, Reg8: 4, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
            // USED -> r4 = r1.stack
            // CODE -> <JmpTrue>: <Addr8: 17, Reg8: 4>  # Address: 000000d6
            if (r1.stack) {
                // CODE -> <Mov>: <Reg8: 6, Reg8: 1>
                // USED -> r6 = r1
                // CODE -> <Mov>: <Reg8: 4, Reg8: 2>
                // USED -> r4 = r2
                // CODE -> <PutById>: <Reg8: 6, Reg8: 4, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
                r6 = { stack: r2 }
                // CODE -> <Jmp>: <Addr8: 100>  # Address: 00000138
                goto label_312;
            }
            // CODE -> <Mov>: <Reg8: 4, Reg8: 2>
            // label_214:
            // USED -> r4 = r2
            // CODE -> <JmpFalse>: <Addr8: 95, Reg8: 4>  # Address: 00000138
            if (!r2) {
                // CODE -> <TryGetById>: <Reg8: 4, Reg8: 3, UInt8: 7, string_id: 50>  # String: 'String' (Identifier)
                // USED -> r4 = this.String
                // CODE -> <Mov>: <Reg8: 3, Reg8: 1>
                // USED -> r3 = r1
                // CODE -> <GetById>: <Reg8: 3, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
                // USED -> r3 = r1.stack
                // CODE -> <Call2>: <Reg8: 5, Reg8: 4, Reg8: 5, Reg8: 3>
                // USED -> r5 = this.String(r1.stack)
                // CODE -> <GetById>: <Reg8: 4, Reg8: 5, UInt8: 8, string_id: 19080>  # String: 'endsWith' (Identifier)
                // USED -> r4 = this.String(r1.stack).endsWith
                // CODE -> <Mov>: <Reg8: 7, Reg8: 2>
                // USED -> r7 = r2
                // CODE -> <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 6, string_id: 206>  # String: 'replace' (Identifier)
                // USED -> r6 = r2.replace
                // CODE -> <CreateRegExp>: <Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169>  # String: '^.+\\n.+\\n' (String)  # String: '' (Identifier)
                // Error: CreateRegExp at address 254: Expected Reg8 and three UInt32 arguments: Reg8: 3, string_id: 7559, string_id: 11303, UInt32: 169
                // CODE -> <Call3>: <Reg8: 3, Reg8: 6, Reg8: 7, Reg8: 3, Reg8: 8>
                // USED -> r3 = r2.replace(r1.stack, "")
                // CODE -> <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
                // USED -> r3 = this.String(r1.stack).endsWith(r2.replace(r1.stack, ""))
                // CODE -> <JmpTrue>: <Addr8: 33, Reg8: 3>  # Address: 00000138
                if (this.String(r1.stack) {
                    // CODE -> <Mov>: <Reg8: 3, Reg8: 1>
                    // USED -> r3 = r1
                    // CODE -> <GetById>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 12363>  # String: 'stack' (Identifier)
                    r4 = r1.stack
                    // CODE -> <Mov>: <Reg8: 5, Reg8: 2>
                    r5 = r2
                    // CODE -> <LoadConstString>: <Reg8: 2, string_id: 12321>  # String: '\n' (Identifier)
                    // USED -> r2 = "\n"
                    // CODE -> <PutById>: <Reg8: 3, Reg8: 2, UInt8: 1, string_id: 12363>  # String: 'stack' (Identifier)
                    r3 = { stack: "\n" }
                }
            }
            // CODE -> <Jmp>: <Addr8: 4>  # Address: 0000013c
            // label_312:
            goto label_316;
            // CODE -> <Catch>: <Reg8: 2>
            r2 = caughtException
        }
        // CODE -> <Throw>: <Reg8: 1>
        // label_316:
        r1 = throw r7
    }
    // CODE -> <CompleteGenerator>: <>
    // label_318:
    // CODE -> <Ret>: <Reg8: 0>
    return r0;
}