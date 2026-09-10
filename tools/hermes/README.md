# tools/hermes

Fetches official, per-bytecode-version `hermesc` binaries (via the
[`hermes-compiler`](https://www.npmjs.com/package/hermes-compiler) npm package)
and uses them to produce Hermes bytecode dumps — for testing/validating Hermes2JS output against the real compiler,
without installing a full react-native/Expo sandbox app.

Supported bytecode versions and their pinned npm versions live in
[`versions.json`](./versions.json) — that file is the single source of truth; scripts below read it rather than
hardcoding version lists.

## Install a compiler

```shell
chmod +x tools/hermes/lib/platform.sh
chmod +x tools/hermes/fetch_compiler.sh

./tools/hermes/fetch_compiler.sh 96
./tools/hermes/fetch_compiler.sh 98

## Verify install
find tools/hermes/compilers -name hermesc -type f
```

(the binary's path is platform-dependent — `osx-bin` / `linux64-bin` /
`win64-bin` — see `lib/platform.sh`, which both scripts below use so the platform logic lives in one place.)

## Usage — dump_bytecode.sh

```shell
chmod +x tools/hermes/lib/platform.sh
chmod +x tools/hermes/dump_bytecode.sh

./tools/hermes/compilers/96/node_modules/hermes-compiler/hermesc/osx-bin/hermesc hermesc -version
./tools/hermes/compilers/98/node_modules/hermes-compiler/hermesc/osx-bin/hermesc hermesc -version

## 96
./tools/hermes/dump_bytecode.sh \
    96 \
    apps/testy/96/index.android.bundle \
    apps/testy/96/output/hermesc-output.hdump

./tools/hermes/dump_bytecode.sh \
    96 \
    apps/testy/96/index.android.bundle \
    apps/testy/96/output/hermesc-output.hdump \
    --pretty

## 98
./tools/hermes/dump_bytecode.sh \
    98 \
    apps/testy/98/index.android.bundle \
    apps/testy/98/output/hermesc-output.hdump \
    --pretty
```

`dump_bytecode.sh` validates the requested version against `versions.json` and checks the compiler is installed before running —
if not, it tells you to run `fetch_compiler.sh <version>` first.

### direct usage of `hermesc`

```shell
find . -name "hermesc" -type f

HERMESC=tools/hermes/compilers/96/node_modules/hermes-compiler/hermesc/$(uname -s | grep -q Linux && echo linux64-bin || echo osx-bin)/hermesc

"$HERMESC" -version

"$HERMESC" \
    -b \
    -dump-bytecode \
    "apps/testy/96/index.android.bundle" > "apps/testy/96/output/hermesc-output.hdump"

"$HERMESC" \
    -b \
    -dump-bytecode \
    -pretty \
    "apps/testy/96/index.android.bundle" > "apps/testy/96/output/hermesc-output.hdump"
```

## Layout

```
tools/hermes/
├── README.md          — this file
├── versions.json       — bytecode-version → npm-version pins (source of truth)
├── fetch_compiler.sh   — installs a pinned hermesc for one bytecode version
├── dump_bytecode.sh    — runs hermesc -dump-bytecode against a bundle
├── lib/
│   └── platform.sh      — shared OS → hermesc-subdir detection, sourced by both scripts above
└── compilers/            — gitignored; populated by fetch_compiler.sh
    ├── 96/node_modules/hermes-compiler/...
    └── 98/node_modules/hermes-compiler/...
```

```shell
open "/Applications/Python 3.13/Install Certificates.command"

# hermes_disassembler/data/opcodes/<bytecode_version>.json
python tools/hermes/generate_opcode_tables.py 96 0.14.1
python tools/hermes/generate_opcode_tables.py 98 250829098.0.14

# hermes_disassembler/data/builtins/<bytecode_version>.json
python tools/hermes/generate_builtins_table.py 96 0.14.1
python tools/hermes/generate_builtins_table.py 98 250829098.0.14


```