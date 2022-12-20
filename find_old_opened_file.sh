#!/bin/bash

# This script is designed to run on MacOS.
# This is a script to find the files that were last opened more than a year ago.
# The script checks the file's "Last opened time" rather than "Last accessed time (atime)".
# Files without "Last opened time" won't be checked.

# Ref: 
# https://ss64.com/osx/mdfind.html
# https://developer.apple.com/documentation/coreservices/kmditemlastuseddate
# https://developer.apple.com/documentation/coreservices/file_metadata/mditem

if [ $# -ne 1 ]; then
	echo "Usage: $0 [dirname in fullpath]"
	exit 1
fi

# Search for files that were last opened more than a year ago.

dirpath=$1

#mdfind -0 -onlyin $dirpath 'kMDItemLastUsedDate <= $time.today(-365)' | xargs -0 mdls -name kMDItemLastUsedDate -name kMDItemPath

mdfind -0 -onlyin $dirpath 'kMDItemLastUsedDate <= $time.today(-365)' | xargs -0 mdls -name kMDItemLastUsedDate -name kMDItemPath | sed -E 's/.+= //g' | perl -pe 's/([^"])\n/\1 /g' | sort