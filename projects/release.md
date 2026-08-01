# Release

```shell
# npx expo prebuild
# HermesTestApp/
#├── android/
#├── ios/
#├── app/
#├── package.json

#rm -rf node_modules package-lock.json yarn.lock
#npm install

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

# /android/app/build/generated/assets/react/release/index.android.bundle
# android/app/build/outputs/apk/release/app-release.apk
```
  