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

# if index.android.bundle: Hermes JavaScript bytecode, version 96 causes error ->
# vendor/hermes-dec/src/hermes_dec/parsers/hbc_bytecode_parser.py
# if builtin_number < len(builtin_functions):
#    builtin = builtin_functions[builtin_number]
# else:
#    builtin = f"<Builtin {builtin_number}>"
```

### hermesc
```shell
find ../../ -name "hermesc" -type f
../../HermesTestApp/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    index.android.bundle

../../HermesTestApp/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    -pretty \
    index.android.bundle
```

## Test app

- Coach-ify AI: Workout Planner
- unzip https://www.decompiler.com/
- some.testy.apk / resources / assets / index.android.bundle
- download the file :p

```shell
% file index.android.bundle
index.android.bundle: Hermes JavaScript bytecode, version 96
```

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