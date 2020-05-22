import os
import socket
import argparse
import struct
ETH_P_ALL = 0x0003
ETH_SIZE = 14

def sniffing(nic):
	if os.name == 'nt':
		address_familiy = socket.AF_INET
		protocol_type = socket.IPPROTO_IP
	else:
		address_familiy = socket.AF_PACKET
		protocol_type = socket.ntohs(ETH_P_ALL)

	with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
		sniffe_sock.bind((nic, 0))

		if os.name == 'nt':
			sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
		while True:
			data, _ = sniffe_sock.recvfrom(65535)
			ethernet_check = struct.unpack('!H',data[12:ETH_SIZE])
			if ethernet_check[0] == 2048: # ether_type이 IPv4인 경우
				ethernet_header = make_ethernet_header(data[:ETH_SIZE])
				for item in ethernet_header.items():
					print('{0} : {1}'.format(item[0], item[1]))

				ip_version_length = struct.unpack('!B',data[ETH_SIZE:ETH_SIZE+1])
				ip_header_length = ""
				ip_header_length = str(hex(ip_version_length[0]))
				num_length = int(ip_header_length[3]) # header_length 값을 받아옴

				ip_header = make_ip_header(data[ETH_SIZE:ETH_SIZE+4*num_length]) # ip header를 추출 (header_length 만큼)
		
				for item in ip_header.items():
					print('{0} : {1}'.format(item[0], item[1]))
				dumpcode(data)
				if os.name == 'nt':
					sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
			else: # ether_type이 IPv4가 아닌 경우
				continue
def make_ethernet_header(raw_data):
	ether = struct.unpack('!6B6BH', raw_data)
	print('[1] ETHERNET_PACKET----------------------------------')
	return {'[dst]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
		'[src]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
		'[ether_type]':ether[12]}

def make_ip_header(raw2_data):
	ip = struct.unpack('!BBHHBBBBH4B4B',raw2_data)
	print('\n[2] IP_PACKET----------------------------------------')
	hex_versionlength= ""
	hex_versionlength = str(hex(ip[0])) # ip header의 첫 1byte를 받아옴
	version = int(hex_versionlength[2]) # version(4)을 int형으로 변수에 저장
	header_length = int(hex_versionlength[3]) # header_length(5)를 int형으로 변수에 저장
	return{'[version]':'%x' % version,
		'[header_length]':'%x' % header_length,
		'[tos]':'%x' % ip[1],
		'[total_length]':'%d' % ip[2],
		'[id]':'%d' % ip[3],
		'[flag]':'%x' % ip[4],
		'[offset]':'%x' % ip[5],
		'[ttl]':ip[6],
		'[protocol]':ip[7],
		'[checksum]':ip[8],
		'[src]':'%d:%d:%d:%d' % ip[9:13],
		'[dst]':'%d:%d:%d:%d' % ip[13:17]}
	
def dumpcode(buf):
	print("\n")
	print('Raw Data')
	print("%7s"% "offset ", end='')

	for i in range(0, 16):
		print("%02x " % i, end='')

		if not (i%16-7):
			print("- ", end='')

	print("")

	for i in range(0, len(buf)):
		if not i%16:
			print("0x%04x" % i, end= ' ')

		print("%02x" % buf[i], end= ' ')

		if not (i % 16 - 7):
			print("- ", end='')

		if not (i % 16 - 15):
			print(" ")

	print("\n")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')
	parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
	args = parser.parse_args()

	while True: 
		sniffing(args.i)