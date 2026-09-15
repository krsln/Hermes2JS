# CFG – Control Flow Graph

## IR – Intermediate Representation

https://github.com/P1sec/hermes-dec   
https://p1sec.github.io/hermes-dec/opcodes_table.html   
https://github.com/facebook/hermes/tree/main/include/hermes/BCGen

```shell
tree -I '__pycache__|__init__.py' hermes_decompiler

# diff 
git diff main...feature/from-26-09-15 > ~/Downloads/hermes2js.diff
```

## Testy

```shell
# 98
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/focused -o ./apps/demo/fixtures/98/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/focused -o ./apps/demo/fixtures/98/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/98/sections -o ./apps/demo/fixtures/98/results
# WARNING 4
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
## 96
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --log-level WARNING
# WARNING 1071
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 999 

## 98
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections/ -o ./apps/testy/98/output/results/
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections/ -o ./apps/testy/98/output/results/ --log-level WARNING
# WARNING 1032
python scripts/decompile_sections.py -i ./apps/testy/98/output/sections/ -o ./apps/testy/98/output/results/ --start 1 --end 999 
```
