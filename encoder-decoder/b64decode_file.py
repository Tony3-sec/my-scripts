#!/usr/bin/env python

'''
equivalent to:
base64 -D -i infile -o outfile
'''

import base64
import os
import sys
import argparse

def b64decode_file(file_data):
	path = os.getcwd()
	filename = file_data
	with open((path + str('/') + filename), 'r') as f:
		encoded_data = f.read()
		decoded_data = base64.b64decode(encoded_data)

	print(decoded_data.rstrip('\n')) # rstrip for removing extra newline


parser = argparse.ArgumentParser(description="base64 decode from file")
parser.add_argument("-f", "--file", action="store", help="File to base64 decode", dest="FILE")
args = parser.parse_args()

if args.FILE:
	b64decode_file(sys.argv[2])
else:
	parser.print_help()