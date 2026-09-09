# Usage

## Prep

### get index.android.bundle

- get apk
- decompile → use https://www.decompiler.com/
- get bundle file → / resources / assets / index.android.bundle
- download the file :p

## Step—1 Disassemble

| hermes-dec

```bash
file apps/testy/96/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
./vendor/run-hermes-dec.sh apps/testy/96/index.android.bundle

file apps/testy/98/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 98
./vendor/run-hermes-dec.sh apps/testy/98/index.android.bundle

python scripts/run-hermes-disassembler.py apps/testy/96/index.android.bundle apps/testy/96/output/custom.hasm
python scripts/run-hermes-disassembler.py apps/testy/98/index.android.bundle apps/testy/98/output/custom.hasm
```

## Step—2 Split

Splits `output.hasm` into one file per function, using the
`===============` separator lines the disassembler emits between functions.

```shell
python scripts/split_output_file.py -i <input.hasm> -o <output_dir> [options]

# Basic split
python scripts/split_output_file.py -i apps/testy/96/output/output.hasm -o apps/testy/96/output/sections
# Total sections: 15248
python scripts/split_output_file.py -i apps/testy/98/output/output.hasm -o apps/testy/98/output/sections
# Total sections: 14268

# With manifest + INFO logging
python scripts/split_output_file.py -i apps/testy/output/output.hasm -o sections --manifest sections/manifest.json -v

# Dry run first, to check section count/naming before writing anything
python scripts/split_output_file.py -i apps/testy/output/output.hasm -o sections --dry-run -v

#--------------------------
## copy files to fixtures
 
# section_15042-15216
cp apps/testy/96/output/sections/section_{15042..15216}.hasm  apps/demo/fixtures/96/sections/
cp apps/testy/96/output/sections/function_{15042..15216}_*.hasm apps/demo/fixtures/96/sections/

# section_9446-9542
cp apps/testy/98/output/sections/section_{9446..9542}.hasm apps/demo/fixtures/98/sections/
cp apps/testy/98/output/sections/function_{9446..9542}_*.hasm apps/demo/fixtures/98/sections/
```

## Step—3 Decompile

Converts each discovered `section_<n>.hasm` into a corresponding `section_<n>.js`.

```shell
python scripts/decompile_sections.py -i <sections_dir> -o <results_dir> [options]


python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --log-level WARNING
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --no-verbose

python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --strict
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --start 100 --end 1000
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --log-level DEBUG
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections -o ./apps/testy/98/output/results --log-level WARNING --no-verbose

python scripts/decompile_sections.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
