"""
Tests for FunctionKindIndex - the cross-section resolver that decides
which functions are generator/async bodies.

The cases below are the two real lowering shapes, because the whole point
of the resolver is that neither per-function signal works on both:
<StartGenerator> exists only up to hbc96, and header Kind bits only from
hbc97 - and even then they sit on the stub, never on the body.
"""

from hermes_decompiler.frontend.parsing.FunctionKindResolver import FunctionKindIndex


def _section(header: str, body: str = "") -> str:
    return f"\n=> {header}\n\nBytecode listing:\n\n{body}\n"


def _v96_generator() -> list[tuple[int, str]]:
    """LAYOUT_V96: no Kind bits; body is identified by CreateGenerator and <StartGenerator>."""
    return [
        (100, _section(
            '[Function #100 "caller" of 9 bytes]: 1 params',
            "==> 00000000: <CreateGeneratorClosure>: <Reg8: 1, Reg8: 0, function_id: 101>  # Function: [#101 gen]",
        )),
        (101, _section(
            '[Function #101 "gen" of 9 bytes]: 1 params',
            "==> 00000000: <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 102>  # Function: [#102 gen]",
        )),
        (102, _section(
            '[Function #102 "gen" of 9 bytes]: 1 params',
            "==> 00000000: <StartGenerator>\n==> 00000002: <ResumeGenerator>: <Reg8: 1, Reg8: 2>",
        )),
    ]


def _v98_async() -> list[tuple[int, str]]:
    """hbc97+: no suspend/resume opcodes at all; async kind sits two links above the body."""
    return [
        (200, _section(
            '[Async function #200 "doWork" of 9 bytes]: 1 params',
            "==> 00000000: <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 201>  # Function: [#201 ?anon_0_doWork]",
        )),
        (201, _section(
            '[Generator function #201 "?anon_0_doWork" of 9 bytes]: 1 params',
            "==> 00000000: <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 202>  # Function: [#202 ?anon_0_doWork]",
        )),
        (202, _section(
            '[Function #202 "?anon_0_doWork" of 9 bytes]: 1 params',
            "==> 00000000: <LoadConstZero>: <Reg8: 0>\n==> 00000002: <Ret>: <Reg8: 0>",
        )),
    ]


def test_v96_body_resolved_without_kind_bits():
    index = FunctionKindIndex.from_sections(_v96_generator())

    body = index.facts_for(102)
    assert body.is_generator_body
    assert body.has_start_generator
    # No Kind bits exist on this layout, so there is no evidence of which
    # keyword it came from - the resolver must say so rather than guess.
    assert body.source_kind == "unknown"
    assert not body.is_async_source

    assert index.facts_for(101).role == "stub"
    assert index.facts_for(100).role == "normal"


def test_v98_body_resolved_without_any_suspend_opcode():
    index = FunctionKindIndex.from_sections(_v98_async())

    body = index.facts_for(202)
    # The body carries neither a suspend opcode nor a non-normal header -
    # only the CreateGenerator edge from another section identifies it.
    assert body.is_generator_body
    assert not body.has_start_generator
    assert body.header_kind == "normal"


def test_async_kind_propagates_down_the_stub_chain():
    index = FunctionKindIndex.from_sections(_v98_async())

    body = index.facts_for(202)
    # 'async' is only readable on the outermost stub; 'generator' on the
    # inner one must not win, or every async function reads as a plain
    # generator.
    assert body.source_kind == "async"
    assert body.is_async_source
    assert body.stub_ids == (200, 201)

    assert index.facts_for(200).body_id == 202
    assert index.facts_for(201).body_id == 202


def test_plain_generator_is_not_reported_as_async():
    sections = [
        (300, _section(
            '[Generator function #300 "gen" of 9 bytes]: 1 params',
            "==> 00000000: <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 301>  # Function: [#301 gen]",
        )),
        (301, _section('[Function #301 "gen" of 9 bytes]: 1 params')),
    ]

    body = FunctionKindIndex.from_sections(sections).facts_for(301)
    assert body.source_kind == "generator"
    assert not body.is_async_source


def test_ordinary_closure_parent_is_not_pulled_into_the_chain():
    """A normal function reaching a stub via CreateClosure is not a stub itself."""
    sections = _v98_async() + [
        (199, _section(
            '[Function #199 "module" of 9 bytes]: 1 params',
            "==> 00000000: <CreateClosure>: <Reg8: 1, Reg8: 0, function_id: 200>  # Function: [#200 doWork]",
        )),
    ]

    index = FunctionKindIndex.from_sections(sections)
    assert index.facts_for(199).role == "normal"
    assert index.facts_for(202).stub_ids == (200, 201)


def test_partial_batch_leaves_body_unresolved():
    """A subset that omits the creating section cannot resolve the body."""
    # Only the body itself - the CreateGenerator edge that identifies it
    # lives in the omitted section 201.
    index = FunctionKindIndex.from_sections(_v98_async()[2:])

    body = index.facts_for(202)
    assert not body.is_generator_body
    assert body.role == "normal"


def test_unknown_function_and_empty_index():
    index = FunctionKindIndex.from_sections(_v98_async())
    assert index.facts_for(999) is None

    empty = FunctionKindIndex.empty()
    assert len(empty) == 0
    assert empty.facts_for(202) is None


def test_unparseable_section_is_skipped():
    index = FunctionKindIndex.from_sections(
        _v98_async() + [(400, "no header line here at all")]
    )
    assert index.facts_for(400) is None
    assert index.facts_for(202).is_generator_body
