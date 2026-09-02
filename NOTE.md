# Hermes Disassembler

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf   
https://github.com/P1sec/hermes-dec   
https://p1sec.github.io/hermes-dec/opcodes_table.html  
https://github.com/facebook/hermes/tree/main/include/hermes/BCGen

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
python vendor/hermes-dec/src/hermes_dec/disassembly/hbc_disassembler.py apps/testy/index.android.bundle apps/testy/output/output.hasm

```

### hermesc

```shell
find . -name "hermesc" -type f
./projects/hermes-test-sdk-55/node_modules/hermes-compiler/hermesc/osx-bin/hermesc hermesc -version
./projects/hermes-test-sdk-55/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    "apps/testy/96/index.android.bundle" > "apps/testy/96/output/hermesc-output.hbc"

./projects/hermes-test-sdk-55/node_modules/hermes-compiler/hermesc/osx-bin/hermesc \
    -b \
    -dump-bytecode \
    -pretty \
    "apps/testy/96/index.android.bundle" > "apps/testy/96/output/hermesc-output.hbc"
```
