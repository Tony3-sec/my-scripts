#!/usr/bin/env python

import urllib
import sys
import argparse
import os

'''
This script may (not) decode URL encodings with Unicode chars.
Ensure to set your editor / terminal's char encoding setting to UTF-8
in order to get proper output
'''
def decode_string(string_data):
	print(urllib.unquote(string_data))

def decode_file(file_data):
	path = os.getcwd()
	filename = file_data
	f = open((path + str('/') + filename), 'r')
	d = open('decoded.txt', 'w')
	while True:
		line = f.readline()
		if not line:
			print('Also check "decoded.txt"')
			f.close()
			d.close()
			break
		print(urllib.unquote(line))
		d.write(urllib.unquote(line))	


parser = argparse.ArgumentParser(description="Decode URL encoded data")
parser.add_argument("-s", "--string", action="store", help="String to decode", dest="STRING")
parser.add_argument("-f", "--file", action="store", help="Decode from file", dest="FILE")
args = parser.parse_args()

if args.STRING:
	decode_string(sys.argv[2])
elif args.FILE:
	decode_file(sys.argv[2])
else:
	parser.print_help()
