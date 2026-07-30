# Hermes2JS

**Hermes Assembly (HASM) → JavaScript**

Takes an already-built Hermes bytecode bundle from a React Native app (`index.android.bundle`), disassembles it, splits
it into one file per function, and reconstructs each function as readable JavaScript.

```text
┌────────────────────────┐      scripts/run-hermes-dec.sh        ┌────────────┐
│  index.android.bundle  │ ────────────────────────────────────► │ output.hbc │
│                        │    (vendor/hermes-dec, Python)        └─────┬──────┘
│ (Prebuilt Hermes BC)   │                                             │
└────────────────────────┘                                             │
                                                                       ▼
┌────────────────────────┐      scripts/decompile_sections.py   scripts/split_output_file.py
│     results/*.js       │ ◄───────────────────────────────        sections/*.hbc
│                        │       (one file per function)     
│ (Decompiled JS source) │
└────────────────────────┘
```

> **Important**
>
> Hermes2JS is a decompiler, **not** a compiler. It accepts existing Hermes
> bytecode as input and reconstructs an equivalent JavaScript representation.
>
> Because Hermes bytecode does not preserve all source-level information,
> the generated output is a best-effort approximation and should not be
> expected to match the original source code exactly.

## Sources

- [hermes_rs docs](https://docs.rs/hermes_rs/latest/hermes_rs/all.html)
- [hermes_rs v96 bytecode module](https://docs.rs/hermes_rs/latest/hermes_rs/hermes/v96/index.html)
- [hermes_rs v96 source](https://docs.rs/hermes_rs/latest/src/hermes_rs/hermes/v96/mod.rs.html#3-210)
- [Hermes `BytecodeList.def`](https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeList.def)
- [P1sec/hermes-dec](https://github.com/P1sec/hermes-dec) — vendored disassembly/decompilation toolkit used by
  `run-hermes-dec.sh`

| Step                        | Done by            | Purpose                             |
|-----------------------------|--------------------|-------------------------------------|
| TypeScript/JSX → JavaScript | tsc / Babel        | Make code Hermes-compatible         |
| JavaScript → Bytecode       | Hermes (`hermesc`) | Speed up startup & execution        |
| Runtime Execution           | Hermes engine      | Run the compiled bytecode on device |

## Workflow

```text
Bytecode
    │
    ▼
Parsing
    │
    ▼
Dispatch
    │
    ▼
Opcode Handlers
    │
    ▼
Analysis
    ├── CFG
    ├── Dominance
    ├── Loops
    └── Regions
    │
    ▼
Transforms
    │
    ▼
IR
    │
    ▼
Emit
    │
    ▼
JavaScript
```