#!/usr/bin/env python

import zlib
import os
import argparse

'''
This script will decompress zlib compressed file located in the current working directory
'''

def zlib_decompress_file(file_data):
	path = os.getcwd()
	filename = file_data
	compressed_file = open((path + str('/') + filename), 'rb').read()
	decompressed_data = zlib.decompress(compressed_file)    ## for zlib inflate
	output_file = open('decompress.out', 'wb')
	output_file.write(decompressed_data)
	output_file.close()
	print("Deccompressed!")
	print("Check out 'decompress.out'")


def raw_inflate_file(file_data):
	path = os.getcwd()
	filename = file_data
	compressed_file = open((path + str('/') + filename), 'rb').read()
	decompressed_data = zlib.decompress(compressed_file, -15) ## for raw inflate
	output_file = open('decompress.out', 'wb')
	output_file.write(decompressed_data)
	output_file.close()
	print("Deccompressed!")
	print("Check out 'decompress.out'")

parser = argparse.ArgumentParser(description="Decompress zlib compressed file")
parser.add_argument("-f", "--file", action="store", help="File to decompress", dest="FILE")
parser.add_argument("-z", "--zlib", action="store_true", help="use this option for zlibe decompress", dest="ZLIB_DECOMP")
parser.add_argument("-r", "--raw", action="store_true", help="use this option for raw inflate", dest="RAW_INFLATE")
args = parser.parse_args()

if args.FILE:
	if args.ZLIB_DECOMP:
		zlib_decompress_file(args.FILE)
	elif args.RAW_INFLATE:
		raw_inflate_file(args.FILE)
	else:
		parser.print_help()
else:
	parser.print_help()
