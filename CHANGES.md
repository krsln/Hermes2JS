# Changes

## [Unreleased]

## [2026-09-15]

### Added

* Added native Hermes 96 and Hermes 98 bytecode disassembly support.
* Added a structured Hermes bytecode parser.
* Added `.hasm` disassembly output and section-based processing.
* Added parsing support for:

    * bytecode file headers
    * function headers
    * overflowed function headers
    * opcode definitions and operands
    * string tables
    * built-in tables
    * BigInt tables
    * literal buffers
    * object literal data
    * exception handler tables
    * switch tables
    * debug offsets
    * jump targets
* Added versioned Hermes opcode and built-in definitions.
* Added Hermes compiler tooling for:

    * fetching Hermes compiler versions
    * dumping bytecode with `hermesc`
    * generating opcode and built-in tables
    * managing supported Hermes versions
    * platform-specific compiler handling
* Added Makefile workflows for preparing and decompiling Hermes 96 and Hermes 98 fixtures.
* Added Hermes compiler oracle tests for validating parsed bytecode structures against `hermesc`.
* Added Hermes 96 and Hermes 98 disassembly and decompilation fixtures.
* Added golden-output regression tests for section-level decompilation.

### Changed

* Updated the disassembly workflow to use the in-repository `hermes_disassembler`.
* Reworked fixture processing around Hermes bytecode sections.
* Updated generated-output and fixture naming for Hermes 96/98 section-based workflows.
* Expanded bytecode version support with version-specific opcode and built-in data.

### Fixed

* Fixed parsing of regular, async, and generator function headers.
* Fixed handling of overflowed function headers.
* Fixed jump-target resolution.
* Fixed opcode handling for environment, call, object, property, generator, and control-flow operations.
* Fixed argument ordering for call operations.
* Fixed generator and loop reconstruction issues.
* Fixed handling of exception regions and `try` / `catch` / `finally` structures.
* Fixed redundant control-flow output in generated JavaScript.

### Testing

* Added end-to-end regression coverage for Hermes 96 and Hermes 98.
* Added tests for bytecode metadata and table parsing.
* Added tests for HASM generation and section splitting.
* Added tests comparing parsed disassembler structures with Hermes compiler output.
* Expanded golden-output coverage for Hermes bytecode decompilation.

## [2026-09-01]

### Added

* Added `pyproject.toml` project configuration.
* Added Python package metadata and pytest configuration.
* Added diagnostics for unresolved conditional branches and switch terminators.
* Added dedicated transformations for:

    * loop condition extraction
    * loop update detection
    * `for` induction-variable alias elimination
    * redundant loop jumps
    * loop-carried register handling
* Added region-level expression transformations for:

    * boolean `&&` / `||` chain folding
    * conditional / ternary expressions
    * nullish assignment (`??=`)
    * return-value resolution
    * throw-value resolution
* Added a compositional JavaScript printer architecture with:

    * `ExpressionPrinter`
    * `StatementPrinter`
    * `RegionPrinter`
    * `PrinterContext`
    * `ConditionCommentPrinter`
    * `PrinterVisitor`

### Changed

* Substantially improved CFG → Region → JavaScript reconstruction.
* Refined dominance, post-dominance, and loop analysis.
* Improved reconstruction of:

    * `while`
    * `do...while`
    * `for`
    * `for...of`
    * `for...in`
    * `break`
    * `continue`
    * labeled exits
    * nested loop exits
* Improved `try` / `catch` / `finally` reconstruction.
* Improved handling of fragmented Hermes exception ranges.
* Improved nested exception-region analysis.
* Improved `finally` wrapper detection.
* Improved matching of duplicated and inlined `finally` bodies.
* Improved register definition and value tracking.
* Added dead register-move elimination.
* Replaced the monolithic JavaScript printer with a compositional printer architecture.
* Improved opcode handler loading, validation, argument patterns, and register/value handling.
* Clarified the separation between Hermes2JS and the external `hermes-dec` disassembler.
* Moved `hermes-dec` from a vendored dependency to an externally fetched tool.

### Fixed

* Fixed incorrect reconstruction of complex loop control flow.
* Fixed incorrect handling of nested `try` / `catch` / `finally` structures.
* Fixed incorrect register resolution caused by linear bytecode-order processing.
* Fixed incorrect expression folding caused by insufficient identity and structural checks.
* Fixed incorrect relocation of statements around nested exception regions.
* Fixed incorrect handling of compiler-generated control-flow shapes.

### Testing

* Expanded JavaScript expected-output fixtures.
* Added bytecode sections covering complex control-flow scenarios.
* Added coverage for iterator and loop reconstruction.
* Added coverage for nested `try` / `catch` / `finally` scenarios.
* Expanded opcode-handler validation tests.
* Updated expected outputs for improved structural reconstruction.

## [2026-08-15]

### Changed

* Reorganized the project folder structure.
* Moved `dispatch`, `opcode`, and `parsing` into `frontend`.
* Moved `io` into `core/IO.py`.
* Renamed and reorganized analysis transforms.
* Improved handler and printer organization.
* Improved opcode catalog and opcode verification tests.
* Refined structurer implementations.

### Added

* Added raw JavaScript output files (`*_raw.js`).

### Improved

* Improved opcode handlers.
* Improved JavaScript printing.
* Improved structural transformation and region structuring.

## [2026-08-01]

### Added

* Added React Native test applications for generating Hermes bundles from different Hermes versions.
* Added Hermes 96 and Hermes 98 test bundles.
* Added disassembled and split Hermes sections for use as decompiler fixtures.
* Added `Terminator` abstraction.
* Added documentation for handler classes.

### Changed

* Reorganized the project structure.
* Moved region rendering into `emit/`.
* Reorganized region analysis under `analysis/`.
* Reconstructed opcode handlers.
* Renamed and reorganized scripts.

### Improved

* Improved logging.
* Improved `TryStructurer` and `SwitchStructurer`.
* Improved `Construct`, `SelectObject`, and `CallBuiltin` handlers.
* Improved `OpcodeEntry` and `OpcodeResult`.

## [2026-07-26]

### Changed

* Introduced the initial project folder structure.
