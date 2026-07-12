# Hermes2JS

#### Step—1 Disassemble

goto Disassembler

#### Step—2 -> Conversion

Splitter

```shell
python conversion/splitter/hermes_splitter.py --input apps/Coachify/output/output.hbc --output apps/Coachify/output/sections
python conversion/splitter/hermes_splitter.py --input apps/Testy/output/output.hbc --output apps/Testy/output/sections

# goto conversion/splitter.py
```

Decompile

```shell
# goto conversion/converter.py
```

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf


https://p1sec.github.io/hermes-dec/opcodes_table.html
--
business@Hell-MacBook-Pro hermes-dec-main % file index.android.bundle
index.android.bundle: Hermes JavaScript bytecode, version 96

Hermes Assembly (HASM)
https://docs.rs/hermes_rs/latest/hermes_rs/all.html  
https://docs.rs/hermes_rs/latest/hermes_rs/hermes/v96/index.html  
https://docs.rs/hermes_rs/latest/src/hermes_rs/hermes/v96/mod.rs.html#3-210

https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeList.def

disassembled Hermes bytecode -> Reconstructing to JavaScript
Hermes HASM to JavaScript Converter

| Step                        | Done by            | Purpose                             |
|-----------------------------|--------------------|-------------------------------------|
| TypeScript/JSX → JavaScript | tsc / Babel        | Make code Hermes-compatible         |
| JavaScript → Bytecode       | Hermes (`hermesc`) | Speed up startup & execution        |
| Runtime Execution           | Hermes engine      | Run the compiled bytecode on device |

## Learn in hermes

- if / else
- ternary operator
- throw
- async / await
