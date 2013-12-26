# This script extracts audio samples from an .wav file
# @author Stanley Hung

#helper function in case of any errors

import struct

def error(actual, expected):
	print "ERROR, expected: ", expected, " received: ", actual
	exit(1)

#Get WAV information from file
wavName = "26. I Need You"
fileName = wavName + ".wav"
print "Getting WAV metadata from file: " + fileName
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
subChunkSize1 = struct.unpack('I', f.read(4))[0]
if subChunkSize1 != 16:
	error(subChunkSize1, 16)
audioFormat = struct.unpack('H', f.read(2))[0]
if audioFormat != 1:
	error(audioFormat, 1)
numChannels = struct.unpack('H', f.read(2))[0]
if numChannels != 1 and numChannels != 2:
	error(numChannels, 1)
sampleRate = struct.unpack('I', f.read(4))[0]
if sampleRate != 8000 and sampleRate != 44100:
	error(sampleRate, 44100)
byteRate = struct.unpack('I', f.read(4))[0]
blockAlign = struct.unpack('H', f.read(2))[0]
bitsPerSample = struct.unpack('H', f.read(2))[0]
bytesPerSample = bitsPerSample / 8
dataHeader = f.read(4)
if dataHeader != 'data':
	error(dataHeader, 'data')
dataSize = struct.unpack('I', f.read(4))[0]
numSamples = (dataSize / numChannels) / bytesPerSample
print "There are " + str(numSamples) + " samples in the files"

#write WAV metadata into output file
fileName = wavName + ".csv"
print "Writing WAV metadata into output file: " + fileName
f2 = open(fileName, 'w')
f2.write(wavName + '\n')
f2.write('numChannels,' + str(numChannels) + ',sampleRate,' + str(sampleRate) +
	',AvgBytesPerSec,' + str(byteRate) + ',bitsPerSample,' + str(bitsPerSample) +
	'\n')
for i in range(0, numChannels):
	f2.write('channel ' + str(i) + ',')
f2.write('\n')	

#determine how the data is stored (endianess)
if bytesPerSample == 1:
	#unsigned byte
	storageType = 'B'
elif bytesPerSample == 2:
	#signed integer
	storageType = 'h'
elif bytesPerSample == 4:
	storageType = 'i' 

#parse and write sample data
print "Beginning to parse data...\n"
done = False
while True:
	for i in range(0, numChannels):
		data = f.read(bytesPerSample)
		if data != "":
			data = struct.unpack(storageType, data)[0]
			f2.write(str(data) + ',')
		else:
			print "length is: " + str(len(data))
			print "data is: " + data
			print "type is: " + str(type(data))
			done = True
	f2.write('\n')
	if done == True:
		break
f2.close()
print 'SUCCESS: samples written to output file'