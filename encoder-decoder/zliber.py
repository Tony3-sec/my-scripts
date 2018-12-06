#!/usr/bin/env python

'''
zlib compress or decompress the payload
'''
import sys
import argparse
import zlib
import binascii
## decompress hex string
def decomp(hexstring):
	d = binascii.unhexlify(hexstring)
	decompressed = zlib.decompress(d)

	print(decompressed)
## compress plain text string
def comp(plain_text):
	c = zlib.compress(plain_text)
	compressed = binascii.hexlify(c)

	print(compressed)

parser = argparse.ArgumentParser(description="zlib compress or decompress the payload")
parser.add_argument("-d", "--decompress", action="store", help="hex string to decompress", dest="HEX")
parser.add_argument("-c", "--compress", action="store", help="plain text string to compress", dest="PLAIN")
args = parser.parse_args()

if args.HEX:
	decomp(sys.argv[2])
elif args.PLAIN:
	comp(sys.argv[2])
else:
	parser.print_help()