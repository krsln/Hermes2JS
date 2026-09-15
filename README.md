# Hermes2JS

**Hermes Assembly (HASM) → JavaScript**

Hermes2JS takes an already-built Hermes bytecode bundle from a React Native app (for example, `index.android.bundle`),
disassembles it, splits it into one file per function, and reconstructs each function as readable JavaScript.

```text
┌────────────────────────┐              
│       assets/          │      scripts/run-hermes-disassembler.py     ┌──────────────────────────┐
│  index.android.bundle  │ ────────────────────or────────────────────► │ disassembler-output.hasm │
│ (Prebuilt Hermes BC)   │          vendor/run-hermes-dec.sh           └───────────┬──────────────┘
│                        │          (external hermes-dec tool)                     │
└────────────────────────┘                                                         │
                                                                                   ▼
┌────────────────────────┐       scripts/decompile_sections.py          scripts/split_output_file.py
│     results/*.js       │ ◄─────────────────────────────────────────        function_<id>_*.hasm
│                        │           (one file per function)
│ (Decompiled JS source) │
└────────────────────────┘
```

> **Important**
>
> Hermes2JS is a decompiler, **not a compiler**. It accepts existing Hermes
> bytecode as input and reconstructs an equivalent JavaScript representation.
>
> Because Hermes bytecode does not preserve all source-level information,
> the generated output is a best-effort approximation and should not be
> expected to match the original source code exactly.

## Sources

* [hermes-dec](https://github.com/P1sec/hermes-dec) — external Hermes bytecode disassembly tool
* https://p1sec.github.io/hermes-dec/opcodes_table.html
* https://github.com/facebook/hermes/tree/main/include/hermes/BCGen

## Hermes Bytecode Pipeline

| Step                        | Done by            | Purpose                               |
|-----------------------------|--------------------|---------------------------------------|
| TypeScript/JSX → JavaScript | `tsc` / Babel      | Make code Hermes-compatible           |
| JavaScript → Bytecode       | Hermes (`hermesc`) | Compile JavaScript to Hermes bytecode |
| Runtime Execution           | Hermes engine      | Run the compiled bytecode on device   |
| Bytecode → Assembly         | `hermes-dec`       | Disassemble existing Hermes bytecode  |
| Assembly → JavaScript       | Hermes2JS          | Reconstruct readable JavaScript       |

## Workflow

```text 
Bytecode → Parsing → Dispatch → Opcode Handlers → Analysis → Transforms → IR → Emit → JavaScript
                                                      │
                                                      └── CFG, Dominance, Loops, Regions
```

## Third-Party Tools

Hermes2JS uses [hermes-dec](https://github.com/P1sec/hermes-dec) as an **external tool** for disassembling Hermes
`.bundle` files.

`hermes-dec` is licensed separately under **AGPL-3.0**. It is **not included in this repository** and is fetched
separately by:

```bash
./vendor/fetch-hermes-dec.sh
```

The fetched `hermes-dec` source remains subject to its own license terms.

## License

Hermes2JS is licensed under the **MIT License**.

See [LICENSE](LICENSE) for the full license text.

The MIT License applies to the Hermes2JS source code itself. Third-party tools and dependencies remain subject to their
respective licenses.
