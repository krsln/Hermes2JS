# CFG – Control Flow Graph

## IR – Intermediate Representation

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf   
https://github.com/P1sec/hermes-dec   
https://github.com/facebook/hermes/tree/main/include/hermes/BCGen

https://raw.githubusercontent.com/facebook/hermes/hermes-v260318099.0.1/include/hermes/BCGen/HBC/BytecodeList.def  
https://p1sec.github.io/hermes-dec/opcodes_table.html

```shell
tree -I '__pycache__|__init__.py' hermes_decompiler

# diff 
git diff main...feature/from-2025-09-01 > hermes2js.diff
```

## Testy

```shell
# 98
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/focused -o ./apps/demo/fixtures/98/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/focused -o ./apps/demo/fixtures/98/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/sections -o ./apps/demo/fixtures/98/results
# WARNING 53
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/sections -o ./apps/demo/fixtures/98/results --no-verbose

# 96
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/focused -o ./apps/demo/fixtures/96/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/focused -o ./apps/demo/fixtures/96/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --log-level DEBUG
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --log-level WARNING

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --no-verbose
```

## whole sections

```shell

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --log-level WARNING
# WARNING 1071

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 999 --end 1999 

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 4999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 5000 --end 9999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 10000 --end 14999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 15000 --end 19999
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 20000 --end 24999 
```

## usage hermes-dec

```shell
python vendor/hermes-dec/src/hermes_dec/disassembly/hbc_disassembler.py apps/testy/98/index.android.bundle apps/testy/98/output/output.hasm

```

open cases
==> 00000009: <GetBuiltinClosure>: <Reg8: 3, UInt8: 57>  # Built-in function: [#57 spawnAsync]
==> 00000009: <GetBuiltinClosure>: <Reg8: 3, UInt8: 57>

==> 00000024: <NewObjectWithBuffer>: <Reg8: 3, UInt16: 2, UInt16: 2, UInt16: 12808, UInt16: 23461>  # Object: {'id': 1, 'name': 'Ada'}
==> 00000024: <NewObjectWithBuffer>: <Reg8: 3, UInt16: 2, UInt16: 2, UInt16: 12808, UInt16: 23461>

==> 00000018: <NewArrayWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 5, UInt16: 17493>  # Array: [5, 3, 8, 1, 9]
==> 00000018: <NewArrayWithBuffer>: <Reg8: 4, UInt16: 5, UInt16: 5, UInt16: 17493>
