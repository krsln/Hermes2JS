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

rm -rf node_modules package-lock.json yarn.lock
npm install

# rm -rf ios
rm -rf android/app/build android/build android/.gradle
npx expo prebuild --platform android --clean

cd android
echo "sdk.dir=/Users/mehmet/Library/Android/sdk" > local.properties
# ----------------------- if gets error
# android/gradle/wrapper/gradle-wrapper.properties
# distributionUrl=https\://services.gradle.org/distributions/gradle-8.13-bin.zip

#which node
# android/gradle.properties
# NODE_BINARY=/usr/local/bin/node

# -----------------------
./gradlew clean
./gradlew assembleRelease --stacktrace

# android/app/build/outputs/apk/release/app-release.apk
```
  