#!/bin/bash

## This script will convert packet caputre file (in current directory) to tcpdump capture format.

echo "converting pcap to tcpdump file format...."

pcap_exts=$(ls | grep "\.pcap\|\.flow\|\.cap\|\.pcapng") #list of possible pcap files
header="converted_"

for pcapfile in $pcap_exts
do 
	file $pcapfile | grep -v "tcpdump" > /dev/null #check whether or not the file is in tcpdump capture format

	if [ $? -eq 0 ]; then
		newfile=$header$pcapfile #create new output filename
		editcap -F libpcap $pcapfile $newfile #convert the file to tcpdump capture format
	fi
done

echo "Complete!"
