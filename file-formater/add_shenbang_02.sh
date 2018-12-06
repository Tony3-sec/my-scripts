#!/bin/bash
## Add shenbang according to file extension
# Exit if no args
if [ $# -eq 0 ]; then
	echo "Usage: $0 [filename]"
	exit 1
fi

for file in $@
do
	# Exit if file does not exist
	if [ ! -f $file ]; then
		echo "file does not exist"
		exit 2
	fi
	# Get file extension
	ext=$(echo "$file" | rev | cut -c 1-3 | rev)
	# Delete old shenbang and add new one. Exit if file type is unknown
	case "$ext" in
		\.sh)
			sed -i '' -e '/^#!/d' $file; sed -i '' -e '1i\
\#!/bin/bash
' $file
;;
		\.py)
			sed -i '' -e '/^#!/d' $file; sed -i '' -e '1i\
\#!/usr/bin/python
' $file
;;
		\.rb)
			sed -i '' -e '/^#!/d' $file; sed -i '' -e '1i\
\#!/usr/bin/ruby
' $file
;;
		\.pl)
			sed -i '' -e '/^#!/d' $file; sed -i '' -e '1i\
\#!/usr/bin/perl
' $file
;;
		*)
			echo "Unknown file type: $file"
			exit 3
	esac
	echo "$file: complete!"
done
