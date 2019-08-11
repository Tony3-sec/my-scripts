#!/usr/bin/env python

'''
XOR the file
'''
import binascii
import argparse

def XORfile(input_file, key):

	output_file = 'XORed.bin'
	key = bytearray(binascii.unhexlify(key))
	key_length = len(key)

	with open(input_file, 'rb') as fin:
		file_contents = bytearray(fin.read())

	file_size = len(file_contents)
	XORed_bytearray = bytearray(file_size)

	with open(output_file, 'wb') as fout:
		
		j = 0

		if (key_length > 1):
			for i in range(0, file_size):
				if (j >= key_length): ## if the key gets to end, set the key back to beginning.
					j = 0
				XORed_bytearray[i] = file_contents[i] ^ key[j]
				j += 1
		else:
			for i in range(0, file_size):
				XORed_bytearray[i] = file_contents[i] ^ key[j]

		fout.write(XORed_bytearray)

	print('check out ' + str(output_file))

parser = argparse.ArgumentParser(description="XOR the file")
parser.add_argument("-i", "--input_file", action="store", required=True)
parser.add_argument("-k", "--key", action="store", help="XOR key in hex format", required=True)
args = parser.parse_args()

XORfile(args.input_file, args.key)