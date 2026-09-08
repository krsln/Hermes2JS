#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_ROOT="$SCRIPT_DIR"
COMPILERS_DIR="$HERMES_ROOT/compilers"
VERSIONS_FILE="$HERMES_ROOT/versions.json"

# shellcheck source=./lib/platform.sh
source "$SCRIPT_DIR/lib/platform.sh"

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

if ! python3 -c "
import json, sys
data = json.load(open('$VERSIONS_FILE'))
entry = data['versions'].get('$VERSION')
sys.exit(0 if entry and entry.get('npm_version') else 1)
" 2>/dev/null; then
    echo "Error: bytecode version '$VERSION' is not a known, installable version." >&2
    echo "  See $VERSIONS_FILE for supported versions." >&2
    exit 1
fi

COMPILER_DIR="$COMPILERS_DIR/$VERSION"
HERMESC="$(hermes_compiler_bin_path "$COMPILER_DIR")"

if [[ ! -d "$COMPILER_DIR" ]] || [[ ! -x "$HERMESC" ]]; then
    echo "Error: hermesc for version $VERSION not installed yet:" >&2
    echo "  $HERMESC" >&2
    echo >&2
    echo "Install it first:" >&2
    echo "  ./tools/hermes/fetch_compiler.sh $VERSION" >&2
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