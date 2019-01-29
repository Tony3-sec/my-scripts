#!/usr/bin/env python

import zlib
import os
import argparse
import sys

'''
This script will decompress zlib compressed file located in the current working directory
'''

def decompress_file(file_data):
	path = os.getcwd()
	filename = file_data
	compressed_file = open((path + str('/') + filename), 'rb').read()
	decompressed_data = zlib.decompress(compressed_file)
	output_file = open('decompress.out', 'wb')
	output_file.write(decompressed_data)
	output_file.close()
	print("Deccompressed!")
	print("Check out 'decompress.out'")

parser = argparse.ArgumentParser(description="Decompress zlib compressed file")
parser.add_argument("-f", "--file", action="store", help="File to decompress", dest="FILE")
args = parser.parse_args()

if args.FILE:
	decompress_file(sys.argv[2])
else:
	parser.print_help()