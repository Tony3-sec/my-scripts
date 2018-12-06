#!/usr/bin/env python

## Remove parentheses and space from filename in current directory

import os
import re

print('Removing parentheses and space from filename.....')

files = os.listdir('.')

for f in files:
	newname = re.sub('[ \(\)]', '', f)
	os.rename(f, newname)

print('Completed!')
