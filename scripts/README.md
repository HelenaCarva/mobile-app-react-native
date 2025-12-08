# Mobile App (React Native)

A cross-platform mobile application built with React Native.

## Features

- Cross-platform support (iOS & Android)
- Modern UI with React Native Paper
- State management with Redux Toolkit
- Navigation with React Navigation
- API integration with Axios

## Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher) or yarn
- React Native CLI
- Xcode (for iOS development)
- Android Studio (for Android development)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mobile-app-react-native.git
   ```

2. Install dependencies:
   ```bash
   cd mobile-app-react-native
   npm install
   # or
   yarn install
   ```

3. For iOS:
   ```bash
   cd ios && pod install && cd ..
   ```

## Running the App

- iOS:
  ```bash
  npx react-native run-ios
  ```

- Android:
  ```bash
  npx react-native run-android
  ```

## Configuration

Copy `.env.example` to `.env` and update the environment variables:
```bash
cp .env.example .env
```

## Scripts

- `start`: Start Metro bundler
- `ios`: Run on iOS simulator
- `android`: Run on Android emulator
- `test`: Run unit tests
- `lint`: Run ESLint
- `format`: Format code with Prettier

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.

## License

[MIT](https://choosealicense.com/licenses/mit/)