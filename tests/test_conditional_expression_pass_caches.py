"""
`ConditionalExpressionRegionPass` keeps the reach of a block, the owner of an instruction and the writers of a register
instead of recomputing them for every reader it asks about (F-320; 98/2619 `beginWork` spent two thirds of its render
time rebuilding them, 180 000 times). The tests check the helpers against a plain scan.
"""

import importlib
from types import SimpleNamespace

_PASS = importlib.import_module(
    "hermes_decompiler.backend.transforms.region_passes.ConditionalExpressionRegionPass"
).ConditionalExpressionRegionPass


class _Block:
    def __init__(self, name, instructions=()):
        self.name = name
        self.instructions = list(instructions)
        self.successors = []
        self.predecessors = []


class _Instruction:
    def __init__(self, dest_reg):
        self.dest_reg = dest_reg


def _block(name, instructions=()):
    return _Block(name, instructions)


def _link(a, b):
    a.successors.append(b)
    b.predecessors.append(a)


def _instruction(dest_reg):
    return _Instruction(dest_reg)


def _pass(blocks):
    instance = object.__new__(_PASS)
    instance.cfg = SimpleNamespace(blocks=blocks)

    return instance


def test_reach_follows_successors_and_predecessors():
    a, b, c, d = (_block(n) for n in "abcd")
    _link(a, b)
    _link(b, c)
    _link(c, b)  # a loop
    _link(a, d)
    instance = _pass([a, b, c, d])

    assert instance._reach(a, forward=True) == {a, b, c, d}
    assert instance._reach(c, forward=True) == {b, c}
    assert instance._reach(c, forward=False) == {a, b, c}
    assert instance._reach(d, forward=False) == {a, d}


def test_owner_and_writers_are_rebuilt_when_an_instruction_is_added():
    first, second = _instruction(1), _instruction(2)
    block = _block("a", [first])
    instance = _pass([block])

    assert instance._instruction_owner() == {first: block}
    assert instance._writers_of(1) == [(first, block)]
    assert instance._writers_of(2) == []

    block.instructions.append(second)

    assert instance._instruction_owner() == {first: block, second: block}
    assert instance._writers_of(2) == [(second, block)]
