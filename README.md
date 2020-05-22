# Network-Socket-and-Packet-Sniffing-on-Linux

This is about socket communication and packet sniffing on the network. Development language is Python, and the driving test was performed through Linux.

<h2>JEONGMUK LIM <br>
Department of Computer Science<br>
Chungbuk National University<br>
<br>
충북대학교 컴퓨터공학과 임정묵<h2><br>

 <br>
 
-Conditions <br>

1) Output of Ethernet and IP headers <br>
2) Using while statement to write multiple times <br>
3) Read the part that contains the length of the IP header first, then cut the IP header part based on the value and parse it. <br>
4) The IP header option does not need to be considered. <br>
5) Write only when Ethernet Type is IPv4 <br>
<br>
<br>
● packet_sniffer.py <br>
○ -i : NIC Name <br>
<br>
<br>
● server.py <br>
○ -p: port number for connection <br>
<br>
<br>
● client.py <br>
○ -p: port number for connection <br>
○ -i:  host address <br>
<br>
<br>

### Input Example (Packet Sniffing)
	$ python3 packet_sniffer.py -i lo
	
### Input Example (Client-Server)
	$ python server.py -p 8888
	$ python client.py -i 127.0.0.1 -p 8888
  
  
![alt text](https://github.com/mook6688/jeongmoogy/blob/master/6%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C/result.PNG)

![alt text](https://github.com/mook6688/jeongmoogy/blob/master/6%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C/result.PNG)

![alt text](https://github.com/mook6688/jeongmoogy/blob/master/6%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C/result.PNG)


