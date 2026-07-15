# Hermes2JS

> Hermes Assembly (HASM)

https://docs.rs/hermes_rs/latest/hermes_rs/all.html  
https://docs.rs/hermes_rs/latest/hermes_rs/hermes/v96/index.html  
https://docs.rs/hermes_rs/latest/src/hermes_rs/hermes/v96/mod.rs.html#3-210

https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeList.def

Disassembled Hermes bytecode -> Reconstructing to JavaScript
Hermes HASM to JavaScript Converter

| Step                        | Done by            | Purpose                             |
|-----------------------------|--------------------|-------------------------------------|
| TypeScript/JSX → JavaScript | tsc / Babel        | Make code Hermes-compatible         |
| JavaScript → Bytecode       | Hermes (`hermesc`) | Speed up startup & execution        |
| Runtime Execution           | Hermes engine      | Run the compiled bytecode on device |

#### Step—1 Disassemble

```shell
chmod +x scripts/bootstrap.sh
chmod +x scripts/disassemble.sh

./scripts/bootstrap.sh
./scripts/disassemble.sh testy
```

#### Step—2 Split

```shell
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o apps/testy/output/sections

# Manifest & dry-run
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o sections --manifest sections/manifest.json -v
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o sections --dry-run -v
```

#### Step—3 Decompile

```shell
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ 
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
