# Init

https://docs.expo.dev/tutorial/create-your-first-app/

```bash
# Create a project named StickerSmash
npx create-expo-app@latest HermesTestApp

# CLI will prompt you to choose a template. Select SDK 57.
Select an Expo SDK version > SDK 57

# Navigate to the project directory
cd HermesTestApp

# ls -ld node_modules
# sudo chown -R $(whoami):staff node_modules
```

```shell
# npx expo prebuild
# HermesTestApp/
#├── android/
#├── ios/
#├── app/
#├── package.json

# rm -rf ios
npx expo prebuild --platform android
npx expo prebuild --platform android --clean

cd android
echo "sdk.dir=/Users/mehmet/Library/Android/sdk" > local.properties

# android/gradle/wrapper/gradle-wrapper.properties
# distributionUrl=https\://services.gradle.org/distributions/gradle-8.13-bin.zip

which node
# android/gradle.properties
# NODE_BINARY=/usr/local/bin/node

# -----------------------

./gradlew clean
./gradlew assembleRelease --stacktrace

# android/app/build/outputs/apk/release/app-release.apk
```

```text
testy/

    ControlFlow/
        While.ts
        DoWhile.ts
        For.ts
        Switch.ts
        If.ts

    Objects/
        ObjectLiteral.ts
        Property.ts

    Arrays/
        Array.ts
        Spread.ts

    Functions/
        Arrow.ts
        Closure.ts
        DefaultParameter.ts

    Exceptions/
        TryCatch.ts

    Iterators/
        ForOf.ts
        ForIn.ts

    Classes/
        Class.ts
```