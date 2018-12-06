#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print('Please type hex data')
else:
	#print(len(sys.argv))
	print(sys.argv[1].decode('hex'))