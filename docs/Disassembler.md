# Hermes Disassembler

https://www.politesi.polimi.it/retrieve/17e4c202-4d63-43f1-97d9-84a925bb9130/2023_05_Falvo.pdf   
https://github.com/P1sec/hermes-dec 
https://p1sec.github.io/hermes-dec/opcodes_table.html   


## usage example

```shell
# basic
python hbc_disassembler.py  index.android.bundle > output.hbc
python hbc_decompiler.py  index.android.bundle > output.js
python hbc_file_parser.py  index.android.bundle > outputParser.js

# goto disassembler/run_disassemble.sh
```

## Test app

Coachify AI: Workout Planner   
https://apps.apple.com/tr/app/coachify-ai-workout-planner/id6449539939?l=tr  
https://apkpure.com/coachify-ai/ai.coachify.coachify/download

unzip
https://www.decompiler.com/

ai.coachify.coachify.apk / resources / assets / index.android.bundle

download the file :p

```shell
% file index.android.bundle
index.android.bundle: Hermes JavaScript bytecode, version 96
```