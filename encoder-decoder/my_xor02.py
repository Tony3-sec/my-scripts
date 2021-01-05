#!/usr/bin/env python

'''
This script will XOR the data. 
The key and the payload must be in hex format
Simplified the code from my_xor.py
'''

import binascii

#enc = "796f757220495020616464726573732069733a203139322e3136382e31302e3120686f73746e616d652069732057494e2d484f47455f6675"
enc = "f02a1dfb6521d96509ed211aec361ba92c1bb36559b07746b87350a77458a77448e12a1bfd2b09e42048e03648de0c26a40d27ce0037ef30"
key = "894568"
dec = ""

n = 2
m = 0
## if key is single byte
if ( (len(key) / 2) == 1):
	for i in range(0, len(enc), n):
		dec += hex(int(enc[i:i+n], 16) ^ int(key[m:m+n], 16)).replace('0x', '').zfill(2)
else:
	for i in range(0, len(enc), n):
		dec += hex(int(enc[i:i+n], 16) ^ int(key[m:m+n], 16)).replace('0x', '').zfill(2)
		m += n
		## if the key gets to end, set the key back to beginning.
		if (m >= len(key)):
			m = 0

print(dec)
#dec = dec.replace('0d0d', '0d0a') ## not sure why but when hex contains '0d0d' it doesn't print properly so replacing to '0d0a'
#print(binascii.unhexlify(dec))
print(repr(binascii.unhexlify(dec)))
print("")
