#!/bin/bash

# script to perform ROT13 substitution

raw_table='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot_table='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

if [ $# -ne 1 ]; then
	echo "Usage: $0 [string]"
	exit 1
fi

echo $1 | tr "$raw_table" "$rot_table"