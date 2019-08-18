#!/usr/bin/env python

'''
Convert decimal to IP

$ python DecimalToIP.py 2130706433
127.0.0.1
'''

import socket
import struct
import sys

if len(sys.argv) < 2:
	print('Needs decimal as arg')
else:
	print(socket.inet_ntoa(struct.pack('!L', int(sys.argv[1]))))