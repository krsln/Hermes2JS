# CFG – Control Flow Graph

https://raw.githubusercontent.com/facebook/hermes/hermes-v260318099.0.1/include/hermes/BCGen/HBC/BytecodeList.def

# IR – Intermediate Representation

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
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/sections -o ./apps/demo/fixtures/98/results --no-verbose

# 96
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/focused -o ./apps/demo/fixtures/96/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/focused -o ./apps/demo/fixtures/96/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --log-level DEBUG
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --log-level WARNING

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --no-verbose

# ControlFlow
################ 
# whileTest 15047
# forTest 15051
# forEachTest 15053, 15054
# Switch 15056
# nestedLoopTest 15058
# complexTest 15060
# IfTests 15062, 15063
# Labeled Tests 15065, 15066, 15067, 15068
# ternaryTest 15070, 15071, 15072, 15073

# Exceptions
# Exception Tests 15075-15090

# Iterators
# IteratorTests 15092, 15093

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/  --log-level WARNING
# WARNING 725 
```

## whole sections

```shell

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --log-level WARNING

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 999 --end 1999 

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 4999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 5000 --end 9999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 10000 --end 14999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 15000 --end 19999
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 20000 --end 24999 
```