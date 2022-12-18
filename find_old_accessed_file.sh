#!/bin/bash

# This is a script to find the files that were last accessed more than a year ago.
# Ref: 大角祐介著 UNIX シェルスクリプト　マスターピース132 P.82 ~ P.84 SBクリエイティブ社

if [ $# -ne 1 ]; then
	echo "Usage: $0 [dirname in fullpath]"
	exit 1
fi

dirpath=$1

# Search for files that were last accessed more than a year ago, excluding hidden files.

find $dirpath -type f -name "[^/\.]*" -atime +364 -print0 | xargs -0 stat -f "%Sa %N" -t "%Y-%m-%d %H:%M:%S" | sort