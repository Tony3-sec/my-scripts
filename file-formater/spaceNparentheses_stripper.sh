#!/bin/bash
## Remove space and parentheses from filename

# set only new line char as a field separator
IFS='
'

for oldname in $(ls)
do
	if [ -d $oldname ]; then
		: # ignore if its directory
	else
		echo "$oldname" | grep -E '[ \(\)]' >/dev/null 2>&1
		# if filename contains space or parentheses
		if [ $? -eq 0 ]; then
			newname=$(echo "$oldname" | sed -E 's/[ \(\)]//g')
			mv "$oldname" "$newname"
			echo "Changed filename "$oldname" to "$newname""
		fi
	fi
done