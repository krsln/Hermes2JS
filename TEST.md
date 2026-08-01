# CFG - Control Flow Graph

https://raw.githubusercontent.com/facebook/hermes/hermes-v260318099.0.1/include/hermes/BCGen/HBC/BytecodeList.def

# IR - Intermediate Representation

https://p1sec.github.io/hermes-dec/opcodes_table.html

```shell
tree -I '__pycache__|__init__.py' hermes_decompiler
```

## Testy

```shell
python scripts/decompile_sections.py -i ./apps/demo/fixtures/one -o ./apps/demo/fixtures/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/one -o ./apps/demo/fixtures/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --no-verbose

# 96
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/one -o ./apps/demo/fixtures/96/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/one -o ./apps/demo/fixtures/96/results --log-level DEBUG

python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results
python scripts/decompile_sections.py -i ./apps/demo/fixtures/96/sections -o ./apps/demo/fixtures/96/results --no-verbose

# Exception Tests 15075-15090

```

## Coach

```shell
python scripts/decompile_sections.py -i ./apps/coachy/fixtures/one -o ./apps/coachy/fixtures/results

python scripts/decompile_sections.py -i ./apps/coachy/fixtures/sections -o ./apps/coachy/fixtures/results

python scripts/decompile_sections.py -i ./apps/coachy/fixtures/sections -o ./apps/coachy/fixtures/results --no-verbose
python scripts/decompile_sections.py -i ./apps/coachy/fixtures/sections -o ./apps/coachy/fixtures/results --strict
python scripts/decompile_sections.py -i ./apps/coachy/fixtures/sections -o ./apps/coachy/fixtures/results --strict --no-verbose

```

**Examples**

```shell
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --no-verbose

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 999 --end 1999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1999 --end 2999 

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 4999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 5000 --end 9999 

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 10000 --end 14999 
python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 15000 --end 19999

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 20000 --end 24999 

python scripts/decompile_sections.py -i ./apps/testy/96/output/sections/ -o ./apps/testy/96/output/results/ --start 1 --end 9 --report ./apps/testy/output/run_report.json -v
```

## Region Tree

Un-comment or change logging level to `logging.DEBUG` → scripts/decompile_sections.py

```python
import logging
from hermes_decompiler.core.logging import configure_logging, logging_test, get_logger

logger = get_logger(__name__)
# configure_logging(level=logging.INFO, use_color=True)
configure_logging(level=logging.DEBUG, use_color=True)
logging_test()
```

```text
===== REGION TREE =====
SequenceRegion
    Block 0
    LoopRegion(header=1)
        SequenceRegion
            Block 1
            Block 2
            Block 3
            LoopRegion(header=10)
                SequenceRegion
                    Block 10
                    Block 9
    Block 4
    LoopRegion(header=5)
        SequenceRegion
            Block 5
            Block 6
            Block 7
            Block 8
    Block 11
```

## Done Stuff | from 2025-08-01

- LoopKind +-> FOR_OF, FOR_IN | ForEachRecognizer





