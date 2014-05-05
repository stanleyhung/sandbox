import socket
#Creates a socket object that uses IP addressing with UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Sends a magic packet (6 bytes of FF strings followed by PC's MAC address 16 times)
s.connect((socket.gethostbyname(socket.gethostname()), 9))
s.sendall('Turn On')