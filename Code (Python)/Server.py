import socket

UDP_IP = ¨192.168.137.81¨
UDP_port = 5005 #domain

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
  
	Message = str(value)
  
	sock.sendto(Message.encode(), (UDP_IP, 	UDP_port))
