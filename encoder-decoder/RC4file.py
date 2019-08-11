#!/usr/bin/env python

'''
RC4 encrypt / decrypt the file 
'''

import argparse
from Crypto.Cipher import ARC4


def decryptor(input_file, key):

	output_file = 'decrypted.bin'

	with open(input_file, 'rb') as fin:
		file_contents = fin.read()
		decrypted_data = ARC4.new(key).decrypt(file_contents)
	
	with open(output_file, 'wb') as fout:
		fout.write(decrypted_data)

	print('check out ' + str(output_file))


def encryptor(input_file, key):

	output_file = 'encrypted.bin'

	with open(input_file, 'rb') as fin:
		file_contents = fin.read()
		encrypted_data =  ARC4.new(key).encrypt(file_contents)

	with open(output_file, 'wb') as fout:
		fout.write(encrypted_data)

	print('check out ' + str(output_file))

parser = argparse.ArgumentParser(description="RC4 encrypt / decrypt the file")
parser.add_argument('-e', '--encrypt', action='store_true')
parser.add_argument('-d', '--decrypt', action='store_true')
parser.add_argument("-i", "--input_file", action="store", required=True)
parser.add_argument("-k", "--key", action="store", help="RC4 key", required=True)
args = parser.parse_args()

if args.encrypt:
	encryptor(args.input_file, args.key)
elif args.decrypt:
	decryptor(args.input_file, args.key)
else:
	parser.print_help()
