'''
Send SSDP M-SEARCH packet with spoofed source IP address.
Tested on CentOS 6
'''
import socket, sys, struct

# create ssdp M-SEARCH payload
data = "M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: 3\r\nST: ssdp:all\r\n\r\n"

# create raw socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error , msg:
    print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
    
# checksum functions needed for calculation checksum
def checksum(msg):
    s = 0
     
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
        s = s + w
     
    s = (s>>16) + (s & 0xffff);
    s = s + (s >> 16);
     
    #complement and mask to 4 byte short
    s = ~s & 0xffff
     
    return s
    
packet = ''
source_ip = '192.168.10.11' # spoof source IP if you want
dest_ip = '192.168.10.1'

# IP header field
ip_ihl = 5
ip_ver = 4
ip_tos = 0
ip_tot_len = 0 # kernel will fill the correct total length
ip_id = 12345
ip_fragment_offset = 0
ip_ttl = 255
ip_proto = socket.IPPROTO_UDP # protocol number (TCP=6, UDP=17)
ip_checksum = 0 # kernel will fill the correct checksum
ip_src = socket.inet_aton(source_ip)
ip_dst = socket.inet_aton(dest_ip)

ip_ihl_ver = (ip_ver << 4) + ip_ihl

# the ! in the pack format string means network order
ip_header = struct.pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_fragment_offset, ip_ttl, ip_proto, ip_checksum, ip_src, ip_dst)

# pseudo header fields
source_address = socket.inet_aton(source_ip)
dest_address = socket.inet_aton(dest_ip)
placeholder = 0
protocol = socket.IPPROTO_UDP # protocol type (TCP=6, UDP=17)
udp_header_len = 8
user_dgram_len = udp_header_len + len(data)
print('user_dgram_len is: ' + str(user_dgram_len))

# UDP header field
udp_src = 5678
udp_dst = 1900
udp_check = 0 # This is temporary value
udp_header = struct.pack('!HHHH', udp_src, udp_dst, user_dgram_len, udp_check)
print('udp_header is: ' + str(len(udp_header)))

# calculate checksum
psh = struct.pack('!4s4sBBH', source_address, dest_address, placeholder, protocol, user_dgram_len)
psh = psh + udp_header + data
print('length of psh is: ' + str(len(psh)))
if len(psh) % 2 != 0:
    padding = struct.pack("!B", 0)
    psh = psh + padding
udp_check = checksum(psh) 

# create UDP header with real checksum value
udp_header = struct.pack('!HHH', udp_src, udp_dst, user_dgram_len) + struct.pack('H', udp_check)
# put everything and create UDP packet
packet = ip_header + udp_header + data
print('packet is: ' + str(len(packet)))
# send the packet!
s.sendto(packet, (dest_ip , 0 ))
