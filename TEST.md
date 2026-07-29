# CFG - Control Flow Graph

# IR - Intermediate Representation

**control data /fixtures**

```shell
tree -I '__pycache__|__init__.py' hermes_decompiler
tree -I '__pycache__|__init__.py|ir|handlers|regions' hermes_decompiler

```

```shell
python scripts/decompiler.py -i ./apps/demo/fixtures/one -o ./apps/demo/fixtures/results

python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results

python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --no-verbose
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --strict
python scripts/decompiler.py -i ./apps/demo/fixtures/sections -o ./apps/demo/fixtures/results --strict --no-verbose
```

```shell
python scripts/decompiler.py -i ./apps/coachy/fixtures/sections -o ./apps/coachy/fixtures/results

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

## Region Tree

Un-comment or change logging level to `logging.DEBUG` → scripts/decompiler.py

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