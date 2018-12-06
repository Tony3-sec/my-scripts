#!/usr/bin/python
# This is a simple script to decode / encode custom base64
# Fill the "CUSTOM_ALPHABET" with custom base64 table

'''
# Standard table
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
'''

import string
import base64
import argparse

STANDARD_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

#ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
#DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)

parser = argparse.ArgumentParser(description="Decode or encode custom base64")
parser.add_argument("-s", "--string", action="store", help="String to encode / decode", dest="STRING")
parser.add_argument("-d", "--decode", action="store_true", help="Decode the string", dest="DECODE")
parser.add_argument("-e", "--encode", action="store_true", help="Encode the string", dest="ENCODE")
parser.add_argument("-t", "--table", action="store", help="Table for custom base64", dest="TABLE")

args = parser.parse_args()

if args.DECODE and args.TABLE and not args.ENCODE:
	CUSTOM_ALPHABET = args.TABLE
	DECODE_TRANS = string.maketrans(CUSTOM_ALPHABET, STANDARD_ALPHABET)
	print(base64.b64decode(args.STRING.translate(DECODE_TRANS)))
elif args.ENCODE and args.TABLE and not args.DECODE:
	CUSTOM_ALPHABET = args.TABLE
	ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
	print(base64.b64encode(args.STRING.translate(ENCODE_TRANS)))
else:
	parser.print_help()
