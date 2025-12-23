const fs = require('fs');
const path = require('path');

const packageJson = JSON.parse(fs.readFileSync(path.join(__dirname, 'package.json'), 'utf8'));

console.log(`# ${packageJson.name} v${packageJson.version}`);

if (process.platform === 'win32') {
    console.log('## Running on Windows');
    console.log('To run the app on Android, use:');
    console.log('  npx react-native run-android');
    console.log('To run the app on iOS, use:');
    console.log('  npx react-native run-ios');
} else {
    console.log('## Running on non-Windows platform');
    console.log('To run the app on Android, use:');
    console.log('  export ANDROID_HOME=$HOME/Android/Sdk && npx react-native run-android');
    console.log('To run the app on iOS, use:');
    console.log('  npx react-native run-ios');
}