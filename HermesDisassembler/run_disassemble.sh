# run_disassemble.sh
#!/bin/zsh

# Set target app directory name
#Target_Dir="Coachify"
Target_Dir="Testy"

# Define paths
BUNDLE="../Apps/$Target_Dir/index.android.bundle"
OUTPUT="../Apps/$Target_Dir/Output"
TOOLS_DIR="hermes-dec-main"

# Ensure the Output directory exists
mkdir -p "$OUTPUT"

# Run disassembler
echo "🔍 Disassembling..."
python3 "$TOOLS_DIR/hbc_disassembler.py" "$BUNDLE" > "$OUTPUT/output.hbc"

# Run decompiler
echo "🧩 Decompiling..."
python3 "$TOOLS_DIR/hbc_decompiler.py" "$BUNDLE" > "$OUTPUT/output.js"

# Run parser
echo "📦 Parsing structure..."
python3 "$TOOLS_DIR/hbc_file_parser.py" "$BUNDLE" > "$OUTPUT/outputParser.js"

echo "✅ Done. Outputs saved to $OUTPUT"