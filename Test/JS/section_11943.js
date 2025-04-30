function function_11943(param0, param1, param2, param3, param4, param5, param6, param7) {
    // CODE -> <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED -> r6 = param2
    // CODE -> <LoadParam>: <Reg8: 2, UInt8: 6>
    // USED -> r2 = param6
    // CODE -> <LoadParam>: <Reg8: 7, UInt8: 7>
    r7 = param7
    // CODE -> <LoadConstUndefined>: <Reg8: 0>
    // USED -> r0 = undefined
    // CODE -> <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 3>
    r4 = param2.call(this, undefined, r3)
    // CODE -> <GetGlobalObject>: <Reg8: 5>
    // USED -> r5 = this
    // CODE -> <TryGetById>: <Reg8: 10, Reg8: 5, UInt8: 1, string_id: 29>  # String: 'Object' (Identifier)
    // USED -> r10 = this.Object
    // CODE -> <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 2, string_id: 132>  # String: 'defineProperty' (Identifier)
    // USED -> r9 = this.Object.defineProperty
    // CODE -> <NewObject>: <Reg8: 8>
    // USED -> r8 = {}
    // CODE -> <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 3, string_id: 252>  # String: 'value' (Identifier)
    // USED -> r8 = { "value": undefined }
    // CODE -> <LoadConstString>: <Reg8: 3, string_id: 54>  # String: '__esModule' (Identifier)
    // USED -> r3 = "__esModule"
    // CODE -> <Call4>: <Reg8: 3, Reg8: 9, Reg8: 10, Reg8: 2, Reg8: 3, Reg8: 8>
    r3 = this.Object.defineProperty(param6, "__esModule", { "value": undefined })
    // CODE -> <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 3>
    r3 = param2.call(this, undefined, r3)
    // CODE -> <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r4.call(this, undefined, r3)
    // CODE -> <NewObjectWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 2, UInt16: 4412, UInt16: 6447>  # Object: {'BASE_URL': 'https://api.themoviedb.org/3', 'API_KEY': 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjMzNDRiMTkzMDI3NTY4MTkzMDQyYmI1MjRhYTg0MiIsIm5iZiI6MTczOTM0NzM3MC4wNDYwMDAyLCJzdWIiOiI2N2FjNTVhYTIxZDBhOTJkNGI5Yjk2M2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yS6WPYjGcaxHkfsYrqmijak7A_NVuEawsL_mYKFdjEc'}
    // USED -> r3 = { BASE_URL: "https://api.themoviedb.org/3", API_KEY: "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjMzNDRiMTkzMDI3NTY4MTkzMDQyYmI1MjRhYTg0MiIsIm5iZiI6MTczOTM0NzM3MC4wNDYwMDAyLCJzdWIiOiI2N2FjNTVhYTIxZDBhOTJkNGI5Yjk2M2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yS6WPYjGcaxHkfsYrqmijak7A_NVuEawsL_mYKFdjEc" }
    // CODE -> <LoadConstString>: <Reg8: 7, string_id: 4525>  # String: 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjMzNDRiMTkzMDI3NTY4MTkzMDQyYmI1MjRhYTg0MiIsIm5iZiI6MTczOTM0NzM3MC4wNDYwMDAyLCJzdWIiOiI2N2FjNTVhYTIxZDBhOTJkNGI5Yjk2M2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yS6WPYjGcaxHkfsYrqmijak7A_NVuEawsL_mYKFdjEc' (String)
    // USED -> r7 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjMzNDRiMTkzMDI3NTY4MTkzMDQyYmI1MjRhYTg0MiIsIm5iZiI6MTczOTM0NzM3MC4wNDYwMDAyLCJzdWIiOiI2N2FjNTVhYTIxZDBhOTJkNGI5Yjk2M2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yS6WPYjGcaxHkfsYrqmijak7A_NVuEawsL_mYKFdjEc"
    // CODE -> <NewObject>: <Reg8: 4>
    // USED -> r4 = {}
    // CODE -> <LoadConstString>: <Reg8: 6, string_id: 4098>  # String: 'application/json' (String)
    r6 = "application/json"
    // CODE -> <TryGetById>: <Reg8: 5, Reg8: 5, UInt8: 3, string_id: 15>  # String: 'HermesInternal' (Identifier)
    // USED -> r5 = this.HermesInternal
    // CODE -> <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 4, string_id: 120>  # String: 'concat' (Identifier)
    // USED -> r6 = this.HermesInternal.concat
    // CODE -> <LoadConstString>: <Reg8: 5, string_id: 1336>  # String: 'Bearer ' (String)
    // USED -> r5 = "Bearer "
    // CODE -> <Call2>: <Reg8: 5, Reg8: 6, Reg8: 5, Reg8: 7>
    r5 = this.HermesInternal.concat.call(this, "Bearer ", "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjMzNDRiMTkzMDI3NTY4MTkzMDQyYmI1MjRhYTg0MiIsIm5iZiI6MTczOTM0NzM3MC4wNDYwMDAyLCJzdWIiOiI2N2FjNTVhYTIxZDBhOTJkNGI5Yjk2M2EiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.yS6WPYjGcaxHkfsYrqmijak7A_NVuEawsL_mYKFdjEc")
    // CODE -> <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 11944>  # Function: [#11944  of 37 bytes]: 1 params @ offset 0x0021917e
    // USED -> r3 = // Closure function_11944 with env r1
    // CODE -> <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = // Closure function_11944 with env r1(undefined)
    // CODE -> <CreateClosure>: <Reg8: 1, Reg8: 1, function_id: 11948>  # Function: [#11948  of 37 bytes]: 1 params @ offset 0x002192a7
    // USED -> r1 = // Closure function_11948 with env r1
    // CODE -> <Call1>: <Reg8: 1, Reg8: 1, Reg8: 0>
    r1 = // Closure function_11948 with env r1(undefined)
    // CODE -> <Ret>: <Reg8: 0>
    return undefined;
}