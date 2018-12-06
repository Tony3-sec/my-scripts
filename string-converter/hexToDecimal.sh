#!/bin/bash

## Convert hex to decimal

if [ $# -ne 1 ]; then
        echo "Usage: $0 [hex data]"
        exit 1
fi

head=0x
data=$1
hex=$head$data

echo $(($hex))
