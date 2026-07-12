# Hermes 2 JS


#### TODO: String Mapping
==> 00000040: <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 5, string_id: 100>  # String: 'console' (Identifier)
string_id -> # String:

#### TODO: Address Mapping
==> 00000079: <Jmp>: <Addr8: 32>  # Address: 00000099

#### TODO: Object Mapping
==> 0000008a: <NewObjectWithBuffer>: <Reg8: 0, UInt16: 4, UInt16: 4, UInt16: 11077, UInt16: 9225>  # Object: {'title': 'Join Coachify AI Competition', 'message': 'Join Coachify AI Competition', 'url': 'https://coachify.ai/download?ref=compshare', 'subject': 'Join Coachify AI Competition'}


## opcodes

Reg8 -> typically refers to an **8-bit register**.

Map each instruction to JavaScript:

- <LoadConstString> → Assign a string literal.
- <GetByIdShort> → Property access (obj.prop).
- <Call2> → Function call (func(arg1, arg2)).
- <Ret> → return statement.
- <JmpTrue> → if condition or goto-like label.
- Generator ops (<StartGenerator>, <ResumeGenerator>) → function* and yield.

## Learn in hermes

- if / else
- ternary operator
- throw
- async / await

