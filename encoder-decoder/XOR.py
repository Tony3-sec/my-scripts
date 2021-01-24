#!/usr/bin/env python

import binascii

#data = "79746a6512051b1e187b68036563606603190d7e76730c17746a736667"
data = "f02a1dfb6521d96509ed211aec361ba92c1bb36559b07746b87350a77458a77448e12a1bfd2b09e42048e03648de0c26a40d27ce0037ef30"
data = bytearray(binascii.unhexlify(data))
data_length = len(data)

XORed_bytearray = bytearray(data_length)

#key = "23"
key = "894568"
key = bytearray(binascii.unhexlify(key))
key_length = len(key)

j = 0

if (key_length == 1): ## if XOR key is single byte
	for i in range(0, data_length):
	    XORed_bytearray[i] = data[i] ^ key[j]
	    #key[j] += 1 ## uncomment if the key is incremented by 1
else:
	for i in range(0, data_length):
		if (j >= key_length): ## reset index when the key reaches the end
			j = 0
		XORed_bytearray[i] = data[i] ^ key[j]
		j += 1

print(XORed_bytearray)