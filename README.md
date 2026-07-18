# Hermes2JS

**Hermes Assembly (HASM) → JavaScript**

Takes an already-built Hermes bytecode bundle from a React Native app
(`index.android.bundle`), disassembles it, splits it into one file per
function, and reconstructs each function as readable JavaScript.

```
index.android.bundle      scripts/disassemble.sh        scripts/hermes_splitter.py        scripts/decompiler.py
(prebuilt Hermes    ───────────────────────►   output.hbc     ───────────────────►   sections/*.hbc   ─────────►   results/*.js
 bytecode bundle,        (vendor/hermes-dec,        (+ output.js,                    (one file per
 built elsewhere)         Python toolkit)            outputParser.js)                  function)
```

> This repo does **not** compile JS/TS to Hermes bytecode — it starts from a
> bundle that was already built (e.g. by a React Native release build with
> Hermes enabled). See the table at the bottom for what happens upstream.
>
> Output is a best-effort reconstruction, not a byte-for-byte reversal of the
> original source. Variable names, comments, and original formatting are not
> recoverable).

## Sources

- [hermes_rs docs](https://docs.rs/hermes_rs/latest/hermes_rs/all.html)
- [hermes_rs v96 bytecode module](https://docs.rs/hermes_rs/latest/hermes_rs/hermes/v96/index.html)
- [hermes_rs v96 source](https://docs.rs/hermes_rs/latest/src/hermes_rs/hermes/v96/mod.rs.html#3-210)
- [Hermes `BytecodeList.def`](https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeList.def)
- [P1sec/hermes-dec](https://github.com/P1sec/hermes-dec) — vendored disassembly/decompilation toolkit used by
  `disassemble.sh`

| Step                        | Done by            | Purpose                             |
|-----------------------------|--------------------|-------------------------------------|
| TypeScript/JSX → JavaScript | tsc / Babel        | Make code Hermes-compatible         |
| JavaScript → Bytecode       | Hermes (`hermesc`) | Speed up startup & execution        |
| Runtime Execution           | Hermes engine      | Run the compiled bytecode on device |

