"""Helpers for turning Hermes-derived names into valid JS identifiers.

Names read from the bytecode's function table are not guaranteed to be
syntactically valid JavaScript identifiers. Most notably, Hermes (and
this project's own disassembler - see `HasmWriter.py`'s
`_format_function_reference`) represents an anonymous generator/async
body as `?anon_<n>_...`, where the leading `?` marks it as a
synthesized, non-source name. Emitting that string directly as an
`Identifier` node produces invalid JS (`?` is never legal in an
identifier), so every call site that turns a function-table-resolved
name into an `Identifier` should run it through `to_js_identifier()`
first.
"""

import re

__all__ = ["to_js_identifier"]

# Anything that's never valid in a JS identifier (letters, digits, `_`
# and `$` are the only legal characters at any position; the "can't
# start with a digit" rule is handled separately below since digits
# ARE otherwise valid characters, just not in the leading position).
_INVALID_CHAR = re.compile(r'[^A-Za-z0-9_$]')


def to_js_identifier(name: str) -> str:
    """Best-effort rewrite of `name` into a syntactically valid JS identifier.

    A no-op for any name that's already a valid identifier (every
    ordinary source-derived name from the function table). Only
    rewrites the cases that aren't - currently just Hermes's own
    `?anon_0_...` synthesized-name marker - by replacing each invalid
    character with `_` and guarding against a leading digit.
    """
    if not name:
        return "anonymous"

    sanitized = _INVALID_CHAR.sub('_', name)

    if sanitized[:1].isdigit():
        sanitized = f'_{sanitized}'

    # Sanitizing could in principle empty the string out entirely (a
    # name made up of nothing but invalid characters) - fall back
    # rather than emit an empty Identifier.
    return sanitized or "anonymous"
