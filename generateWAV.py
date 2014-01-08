
import struct

#set .wav file attributes
fileName = "test.wav"
numSamples = 7500*3
Numchannels = 1
sampleRate = 6000
bitsPerSample = 8
byteRate = sampleRate * Numchannels * bitsPerSample/8
subchunksize = Numchannels * bitsPerSample/8 * numSamples
chunkSize = 36 + subchunksize

f = open(fileName, 'w')

#Write RIFF header
f.write('RIFF')
f.write(struct.pack('i', chunkSize))
f.write('WAVE')

#write WAVE format header
f.write('fmt ')
f.write(struct.pack('i', 16)) #16 = PCM
f.write(struct.pack('h', 1)) #Audioformat = PCM (1)
f.write(struct.pack('h', Numchannels))
f.write(struct.pack('i', sampleRate))
f.write(struct.pack('i', byteRate))
f.write(struct.pack('h', Numchannels * bitsPerSample / 8))
f.write(struct.pack('h', bitsPerSample))

#write WAVE data subchunk
f.write('data')
f.write(struct.pack('i', subchunksize))

#determine what struct to use to write data
if bitsPerSample == 8:
	format = 'B'
elif bitsPerSample == 16:
	format = 'h'
elif bitsPerSample == 32:
	format = 'i'
else:
	format = 'x'

#write data
for i in range(0, numSamples/3):
	f.write(struct.pack(format, 128))

for i in range(0, numSamples/3):
	f.write(struct.pack(format, 127))

for i in range(0, numSamples/3):
	f.write(struct.pack(format, 128))

f.flush()