# Test Projects

https://docs.expo.dev/tutorial/create-your-first-app/

| React Native Version     | Hermes Bytecode Version (HBC) | Notes / Status                   |
|--------------------------|-------------------------------|----------------------------------|
| React Native 0.84+       | Version 98 / 99+              | next-generation Hermes V1 engine |
| React Native 0.74 – 0.83 | Version 96                    | Common                           |
| React Native 0.71 – 0.73 | Version 93                    |                                  |

| React Native | Expo SDK | Komut                                                            |
|--------------|----------|------------------------------------------------------------------|
| **0.83**     | **55**   | `npx create-expo-app@latest MyTestApp --template default@sdk-55` |
| 0.85         | 56       | `npx create-expo-app@latest MyTestApp --template default@sdk-56` |
| 0.86         | 57       | `npx create-expo-app@latest MyTestApp` (veya `@sdk-57`)          |

```shell
# Version 98
npx create-expo-app@latest hermes-test-sdk-57 --template default@sdk-57

# Version 96
npx create-expo-app@latest hermes-test-sdk-55 --template default@sdk-55
```

### Notes

```bash
# Create a project named StickerSmash
npx create-expo-app@latest hermes-test-app

# CLI will prompt you to choose a template. Select SDK 57.
Select an Expo SDK version > SDK 57

# Navigate to the project directory
cd HermesTestApp

# ls -ld node_modules
# sudo chown -R $(whoami):staff node_modules
```
