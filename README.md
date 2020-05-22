# Network-Socket-and-Packet-Sniffing-on-Linux
This is about socket communication and packet sniffing on the network. Development language is Python, and the driving test was performed through Linux.
================================
충북대학교 컴퓨터공학과 임정묵(2015040033)
================================
-Conditions <br>

1) Output of Ethernet and IP headers <br>
2) Using while statement to write multiple times <br>
3) Read the part that contains the length of the IP header first, then cut the IP header part based on the value and parse it. <br>
4) The IP header option does not need to be considered. <br>
5) Write only when Ethernet Type is IPv4 <br>

● packet_sniffer.py <br>

○ -i : NIC Name <br>


### Input Example
	$ python3 packet_sniffer.py -i lo
