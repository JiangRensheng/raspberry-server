from socket import *
import threading
import sys
import time

HOST ='54.251.99.166'
PORT = 8888
conn_list ={}
def connect(name):
	time.sleep(0.1)
	s= socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(name)
	conn_list[name] = s 
	while 1:
		data = s.recv(1024)
		print data		

def send(msg, frm):
	conn_list[frm].sendall(msg)

def closeall():
	for c in conn_list:
		c.close()

def close(name):
	conn_list[name].close()

t = threading.Thread(target = connect, args=('D',))
t.start()
while 1:
	input=sys.stdin.readline();
	send(input, 'D')