async function* anon_11946(param0, param1) {
    // CODE -> <StartGenerator>: <>
    // StartGenerator: prepare generator context and jump to next instruction
    // CODE -> <ResumeGenerator>: <Reg8: 0, Reg8: 1>
    r0 = await yield; // Resume generator
    // CODE -> <JmpTrueLong>: <Addr32: 244, Reg8: 1>  # Address: 000000f8
    label_4:
    if (r1) {
        // CODE -> <LoadParam>: <Reg8: 1, UInt8: 1>
        // USED -> r1 = param1
        // CODE -> <GetById>: <Reg8: 6, Reg8: 1, UInt8: 1, string_id: 7574>  # String: 'query' (Identifier)
        // USED -> r6 = param1.query
        // CODE -> <GetEnvironment>: <Reg8: 1, UInt8: 2>
        r1 = getEnvironment(2);
        // CODE -> <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 1>
        r2 = r1[1]
        // CODE -> <GetById>: <Reg8: 8, Reg8: 2, UInt8: 2, string_id: 6728>  # String: 'BASE_URL' (Identifier)
        // USED -> r8 = r2.BASE_URL
        // CODE -> <GetGlobalObject>: <Reg8: 2>
        // USED -> r2 = this
        // CODE -> <JmpTrue>: <Addr8: 30, Reg8: 6>  # Address: 00000040
        if (param1.query) {
            // CODE -> <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 15>  # String: 'HermesInternal' (Identifier)
            // USED -> r3 = this.HermesInternal
            // CODE -> <GetByIdShort>: <Reg8: 5, Reg8: 3, UInt8: 4, string_id: 120>  # String: 'concat' (Identifier)
            // USED -> r5 = this.HermesInternal.concat
            // CODE -> <LoadConstString>: <Reg8: 4, string_id: 6377>  # String: '' (Identifier)
            // USED -> r4 = ""
            // CODE -> <LoadConstString>: <Reg8: 3, string_id: 995>  # String: '/discover/movie?sort_by=popularity.desc' (String)
            // USED -> r3 = "/discover/movie?sort_by=popularity.desc"
            // CODE -> <Call3>: <Reg8: 5, Reg8: 5, Reg8: 4, Reg8: 8, Reg8: 3>
            r5 = `${r2.BASE_URL}/discover/movie?sort_by=popularity.desc`
            // CODE -> <Jmp>: <Addr8: 41>  # Address: 00000067
            goto label_103;
        }
        // CODE -> <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 9415>  # String: 'encodeURIComponent' (Identifier)
        label_64:
        // USED -> r4 = this.encodeURIComponent
        // CODE -> <LoadConstUndefined>: <Reg8: 3>
        // USED -> r3 = undefined
        // CODE -> <Call2>: <Reg8: 7, Reg8: 4, Reg8: 3, Reg8: 6>
        r7 = this.encodeURIComponent.call(this, undefined, param1.query)
        // CODE -> <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 3, string_id: 15>  # String: 'HermesInternal' (Identifier)
        // USED -> r3 = this.HermesInternal
        // CODE -> <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 4, string_id: 120>  # String: 'concat' (Identifier)
        // USED -> r6 = this.HermesInternal.concat
        // CODE -> <LoadConstString>: <Reg8: 4, string_id: 6377>  # String: '' (Identifier)
        // USED -> r4 = ""
        // CODE -> <LoadConstString>: <Reg8: 3, string_id: 2228>  # String: '/search/movie?query=' (String)
        // USED -> r3 = "/search/movie?query="
        // CODE -> <Call4>: <Reg8: 5, Reg8: 6, Reg8: 4, Reg8: 8, Reg8: 3, Reg8: 7>
        r5 = `${r2.BASE_URL}/search/movie?query=${r7}`
        // CODE -> <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 6, string_id: 7603>  # String: 'fetch' (Identifier)
        label_103:
        // USED -> r4 = this.fetch
        // CODE -> <NewObject>: <Reg8: 3>
        // USED -> r3 = {}
        // CODE -> <LoadConstString>: <Reg8: 6, string_id: 7782>  # String: 'GET' (Identifier)
        // USED -> r6 = "GET"
        // CODE -> <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 6, string_id: 158>  # String: 'method' (Identifier)
        // USED -> r3 = { "method": "GET" }
        // CODE -> <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 1>
        r1 = r1[1]
        // CODE -> <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 7, string_id: 169>  # String: 'headers' (Identifier)
        // USED -> r1 = r1.headers
        // CODE -> <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 1, string_id: 169>  # String: 'headers' (Identifier)
        // USED -> r3 = { "method": GET, "headers": r1.headers }
        // CODE -> <LoadConstUndefined>: <Reg8: 1>
        // USED -> r1 = undefined
        // CODE -> <Call3>: <Reg8: 1, Reg8: 4, Reg8: 1, Reg8: 5, Reg8: 3>
        r1 = this.fetch.call(this, undefined, r5, { "method": GET, "headers": r1.headers })
        // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 00000090
        await yield; // Resume at label_4
        // CODE -> <Ret>: <Reg8: 1>
        return r1;
        // CODE -> <ResumeGenerator>: <Reg8: 1, Reg8: 3>
        // USED -> r1 = await yield; // Resume generator
        // CODE -> <JmpTrue>: <Addr8: 98, Reg8: 3>  # Address: 000000f5
        if ({ "method": GET, "headers": r1.headers }) {
            // CODE -> <GetById>: <Reg8: 3, Reg8: 1, UInt8: 8, string_id: 7823>  # String: 'ok' (Identifier)
            // USED -> r3 = r1.ok
            // CODE -> <JmpTrue>: <Addr8: 57, Reg8: 3>  # Address: 000000d5
            if (r1.ok) {
                // CODE -> <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 9, string_id: 14>  # String: 'Error' (Identifier)
                // USED -> r4 = this.Error
                // CODE -> <GetById>: <Reg8: 5, Reg8: 1, UInt8: 10, string_id: 9563>  # String: 'statusText' (Identifier)
                // USED -> r5 = r1.statusText
                // CODE -> <TryGetById>: <Reg8: 2, Reg8: 2, UInt8: 3, string_id: 15>  # String: 'HermesInternal' (Identifier)
                // USED -> r2 = this.HermesInternal
                // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 120>  # String: 'concat' (Identifier)
                // USED -> r3 = this.HermesInternal.concat
                // CODE -> <LoadConstString>: <Reg8: 2, string_id: 1468>  # String: 'Failed to fetch movies: ' (String)
                // USED -> r2 = "Failed to fetch movies: "
                // CODE -> <Call2>: <Reg8: 11, Reg8: 3, Reg8: 2, Reg8: 5>
                r11 = `Failed to fetch movies: ${r1.statusText}`
                // CODE -> <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 11, string_id: 216>  # String: 'prototype' (Identifier)
                r3 = this.Error.prototype
                // CODE -> <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 4>
                // USED -> r3 = createThis(r3, r4);
                // CODE -> <Mov>: <Reg8: 12, Reg8: 3>
                r12 = r3;
                // CODE -> <Construct>: <Reg8: 2, Reg8: 4, UInt8: 2>
                r2 = new r4(arg0, arg1);
                // CODE -> <SelectObject>: <Reg8: 2, Reg8: 3, Reg8: 2>
                // USED -> r2 = r3[r2]
                // CODE -> <Throw>: <Reg8: 2>
                r2 = throw r3[r2]
            }
            // CODE -> <GetById>: <Reg8: 2, Reg8: 1, UInt8: 12, string_id: 8033>  # String: 'json' (Identifier)
            label_213:
            // USED -> r2 = r1.json
            // CODE -> <Call1>: <Reg8: 2, Reg8: 2, Reg8: 1>
            r2 = r1.json.call(this, await yield)
            // CODE -> <SaveGenerator>: <Addr8: 4>  # Address: 000000e3
            await yield; // Resume at label_4
            // CODE -> <Ret>: <Reg8: 2>
            return r2;
            // CODE -> <ResumeGenerator>: <Reg8: 2, Reg8: 3>
            r2 = await yield; // Resume generator
            // CODE -> <JmpTrue>: <Addr8: 12, Reg8: 3>  # Address: 000000f2
            if (createThis(r3, r4) {
                // CODE -> <GetById>: <Reg8: 3, Reg8: 2, UInt8: 13, string_id: 9125>  # String: 'results' (Identifier)
                // USED -> r3 = r2.results
                // CODE -> <CompleteGenerator>: <>
                // CODE -> <Ret>: <Reg8: 3>
                return r2.results;
            }
            // CODE -> <CompleteGenerator>: <>
            label_242:
            // CODE -> <Ret>: <Reg8: 2>
            return r2;
        }
        // CODE -> <CompleteGenerator>: <>
        label_245:
        // CODE -> <Ret>: <Reg8: 1>
        return r1;
    }
    // CODE -> <CompleteGenerator>: <>
    label_248:
    // CODE -> <Ret>: <Reg8: 0>
    return r0;
}