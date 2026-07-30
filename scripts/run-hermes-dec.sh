#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

usage() {
    cat <<EOF
Usage:
  $(basename "$0") <bundle-path>

Example:
  $(basename "$0") apps/testy/96/index.android.bundle
EOF
}

# Help
if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    exit 0
fi

# Validate argument
if [[ $# -ne 1 ]]; then
    echo "❌ Missing bundle path."
    usage
    exit 1
fi

BUNDLE="$1"

# Convert to absolute path if necessary
if [[ "$BUNDLE" != /* ]]; then
    BUNDLE="$PWD/$BUNDLE"
fi

if [[ ! -f "$BUNDLE" ]]; then
    echo "❌ Bundle not found:"
    echo "   $BUNDLE"
    exit 1
fi

OUTPUT="$(dirname "$BUNDLE")/output"
TOOLS_DIR="$SCRIPT_DIR/../vendor/hermes-dec"

mkdir -p "$OUTPUT"

echo "🔍 Disassembling..."
python "$TOOLS_DIR/src/hermes_dec/disassembly/hbc_disassembler.py" "$BUNDLE" > "$OUTPUT/output.hbc"

#echo "🧩 Decompiling..."
#python "$TOOLS_DIR/src/hermes_dec/decompilation/hbc_decompiler.py" "$BUNDLE" > "$OUTPUT/output.js"

#echo "📦 Parsing structure..."
#python "$TOOLS_DIR/src/hermes_dec/parsers/hbc_file_parser.py" "$BUNDLE" > "$OUTPUT/outputParser.js"


echo "✅ Done."
echo "📁 Output: $OUTPUT"