import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Thread server -p port")
parser.add_argument('-p', help = "port_number", required = True)
args = parser.parse_args()

host = '127.0.0.1'
port =  int(args.p) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept() 
print("채팅 환경 구축 중..")
print("연결 완료!")
print('연결된 클라이언트 주소 : ', addr[0], ':', addr[1]) 

data = "보낼 문자열을 입력하세요."
conn.send(data.encode('utf-8'))

def sendMessage(): #클라이언트에 채팅 보낼 때
    while True:
        data = input()  # 입력을 str로 data에 저장
        data = '[server] : ' + data
        data = data.encode("utf-8") #보내는 data utf-8로 인코딩
        conn.send(data)


def recvMessage(): #클라이언트로 부터 채팅을 받을 때
    while True:
        data = conn.recv(1024)
        if not data: 
            continue
        else :
            data = data.decode("utf-8") #utf-8로 디코딩
            print('[client] : ' + data)


threading._start_new_thread(sendMessage, ()) #보내는 thread start
threading._start_new_thread(recvMessage, ()) #받는 thread start

while True: 
        pass