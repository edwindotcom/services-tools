#!/bin/bash
if [ "$1" == "" ]; then
    echo 'Pulls and pushes pref.js to your phone.'
    echo 'Usage: ./modPref.sh [pull|push]'
    exit
fi
echo "Plug in your device"
adb wait-for-device
echo "Found device"
PROFILE=$(adb shell echo -n "/data/b2g/mozilla/*.default")
PREFS_JS=$PROFILE/prefs.js
if [ $1 == "pull" ]; then
    root=eval adb shell echo -n "/data/b2g/mozilla/*.default"
    pref="/prefs.js"
    echo $root$pref
    echo "Copied prefs.js to local, please edit file"
    adb pull $PREFS_JS &>/dev/null || echo 'Error pulling pref'
elif [ $1 == "push" ]; then
    echo 'pushing prefs.js to b2g device'
    adb shell stop b2g
    adb push prefs.js $PREFS_JS
    adb shell start b2g
    echo 'restarting b2g device'
fi
