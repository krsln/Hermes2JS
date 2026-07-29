# Usage

## Step—1 Disassemble

```shell
chmod +x scripts/bootstrap.sh
chmod +x scripts/disassemble.sh

./scripts/bootstrap.sh
```

```shell
./scripts/disassemble.sh <app_name>

file apps/coachy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
./scripts/disassemble.sh coachy

file apps/testy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 98
./scripts/disassemble.sh testy

```

### Notes: Hermes JavaScript bytecode, version 98

if index.android.bundle: Hermes JavaScript bytecode, version 98 causes error ->

```python
# ../vendor/hermes-dec/src/hermes_dec/hbc/hbc98.py de 
from typing import List

_builtin_function_names: List[str] = [
    # ...
    # missing items | date: 2026-07-29
    "makeAsyncIterator",
    "awaitAsyncGenerator",
]
```
or
```python
# vendor/hermes-dec/src/hermes_dec/parsers/hbc_bytecode_parser.py
# search builtin_functions[builtin_number] then change it


# if builtin_number < len(builtin_functions):
#     builtin = builtin_functions[builtin_number]
# else:
#     builtin = f"<Builtin {builtin_number}>"
# 
# comment += '  # Built-in function: [#%d %s]' % (
#     builtin_number,
#     builtin,
# )
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

Converts each discovered `section_<n>.hbc` into a corresponding
`section_<n>.js`.

```shell
python scripts/decompiler.py -i <sections_dir> -o <results_dir> [options]
```

**control data /fixtures**

```shell
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --no-verbose
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --strict
```

**Examples**

```shell
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --no-verbose

python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --strict
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --start 100 --end 200
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level DEBUG
python scripts/decompiler.py -i ./apps/testy/output/sections -o ./apps/testy/output/results --log-level WARNING --no-verbose

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
