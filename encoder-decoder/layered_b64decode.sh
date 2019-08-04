#!/bin/bash

# script to decode multi encoded base64 data

#b64_data='WVVjNWJscFJQVDA9'
b64_data='V1ZWak5XSnNjRkpRVkRBOQ=='

while true;
	do
		b64_data=$(echo -n $b64_data | base64 -D 2>/dev/null)
		if [ $? -ne 0 ]; then
			break
		else
			echo $b64_data
		fi
	done