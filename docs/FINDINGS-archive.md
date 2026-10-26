# Findings archive (resolved)

Resolved decompiler findings, oldest first. Each entry records the symptom, the cause, the fix and the test that guards it, so a regression of the same class can be traced. Open findings and measurements live in `FINDINGS.md`. Examples are `<bundle>/<function id>` (bundles 96 and 98).

- **F-100 Silent drop** (96/652, `_interopDefault`; 96/15102, 98/167). The last test pattern lost its own last
  test; ShortCircuit crossed form and `SharedTailDuplicationCfgPass`. Test:
  `tests/test_shared_tail_conditions.py`.
- **F-101 Value-producing ternary and `||`/`&&` whose value is only tested** (96/12188). New
  `ValueConditionFoldCfgPass`: the value diamond is collapsed into a single block before ShortCircuit. 8dda5b3.
- **F-102 `||` chains with the same target and setup** (96/4456, 96/150). Setups such as `LoadParam` split the
  chain. A constant comparison now counts as a `case` only if it re-compares the same value.
  c533987.
- **F-103 Crossed folding when the condition contains a call** (98/11891). If the call in the setup is leftmost in
  the condition, it is accepted because the order is preserved. c533987.
- **F-104 Pure setup that is no longer read** (96/4543). A `getEnvironment(0)` with its name resolved was blocking the fold.
  c533987.
- **F-105 Identity-aware substitution.** Register names in a subtree inlined from another instruction are now resolved
  during folding with that instruction's own state. Three wrong outputs were fixed: 96/11316 `.value.value`, 96/9150
  `in r0[1][1]`, 96/9595 `undefined.deepEqual`. In addition, the `r1 === ""` arm was being dropped in 96/3414.
  c533987.
- **F-106 `repoint_references` region filter.** Conditions of regions preceding the fold were being repointed because
  they were mistaken for the value of a register defined later (98/2463 `r6 ||`). 8dda5b3.
- **F-107 98/2917 crash.** Adding an edge block in a function with handlers made `compute_dominators` raise
  `KeyError`; edge blocks are no longer added in functions with handlers. d5c83ad.
- **F-108 De Morgan printing.** `!(a && !b)` → `!a || b`; only in the printer, only inside
  `&&`/`||`, and only for equality negations (NaN-safe). 8dda5b3.
- **F-109 `TypeOfIs`/`JmpTypeOfIs` bit mapping** (part of F-02; 98/9594). The mapping was a guess
  (`TYPEOF_FLAGS`/`_TYPE_BITS`); measured with `hermesc`: undefined=1, null=2, string=4, symbol=8,
  boolean=16, number=32, bigint=64, function=128, object=256 (`typeof x === "object"` = 258, its inverse 253).
  Shared resolver `frontend/handlers/shared/_typeof_mask.py`; most masks are
  written as complements (`typeof x !== "object"`). The output of 667 functions changed in 98 (115 of them
  had `<unresolved_typeof_mask_…>`); these opcodes do not occur in 96. Test: `tests/test_typeof_mask.py`.
- **F-110 Printer: the `!` produced by De Morgan was grouped incorrectly** (the other part of F-02). The parent node
  still took `!(a && b)` for a `!` and did not add parentheses: `!!(…)` changes the value,
  `!(a && b) && c` → `P || Q && c`. 9 functions in 96, 6 in 98.
  Test: `tests/test_printer_negation_grouping.py`.
- **F-111 Stale inlined read** (F-01; 96/4456, 96/9118, 98/12478, 98/13745, 98/9542...). When inlining into the reader
  `r1 = r0[0]`, it was not known at that point whether a later definition of `r0` would be printed. The scratch
  pass now collects the printed definitions (`printed_definitions`) and hands them to the real pass. Prevalence:
  the output of 1571 functions changed in 96 and 1079 in 98; in ~94% of the changed ones the old output
  had an assignment, printed immediately before, to the register being read. The goto count did not change. 13 golden functions
  (26 files) were regenerated; among those inspected one by one, the old output contained a stale read. Test: `tests/test_stale_inlined_read.py`.
- **F-112 `this` changed when a bare-register callee was replaced by a member access.** When `r4` in `r4(x)` was replaced
  by `env[1]` during folding, it became `env[1](x)` (this=env); it is now `env[1].call(undefined, x)`
  (`keep_call_this_unbound`). 98/11891 and 98/10829. Test: `tests/test_stale_inlined_read.py`.
- **F-113 Widened copy of the shared exit** (part of F-10; 96/10518, 98/4916, 96/2266, 98/2768,
  96/169 ...). If a goto remains, a third attempt (`SharedReturnDuplicationCfgPass(widen=True)`) also copies `throw` exits and
  the closing `return` that another block falls into; the result is accepted only if every register read by the tail
  reaches a single value on every path (`_reads_the_same_on_every_path`) and only if it is goto-free. 21 functions lost their gotos
  (96: 396→383, 98: 400→392). A tail copy containing expressions was tried and fixed
  58 functions, but gave a wrong result in 96/9349; it was not added. Test: `tests/test_shared_return_widened.py`.
- **F-114 Multi-block shared tail** (part of F-10; 98/1871 `get`, 98/1872 `getEnforcing`, 98/244, 98/249,
  98/360, 98/408, 98/6251). `a != null ? a(p) : null` followed by `?? (m[p] ?? null)`: the second operand is a
  two-block tail with an inner test; one test jumps to it, another falls into it. `SharedTailDuplicationCfgPass(regions=True)` copies this
  small forward region (<=4 blocks, <=12 instructions, single exit `END`) to the test that falls through. It runs only in the third attempt, as a last resort: when enabled on every attempt it
  broke the `||`/`&&` chain in goto-free functions (96/7424) and turned the `max/min` compression into a goto in 98/14169. 98: 392→385. Test: `tests/test_shared_return_widened.py`.
- **F-115 A copy written in an arm was taken to be a single definition after the join** (96/4846, 96/10300, 98/12079 `binarySubdivide`;
  also 96/12935 `isArrayish`, 98/2503 `getNextLanes`, 98/8193 `compareIdentifiers` ... 20 functions). `r14 = r0; if (c) {
  r14 = param3 }; r10 = r14`: because `Mov r13, r10` holds the same node as the value (`param3`) of the `Mov r14, r13` in the arm,
  `UnfoldedMergeRepairPass` called it "ambiguous" and did not repair it, and the reader printed `r10 = param3` (it should have been
  `r0` when `c` is false). A `Mov` whose value is the arm's own source is no longer counted (`_is_source_mov_of`). A general
  `is_join_value` guard was tried and abandoned because it broke 10 tests (ternary/default join folds).
  The `isArrayish` test now expects `r0 = r1` instead of `r0 = r3` (the global object, never written on that path). All 20
  functions whose output changed show the same pattern (the missing assignment is printed, the read goes back to the register). Test: `tests/test_shared_return_widened.py`.
  The remaining path in 96/12935 is in F-116.
- **F-116 Chained `Mov` readers and the arm's default** (96/12935, 98/6200 `isArrayish`; the output of ~50 functions
  changed). `r2 = a instanceof F` (inlined in the test) / `r2 = r3` in the arm, followed by `Mov r1, r2`, `Mov r0, r1`:
  `UnfoldedMergeRepairPass` counted the `Mov` behind the reader (`Mov r0, r1`), which holds the same node, as "another owner" and
  did not repair it; on the `instanceof` true path `r1` read the global object. `Mov`s that later copy the reader's register
  (`_chained_reader_movs`; excluding, in a loop, a `Mov` BEFORE the reader) now count as a chain. In addition, the
  branch "the register written in the arm is read by name after the `if`" did not print the default that the `if`'s own test inlines
  (`r1 = len >= 0`); `_reprint_unprinted_default` was added there too. Result: `r1` is assigned on the `length < 0` path.
  Effect: in about 50 functions a missing assignment is printed / a dead default (`r0 = param1`) disappears /
  `return r0` replaces `return param1` (96/1666, 98/2360 `diffProperties`). About ten sampled functions were
  compared against the bytecode; not all were verified one by one. Test: `tests/test_boolean_chain_copy_reads_register.py`.
- **F-117 Shared tail containing statements** (part of F-10; 96/2019, 96/12456, 96/13816, 98/8735 ... 38 functions).
  `SharedReturnDuplicationCfgPass(statements=True)`: if a goto remains after three attempts, a fourth attempt also copies a `return`/`throw` tail containing
  up to 6 ordinary instructions (with the path-independence guard) to the jumper.
  96: 383→358, 98: 385→372, no function regressed. IMPORTANT: the `value`/`statement` nodes of the copied instructions must be
  deep-copied; when shared, a fold took the assignment from the copy (96/12456: the `!param1` arm returned an unassigned `r1`).
  In the previous round I saw a "wrong result" because of this, but 96/9349 `cmp` is broken independently of the tail (F-118). The
  "read of a register unassigned on every path" check on the outputs (crude, structural if/else) flagged only those already broken before.
  Tests: `tests/test_shared_return_widened.py`.
- **F-118 Consecutive binary ternaries get mixed up** (96/9349 `cmp`, `===`/`!==` arms). `r1 = typeof a !== "object"
  ? a : a.version; r0 = typeof c !== "object" ? c : c.version; return r1 === r0`: when the same `typeof` register (`r3`) is used
  twice, the first expression carries the second one's test (`(r1 !== "object") ? param1 : ...`) and unread registers;
  `return` reads the wrong `r0`. Independent of goto (present in the baseline too).
  **Partially resolved.** `ConditionalExpressionRegionPass`: if the register in the ternary's test is changed, between the branch and the reader
  (along the flow), by a definition that is re-*printed*, the reader reads that register instead of a copy of the ternary
  (`repoint_references(..., reader_value=)`); if it cannot be proven that the register is filled at that point, the merge is not folded
  BEFORE the arm is absorbed (`_peek_arm_result`). A write that was folded into its readers and never printed (`Mov r3, r1` in 96/8499,
  `r3 = console.log` in 98/9485) and a redefinition that is PRINTED by the reader itself do not count: the copy
  still reads correctly in the text. Two tiers: printed redefinition → the register is read (not folded if unsafe);
  folded-only write → the register is read only if both conditions hold (not overwritten in between + the folded expression
  runs before the reader, or a previously printed default exists; `_register_holds_merge`), otherwise the copy is kept
  (a copy in 96/8499 because `r1` is overwritten). As a result 98/9485, 9486, 9490 are all in the form `console.log(200, r6, r5)`,
  consistent. Full suite (96+98): ~286 functions changed (96: 126, 98: 160), goto 96: 358→359 (96/12624: the old
  `r1 = (r2 !== "object") ? "object" : r4.params` swallowed an `||` chain, the new output is faithful but has a goto), 98:
  372. Examples: 96/10194 wrong `!r0` test → `r8`; the `r5.retries`/`r5.name` copies in 98/9490 were read after the printed
  `r5 = getParentEnvironment(0)` (golden updated). **Open:** the full function 96/9349 `cmp` (empty
  `if {} else {}` arms inside a switch, `return r3 === r1`) is broken independently of tail/ternary, it was also there in the baseline; the loop
  conditions' copies (the 96/12561 pattern) do not go through this pass.
- **F-119 Shared exit copy in functions with exception handlers** (part of F-10; 96/3900
  `normalizeRootMargin`, 96/1363, 96/10844, 96/12298, 96/2813, 96/4231, 96/1907, 96/2413, 96/8034, 96/9338,
  98/11643, 98/1635, 98/2811, 98/3382, 98/5884, 98/8176 - 16 functions). `SharedReturnDuplicationCfgPass` did not run at all
  if the function had any exception handler; even a `for-of` brings in a handler, so the leading `if (c) return X` exits
  stayed as `goto`. Now only blocks in the protected range and handler entries are
  skipped (the copy is always placed outside the range). In functions with handlers the path-independence check
  (`_reads_the_same_on_every_path`) is also applied at level 1: otherwise 98/2477 `getComponentNameFromType` turned the
  `r1 = null` / `r1 = displayName || ...` phi into `return null`. What I tried and DISCARDED: "copy to every
  jumper, the original dies" (`every_jumper`, level 5) - it produced wrong output in 96/10211, such as `if (A) {} else if (B) {} r0 = true`.
  Full suite: goto 96: 359→349, 98: 372→366; no other output changed.
- **F-120 Constant read by two exits in a crossed condition** (the non-return sub-shape targeted by F-10; 96/9112-9134
  `parseTranslateX/Y`, `parseScaleX/Y`, `parseRotate`, `parseSkewX/Y`, `parsePerspective`, 96/12212, 96/19, 96/3433,
  96/4491, 98/11215, 98/12081, 98/12630, 98/13801, 98/3236, 98/3974, 98/9557 - 19 functions goto-free). Shape:
  `len !== 1` → `r0 = []`; `isLength(x) || isPercent(x)` → build an object. The existing "crossed" merge
  (`ShortCircuitConditionCfgPass._try_merge_crossed`: `!a && b`) was rejecting the case where, while folding the setup of the second test into the condition, the constant
  load in the setup (`r1 = 0`) was also read by one of the two exits (END). Now the constant load enters the condition and its copy is placed
  in the edge block opened in front of END (`_constants_for_the_end_edge`; only when END is reached by a single path,
  the constant is dead in the arm, and there is no exception handler). Side benefit: 96/4063 `handler` is now the source itself
  (`if (c === -1 && this.utf8BytesNeeded !== 0) ... else if (c === -1)`; the old one read an unassigned `r5`),
  96/9150 `maybeSwapComponents` has a single `&&`/`||` condition instead of two separate `return param1`. Two old tests (9150, 9118) encoded the shape of the old
  output; they were updated while preserving the meaning. Full suite: goto 96: 349→337, 98: 366→359; 23 outputs
  changed, no new goto, the check tool flagged nothing.
- **F-121 Body shared by three or more labels** (the sub-shape targeted by F-10 whose target is in another region and is also reached by fallthrough;
  96/7527 `encoderForArrayFormat`, also 96/748, 96/2095 and similar). `case "comma": case "separator":` are grouped,
  but the third label's test stayed in `default` as `if ("bracket-separator" === r3) goto label_70;`.
  `_ComparisonChainSwitchBuilder._peel_shared_jumps`: equality tests at the start of the default arm that jump to the entry block of the last case
  are added to that case's labels and the branch block is dropped; the change is applied only if the switch is actually built
  (if the chain stays short the region is not broken; on the first attempt `isTransitionProp` was broken, caught by a test).
  Test: tests/test_switch_shared_labels.py. Full suite: goto 96: 337→331, 98: 359→356; 17 outputs changed.
  Open: 96/9349 `cmp` (previously broken) now produces a nested switch + `break`; the ternary expressions still read the wrong registers.
- **F-122 `continue` branching to an empty second back edge** (the sub-shape targeted by F-10 consisting of a sibling block in the same region;
  96/8548 `cloneObjectProperties`, 98/7120). `if (c) continue;` was branching not to the loop header but only to an empty
  gate block that falls into the header; in addition, `IfStructurer` gave the first test's else arm and the body to separate arms and lost that arm's edge
  that falls into the body (in the old output the body stayed in only one arm: the output with a goto was not valid JS, but
  writing `continue` instead of `goto` would have made it silently wrong). `ConditionalContinueRegionPass`: the target also counts if it is an empty gate block, and `_rejoin_else_arm` turns the shape `if (c) { T } else { F; if (d) continue; }` into
  `if (!c) { F; if (d) continue; } T` once the CFG edge by which F falls into T is verified. Test: tests/test_conditional_continue_latch.py. Full suite:
  goto 96: 331→330, 98: 356→355; 16 outputs changed (the goto went away in only 2 of them, the rest are the same arm-rejoin
  fix; the check tool flagged nothing, in 2284 and 5130 the old output dropped the body).
- **F-123 Exit block of the guard that ends the function, after the join** (the sub-shape targeted by F-10 consisting of a sibling block;
  98/3552 `canParse`, 96/193 `Ie`, 98/12515 `Ie` and similar). `if (a) { ...; if (c) return x; } TAIL`: because the guard's
  exit is laid out after TAIL, `if (c) goto label` remains, and either TAIL was copied or the else arm lost the edge that falls into TAIL.
  Two parts: (1) `_DominanceIfBuilder._arm_guard_falls_into` counts the function-ending block that the arm's guard reaches by falling through
  as the join (not inside a loop; if the arm's code after the join has not been laid out); (2) the new
  `GuardExitRegionPass` moves the function-ending exit block that goes only to this branch into `if (c) { ... }`, but only if
  the place the branch falls into is really next in the CFG (not inside a loop).
  During this work a previously hidden miscompilation surfaced: in the loops 98/8982 `checkEqual` and 98/5330
  `do { x = it.next(); if (x === undefined) goto RETURN_TRUE; ... } while (c)`, `_absorb_residual_conditional` turned
  the jump into `if (x !== undefined) { body }` and threw the exit (`return true`) after the loop; the first attempt was hidden only
  because another goto forced a retry. Now a branch inside a loop that leaves the loop and jumps to a `return` block it cannot
  return from is not absorbed (`_compound_folder._reaches`).
  Tests: tests/test_guard_exit_region.py (canParse, checkEqual); the 96/12456 test in tests/test_shared_return_widened.py
  was updated (the tail is no longer copied, a single `r1 = []; return r1;`). Full suite: goto 96: 330→314, 98: 355→335;
  178 outputs changed. Those that got worse: 98/5330 (goto-free but a nested switch instead of an `||` chain), 96/2408 (else-if pile),
  98/2620 `appendAllChildren` (two gotos came back; the old output was wrong because of the same bug) - these are losses in readability, gains in
  correctness. Of the 4 files flagged by the check tool, 193, 12515 and 8982 were inspected by hand (no real unassigned read); 98/2693 was only
  eyeballed, and most of the 178 changes were not read one by one.
- **F-124 Else-if with a second `=== null` test that drops a `return`** (partially resolved; 98/11208 `wrappedFn`, 96/4157 `parseFileSlash`,
  96/1139 `processColor`; it was wrong output). `if (a === undefined) goto R; if (a === null) goto R; ...` (R: `return a`) became in the output
  `if (a === undefined) { return a; } else if (a !== null) {...}`: the `return a` for `a === null` disappears and
  the function returns `undefined`. Cause: `_absorb_residual_conditional` took the constant comparison to be a `case` link
  (`SwitchStructurer` merges them) and dropped the jump; but two labels sharing the same body do not make a `switch` (two separate bodies
  are required, `_MIN_CASES = 2`). `_compound_folder._case_chain_has_two_bodies`: if the chain does not have at least two separate bodies this exemption is
  not applied. Test: tests/test_shared_return_labels.py. Full suite: goto count unchanged (96: 314, 98: 335); 20 outputs changed,
  all of them functions that used to silently drop the `null` return or already had gotos (96/4157 and 98/11208 are now correct with `case undefined:
  case null:`). Second stage (same day): for 96/1139 `processColor`, `ShortCircuitConditionCfgPass`: two labels with the same body now become
  the single condition `a === undefined || a === null` (`_case_chain_has_another_body`: if there is no other body in the chain there is no case exemption).
  Because the constant loaded by the second test (`r3 = null`) is also read in later code, `_fold_pure_setup` could not fold it; the constant load
  is now copied to the head of the fall-through path (`_merge(..., rematerialize=)`, reuses F-120's `_constants_for_the_end_edge`). Full suite: goto 96: 314→310, 98: 335→333; 150 outputs changed (mostly: label chains with the same body became an `||` condition instead of
  `switch`/`else if`; files containing `switch` 322→296); in 24 files an extra `rN = constant;` line (the copied load) appeared.
  Updated tests: test_jump_only_shared_return (isTransitionProp is now a single `||` condition + `r0 = true/false`),
  test_shared_tail_conditions (parenthesis form), test_shared_return_labels. Still open: the `if (r2 != null) goto
  label_120` in 96/1139 (the guard's exit, the `_arm_guard_falls_into` restriction) and 96/8976 `processColorInitially` (the shared
  `return (r3 << 24 | r3 >>> 8) >>> 0`, which was dropped in the old version too; nothing is returned after `break` inside the switch). Tried and reverted:
  (1) the restriction that the region's continuation must be the target (it broke the `switchTest` goldens), (2) removing the 'target must end the function' condition of `_arm_guard_falls_into`
  (96: 314→295, 98: 335→322 but in 98/12276 `validateType` the continuation of the else arm was dropped),
  (3) folding a same-body case chain into `||` in `ShortCircuitConditionCfgPass` (it broke two tests).
- **F-125 A chain that falls into `default` after an inverted label drops the shared `return`** (resolved; 96/4122 `defaultPort`; it was wrong output).
  Method: bulk scan (the script is not in the repo; for each function's tree flow graph it checks whether the original CFG edges are still reachable;
  'edge lost' = silent-drop candidate). Lost edges appeared in the output of 172 goto-free functions (96: 86, 98: 86); the 'block missing' class is
  noisy (ReturnValueResolutionPass consumes return blocks) and was not used for the decision. `defaultPort`: in the chain `"ftp","http","ws","https","wss"`,
  when the `"ws"` test is inverted the remaining chain falls into `default`; there `"https"`/`"wss"` are a single body so no `switch` is formed (`_MIN_CASES`),
  but because the `"wss"` test had already been melted away in `_absorb_residual_conditional`, the `return 443` path was lost (`"wss"` returned nothing).
  `_ComparisonChainSwitchBuilder._absorb_nested_chain`: if `default` is a single test chain and tests the same distinguishing expression, the chain
  joins the outer `switch` (labels merge, the pending `_peel_shared_jumps` was queued). Test: tests/test_switch_shared_labels.py.
  Full suite: goto 96: 310→309, 98: 333; 18 outputs changed (all of them either the flattening of a nested `switch`/`else if` pile or the dropped label
  coming back: 96/1308 `getDirectionForKeyword`, 96/7538 and 98/5395 `parserForArrayFormat`, 96/7193 `getStateForAction`; all eyeballed).
  Open: the remaining ~170 lost-edge candidates have not yet been triaged (96/1333, 96/1098, 98/5036, 98/2557 are examples).
- **F-126 A tail jumped over by the arm's own test stays in a single arm** (resolved; 96/1333 `getValidLengthPercentageSizeOrNull`; it was wrong output).
  The `"px"` arm should fall into the `"%"` test for an invalid number; in the output the `"%"` test was inside the other arm, and an invalid `"px"` returned
  `undefined` instead of `return null` (lost edge 0x1a→0x45). Cause: `_DominanceIfBuilder._convert` counted the common tail (`goto_block`) as a join only
  after `duplicated_returns` or if the tail ends the function; if the tail continues (no post-dominator because
  every path goes to its own separate `return`), it made the arm an `else` and pulled the tail into it. New condition: there is no `merge_block`, `goto_block` continues,
  the arm is not in a loop, and a conditional branch inside the arm jumps to `goto_block` (`_arm_tests_into`). Test: tests/test_arm_join_tail.py.
  Full suite: goto 96: 309→308, 98: 333→332; 85 outputs changed (96: 37, 98: 48). Example: 96/9364 `inc` now runs the `switch` after `if (r0) {...}` in every
  case (previously it was inside `if (!r0) { switch }`: the switch was skipped when `r0` was true). The check tool flagged 9 files
  (96: 841, 2590, 2286, 1793, 2088; 98: 2594, 2008, 11908, 2474), most of them mixed functions that already had gotos; in 98/2594 it was verified from the CFG that the tail
  is a join. Note: 98/2619 `beginWork` also takes >2 min (ConditionalExpressionRegionPass recomputes
  the dominator tree for every candidate); this is independent of this change, a separate performance task.
- **F-127 Code jumped over by a sibling arm, `throw` copy, jump-table header** (resolved; 96/273 `q`, 96/277 `E`, 96/150 `ve`, 98/2623 `unwindInterruptedWork`,
  the lost-edge scan after 96/1333; all of them were wrong output). The `dropscan` lost-edge list (96: 86→69 functions) split into three separate causes:
  (1) when the jump target of `_absorb_residual_conditional` is in a sibling arm (`_sits_in_sibling_arm`), it preserved the jump only for `return` targets;
  for a non-`return` target such as `if (state !== "writable" || f()) n(); else ...`, the second test's jump was deleted. The restriction was removed
  (the `case` exemption stays as is); in `_try_fold_and_or_cascade` Case B, if the jump goes to the other arm, no merge is done (in 98/10102
  it produced a broken condition). (2) 96/150: three tests jumped to a single `throw new RangeError(...)`; the old output turned the tests into `!(a||b) && c` and never
  wrote the `throw` (an invalid size silently returned `undefined`; the old test locked in this error). `SharedReturnDuplicationCfgPass`: at level 4 the
  `throw` tail is copied up to 12 instructions (10 instructions with `CreateThis`/`Construct`/`SelectObject` but a single statement). (3) `GuardExitRegionPass`: the `goto EXIT` at the
  end of the arm (EXIT being an exit block entered only through that jump) takes the exit's place; it also puts back an exit block that had been dropped from the tree (consumed).
  (4) A separate hidden bug: `_JumpTableSwitchBuilder` deleted the header block entirely; if the header had other statements
  (`r5 = getParentEnvironment(0)`) they vanished (98/2623: once it became a `switch`, `r5` was never assigned). The header now stays before the switch.
  Tests: tests/test_shared_tail_jumpers.py, test_shared_tail_conditions.py (the 96/150 expectation was corrected). Full suite (f126→f129): files with goto
  96: 308→302, 98: 332→334; 82 + 81 outputs changed; those that were goto-free but now have a `goto` (previously silently wrong): 96: 11, 98: 18 (96/4152 `parseAuthority`,
  96/6502, 98/2183 etc.: the path that falls through with `else if (!x)` is now visible). Tried and reverted: in `SharedTailDuplicationCfgPass`, a copy for every jumper of a short tail
  reached only by the jumpers (it made 96/273 goto-free but dropped the `r11 = param1` statement in 96/998 `mapIntoArray`: the copy + later
  passes); it was not needed, 96/273 is goto-free with the remaining changes too. Open: a `goto` in the loop body in 96/4152 etc. (ShortCircuit does not merge `a || b` in a loop),
  96/2811 `structuredCloneInternal` four identical `case ...: return x;` (no longer one `||`), `dropscan`'s lost edge to the `return undefined` target
  (96/1098) is a false alarm.
- **F-128 A plain block of the arm flows into the shared `return`** (resolved; 96/852 `_wrapNativeSuper`; it was wrong output). `if (undefined === r5) goto T;` and,
  inside the arm, `if (map.has(x)) return get; map.set(x, W);` then plain flow into `T` (the common `return`): `T` is written only
  inside the other arm, and after `map.set(...)` the function returned nothing. `_DominanceIfBuilder._arm_guard_falls_into` (F-123) counted as "falling" into `T`
  only a conditional branch (whose taken edge goes elsewhere); it now also counts as a join when a plain (non-terminator) block of the arm flows into `T`, but
  only if `T` is a `return` (a block that throws in 98/9535 broke the golden). Test: tests/test_arm_join_tail.py. Full suite (f129→f130): files with goto
  96: 302→297, 98: 334→332; 36 + 47 outputs changed, none became `goto`-ful that was goto-free. Added to the repo: scripts/audit/ (drop_scan.py: lost-edge scan
  and `--report`; compare_outputs.py: comparison of two output directories; definite_assignment.py: crude unassigned-read check).
- **F-129 Two tests leaving the loop, the exit region and the loop counter name** (resolved; 96/2026 `refreshCache`; it was wrong output). `for (n = fiber.return; n !== null; n = n.return)
  { if (tag === 24 || tag === 3) { ...found...; return } }`: two tests jump to the same code (`0x31`); in the output the code sat (dead) after the loop's own `return undefined`,
  and `tag === 24` did nothing. Three separate points: (1) `ShortCircuitConditionCfgPass` did not merge blocks that are loop members at all; if both tests leave the loop and jump to the same
  block (`_both_tests_leave_the_loop`) it is now a single `||` condition. (2) `GuardExitRegionPass._try_region_exit`: a multi-block function-ending tail entered by a single branch
  (only that branch enters, no way out) is moved into the branch's `if`; the branch's other edge must be the next piece of work or the loop itself. (3) `InductionVariableNamingPass`: if the counter
  register is written with another value in the body and then read (`r3 = getEnvironment(0); r3[458](...)`), it is not given the name `i`; previously every read became `i`. This third one was
  a hidden error in itself: 96/5408 `_ensureClosestStickyHeader` (`addCells(i)`, which in reality is a `{first,last}` object), 98/2666 `workLoopSync` (`null === i`, which in reality is the result of
  a call) and 98/13448 `cloneRecursive` were writing wrong reads. Test: tests/test_guard_exit_region.py. Full suite (f130→f131): files with goto 96: 297→291,
  98: 332→330; 33 + 24 outputs changed; none became `goto`-ful that was goto-free. The files the check tool reported as 'more unassigned reads' are the loops whose counter name stays `rN` instead of `i`
  (the corrected form of the error). Open: the remaining empty `if (3 !== r4) {}` in 96/2026 (ugly, not wrong).
- **F-130 A plain block of the arm flows into a long shared body** (resolved; 96/269 `addAbortListener`-like; it was wrong output). The same family as F-126/F-128: `if (undefined === r1) goto T;`
  and, inside the arm, `if (r4) { ...; return } r7 = r3[5]; r4 = r7.addEventListener(...)` then plain flow into `T` (a long common setup body, not a `return`). The arm's
  plain (non-terminator) block flowed into `T`, but since `T` is not a `return` the F-128 rule did not apply; `T` was written inside the arm, and the setup code after the arm's exit
  was dropped. `_DominanceIfBuilder._arm_runs_into`: if `T` has a non-terminator predecessor dominated by the arm's entry (`then_entry` dominates it), the arm counts as flowing into `T`;
  added to the F-126 condition in `_convert` as `_arm_tests_into or _arm_runs_into`. Test: tests/test_arm_join_tail.py
  (`test_an_arm_that_runs_on_into_a_long_shared_body_does_not_lose_it`, data arm_runs_into_shared_body_96_269.hasm). Full suite (f131→f132): 96: 25, 98: 32 outputs
  changed; files with goto 96: 291→292, 98: 330→331. The newly `goto`-ful ones (96/13996 `_loop3`, 98/11441 `_loop3`, 98/12534 `anonymous`): the early exit that was previously
  silently dropped (`has(...)` / `r4.aborted`, closing `return 0`) now stays as a visible `goto`; not a regression, but the surfacing of a previously hidden error.
  Open: these three are now `goto`-ful (solvable with ShortCircuit/If), 98/2606 `throwException` is flagged by the check tool (96/2052 family, an improvement).
- **F-131 Short `case` chain and the `return` behind it** (resolved; 96/777 `_unsupportedIterableToArray`; it was wrong output: it returned `undefined` for `Set`).
  `if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /Int.../.test(n)) return f(o)`: `"Map"`/`"Set"` jump to the same block (`Array.from`).
  Level 0 builds the `switch`, but a `goto` remains because the `Arguments` body is shared with the regex test in `default`; level 1 (`return` copy) is goto-free but
  the `"Set"` test is inverted (`"Set" !== r4`) and the rest of the chain + the copied `return` fall into its body: the chain cannot become a `switch` (`min_cases`: a single case) and
  the `Set` edge is lost (the `case` exemption from F-127: the target is in a sibling arm but a `switch` is expected; when it cannot be built, a silent loss). `_ComparisonChainBuilder`:
  (1) the inner chain (`_absorb_nested_chain`) joins before the `min_cases` check (`Map`+`Set` one case, `Arguments` the second); (2) the tail of `default` after the chain
  (the `return r0` into which every arm flows; only if it is the last child of the root section and all previous cases end with `return`/`throw`) is moved
  to after the `switch`. Test: tests/test_switch_shared_labels.py. Full suite (f132→f133): 36 outputs changed in 96 (mostly `if`→`switch`: 96/7102 `getStateForAction`, 96/2601), 24 changed in 98 (98/5268, 10650, 11038 `getStateForAction`: `SET_PARAMS`/`REPLACE_PARAMS` common `case`), files with goto 331→330, no new `goto`-ful ones; no crash in either suite (after F-132).
- **F-132 F-129 regression: merging two tests in a loop left stale analysis behind** (resolved; 5 sections crashed in 96 and 1 in 98: 96/2075, 2264, 2581, 2590, 13786, 98/2617).
  In F-129, `ShortCircuitConditionCfgPass` started merging two tests that are loop members (`_both_tests_leave_the_loop`). The merged block leaves the CFG but the `loop_analysis`
  computed before that still counts it as a loop member; the `If` structurer touched the empty block's `instructions[-1]` and raised `IndexError`. It had not been visible before because
  no merge ever happened in a loop; since I reviewed the f130→f131 diff by looking only at the changed files, the crashes escaped me (the log's "N sections failed"
  line must be checked). `StructuralAnalyzer.build`: if the block count changed, dominators, post-dominators and loops are recomputed; deleted blocks are also removed from the handlers'
  `try_blocks` lists (otherwise `KeyError`: 96/2139, 2146, 2156, 3448). Tests: tests/test_loop_condition_merge_analysis.py.
  `scripts/audit/compare_outputs.py` now skips a file that is not in base (a failed section) and reports it. Reminder: in a full-suite run the `status.txt` exit code and
  the log's "sections failed" must be checked.
- **F-133 A copy read from a three-way join printed the wrong value** (resolved; 96/4775 `interpolate`; it was wrong even in the raw output, `dropscan` had flagged it as a "lost edge"). `r1 = param1; if (r1 < min) { …; r1 = min; if (mode !== "clamp") r1 = param1 } r6 = r1;`:
  the frontend resolution is linear and the last definition of `r1` in address order is the inner `r1 = param1`; `Mov r6, r1` inlined it and wrote `r6 = param1`, and so did all later `r6` reads
  (`-param1`, `param1 - param2`, ...). Yet the clamped `r1 = min` path also reaches that read (when `param7 === "clamp"` the result must be `min`). A two-way join
  can be folded into `?:` (the golden outputs depend on this inlining); a single expression cannot represent a three-way join. `HermesAnalysis.is_nested_join_value`: if the definition is inside two or more
  forward jumps that end before the read and an older definition exists; `get_register_expression` gives the name `rN` for a plain `Identifier` value (same as `JmpTrue`: a fold takes the write or
  `UnfoldedMergeRepairPass` prints it). Test: tests/test_nested_join_copy.py. Full suite (f133→f135): 96: 51 outputs changed (96/8972 `HSVtoRGB`: `r5 = r5 * 255` instead of `r5 = param3 * 255`; 96/4787 `findRange`:
  `return r0 - 1`), files with goto 296→296; 98: 119 outputs changed (mostly a single register name: 98/10760 `typeof r4` (`[, r4] = param1`), 98/12319 `__environment__[4] = r9`), files with goto 330→331 (only 98/9611); no crash. Open: 98/9611 `dt` is now `goto`-ful and `r3.size = r4` (in reality `undefined`): `LoadConstUndefined r4` was folded into a test,
  and is not printed at the join (previously `function_12518` printed it, which was also wrong).
- **F-134 The `case` exemption did not test different values** (resolved; 96/956 `replacer`; it was wrong output: it returned `undefined` for `null`; the number path of 96/8976 `processColorInitially` was also silently dropped). `if (typeof v !== "object") goto R; if (v === null) goto R; REST`: both jump to the same `return`.
  The sibling-arm guard of `_absorb_residual_conditional` (F-127) exempted `case` tests (on the grounds that `SwitchStructurer` would resolve the common target itself), but the "adjacent constant comparison" check only
  looked for a comparison against a constant, not for the same value: `typeof v` and `v` are two different values, no `switch` results, and the `null` arm's `return` was dropped. `same_case_subject` (`_predicates.py`): the neighbouring/parent test must be on the same value.
  Test: tests/test_case_exemption_subject.py. Full suite (f135→f136): 6 outputs changed in 96; 96/8976 is now `goto`-ful (previously it silently dropped the number path: when `r2 === "number"`, `(r3 << 24 | r3 >>> 8) >>> 0` was never returned),
  96/1998, 2504, 11000, 3041 already had `goto`s (the test that jumps to a target in a sibling arm now stays in place). 98: 5 outputs changed, files with goto 331→332 (only 98/11848 `processColorInitially`, the same function as 96/8976); no crash.
- **F-135 Exit from a loop to a shared `return`, code after a zero-iteration loop, and the common instruction of merged `return`s** (resolved; 96/4123 `parseHost`; it was wrong output). The loop over the IPv4 parts
  (`for (i...) { if (n < 0 || n > 255) return null; ... }`) followed by `return a + b`: three separate errors stacked on top of each other. (1) `if (n < 0) goto RET; rest` became `if (n >= 0) { rest }` in the loop body:
  the body ends, the loop continues, there is no `return null`. `LoopBreakStructurer` takes only an exit body with a single predecessor (Shape B); when it could not take the multi-predecessor shared `return`, the If builder
  still turned the branch whose join is outside the loop into `if (!C) {…}`. `_DominanceIfBuilder._leaves_its_loop`: if the join is outside the loop, the branch stays raw; the attempt with return copies (level 1) turns it into a `return`.
  (2) The code (`0x188`) jumped over by the `if (0 < n) { for … }` guard is also the code the loop's exit test falls into: when the last dominator points to a different `return`, the code stays only in the other arm and
  never ran after the loop. `_arm_runs_into_after_loop`: if the exit test of the loop arm falls into `goto_block`, that is the join. (3) At level 1, when `IfTailMergeRegionPass` merged the same `Ret r0` of two arms,
  it kept the arm's original instruction as a shared object; when `ReturnValueResolutionPass` resolved the original (split) block (`return null`) it also rewrote the merged one,
  the `r0 = r3 + r2` assignments in the arms were swallowed and all paths returned `return null`. The merged block now carries a copy of the instruction, and the resolver walks the originals, not the copy that is not in the flow.
  The copy was also taught to `DeadUndefinedStorePass` as a complement (the copy is not in the snapshot, its read was counted as "always live" and `r1 = undefined;` was not deleted).
  Tests: tests/test_loop_exit_shared_return.py. Full suite (f136→f138): 96: 39 outputs changed, files with goto 297→297, no new `goto`, no crash; 98: 29 outputs changed, files with goto 332→335,
  no crash. 3 newly `goto`-ful files in 98 (98/2599 `checkShouldComponentUpdate`, 2609 `updateSimpleMemoComponent`, 10142 `BezierEasing`) used to print `if (eşit) { say }` instead of
  `if (!eşit) break` in the loop (an unequal element did not end the loop, the result stayed `true`: silently wrong); now `if (!eşit) goto label_N` is visible. 96/2590 `completeWork`: the common tail
  (`sibling.return = return`) is in a single place and the inner `for` has no `if/else` (closer to React's `completeUnitOfWork` pattern).

- **F-136 If the end of an arm falls into the shared `return`, the `return` must stay behind the `if`** (resolved; 96/1925 `updateSlot`, 2431; it was wrong output). In the form `if (typeof x !== "object") goto RET; ...; the last else arm falls into RET`, the `return null` block became the *then* arm of the outer test and the last `else` arm ended without ever reaching it (the function returned `undefined` there; since no `goto` appeared either, the retry was not triggered). A clause was added to the join condition of `_DominanceIfBuilder._convert`: if the branch target is a block ending in `Return` (with no successor) and a plain block (non-terminator) of the fallthrough arm falls into it, the target is the join point, not the else arm. Test: `tests/test_arm_runs_into_shared_return.py` (+ `tests/data/arm_runs_into_shared_return_96_1925.hasm`).
  Measurement (F-136): 9 files changed in 96 and 4 in 98, no crash. The new `goto` appears only in the already broken `getComponentNameFromType` (96/1801, 2294; 98/2477): the output used to look valid but was meaningless (`r2 + (…)`), and is now flagged with a `goto`. The rule had at first also merged loop exits (98/4137 `areCompositeKeyComponentsEqual`: the `r4 = true` after the `for` became unreachable); so only blocks that are in no loop are counted (`tests/data/loop_exit_return_after_if_98_4137.hasm`).

- **F-138 (main cause) A computed value written on one arm was inlined into copies on other arms** (resolved in part; 96/1801 `getComponentNameFromType`; it was wrong output). `r3` is last written by the `ForwardRef(...)` arm and every other arm ends in `Mov r1, r3` reading `param1`; the join guard in `OpcodeHandler.get_register_expression` covered only a bare register alias, so the string concatenation was inlined into seven copies (`r1 = r2 + (r2.displayName || r1.name || "") + ")"`). The guard now also keeps the register for a `BinaryExpression` of a join of three or more paths. Constants, environment values and member reads keep inlining on purpose (`reject.call(r0, ...)` in 96/2999, the ternary fold of `arguments[1]` in `tests/test_default_parameter_merge.py`). Test: `tests/test_computed_join_copy.py` (+ `tests/data/computed_join_copy_96_1801.hasm`). The remainder stays open in `FINDINGS.md`.
- **F-144 `for-in` null guard printed around the loop** (resolved; 96/5107 `addAnimatedValuesListenersToProps`; readability, found while working on F-139). `GetPNameList` + `JmpUndefined` printed `r6 = HermesPropertyIterator(r5); if (r6 !== undefined) { for (const r2 in r5) {...} }`. A for-in over null/undefined runs zero times, so `ForEachRegionPass._unwrap_property_list_guard` removes the definition and the `if` when the `if` is the loop's only wrapper, has no `else`, tests `rN !== undefined`, and nothing reads `rN` after the loop. Tests: `tests/test_for_in_property_list_guard.py` (guard removed; guard kept when the register is read after the loop); goldens `96/function_15093_forInTest.js` and `98/function_9480_forInTest.js` regenerated; `tests/test_conditional_continue.py` loses one indentation level.
- **F-141 Empty `if` arms** (resolved; 98/1957 `setEventInitTimeStamp`, 96/8802 `timeoutCallback`, 96/4724 `shouldUseTurboAnimatedModule`, 96/2026). Structuring leaves an arm behind when a branch only skips code earlier passes folded away. New `EmptyIfArmRegionPass` (runs after `TrailingReturnRegionPass`): `if (c) {} else {X}` becomes `if (!c) {X}`, `if (c) {X} else {}` becomes `if (c) {X}`, and `if (c) {}` is dropped when `c` has no side effect. An arm counts as empty exactly as `RegionPrinter._emit_block` decides (a definition no reader folded away is a line of output). A first version based on `is_inert_block` left 83 empty `else`s in 98. Tests: `tests/test_empty_if_arm.py` (+ three `tests/data/empty_*.hasm`). Side effect: `if (A) {} else if (B) {X}` now prints nested (F-145).
- **F-33 A member read inlined across a `try` boundary** (resolved; 98/13768; wrong output, it showed up as an empty `try { } catch`). A value defined inside a `try` range and read after it was inlined into the reader, so the access that can throw ran outside the `try`. `HermesAnalysis.crosses_try_boundary(state)` (definition inside an exception handler range the current instruction is outside of) makes `get_register_expression` keep the register for any value containing a `MemberExpression`. Generator bodies are exempt (the synthetic `try` around them); `DispatchStage` sets `analysis.generator_body`. Test: `tests/test_try_boundary_member_read.py` (+ `tests/data/try_member_read_98_13768.hasm`). 
- **F-32 Extra parentheses around a ternary test** (resolved; printer only). `ExpressionPrinter._visit_test` groups the test of `? :` only when it is itself a ternary, an assignment or a sequence; comparisons, `in`, `&&`, `||`, `??` bind tighter. `(a == null) ? x : y` is now `a == null ? x : y`; a ternary as an operand keeps its parentheses. 499 files changed in 96 and 650 in 98, `goto` and `pathdefs` unchanged. Tests: `tests/test_ternary_test_parens.py`; 8 test files and 12 goldens moved to the new form.
- **F-31 (part) Register copies nothing reads** (resolved in part; 96/1982 `checkIfSnapshotChanged`, 96/12298 `populateParams`). `DeadMovEliminationPass` only removes a copy that is overwritten later in the same sequence; Hermes' allocator also leaves copies that are simply never read (a `Mov r0, r2` in front of a `try`). `DeadUndefinedStorePass` (which already has a backward liveness over the CFG) now also takes `rN = rM;` / `rN = paramM;`. Three things keep a copy: (1) its register holds a parameter (`LoadParam` writes it): reads print as `paramN`, so the liveness cannot see them (96/4846 `r10 = r14` feeds `param3` in the next iteration); (2) a read in an instruction made after the flow snapshot, e.g. a tail merge's copy `Mov r16, r18` whose original is gone (96/4939); (3) the usual region-held reads. The pass now also takes its blocks from the region tree itself, because `graph.blocks()` can miss some. Side effect: 96/12298's `else { r1 = param2; if (!param2) ... }` becomes `else if (!param2)`. Measured: 59 files in 96 (140 lines removed), 34 in 98 (52 lines), `goto` and `pathdefs` unchanged. Tests: `tests/test_dead_register_copy.py` (+ three `tests/data/dead_copy_*.hasm`).
- **F-146 An object made by `new` was evaluated once per read** (resolved; 96/1163 `PlatformColor`, 96/15130 `tag`; it was wrong output). `new Array(n)` (a rest parameter, `CreateThis`/`Construct`/`SelectObject`) was inlined into its readers: the fill loop printed `new Array(r5)[r0] = arguments[r0]`, a fresh array per iteration, and the result held another; in `tag` the array stored in the environment and the array the loop filled were two objects. `get_register_expression` now keeps a `NewExpression` in its register when the read sits in a loop the definition is outside of (`HermesAnalysis.read_enters_loop`) or when the scratch pass of `OpcodeDispatcher` says the definition prints anyway (`printed_definitions`), so an earlier read does not inline what a later one pins. `Mov` of a register that holds a `new` is an alias of it, not a second `new`. A single read still inlines (`r0[0] = new Map()`). Measured: 180 functions in 96 (and 2 in 98) printed `new X(...)[i] = ...` and now none (one `new URLSearchParams()[r2]` is a different shape, F-147); files changed 222 in 96 and 60 in 98, `goto` 299 to 298 in 96. Tests: `tests/test_new_object_identity.py` (+ `tests/data/new_object_identity_96_1163.hasm`, `new_object_stored_then_filled_96_15130.hasm`); goldens 15130, 15155, 15159, 15160 regenerated.
- **F-147 A `new` object read twice printed as several objects** (resolved; 96/4138 `createSearchParams`, 98/10541, 98/158; it was wrong output). The `SelectObject` value is the `NewExpression` itself; the first read inlined it and the second read inlined a copy (`new URLSearchParams()[r2].url = p; ... return new URLSearchParams()`, `new Image().onerror = f; new Image().onload = g`). F-146 only covered a read inside a loop. `get_register_expression` now pins a `NewExpression` on its second read (the branch for a value already read once); the scratch pass records the definition as printed, so the first read of the real pass keeps the register too. A single read still inlines. Measured: 6 files changed in 96 and 8 in 98, only these shapes, `goto` and `pathdefs` unchanged. Test: `tests/test_new_object_identity.py::test_a_new_object_read_three_times_is_one_object` (+ `tests/data/new_object_read_three_times_96_4138.hasm`; the constructor comes from the global object so that `SelectObject` sees a `NewExpression` as in a whole bundle).
- **F-137 `undefined` folded into a test was missing at a join** (resolved; 98/9611 `dt`; it was wrong output: `r3.size = r4` where `r4` must be `undefined`). `LoadConstUndefined r4` was consumed by `JStrictEqual r4, r8` (the test took the constant), and the arm that jumps over `r4 = <closure>` reaches `PutOwnBySlotIdx r3, r4` with `r4` still `undefined`. The join guard (three or more paths) answers a read with `rN` and left every earlier write to a fold or to `UnfoldedMergeRepairPass`; nothing printed the folded constant, so `rN` held the stale `highWaterMark`. The guard now calls `_restore_folded_constants`: earlier `undefined` definitions of the register that were folded are printed again (they ran in the bytecode; `DeadUndefinedStorePass` drops one nothing reads). Other literals are not restored: doing it for every literal broke the `page`/`retries` default folds (98/9490 printed `console.log(200, r8, 1)`). Measured: 3 files changed in 96 and 3 in 98, each only one added `rN = undefined;`, `goto`/`pathdefs` unchanged; 98/9611 still has a `goto` (F-04/F-10 cluster). Test: `tests/test_join_folded_undefined.py` (+ `tests/data/join_folded_undefined_98_9611.hasm`).
- **F-03 `maybeSwapComponents`** (closed, no change of its own; 96/9150). The pattern (two early `return param1` exits and a swap behind an `||`-style join) was fixed with the shared-exit work (F-113 to F-119). Both exits are one `else { return param1; }` and the swap is under the combined test; the copy `r0 = [...param1]` that the swap writes into is the returned array. Test: `tests/test_shared_return_exit.py`.
- **F-04 `parseScaleX` goto** (closed, no change of its own; 96/9118). After the wrong callee was fixed (F-111) the remaining `if (r0) goto label_44` is gone: the output is `if (len === 1 && callee(...)) { ... r0 = r1 } else { r0 = [] }; return r0`, found goto-free in the 2026-10-25 full run. Test: `tests/test_shared_tail_conditions.py::test_the_guard_with_an_empty_else_is_one_if_without_a_goto`.

- **F-149 Loop whose latch leaves through a `return`/`throw` kept a bare `break`** (resolved; 96/11086 `useHandler`, 96/1595, 96/11310, 96/7236, 98/9880; it was wrong output: `break` ran the code after the loop's `throw` instead of the other exit). In `do { ...; if (done) break; ... } while (c); throw ...` the latch's own way out is a `return`/`throw` block while one break leaves the loop elsewhere. LoopBreakStructurer now (a) lets such a bottom-tested latch be a conversion candidate (`_latch_exit_is_terminal`: the latch's single exit is a one-predecessor `return`/`throw` and exactly one other exit edge leaves the loop, so it becomes the `break`; several exits keep the old shape, 96/2052 `throwException` got `goto`s otherwise) and (b) refuses a bare `break` to a merge block that the latch's terminal exit cannot reach (`_is_loops_own_merge_block`, `_reaches_forward`; limited to terminal exits, a conditional exit made 96/1793 `describeNativeComponentFrame` print a `goto`). Measured: 6 files changed in 96 and 5 in 98; `goto` files 96 298 -> 298, 98 335 -> 334 (98/9880 `finish` lost its three); `recomputePluginOrdering` (96/1828, 2321, 98/2493) now throws inside the loop and uses `continue loop_2` where the old `break` fell into the `throw`. `pathdefs` "worse" rows are for-in headers and loop-assigned reads (false positives). Tests: `tests/test_loop_latch_terminal_exit.py` (+ `tests/data/loop_latch_throw_exit_96_11086.hasm`, `loop_latch_return_exit_98_9880.hasm`), `tests/test_guard_exit_region.py` (98/8982 `checkEqual` now `for (const r9 in r10)`).

- **F-140 (part) A folded ternary was copied into tests after its register changed** (resolved; 96/1595 `deepDiffer`; wrong output: `typeof (r5 === undefined ? -1 : arguments[2])` read the `r5` that `r5 = arguments[3]` had since replaced). `ConditionalExpressionRegionPass` hands every reader of the arm's value a copy of the ternary, or the register where the ternary's test was reassigned in between (`reader_value`), but `repoint_references` gave terminators and region conditions the ternary unconditionally. They now ask the same `reader_value` for the instruction whose branch they are (a terminator: its instruction; an `if` region: the last instruction before it, `_preceding_reader`). Measured: 5 files changed in 96 and 10 in 98 (tests such as `(r6.tabBarPosition !== undefined ? ... : "bottom") === "top"` print `r11 === "top"`, the register that holds the merge; 96/3672 and 98/9955 `set` read `r7`/`r8` instead of the stale `(r0 ? param1 : null)`); `goto` 298/334 unchanged, `pathdefs` 96 460 -> 459 (one better, none worse). Test: `tests/test_folded_ternary_stale_test.py` (+ `tests/data/folded_ternary_stale_test_96_1595.hasm`).

## Appendix: `goto` history per change (up to F-123)

Recorded during the round. `pathdefs` came from a survey tool that is not in the repository and was measured only twice (160 / 193 at the start); `n/a` marks values that were not recorded and cannot be reconstructed. Current measurements are in `FINDINGS.md`.

| Date | goto 96 | goto 98 | pathdefs 96 | pathdefs 98 | Tests |
|------|---------|---------|-------------|-------------|-------|
| 2026-10-16 (start of round) | 417       | 413       | 160           | 193           | 954 passed |
| 2026-10-17            | 396       | 402       | 160           | 193           | 957 passed |
| 2026-10-17 (F-01/F-02)| 396       | 400       | n/a     | n/a     | 985 passed |
| 2026-10-18 (F-10 partial)| 383      | 392       | n/a     | n/a     | 987 passed |
| 2026-10-18 (F-114)    | 383       | 385       | n/a     | n/a     | 988 passed |
| 2026-10-18 (F-115)    | 383       | 385       | n/a     | n/a     | 989 passed |
| 2026-10-18 (F-116)    | 383       | 385       | n/a     | n/a     | 990 passed |
| 2026-10-18 (F-117)    | 358       | 372       | n/a     | n/a     | 992 passed |
| 2026-10-19 (F-118)    | 359       | 372       | n/a     | n/a     | 994 passed |
| 2026-10-20 (F-119)    | 349       | 366       | n/a     | n/a     | 996 passed |
| 2026-10-20 (F-120)    | 337       | 359       | n/a     | n/a     | 998 passed |
| 2026-10-20 (F-121)    | 331       | 356       | n/a     | n/a     | 999 passed |
| 2026-10-20 (F-122)    | 330       | 355       | n/a     | n/a     | 1000 passed |
| 2026-10-20 (F-123)    | 314       | 335       | n/a     | n/a     | 1002 passed |