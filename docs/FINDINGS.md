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
| 2026-10-30 | after F-171 (a lossless retry with a `goto` beats a first attempt that loses a path) | 229 | 242 | n/a | n/a | 1076 passed |
| 2026-10-30 | after F-172 (a bottom-tested loop's header branch is an ordinary in-body test) | 217 | 231 | n/a | n/a | 1078 passed |
| 2026-10-31 | after F-173 (a repoint that doubles a pure chain head keeps one) | 217 | 231 | n/a | n/a | 1080 passed |
| 2026-10-31 | after F-174 (a shared `throw` of up to 16 instructions is copied per jumper) | 215 | 230 | n/a | n/a | 1082 passed |
| 2026-10-31 | after F-175 (a parameter's register rewritten in a loop keeps its name) | 215 | 230 | n/a | n/a | 1083 passed |
| 2026-10-31 | after F-176 (a property read before a loop and rewritten in it keeps its register) | 215 | 230 | n/a | n/a | 1085 passed |
| 2026-10-31 | after F-177 (a `case` that runs into the next one prints no `break`) | 215 | 230 | n/a | n/a | 1087 passed |
| 2026-10-31 | after F-178 (the lost-edge scan knows a `return undefined` that carries its `Ret` statement) | 215 | 230 | n/a | n/a | 1088 passed |
| 2026-10-31 | after F-179 (a `case` jump left to a `switch` that did not come is restored as `\|\|`) | 215 | 230 | n/a | n/a | 1090 passed |
| 2026-10-31 | after F-180 (the tests after a restored `case` jump join the same `\|\|`) | 198 | 218 | n/a | n/a | 1090 passed |
| 2026-10-31 | after F-181 (an arm that re-tests the same constant makes the branch target the join) | 193 | 217 | n/a | n/a | 1092 passed |
| 2026-11-01 | after F-182 (a guard that jumps past a `throw` inside a freshly built arm folds) | 193 | 213 | n/a | n/a | 1096 passed |
| 2026-11-01 | after F-183 (a `typeof` test whose arm's own test falls into its target) | 193 | 211 | n/a | n/a | 1098 passed |
| 2026-11-01 | after F-185 (a test jumping to the then arm's entry joins its condition as `\|\|`) | 193 | 210 | n/a | n/a | 1101 passed |
| 2026-11-01 | after F-186 (a shared tail the test skips by jumping to the block behind it) | 192 | 207 | n/a | n/a | 1104 passed |
| 2026-11-01 | after F-187 (an arm that ends in a `Jmp` to the join runs into it) | 190 | 202 | n/a | n/a | 1105 passed |
| 2026-11-02 | after F-188 (a test the try body and the catch both reach ends the catch) | 189 | 201 | n/a | n/a | 1106 passed |
| 2026-11-02 | after F-189 (a longer shared `return` only jumps reach is copied on the last rung) | 188 | 198 | n/a | n/a | 1108 passed |
| 2026-11-02 | after F-191 (a for-of over a parameter is recognized) | 182 | 190 | n/a | n/a | 1110 passed |
| 2026-11-02 | after F-192 (a for-of binding the body assigns is a `let`) | 182 | 190 | n/a | n/a | 1110 passed |
| 2026-11-02 | after F-193 (a shared tail is copied in a function with a `try` when nothing it touches is protected) | 173 | 189 | n/a | n/a | 1112 passed |
| 2026-11-02 | after F-194 (the later of two tests that jump to one short tail gets its own copy, last rung) | 171 | 184 | n/a | n/a | 1114 passed |
| 2026-11-03 | after F-195 (a shared tail inside a try range is copied when its ways in are under the same handlers) | 167 | 179 | n/a | n/a | 1116 passed |
| 2026-11-03 | after F-196 (the later of two tests that jump to a `return`/`throw` tail gets its own copy, last rung) | 166 | 177 | n/a | n/a | 1118 passed |
| 2026-11-03 | after F-197 (a guard whose `return` exit no sequence holds becomes `if (c) { return }`) | 165 | 172 | n/a | n/a | 1119 passed |
| 2026-11-03 | after F-198 (a `break` to the join behind a loop exit that only jumps on) | 165 | 171 | n/a | n/a | 1120 passed |
| 2026-11-03 | after F-200 (`if (c) continue` in a loop with no test and no update) | 161 | 167 | n/a | n/a | 1122 passed |
| 2026-11-03 | after F-202 (a guard's function-ending tail taken from the end of a loop body / `else` arm) | 158 | 164 | n/a | n/a | 1124 passed |
| 2026-11-03 | after F-203 (the crossed `a \|\| b` fold rematerializes an environment load END reads) | 158 | 161 | n/a | n/a | 1125 passed |
| 2026-11-04 | after F-204 (a suspend point whose resume pair is followed by `Mov`s; `SaveGenerator` is kept) | 154 | 161 | n/a | n/a | 1127 passed |
| 2026-11-04 | after F-205 (a resume guard with the rest of the loop body behind it; the yield is what the `Ret` returns) | 153 | 161 | n/a | n/a | 1130 passed |
| 2026-11-05 | after F-199 (`if (c) goto T; REST` at the end of an arm, T what runs when the arm is done) | 150 | 159 | n/a | n/a | 1132 passed |

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
- **F-151 Doubled left operand in a boolean chain (resolved as F-173, see the archive).**

- **F-179 A `case`-chain test that does not become a `switch` lost its jump (resolved, see the archive).**
- **F-184 `IfTailMergeRegionPass` hoists the `return` of a block a raw guard still jumps to (latent; 98/6630 and 96/13834 `getInitialURL` once a guard made the arms share a join).** The two arms of an `if` end in `r1 = X; return r1`; the pass moves the common `return r1` behind the `if`. When the else arm's last block is also the target of a raw `if (c) goto RET` (one predecessor), `GuardExitRegionPass` later moves that block into the guard's `if` WITHOUT its `return`, so the guard falls on into the code after it (`if (r3) { r1 = window.location.href }` followed by the native path; the bytecode returns there). Seen only after widening F-183's rule to every constant comparison (not merged). Skipping the hoist for such a block (`predecessors == [one raw jumper]`) is right but restyled 48 files in 96 / 58 in 98 (half of them without any `goto`: shared tails became repeated `r3 = ...; return r3`, 96/437 and 98/12590 `read` count one more unassigned read); running `GuardExitRegionPass` before the pass broke `test_arm_runs_into_shared_return`. A fix has to let the moved block keep (or get back) its `return`: `tail_origins` already records the original instruction of the hoisted copy.
- **F-201 `if (c) goto T` leaving a nested `if` for code only the other path may run (98/2330 `accumulateDifferences`).** Bytecode: `if (X) { A; if (r16 != null) goto 0x111 } REST; 0x111: ...` inside a loop: the guard sits in the then-arm of `if (X)`, its fall-through (`REST`: the spread/push block that jumps back to the header) lies after that `if` in the OUTER sequence, and the target 0x111 follows `REST`. `_DominanceIfBuilder._convert` finds the guard is the last item of its sequence (`then_start >= len(region.children)`, line ~227) and gives up. Structuring needs the join of `if (X)` split (`if (X && c) { T } else { REST }` with A before it) or a flag; no local rule does it.
- **F-190 An `||` whose second test sits behind statements of the else arm keeps a `goto` into the then arm (98/13588 `get`, 98/10102, 98/9882 and more of the `if (r) goto L;` cluster).** `if (kind !== 1) goto SYNC; r4 = env[1]; if (r4 === undefined) goto SYNC; ...; SYNC: ...`. Both tests jump to the then arm's entry (`if (A || B) { SYNC } else { ... }`), but `B` reads `r4`, set by a statement of the else arm in front of it, so F-185's `_fold_into_sibling_condition` (no printing statement in front) does not apply, and the target is not a lone `return` the copy passes could duplicate (it runs on into the closing `return`). Options: fold a pure load into the condition (`(r4 = env[1]) === undefined`, needs an assignment expression the register printer can keep), or duplicate the small target for the second jump. F-194 solved the part where the target is a short tail running on into a join (98/13588 `get`, 98/9882, 98/12776, 98/5905, 96/13245, 96/2611) by copying it for the later test; what is left is the part where the tail is too long or has several ways in, and the fold of a pure load into the condition. F-203 did the fold for the crossed form when the later code reads the loaded register again and the load is an environment slot (98/2654 `requestUpdateLane`, 98/10102 `start`, 98/10753, 98/13588 `get` now one `||`); loads of other kinds (a property of a register that END changes) are still open. Tried and dropped (not in the code): letting `_fold_pure_setup` ignore the handler check when every path from the exits rewrites the register before the `try` (fixes 98/2676 `flushSpawnedWork`, 3 files goto-free, 96 6259 to 6257); with several setup registers it miscompiled 96/7898 (join reads an arm's inlined load), and even with one register it made 98/2673 `commitRoot` lose a `throw r0` and wrap the whole body in one `try`/`finally` (the structurer mishandles the shared throw block once the fold exists; the old output needed retry level 5). Needs that structurer bug fixed first.
- **F-10 Conditional jump to an exit block.** `if (c) goto finalReturn`: conditional jumps to a shared
  `return` block (examples: 96/2019 `mountDeferredValueImpl`, part of 98/11891). Partly resolved
  (F-113, F-114, F-115, F-117, F-119, and (a) below). Left: (b) jumps whose target is not a `return`
  (sibling region, `none` terminator); the shared-`throw` size part is F-174 (archive). (a) 96/11046 `areDependenciesEqual` is done: see the archive.
- **F-12 `await`/`yield` dispatch and 98 generator opcodes (partly fixed).** 96/12207 `_anon_0`. Without a batch
  table the dispatch cannot be resolved; some generator opcodes are missing in 98. F-204 and F-205 (archive)
  fold the resume pair when `Mov`s follow it and when the guard has the rest of a loop body behind it: 96 prints
  `__resumeIsReturn` in 7 functions now (31 before F-204), 98 in none. Left in 96, not triaged: 3625
  `generateValues`, 3628 `generateEntries`, 12653 (no `goto`); 14482, 14867, 8059 (one `goto` each), 14945 (two).
  Also left, not about the guard: a resumed value read through an inlined expression prints as `await yield`
  (96/12207: `if (await yield)`, `{ "src": await yield }`), because only a read of the register by name makes the
  fold bind it.
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
  parameter that nothing reads are now removed on every path (see the archive). The loop-carried parameter copies that were really wrong output are F-175 (archive). Left: about 620 (96) / 376
  (98) lines `rN = <reg/param>` that no read names, almost all of them the `LoadParam` line itself
  (`r2 = param2;`, about 4000 such lines in 96): reads print as `paramN`, so the liveness cannot tell the
  line is dead and a write to the same register (`r10 = r14` in 96/4846) must stay. Also left: copies that
  are read once (`r1 = {...}; r0 = r1`), which need copy propagation (with F-139).
- **F-145** `if (A) { } else if (B) { X }` now prints as the nested `if (!A) { if (B) { X } }`; it could be
  merged into `if (!A && B)`.