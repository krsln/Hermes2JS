# Usage

## Prep

### get index.android.bundle

- get apk
- decompile → use https://www.decompiler.com/
- get bundle file → / resources / assets / index.android.bundle
- download the file :p

### clone vendor/hermes-dec

```shell
chmod +x scripts/fetch-hermes-dec.sh
chmod +x scripts/run-hermes-dec.sh

# clones https://github.com/P1sec/hermes-dec to vendor/hermes-dec
./scripts/fetch-hermes-dec.sh
```

## Step—1 Disassemble

```bash
#./scripts/run-hermes-dec.sh <bundle_path>

file apps/coachy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
./scripts/run-hermes-dec.sh coachy

# Test Projects' bundles
file apps/testy/96/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
file apps/testy/98/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 98

./scripts/run-hermes-dec.sh apps/testy/96/index.android.bundle
./scripts/run-hermes-dec.sh apps/testy/98/index.android.bundle

```

**Output**

```
apps/<app_name>/output/
├── output.hbc
├── output.js
└── outputParser.js
```

## Step—2 Split

Splits `output.hbc` into one file per function, using the
`===============` separator lines the disassembler emits between functions.

```shell
python scripts/split_output_file.py -i <input.hbc> -o <output_dir> [options]

# Basic split
python scripts/split_output_file.py -i apps/testy/96/output/output.hbc -o apps/testy/96/output/sections
python scripts/split_output_file.py -i apps/testy/98/output/output.hbc -o apps/testy/98/output/sections

# With manifest + INFO logging
python scripts/split_output_file.py -i apps/testy/output/output.hbc -o sections --manifest sections/manifest.json -v

# Dry run first, to check section count/naming before writing anything
python scripts/split_output_file.py -i apps/testy/output/output.hbc -o sections --dry-run -v

#--------------------------
## copy files to fixtures
 
# section_15042-15216
cp apps/testy/96/output/sections/section_{15042..15216}.hbc  apps/demo/fixtures/96/sections/

# section_9446-9542
cp apps/testy/98/output/sections/section_{9446..9542}.hbc apps/demo/fixtures/sections/

```

## Step—3 Decompile

Converts each discovered `section_<n>.hbc` into a corresponding `section_<n>.js`.

```shell
python scripts/decompile_sections.py -i <sections_dir> -o <results_dir> [options]
python scripts/decompile_sections.py -i <sections_dir> -o <results_dir> [options]


python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results
python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --no-verbose

python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --strict
python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --start 100 --end 1000
python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level DEBUG
python scripts/decompile_sections.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level WARNING --no-verbose

python scripts/decompile_sections.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
