#!/usr/bin/env python
import os
import glob

org_ext = '.flow'
new_ext = '.pcap'

print('changing file extension ' + str(org_ext) + ' to ' + str(new_ext) + '...')

## list the file with certain extension in current directory
files = glob.glob('*' + str(org_ext))
## Rename files with new extension
for oldname in files:
	newname = oldname.replace(org_ext, new_ext)
	os.rename(oldname, newname)

print('Completed!')
