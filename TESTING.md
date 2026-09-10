# CFG – Control Flow Graph

## IR – Intermediate Representation

https://github.com/P1sec/hermes-dec   
https://p1sec.github.io/hermes-dec/opcodes_table.html   
https://github.com/facebook/hermes/tree/main/include/hermes/BCGen

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
