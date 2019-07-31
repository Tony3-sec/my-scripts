#!/usr/bin/env python

## Remove parentheses and space from filename in current directory

import os
import re

print('Removing parentheses and space from filename.....')

files = os.listdir('.')

for oldname in files:
	newname = re.sub('[ \(\)]', '', oldname)
	os.rename(oldname, newname)

print('Completed!')
