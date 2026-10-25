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

- **F-03 `maybeSwapComponents`.** A pattern like 96/9150. See `tests/test_shared_return_exit.py`.
  96/9150 itself decompiles correctly now (no `goto`, both `return param1`, swap path right); close
  this if no similar example turns up.
- **F-04 `parseScaleX` goto.** 96/9118: the wrong callee was fixed (F-111); what remains is
  `if (r0) goto label_44` ("target IS a sibling in the same region"). The set-up register
  (`r1 = 0`) is also read at the join, so folding cannot drop it.
- **F-137 `dt` writes a value that should be `undefined`.** 98/9611: `r3.size = r4` where `r4` must be
  `undefined` on that path; a `goto` remains.
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
- **F-140 `deepDiffer`.** 96/1595: several structural problems in one function.
- **F-142 `drop_scan` candidates not triaged yet (96).** 96/1926 `updateFromMap`, 96/2103
  `commitDeletionEffectsOnFiber`, 96/2602 `insertOrAppendPlacementNode`, 96/4152, 96/2811,
  96/6029 `_anon_0_`, 96/7599 `getStateFromPath`, 96/9820, 96/9821 and 96/9831 (component lifecycle),
  96/11086 `useHandler`. Run `drop_scan.py --report` for the current list. The 98 scan has not been
  read yet.

## Open: goto clusters

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