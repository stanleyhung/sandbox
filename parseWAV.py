# This script extracts audio samples from an .wav file
# @author Stanley Hung

#helper function in case of any errors

import struct

def error(actual, expected):
	print "ERROR, expected: ", expected, " received: ", actual
	exit(1)

fileName = "10. Horn Of Plenty.wav"
f = open(fileName, "r")
header = f.read(4)
if header != 'RIFF':
	error(header, 'RIFF')
chunkSize = f.read(4)
format = f.read(4)
if format != 'WAVE':
	error(format, 'WAVE')
fmtID = f.read(4)
if fmtID != 'fmt ':
	error(fmtID, 'fmt ')
subChunkSize1 = struct.unpack('i', f.read(2))[0]
if subChunkSize1 != 16:
	error(subChunkSize1, 16)


print 'SUCCESS'