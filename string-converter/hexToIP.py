#!/usr/bin/env python
import sys

## Convert hexadecimal to IP address

if len(sys.argv) < 2:
	print('Please type hexadecimal')
else:
	i = 0
	j = 2
	ipaddr = ''
	data = sys.argv[1]
	while len(data[i:j]) != 0:
		hex_data = data[i:j] #pick two chars from arg
		octet = '0x' + str(hex_data)
		ipaddr += str(int(octet, 16)) + str('.')
		i += 2
		j += 2
	print(ipaddr.rstrip('.')) #strip last dot and print the IP address

	
