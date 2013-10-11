import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.0.0', 9))
while True:
	print s.recvfrom(65565)
