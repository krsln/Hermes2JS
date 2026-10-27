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

- The 2026-10-25 row decompiles 98 without 98/2619 (F-143: it stalls), so its 98 columns are not
  exactly comparable with the row above. F-32 is printer-only: it changed 499 files in 96 and 650 in
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

- **F-148 `insertOrAppendPlacementNode` loses an edge (96/2602).** The `6 === tag` test's edge to the
  shared body is dropped silently (`drop_scan`). Cause: the case-chain exemption in the compound folder
  (`if_structurer/_compound_folder.py`, `_case_chain_has_two_bodies`) treats the chain as a switch and
  the shared body then has no printed path. Three attempts were reverted (removing the exemption broke 5
  switch tests; excluding Return blocks broke `defaultPort`; excluding blocks with non-test predecessors
  broke 5 switch tests). No safe fix yet.
- **F-142 `drop_scan` candidates (96 triaged, 98 not scanned yet).** The 2026-10-26 report of 96 lists
  seven goto-free functions with a lost edge. Triage: 96/1339 `parseDropShadow`, 96/2103
  `commitDeletionEffectsOnFiber` and 96/7599 `getStateFromPath` are false positives (the lost edge
  goes to a bare `return undefined`/`return r0` where `r0` is `undefined`; the printed `if` without an
  `else` falls off the end, same result). 96/6029 `_anon_0_` is an async state machine (the edge is a
  `SaveGenerator`/`ResumeGenerator` resume; the printed `if/else` with `await` reads right).
  96/1595 and 96/11086 were fixed by F-149 (that report predates it). 96/2602 is F-148 (real).
  Open: run `drop_scan.py` on 98 and read it; re-run 96 to refresh the list.

- **F-10 Conditional jump to an exit block.** `if (c) goto finalReturn`: conditional jumps to a shared
  `return` block (examples: 96/2019 `mountDeferredValueImpl`, part of 98/11891). Partly resolved
  (F-113, F-114, F-115, F-117, F-119). Left: (a) 96/11046, where the return register carries a
  different value per path (a phi) and stays a `goto`; (b) jumps whose target is not a `return`
  (sibling region, `none` terminator).
- **F-11 `goto` inside `try/finally`.** 98/2007 `preprocessException`, 98/10013 `flush`, 96/840. The
  jump crosses the `finally` boundary.
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
- **F-143 Slow function.** 98/2619 takes minutes to decompile (a full 98 run stalls there).

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