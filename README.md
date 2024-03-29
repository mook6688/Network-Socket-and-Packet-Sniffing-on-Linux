# Network Socket and Packet Sniffing on Linux
-------------------------------------------------------
### This is about socket connection and packet sniffing on the network. PL is Python, and the driving test was performed through Linux.
-------------------------------------------------------
<h2> JEONGMUK LIM <br>
Department of Computer Science<br>
Chungbuk National University<br>

> ### - Conditions<br>
>
> 1) Output of Ethernet and IP headers <br>
> 2) Using while statement to write multiple times <br>
> 3) Read the part that contains the length of the IP header first, then cut the IP header part based on the value and parse it. <br>
> 4) The IP header option does not need to be considered. <br>
> 5) Write only when Ethernet Type is IPv4 <br>

<br>
<br>
  ● packet_sniffer.py <br>
  ○ -i : NIC Name <br>
<br>

● server.py <br>
○ -p: port number for connection <br>
<br>

● client.py <br>
○ -p: port number for connection <br>
○ -i:  host address <br>
<br>


### Input Example (Packet Sniffing)
	$ python3 packet_sniffer.py -i lo
	
### Input Example (Client-Server)
	$ python server.py -p 8888
	$ python client.py -i 127.0.0.1 -p 8888
  
### ● Result for Packet Sniffing by packet_sniffer.py

![alt text](https://github.com/mook6688/Network-Socket-and-Packet-Sniffing-on-Linux/blob/master/Result/result.png)

### ● Result for Socket Communication between Server-Client by server.py and client.py

![alt text](https://github.com/mook6688/Network-Socket-and-Packet-Sniffing-on-Linux/blob/master/Result/result(server-client).png)



