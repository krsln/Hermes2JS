"""
A ternary folded onto an EARLIER definition must not be printed there when its
test reads a register that is only set later (`useScrollOffset`, 96/11152):

    r1 = closure; ...; r4 = r4.IS_WEB; if (!r4) r1 = other; store(r1)

`ConditionalExpressionRegionPass` takes the register's last write in the block
as the ternary's default and prints the fold where that write stands, so
`r1 = !r4 ? ... : ...` ended up above the line that sets `r4`.

A fold the reader swallows is a different case: the ternary is read where the
reader stands, which is after the test (`toString`, 96/3602).
"""

import re

from hermes_decompiler.Decompiler import Decompiler

_USE_SCROLL_OFFSET = r"""

=> [Function #11152 "" of 230 bytes]: 8 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x002079cf

Bytecode listing:

==> 00000000: <CreateEnvironment>: <Reg8: 2>
==> 00000002: <LoadParam>: <Reg8: 6, UInt8: 2>
==> 00000005: <LoadParam>: <Reg8: 9, UInt8: 6>
==> 00000008: <LoadParam>: <Reg8: 7, UInt8: 7>
==> 0000000b: <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 11153>  # Function: [#11153 useScrollOffsetWeb of 166 bytes]: 3 params @ offset 0x00207ab5
==> 00000010: <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 11159>  # Function: [#11159 useScrollOffsetNative of 145 bytes]: 3 params @ offset 0x00207cbd
==> 00000015: <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 11165>  # Function: [#11165 getWebScrollableElement of 42 bytes]: 2 params @ offset 0x00207e5a
==> 0000001a: <StoreToEnvironment>: <Reg8: 2, UInt8: 9, Reg8: 0>
==> 0000001e: <GetGlobalObject>: <Reg8: 4>
==> 00000020: <TryGetById>: <Reg8: 11, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000026: <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
==> 0000002b: <NewObject>: <Reg8: 8>
==> 0000002d: <LoadConstTrue>: <Reg8: 0>
==> 0000002f: <PutNewOwnByIdShort>: <Reg8: 8, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
==> 00000033: <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
==> 00000037: <Call4>: <Reg8: 5, Reg8: 10, Reg8: 11, Reg8: 9, Reg8: 5, Reg8: 8>
==> 0000003e: <TryGetById>: <Reg8: 8, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
==> 00000044: <GetByIdShort>: <Reg8: 5, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
==> 00000049: <NewObject>: <Reg8: 4>
==> 0000004b: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 0, string_id: 133>  # String: 'enumerable' (Identifier)
==> 0000004f: <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 11166>  # Function: [#11166 get of 9 bytes]: 1 params @ offset 0x00106b41
==> 00000054: <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 0, string_id: 50>  # String: 'get' (Identifier)
==> 00000058: <LoadConstString>: <Reg8: 0, string_id: 11724>  # String: 'useScrollOffset' (Identifier)
==> 0000005c: <Call4>: <Reg8: 0, Reg8: 5, Reg8: 8, Reg8: 9, Reg8: 0, Reg8: 4>
==> 00000063: <LoadConstZero>: <Reg8: 0>
==> 00000065: <GetByVal>: <Reg8: 4, Reg8: 7, Reg8: 0>
==> 00000069: <LoadConstUndefined>: <Reg8: 0>
==> 0000006b: <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
==> 00000070: <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 4>
==> 00000074: <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
==> 00000077: <GetByVal>: <Reg8: 4, Reg8: 7, Reg8: 4>
==> 0000007b: <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
==> 00000080: <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 4>
==> 00000084: <LoadConstUInt8>: <Reg8: 5, UInt8: 2>
==> 00000087: <GetByVal>: <Reg8: 5, Reg8: 7, Reg8: 5>
==> 0000008b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 5>
==> 00000090: <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 5>
==> 00000094: <LoadConstUInt8>: <Reg8: 5, UInt8: 3>
==> 00000097: <GetByVal>: <Reg8: 5, Reg8: 7, Reg8: 5>
==> 0000009b: <Call2>: <Reg8: 5, Reg8: 6, Reg8: 0, Reg8: 5>
==> 000000a0: <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 5>
==> 000000a4: <LoadConstString>: <Reg8: 5, string_id: 5127>  # String: 'animatedRef is not initialized in useScrollOffset. Make sure to pass the animated ref to the scrollable component to get scroll offset updates.' (String)
==> 000000a8: <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 5>
==> 000000ac: <NewArrayWithBuffer>: <Reg8: 5, UInt16: 5, UInt16: 5, UInt16: 20715>  # Array: ['onScroll', 'onScrollBeginDrag', 'onScrollEndDrag', 'onMomentumScrollBegin', 'onMomentumScrollEnd']
==> 000000b4: <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 5>
==> 000000b8: <GetById>: <Reg8: 4, Reg8: 4, UInt8: 3, string_id: 9473>  # String: 'IS_WEB' (Identifier)
==> 000000be: <JmpFalse>: <Addr8: 6, Reg8: 4>  # Address: 000000c4
==> 000000c1: <Mov>: <Reg8: 1, Reg8: 3>
==> 000000c4: <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 1>
==> 000000c8: <NewObject>: <Reg8: 1>
==> 000000ca: <LoadConstString>: <Reg8: 3, string_id: 6258>  # String: 'function reactNativeReanimated_useScrollOffsetTs1(){const{animatedRef,getWebScrollableElement,offset}=this.__closure;var _animatedRef;if((_animatedRef=animatedRef)!==null&&_animatedRef!==void 0&&_animatedRef.current){const element=getWebScrollableElement(animatedRef.current);offset.value=element.scrollLeft===0?element.scrollTop:element.scrollLeft;}}' (String)
==> 000000ce: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 3, string_id: 92>  # String: 'code' (Identifier)
==> 000000d2: <StoreToEnvironment>: <Reg8: 2, UInt8: 7, Reg8: 1>
==> 000000d6: <NewObject>: <Reg8: 1>
==> 000000d8: <LoadConstString>: <Reg8: 3, string_id: 6260>  # String: 'function reactNativeReanimated_useScrollOffsetTs2(event){const{offset}=this.__closure;offset.value=event.contentOffset.x===0?event.contentOffset.y:event.contentOffset.x;}' (String)
==> 000000dc: <PutNewOwnByIdShort>: <Reg8: 1, Reg8: 3, string_id: 92>  # String: 'code' (Identifier)
==> 000000e0: <StoreToEnvironment>: <Reg8: 2, UInt8: 8, Reg8: 1>
==> 000000e4: <Ret>: <Reg8: 0>
"""

_TO_STRING = r"""

=> [Function #3602 "toString" of 91 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x0015b9c7

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 0>
==> 00000003: <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 15380>  # String: '_searchParamsInstance' (Identifier)
==> 00000009: <LoadConstNull>: <Reg8: 1>
==> 0000000b: <JStrictEqual>: <Addr8: 72, Reg8: 2, Reg8: 1>  # Address: 00000053
==> 0000000f: <GetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 15380>  # String: '_searchParamsInstance' (Identifier)
==> 00000015: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 33>  # String: 'toString' (Identifier)
==> 0000001a: <Call1>: <Reg8: 2, Reg8: 1, Reg8: 2>
==> 0000001e: <GetById>: <Reg8: 4, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000024: <GetByIdShort>: <Reg8: 1, Reg8: 4, UInt8: 4, string_id: 162>  # String: 'indexOf' (Identifier)
==> 00000029: <LoadConstString>: <Reg8: 3, string_id: 1885>  # String: '?' (String)
==> 0000002d: <Call2>: <Reg8: 4, Reg8: 1, Reg8: 4, Reg8: 3>
==> 00000032: <LoadConstInt>: <Reg8: 1, Imm32: -1>
==> 00000038: <Greater>: <Reg8: 1, Reg8: 4, Reg8: 1>
==> 0000003c: <JmpFalse>: <Addr8: 7, Reg8: 1>  # Address: 00000043
==> 0000003f: <LoadConstString>: <Reg8: 3, string_id: 1103>  # String: '&' (String)
==> 00000043: <GetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000049: <Add>: <Reg8: 1, Reg8: 1, Reg8: 3>
==> 0000004d: <Add>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 00000051: <Ret>: <Reg8: 1>
==> 00000053: <GetById>: <Reg8: 0, Reg8: 0, UInt8: 3, string_id: 12484>  # String: '_url' (Identifier)
==> 00000059: <Ret>: <Reg8: 0>
"""


def _render(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_ternary_that_would_print_above_its_test_stays_an_if():
    js = _render(_USE_SCROLL_OFFSET, 11152)

    assert "!r4 ?" not in js
    assert js.index("r4 = r4.IS_WEB;") < js.index("if (r4) {")
    assert re.search(r"r1 = useScrollOffsetNative;", js)
    assert re.search(r"\br2\[6\] = r1;", js)


def test_ternary_read_where_its_reader_stands_still_folds():
    js = _render(_TO_STRING, 3602)

    assert '((r4 <= -1) ? "?" : "&")' in js
