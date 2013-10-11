import socket;
import sys;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 9))
while True:
	print s.recvfrom(65565)
	sys.stdout.flush()
	break
print "DONE\n"
