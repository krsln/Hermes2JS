# IR (Intermediate Representation)

**control data /fixtures**

```shell
tree -I '__pycache__|__init__.py' hermes_decompiler/regions_new
tree -I '__pycache__|__init__.py|two'  

```

```shell

python scripts/decompiler.py -i ./apps/demo/fixtures/one -o ./apps/demo/fixtures/results
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results

python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --no-verbose
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --strict
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --strict --no-verbose
```

**Examples**

```shell
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ 
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --no-verbose

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 999 

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 5999 
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 5000 --end 9999 

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 10000 --end 14999 
python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 15000 --end 19999

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 20000 --end 24999 

python scripts/decompiler.py -i ./apps/testy/output/sections/ -o ./apps/testy/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```
