# Readme

## Install Hermes

```shell
npm --prefix tools/hermes/compilers/96 install
npm --prefix tools/hermes/compilers/98 install
```

## prep

```shell
chmod +x tools/hermes/dump.sh

./tools/hermes/compilers/96/node_modules/hermes-compiler/hermesc/osx-bin/hermesc hermesc -version
./tools/hermes/compilers/98/node_modules/hermes-compiler/hermesc/osx-bin/hermesc hermesc -version
```

## usage

```shell
## 96
./tools/hermes/dump.sh \
    96 \
    apps/testy/96/index.android.bundle \
    apps/testy/96/output/hermesc-output.hasm

./tools/hermes/dump.sh \
    96 \
    apps/testy/96/index.android.bundle \
    apps/testy/96/output/hermesc-output.hasm \
    --pretty

## 98
./tools/hermes/dump.sh \
    98 \
    apps/testy/98/index.android.bundle \
    apps/testy/98/output/hermesc-output.hasm \
    --pretty

```