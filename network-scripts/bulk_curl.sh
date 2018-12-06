#!/bin/bash

## Script to bulk download the file from URL.
## If filename duplicates, append a counter to the filename.

if [ $# -ne 1 ]; then
	echo "Usage: $0 [Needs file as arg]"
	exit 1
fi

URL_list=$1

if [ ! -e $URL_list ]; then
	echo "$URL_list does not exist."
	exit 2
fi

count=0

echo "Fetching files....."

for url in $(cat $URL_list)
	do 
		filename=$(basename "$url")

		if [ -e $filename ]; then
			count=$(($count + 1))
			curl -s $url -o $filename$count
		else
			curl -s $url -O
		fi
	done

echo "Complete!"