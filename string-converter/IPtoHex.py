#!/usr/bin/env python

import sys

'''
Convert IP address to hexadecimal
'''

if len(sys.argv) < 2:
	print('Please type IP address')
else:
	hexadecimal = ''
	octetList = sys.argv[1].split('.')

	for octet in octetList:
		hexadecimal += hex(int(octet)).replace('0x', '').zfill(2)
		## I put zifll because I didn't want to lose the leading zero in hex
		## eg) 0xd -> 0x0d (this is what I want)
		
	print(hexadecimal)
