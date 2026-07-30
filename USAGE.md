# Usage

## Prep

### get index.android.bundle

- get apk
- decompile → use https://www.decompiler.com/
- get bundle file → / resources / assets / index.android.bundle
- download the file :p

### clone vendor/hermes-dec

```shell
chmod +x scripts/bootstrap.sh
chmod +x scripts/disassemble.sh

# clones https://github.com/P1sec/hermes-dec to vendor/hermes-dec
./scripts/bootstrap.sh
```

## Step—1 Disassemble

```shell
#./scripts/disassemble.sh <app_name>

file apps/coachy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
./scripts/disassemble.sh coachy

file apps/testy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 98
./scripts/disassemble.sh testy

```

**Arguments**

| Arg          | Required | Description                                   |
|--------------|----------|-----------------------------------------------|
| `<app_name>` | Yes      | Matches a directory under `apps/<app_name>/`. |

**Input** (you must provide this)

```
apps/<app_name>/index.android.bundle
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
python scripts/hermes_splitter.py -i <input.hbc> -o <output_dir> [options]


# Basic split
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o apps/testy/output/sections

# With manifest + INFO logging
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o sections --manifest sections/manifest.json -v

# Dry run first, to check section count/naming before writing anything
python scripts/hermes_splitter.py -i apps/testy/output/output.hbc -o sections --dry-run -v
```

## Step—3 Decompile

Converts each discovered `section_<n>.hbc` into a corresponding `section_<n>.js`.

```shell
python scripts/decompiler.py -i <sections_dir> -o <results_dir> [options]


python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --no-verbose

python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --strict
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --start 100 --end 1000
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level DEBUG
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level WARNING --no-verbose

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
