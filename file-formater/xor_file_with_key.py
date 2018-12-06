#!/usr/bin/env python

## XOR file with key

import sys
import os

if len(sys.argv) != 3:
	print('Usage: ' + os.path.basename(sys.argv[0]) + ' [filename] [XOR key]')
else:
	binfile = bytearray(open(sys.argv[1], 'rb').read())
	key = int('0x' + sys.argv[2], 16)
	xord_byte_array = bytearray(len(binfile))
	
	for i in range(len(binfile)):
		xord_byte_array[i] = binfile[i] ^ key	
	print(xord_byte_array)