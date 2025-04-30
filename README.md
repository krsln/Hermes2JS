# Hermes2JS

#### Step—1

https://www.decompiler.com/

#### Step—2 -> HermesDisassembler

https://github.com/P1sec/hermes-dec


```shell
#HermesDisassembler/hermes-dec-main/
#Apps/xx/index.android.bundle
#Apps/xx/Output
python hbc_disassembler.py  index.android.bundle > output.hbc
python hbc_decompiler.py  index.android.bundle > output.js
python hbc_file_parser.py  index.android.bundle > outputParser.js
```

#### Step—3 -> HermesAssembly2JS

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf


https://p1sec.github.io/hermes-dec/opcodes_table.html
--
business@Hell-MacBook-Pro hermes-dec-main % file index.android.bundle
index.android.bundle: Hermes JavaScript bytecode, version 96

Hermes Assembly (HASM)
https://docs.rs/hermes_rs/latest/hermes_rs/all.html  
https://docs.rs/hermes_rs/latest/hermes_rs/hermes/v96/index.html  
https://docs.rs/hermes_rs/latest/src/hermes_rs/hermes/v96/mod.rs.html#3-210

https://github.com/facebook/hermes/blob/main/include/hermes/BCGen/HBC/BytecodeList.def

disassembled Hermes bytecode -> Reconstructing to JavaScript
Hermes HASM to JavaScript Converter
