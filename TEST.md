# IR (Intermediate Representation)

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

uncomment to activate → LoopStructurer → hermes_decompiler/regions/building/Structurers.py

```python
class LoopStructurer:

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):

        if self.cfg.loop_analysis is None:
            return

        roots = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        for loop in roots:
            self._build_loop(loop, self.graph.root)

        # TODO: activate with a condition
        # print("\n===== REGION TREE =====")
        # self._dump(self.graph.root)
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