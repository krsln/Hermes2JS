# Findings

Open decompiler findings and the measurements that track them. Resolved findings are in
[`FINDINGS-archive.md`](FINDINGS-archive.md).

Examples are written `<bundle>/<function id>`; 96 and 98 are the two test bundles. Every finding has
an id (`F-n`), a status, an example function, a one-sentence symptom and, once fixed, the test that
guards it. Commit messages and tests refer to findings by id.

How to update:

1. Measure first (see [Measurements](#measurements)); add a row.
2. A finding that is still open stays here; a fixed one moves to `FINDINGS-archive.md` as a full
   entry (symptom, cause, fix, test, numbers) and is deleted from this file.
3. New findings take the next free id (the highest id in the archive plus one).

## Measurements

Tools are in `scripts/audit/` (see its `readme.md`). Both bundles are decompiled in full for every
row; a row is only added when all of its columns were measured on the same tree.

| Date | Change | goto 96 | goto 98 | pathdefs 96 | pathdefs 98 | Tests |
|------|--------|---------|---------|-------------|-------------|-------|
| 2026-10-16 | start of the round (`29c4aff`) | 417 | 413 | 461 | 699 | 954 passed |
| 2026-10-24 | after F-136 | 299 | 336 | 463 | 681 | 1019 passed |
| 2026-10-25 | after F-138 (join guard), F-144, F-141, F-33, F-32 | 299 | 335 | 462 | 681 | 1031 passed |
| 2026-10-25 | after F-31 (dead copies, part) | 299 | 335 | 462 | 682 | 1034 passed |
| 2026-10-25 | after F-146 (`new` identity) | 298 | 335 | 459 | 682 | 1037 passed |
| 2026-10-25 | after F-147 (`new` read twice) | 298 | 335 | 459 | 682 | 1038 passed |
| 2026-10-25 | after F-137 (folded `undefined` at a join) | 298 | 335 | 459 | 682 | 1039 passed |
| 2026-10-26 | after F-149 (loop latch with a terminal exit) | 298 | 334 | 460 | 683 | 1042 passed |
| 2026-10-26 | after F-140 (stale folded ternary in a test) | 298 | 334 | 459 | 683 | 1043 passed |
| 2026-10-26 | after F-140 (copy read on a path the write cannot reach) | 298 | 334 | 459 | 683 | 1044 passed |
| 2026-10-26 | after F-150 (merge repair and the other arm) | 298 | 334 | 457 | 683 | 1045 passed |
| 2026-10-26 | after F-151 (BooleanChain and the other arm) | 298 | 334 | 457 | 683 | 1045 passed |
| 2026-10-27 | after F-143 (dominator tree cached), 98 now WITH 98/2619 | 298 | 335 | 457 | 684 | 1046 passed |
| 2026-10-27 | after F-152 (case chain: same value only) | 298 | 335 | 456 | 684 | 1047 passed |
| 2026-10-28 | after F-154 (retries for a tree that lost a path; closes F-148) | 298 | 335 | 457 | 684 | 1049 passed |
| 2026-10-28 | after F-153 part (level 5: a copy of a shared tail per way in) | 298 | 335 | 457 | 684 | 1050 passed |
| 2026-10-28 | after F-10(a) (shared return of different constants) | 297 | 335 | 457 | 684 | 1050 passed |
| 2026-10-28 | after F-155 (an arm that runs into the branch target, in a retry) | 287 | 326 | 456 | 683 | 1052 passed |
| 2026-10-28 | after F-156 (try `return` beside a catch jump) | 287 | 326 | 456 | 683 | 1053 passed |
| 2026-10-29 | after F-157 (arm runs into the target, first attempt) | 284 | 325 | n/a | n/a | 1054 passed |
| 2026-10-29 | after F-158 (a `jmp` to a shared return takes the return along) | 278 | 317 | n/a | n/a | 1055 passed |
| 2026-10-29 | after F-159 (arm's last test jumps onto the tail, falls into a return) | 274 | 315 | n/a | n/a | 1056 passed |
| 2026-10-29 | after F-161 (merged test no longer a predecessor of a return copy) | 273 | 314 | n/a | n/a | 1057 passed |
| 2026-10-29 | after F-162 (own-value return copies, level 5) | 268 | 303 | n/a | n/a | 1059 passed |
| 2026-10-29 | after F-163 (an `if` arm's jump to the join is dropped) | 249 | 269 | n/a | n/a | 1060 passed |
| 2026-10-29 | after F-164 (try exit jump to an emptied finally copy; closes F-11) | 248 | 268 | n/a | n/a | 1061 passed |
| 2026-10-29 | after F-165 (try exit jump to an `if` join / out of an `if` arm) | 244 | 265 | n/a | n/a | 1062 passed |
| 2026-10-29 | after F-166 (`for-of` whose try covers only the body; break out of a top-tested loop) | 242 | 263 | n/a | n/a | 1064 passed |
| 2026-10-29 | after F-167 (iterator close copies inside a recognized `for-of`) | 242 | 263 | n/a | n/a | 1066 passed |
| 2026-10-30 | after F-168 (exits in the gaps of a merged try range) | 240 | 259 | n/a | n/a | 1068 passed |
| 2026-10-30 | after F-169 (short-circuit folds inside loop bodies) | 232 | 244 | n/a | n/a | 1071 passed |
| 2026-10-30 | after F-170 (arm with one private `return`, test past its first block) | 228 | 240 | n/a | n/a | 1074 passed |

- The 2026-10-25 to 2026-10-26 rows decompile 98 without 98/2619 (F-143: it stalled), so their 98
  columns are not exactly comparable with the 2026-10-27 row, which includes it (+1 `goto` file, +1
  `pathdefs`). F-32 is printer-only: it changed 499 files in 96 and 650 in
  98 and moved neither `goto` nor `pathdefs`. The F-31 row changed 59 files in 96 and 34 in 98, only by
  removing lines (plus the restructured 96/12298); its `pathdefs` +1 in 98 is 98/1753 `previousSibling`, where
  the removed `r5 = r6` is overwritten by the destructuring on the next line (audit noise).
- `goto`: number of functions whose output still contains `goto label_N`.
- `pathdefs`: number of functions with at least one register read that is not assigned on every path
  (`scripts/audit/definite_assignment.py`, piped through `cut -d: -f1 | sort -u | wc -l`). It is a
  rough check (for-of/for-in heads and switch arms give false positives), so compare rows, not
  absolute values.
- Both rows were measured with the same scripts: the first by checking out `29c4aff` and decompiling
  both bundles in full, the second on the current tree. Reading the `pathdefs` change: the
  per-file comparison (`compare_outputs.py`) finds about as many files with more unassigned reads
  (96: 39, 98: 71) as with fewer (96: 38, 98: 61), so the check is noise-dominated at this level (not triaged per file); the totals are flat for 96 (+2) and
  better for 98 (-18).
- Older notes recorded `pathdefs` of 160 (96) and 193 (98) from a survey tool that is not in the
  repository; those numbers are not comparable with this column and were dropped. The per-change
  history of the `goto` count up to F-123 is in the archive appendix.

## Open: wrong or misleading output

The output is wrong or misleading. Because it contains no `goto` it does not show in the `goto` count.

- **F-138 `getComponentNameFromType` (partly fixed).** 96/1801, 96/2294, 98/2477. The main cause (a
  computed value inlined into copies on other arms) is fixed, see the archive. Left: (a) inside the
  `ForwardRef` arm `BooleanChainRegionPass` copies `r2.displayName || r1.name || ""` into a test that
  stands after `r1`/`r2` were redefined: two garbage lines in 96/1801 and 96/2294 (a fix that checked
  the operands for redefinition produced unassigned reads in 96/2200, 98/2930 and 98/2614 and was
  dropped); (b) the last `Mov r1, r3; Ret r1` is a join of two paths and prints `return r1`, which is
  wrong when `displayName` is truthy (widening the join guard to two paths broke 17 tests); (c) four
  `goto`s remain (F-10 cluster).
- **F-139 Messy `for-in` (partly fixed).** 96/1339 `parseDropShadow`. The null-guard scaffold is gone
  (F-144); what is left are loop-carried `Mov`s in the for-in header that need copy propagation. About
  18 functions in 96 and 20 in 98 still print an unrecognized `HermesPropertyIterator`.
- **F-140 `deepDiffer` (partly fixed).** 96/1595. The loop shape (F-149), the stale
  `typeof (r5 === undefined ? ...)` and the unassigned `r17` (both in the archive) are done. Left:
  the pair `r5 = arguments[2]; r1 = r5 === undefined ? -1 : arguments[2]` (correct but noisy).
- **F-151 Doubled left operand in a boolean chain (partly fixed).** `r3 = null !== r7 && (null !== r7 &&
  null !== r7.memoizedState)` (96/2108, 96/2088, 96/4422 `accessible`, 98/2639 and others; about 7 files
  in 96 and 8 in 98). Cause (traced on 96/2108): a source expression that occurs twice
  (`r7 !== null && r7.memoizedState !== null` in two statements) folds twice, and the second fold's
  structural repoint of its arm value finds the FIRST fold's right operand (`B` inside `A && B`) and
  wraps it again. Tried and rejected: sealing a fold's result so that a look-alike is not matched as its
  right operand: it removed the doubled heads in 14 files but dropped terms in `X || Y || Z` chains
  (98/3783 `_performTransitionSideEffects` lost two alternatives), because those later repoints are the
  intended structural copies. A real fix has to tell a copy of the arm value (a `Mov`) from an identical
  second source expression, e.g. by the reader's address relative to the arm.

- **F-153 A join block printed in only one arm (98/10128 open; 98/2216 fixed in part; 96/15065 open).**
  Bytecode of 2216: `if (r5 == null) goto J; ... r3 = null; if (startsWith) goto END; ...; if (includes)
  goto J; r5 = "file://" + r7; J: r3 = r5; END: store r3`. `J` has three ways in. Faults:
  (a) `_DominanceIfBuilder._convert` makes `J` the `else` arm of the first test (`has_else`, since the
  post-dominator `END` is a later block) although the `then` arm falls and jumps into `J` as well; the
  arm's flow into `J` is dropped (`drop_scan`: edges 0x56->0x96, 0x8e->0x96).
  (b) `_CompoundConditionFolder._absorb_residual_conditional` drops a jump that lands INSIDE the arm it
  builds: 96/15065 (golden, `labeledBreakTest`) prints `if (r5 !== 1) log else if (j === 1) break` and loses
  the `log` on `r5 === 1 && j !== 1` (bytecode: the `j === 1` test falls through into the `log` block). The
  golden file records the wrong output.
  (c) The frontend inlines `Mov r3, r5` into the read after the join (`r4[5] = r5`) although another path
  reaches it with `r3 = null`.
  Direct guards for (a) and (b) moved 26 (96) / 20 (98) more `goto` lines into other functions (20 of them
  had no lost edge before) and were NOT kept. Done for 2216 (resolved in the archive entry F-153a): retry level 5
  copies a small tail per way in. Open: 98/10128 `interpolate` (the tail `Mov r14, r17; if (r17 <= r12) goto C` has
  three ways in; the `else` arm of `x < r9` ends without running on into it, so a clamped `x` never reaches the range
  test; the `identity` tests jump to the final `return r7`, whose register holds a different non-constant value per path,
  so `SharedReturnDuplicationCfgPass` refuses to copy it and `duplicated_returns` stays off). Tried: level 5 for a tail
  that ends in a test (split the test off, one copy per way in): the first two ranges structure right, the later part gets
  `goto`s. Tried (2026-10-28): the F-155 clause (`_arm_falls_into`) with the retry flag instead of `duplicated_returns`:
  `flow_audit` then reports 0 lost paths and no `goto`, but the output is WRONG (the `identity` path falls into the code
  after the `if` and `r7 = r8` overwrites it), so it was not kept: that clause is only exact when the arm's other exits are
  real `return`s. Tried: letting a jumper that sets the register itself (`Mov r7, r10; if (...) goto RET`) be copied
  whatever the other paths hold: 3 tests broke (98/1871, 98/2216 among them). Next idea: copy `Ret r7` for those jumpers
  only (exact: each copy returns the value its own block set) and leave the closing return alone; the lost-path check
  cannot see the second fault (it only asks whether the target is reachable at all), 96/15065 and 98/9456 `labeledBreakTest` (b: the
  fall-through test into a shared `log` block; their goldens are wrong).

- **F-142 `drop_scan` candidates (refreshed 2026-10-28, both bundles).** `drop_scan.py --report` now lists
  3 goto-free functions in 96 and 4 in 98. 96/1339 `parseDropShadow`, 96/2103 `commitDeletionEffectsOnFiber`
  are false positives (the lost edge goes to a bare `return undefined`/`return r0` where `r0` is `undefined`; falling
  off the end is the same). 96/6029 `_anon_0_` is an async state machine (the edge is a resume; the printed
  `if/else` with `await` reads right). 98/9535 is a false positive; 98/2594 is a `Catch` edge, probably one too.
  98/2216 `getScriptURL` was real (F-153a, fixed); 98/10128 is real and open (F-153). Fixed since the first report: 96/1595, 96/11086 (F-149),
  96/2602 (F-148, closed by F-154), 98/7358 (F-152), 98/12551 and 98/4047 (F-154).

- **F-10 Conditional jump to an exit block.** `if (c) goto finalReturn`: conditional jumps to a shared
  `return` block (examples: 96/2019 `mountDeferredValueImpl`, part of 98/11891). Partly resolved
  (F-113, F-114, F-115, F-117, F-119, and (a) below). Left: (b) jumps whose target is not a `return`
  (sibling region, `none` terminator). (a) 96/11046 `areDependenciesEqual` is done: see the archive.
- **F-12 `await`/`yield` dispatch and 98 generator opcodes.** 96/12207 `_anon_0`. Without a batch
  table the dispatch cannot be resolved; some generator opcodes are missing in 98.
- **F-13 Loops with two latches.** The "expected exactly one latch" warning: 13 functions in 96, 22 in 98.
- **F-14 `for-of` generator unrolling.** The loop stays as an unrolled generator.
- **F-15 Shared tail returns.** 96/10216.
- **F-16 A constant set-up read by `Ret`.** 96/150 `ve`: `r0 = undefined` in the set-up is read by
  `Ret r0`, so the first `typeof` test cannot join the `||` chain (the output is correct but nested).
- **F-17 `getStateForAction`.** 96/7152: large and already `goto`-ful; its `pathdefs` flag is accepted.
  Skip it unless it is handled on its own.
- **F-18 Long tail of "different region" gotos.** About 230 functions with no single common cause;
  the cheapest start is the small ones (one `goto`, under 26 lines: 79 functions).

## Open: readability

- **F-30** Loop condition `i < r8; r8 = r8.length`.
- **F-31 Redundant copies (partly fixed).** `r2 = r3`, `r1 = {...}; r0 = r1`. Copies of a register or a
  parameter that nothing reads are now removed on every path (see the archive). Left: about 620 (96) / 376
  (98) lines `rN = <reg/param>` that no read names, almost all of them the `LoadParam` line itself
  (`r2 = param2;`, about 4000 such lines in 96): reads print as `paramN`, so the liveness cannot tell the
  line is dead and a write to the same register (`r10 = r14` in 96/4846) must stay. Also left: copies that
  are read once (`r1 = {...}; r0 = r1`), which need copy propagation (with F-139).
- **F-145** `if (A) { } else if (B) { X }` now prints as the nested `if (!A) { if (B) { X } }`; it could be
  merged into `if (!A && B)`.