import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Echo client -p port -i host")
parser.add_argument('-p', help = "port_number", required = True)
parser.add_argument('-i', help = "host_name", required = True)
args = parser.parse_args()

host = args.i
port = int(args.p)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recvChat(): #서버로 부터 채팅 받을 때
    while True:
        try:
            data = s.recv(1024)
            if not data:
                continue
            print(data.decode('utf-8'))
        except:
            pass

def sendChat(): #서버로 채팅 보낼 때
    while True:
        data = input()
        data = data.encode('utf-8')
        s.send(data)

threading._start_new_thread(sendChat, ()) #보내는 thread
threading._start_new_thread(recvChat, ()) #받는 thread 

while True:
    pass