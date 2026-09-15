#!/usr/bin/env bash
# Shared helpers for locating the per-platform hermesc binary inside a
# `hermes-compiler` npm install. Sourced by fetch_compiler.sh and dump.sh
# so platform detection lives in exactly one place.

# hermes_platform_bin
#   Echoes the hermes-compiler npm package's platform subdirectory name
#   for the current OS: linux64-bin / osx-bin / win64-bin.
hermes_platform_bin() {
    case "$(uname -s)" in
        Linux*)  echo "linux64-bin" ;;
        Darwin*) echo "osx-bin" ;;
        *)       echo "win64-bin" ;;
    esac
}

# hermes_compiler_bin_path <compiler-dir>
#   Echoes the full path to the hermesc binary inside a
#   tools/hermes/compilers/<version> directory, for the current platform.
hermes_compiler_bin_path() {
    local compiler_dir="$1"
    echo "$compiler_dir/node_modules/hermes-compiler/hermesc/$(hermes_platform_bin)/hermesc"
}