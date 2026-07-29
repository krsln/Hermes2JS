#!/bin/zsh
set -e

# git ls-remote https://github.com/P1sec/hermes-dec.git HEAD
#HERMES_DEC_COMMIT="66bb3449ace7ed48b400878da045e89e3a45bff2"
HERMES_DEC_COMMIT="648be12f721775d952d6e67b20b5930c929b2495"
VENDOR_DIR="vendor/hermes-dec"

if [[ ! -d "$VENDOR_DIR" ]]; then
    echo "📥 Fetching hermes-dec..."

    git clone https://github.com/P1sec/hermes-dec.git "$VENDOR_DIR"
    git -C "$VENDOR_DIR" checkout "$HERMES_DEC_COMMIT"

    echo "Remove git history; keep only the source snapshot"
    rm -rf "$VENDOR_DIR/.git"
else
    echo "✅ hermes-dec already present"
fi