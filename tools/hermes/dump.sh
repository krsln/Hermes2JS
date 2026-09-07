#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_ROOT="$SCRIPT_DIR"
COMPILERS_DIR="$HERMES_ROOT/compilers"

usage() {
    echo "Usage:"
    echo "  $0 <hermes-version> <input-file> [output-file]"
    echo
    echo "Options:"
    echo "  --pretty    Generate pretty Hermes bytecode dump"
    echo
    echo "Examples:"
    echo "  $0 96 apps/testy/96/index.android.bundle"
    echo "  $0 96 apps/testy/96/index.android.bundle output.hasm"
    echo "  $0 98 apps/testy/98/index.android.bundle --pretty"
    exit 1
}

if [[ $# -lt 2 ]]; then
    usage
fi

VERSION="$1"
INPUT="$2"
OUTPUT=""
PRETTY=false

shift 2

while [[ $# -gt 0 ]]; do
    case "$1" in
        --pretty)
            PRETTY=true
            shift
            ;;
        *)
            if [[ -n "$OUTPUT" ]]; then
                echo "Error: Unexpected argument: $1" >&2
                usage
            fi

            OUTPUT="$1"
            shift
            ;;
    esac
done

COMPILER_DIR="$COMPILERS_DIR/$VERSION"
HERMESC="$COMPILER_DIR/node_modules/hermes-compiler/hermesc/osx-bin/hermesc"

if [[ ! -d "$COMPILER_DIR" ]]; then
    echo "Error: Hermes compiler directory not found:" >&2
    echo "  $COMPILER_DIR" >&2
    exit 1
fi

if [[ ! -x "$HERMESC" ]]; then
    echo "Error: hermesc not found:" >&2
    echo "  $HERMESC" >&2
    echo >&2
    echo "Install the compiler first:" >&2
    echo "  cd $COMPILER_DIR && npm install" >&2
    exit 1
fi

if [[ ! -f "$INPUT" ]]; then
    echo "Error: Input file not found:" >&2
    echo "  $INPUT" >&2
    exit 1
fi

if [[ -z "$OUTPUT" ]]; then
    OUTPUT="${INPUT%.*}.hdump"
fi

ARGS=(
    -b
    -dump-bytecode
)

if [[ "$PRETTY" == true ]]; then
    ARGS+=(
        -pretty
    )
fi

echo "Hermes version: $VERSION"
echo "Compiler:       $HERMESC"
echo "Input:          $INPUT"
echo "Output:         $OUTPUT"

"$HERMESC" \
    "${ARGS[@]}" \
    "$INPUT" \
    > "$OUTPUT"

echo "Done."