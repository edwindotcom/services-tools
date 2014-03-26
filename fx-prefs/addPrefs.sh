#!/bin/bash
if [ "$1" == "" ]; then
  echo 'appends pref to your profile pref.js'
  echo 'Usage: ./addPref.sh [file with prefs] [prefs.js file]'
  exit
fi

cat $1 >> $2 
echo "pref added"
tail "$2"
