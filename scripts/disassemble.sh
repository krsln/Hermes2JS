#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

usage() {
    cat <<EOF
Usage:
  $(basename "$0") <target-dir>

Example:
  $(basename "$0") testy
EOF
}

# Help
if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    exit 0
fi

# Validate argument
if [[ $# -ne 1 ]]; then
    echo "❌ Missing target directory."
    usage
    exit 1
fi

TARGET_DIR="$1"

BUNDLE="$SCRIPT_DIR/../apps/$TARGET_DIR/index.android.bundle"
OUTPUT="$SCRIPT_DIR/../apps/$TARGET_DIR/output"
TOOLS_DIR="$SCRIPT_DIR/../vendor/hermes-dec"

# Validate input
if [[ ! -f "$BUNDLE" ]]; then
    echo "❌ Bundle not found:"
    echo "   $BUNDLE"
    exit 1
fi

mkdir -p "$OUTPUT"

echo "🔍 Disassembling..."
python3 "$TOOLS_DIR/src/hermes_dec/disassembly/hbc_disassembler.py" "$BUNDLE" > "$OUTPUT/output.hbc"

echo "🧩 Decompiling..."
python3 "$TOOLS_DIR/src/hermes_dec/decompilation/hbc_decompiler.py" "$BUNDLE" > "$OUTPUT/output.js"

echo "📦 Parsing structure..."
python3 "$TOOLS_DIR/src/hermes_dec/parsers/hbc_file_parser.py" "$BUNDLE" > "$OUTPUT/outputParser.js"

echo "✅ Done."
echo "📁 Output: $OUTPUT"