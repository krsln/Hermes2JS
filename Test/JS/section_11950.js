async function* anon_11950(param0, param1) {
    // CODE -> <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE -> <ResumeGenerator>: <Reg8: 0, Reg8: 3>
    r0 = await yield; // Resume generator
    // CODE -> <JmpTrueLong>: <Addr32: 233, Reg8: 3>  # Address: 000000ed
    // label_4:
    if (r3) {
        // CODE -> <LoadParam>: <Reg8: 1, UInt8: 1>
        r1 = param1
        // CODE -> <LoadConstUndefined>: <Reg8: 6>
        // USED -> r6 = undefined
        // CODE -> <LoadConstUndefined>: <Reg8: 2>
        r2 = undefined
        // CODE -> <GetGlobalObject>: <Reg8: 3>
        // USED -> r3 = this
        // CODE -> <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 1, string_id: 7603>  # String: 'fetch' (Identifier)
        // USED -> r5 = this.fetch
        // CODE -> <GetEnvironment>: <Reg8: 4, UInt8: 2>
        r4 = getEnvironment(2);
        // CODE -> <LoadFromEnvironment>: <Reg8: 7, Reg8: 4, UInt8: 1>
        r7 = r4[1]
        // CODE -> <GetById>: <Reg8: 17, Reg8: 7, UInt8: 2, string_id: 6728>  # String: 'BASE_URL' (Identifier)
        r17 = r7.BASE_URL
        // CODE -> <Mov>: <Reg8: 15, Reg8: 1>
        r15 = r1
        // CODE -> <GetById>: <Reg8: 13, Reg8: 7, UInt8: 3, string_id: 7508>  # String: 'API_KEY' (Identifier)
        r13 = r7.API_KEY
        // CODE -> <TryGetById>: <Reg8: 1, Reg8: 3, UInt8: 4, string_id: 15>  # String: 'HermesInternal' (Identifier)
        // USED -> r1 = this.HermesInternal
        // CODE -> <GetByIdShort>: <Reg8: 9, Reg8: 1, UInt8: 5, string_id: 120>  # String: 'concat' (Identifier)
        // USED -> r9 = this.HermesInternal.concat
        // CODE -> <LoadConstString>: <Reg8: 18, string_id: 6377>  # String: '' (Identifier)
        r18 = ""
        // CODE -> <LoadConstString>: <Reg8: 16, string_id: 1447>  # String: '/movie/' (String)
        r16 = "/movie/"
        // CODE -> <LoadConstString>: <Reg8: 14, string_id: 2315>  # String: '?api_key=' (String)
        r14 = "?api_key="
        // CODE -> <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
        // USED -> r4 = this.HermesInternal.concat.call(this, this, r4, this.fetch, undefined, r7, r8)
        // CODE -> <NewObject>: <Reg8: 1>
        // USED -> r1 = {}
        // CODE -> <LoadConstString>: <Reg8: 8, string_id: 7782>  # String: 'GET' (Identifier)
        // USED -> r8 = "GET"
        // CODE -> <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 8, string_id: 158>  # String: 'method' (Identifier)
        // USED -> r1 = { method: "GET" }
        // CODE -> <GetByIdShort>: <Reg8: 7, Reg8: 7, UInt8: 6, string_id: 169>  # String: 'headers' (Identifier)
        // USED -> r7 = r7.headers
        // CODE -> <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 7, string_id: 169>  # String: 'headers' (Identifier)
        // USED -> r1 = { method: "GET", headers: r7.headers }
        // CODE -> <Call3>: <Reg8: 1, Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 1>
        // USED -> r1 = await this.fetch(this.HermesInternal.concat.call(this, this, r4, this.fetch, undefined, r7, r8), { method: "GET", headers: r7.headers })
        // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 00000067
        // await yield; // check: JSConverter.Dispatcher // Resume at label_4
        // CODE -> <Ret>: <Reg8: 1>
        return await this.fetch(this.HermesInternal.concat.call(this, this, r4, this.fetch, undefined, r7, r8), { method: "GET", headers: r7.headers });
        // CODE -> <ResumeGenerator>: <Reg8: 1, Reg8: 4>
        r1 = await yield; // Resume generator
        // CODE -> <JmpTrue>: <Addr8: 101, Reg8: 4>  # Address: 000000cf
        if (this.HermesInternal.concat.call(this, this, r4, this.fetch, undefined, r7, r8) {
            // CODE -> <Mov>: <Reg8: 2, Reg8: 1>
            r2 = r1
            // CODE -> <GetById>: <Reg8: 4, Reg8: 1, UInt8: 7, string_id: 7823>  # String: 'ok' (Identifier)
            // USED -> r4 = r1.ok
            // CODE -> <JmpTrue>: <Addr8: 60, Reg8: 4>  # Address: 000000b2
            if (r1.ok) {
                // CODE -> <TryGetById>: <Reg8: 5, Reg8: 3, UInt8: 8, string_id: 14>  # String: 'Error' (Identifier)
                // USED -> r5 = this.Error
                // CODE -> <Mov>: <Reg8: 4, Reg8: 2>
                // USED -> r4 = r2
                // CODE -> <GetById>: <Reg8: 6, Reg8: 4, UInt8: 9, string_id: 9563>  # String: 'statusText' (Identifier)
                // USED -> r6 = r2.statusText
                // CODE -> <TryGetById>: <Reg8: 3, Reg8: 3, UInt8: 4, string_id: 15>  # String: 'HermesInternal' (Identifier)
                // USED -> r3 = this.HermesInternal
                // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 5, string_id: 120>  # String: 'concat' (Identifier)
                // USED -> r4 = this.HermesInternal.concat
                // CODE -> <LoadConstString>: <Reg8: 3, string_id: 556>  # String: 'Failed to fetch movie details: ' (String)
                // USED -> r3 = "Failed to fetch movie details: "
                // CODE -> <Call2>: <Reg8: 17, Reg8: 4, Reg8: 3, Reg8: 6>
                r17 = `Failed to fetch movie details: ${r2.statusText}`
                // CODE -> <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 10, string_id: 216>  # String: 'prototype' (Identifier)
                // USED -> r4 = this.Error.prototype
                // CODE -> <CreateThis>: <Reg8: 4, Reg8: 4, Reg8: 5>
                r4 = createThis(prototype=this.Error.prototype, constructor=this.Error)
                // CODE -> <Mov>: <Reg8: 18, Reg8: 4>
                r18 = r4
                // CODE -> <Construct>: <Reg8: 3, Reg8: 5, UInt8: 2>
                r3 = new this.Error(arg0, arg1);
                // CODE -> <SelectObject>: <Reg8: 3, Reg8: 4, Reg8: 3>
                // USED -> r3 = r4[r3]
                // CODE -> <Throw>: <Reg8: 3>
                r3 = throw r4[r3]
            }
            // CODE -> <Mov>: <Reg8: 3, Reg8: 2>
            // label_178:
            // USED -> r3 = r2
            // CODE -> <GetById>: <Reg8: 2, Reg8: 3, UInt8: 11, string_id: 8033>  # String: 'json' (Identifier)
            // USED -> r2 = r2.json
            // CODE -> <Call1>: <Reg8: 2, Reg8: 2, Reg8: 3>
            // USED -> r2 = await r2.json()
            // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 000000c3
            // await yield; // check: JSConverter.Dispatcher // Resume at label_4
            // CODE -> <Ret>: <Reg8: 2>
            return await r2.json();
            // CODE -> <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            r2 = await yield; // Resume generator
            // CODE -> <JmpTrue>: <Addr8: 6, Reg8: 3>  # Address: 000000cc
            if (r2) {
                // CODE -> <CompleteGenerator>: <>
                // CODE -> <Ret>: <Reg8: 2>
                return r2;
            }
            // CODE -> <CompleteGenerator>: <>
            // label_204:
            // CODE -> <Ret>: <Reg8: 2>
            return r2;
        }
        // CODE -> <CompleteGenerator>: <>
        // label_207:
        // CODE -> <Ret>: <Reg8: 1>
        return r1;
        // CODE -> <Catch>: <Reg8: 1>
        // USED -> r1 = caughtException
        // CODE -> <GetGlobalObject>: <Reg8: 2>
        // USED -> r2 = this
        // CODE -> <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 12, string_id: 122>  # String: 'console' (Identifier)
        // USED -> r4 = this.console
        // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 13, string_id: 147>  # String: 'error' (Identifier)
        // USED -> r3 = this.console.error
        // CODE -> <LoadConstString>: <Reg8: 2, string_id: 2291>  # String: 'Error fetching movie details:' (String)
        // USED -> r2 = "Error fetching movie details:"
        // CODE -> <Call3>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2, Reg8: 1>
        r2 = this.console.error("Error fetching movie details:", caughtException)
        // CODE -> <Throw>: <Reg8: 1>
        r1 = throw caughtException
    }
    // CODE -> <CompleteGenerator>: <>
    // label_237:
    // CODE -> <Ret>: <Reg8: 0>
    return r0;
}