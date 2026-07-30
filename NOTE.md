# Hermes Disassembler

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf   
https://github.com/P1sec/hermes-dec   
https://p1sec.github.io/hermes-dec/opcodes_table.html

## usage hermes-dec

```shell
# basic
echo "🔍 Disassembling..."
python3 "hermes-dec/src/hermes_dec/disassembly/hbc_disassembler.py" "assets/index.android.bundle" > "output.hbc"

echo "🧩 Decompiling..."
python3 "hermes-dec/src/hermes_dec/decompilation/hbc_decompiler.py" "assets/index.android.bundle" > "output.js"

echo "📦 Parsing structure..."
python3 "hermes-dec/src/hermes_dec/parsers/hbc_file_parser.py" "assets/index.android.bundle" > "outputParser.js"
```

**Examples**

```shell
python "vendor/hermes-dec/src/hermes_dec/disassembly/hbc_disassembler.py" "apps/testy/index.android.bundle" > "apps/testy/output/output.hbc"
```

### hermesc

```shell
find . -name "hermesc" -type f
./HermesTestApp/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    "apps/testy/index.android.bundle" > "apps/testy/output/hermesc-output.hbc"

./HermesTestApp/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    -pretty \
    "apps/testy/index.android.bundle" > "apps/testy/output/hermesc-output.hbc"
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
