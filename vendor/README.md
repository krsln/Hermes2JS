# Vendor

### clone vendor/hermes-dec

```shell
chmod +x vendor/fetch-hermes-dec.sh
chmod +x vendor/run-hermes-dec.sh

# clones https://github.com/P1sec/hermes-dec to vendor/hermes-dec
./vendor/fetch-hermes-dec.sh
```

## Usage

```bash
#./vendor/run-hermes-dec.sh <bundle_path>

file apps/coachy/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
./vendor/run-hermes-dec.sh coachy

# Test Projects' bundles
file apps/testy/96/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 96
file apps/testy/98/index.android.bundle
# index.android.bundle: Hermes JavaScript bytecode, version 98

./vendor/run-hermes-dec.sh apps/testy/96/index.android.bundle
./vendor/run-hermes-dec.sh apps/testy/98/index.android.bundle

```

**Output**

```
apps/<app_name>/output/
├── output.hasm
├── output.js
└── outputParser.js
```