#!/usr/bin/env python

'''
RC4 encryptor / decryptor
'''

import argparse
import binascii
from Crypto.Cipher import ARC4

def decryptor(data, key):
	print(ARC4.new(key).decrypt(binascii.unhexlify(data)))

def encryptor(data, key):
	#print(ARC4.new(key).encrypt(binascii.hexlify(data)))
	print("hex: " + binascii.hexlify(ARC4.new(key).encrypt(data)))
	print("raw: " + ARC4.new(key).encrypt(data))

#data = '2911b7fa98'
#key = '56'


parser = argparse.ArgumentParser(description="RC4 encryptor / decryptor")
parser.add_argument("-t", "--text", action="store", help="text to encrypt (arg: plain text) / decrypt (arg: hex format)", required=True)
parser.add_argument("-k", "--key", action="store", help="RC4 key", required=True)
parser.add_argument('-e', '--encrypt', action='store_true')
parser.add_argument('-d', '--decrypt', action='store_true')
args = parser.parse_args()

if args.encrypt:
	encryptor(args.text, args.key)
elif args.decrypt:
	decryptor(args.text, args.key)
else:
	parser.print_help()