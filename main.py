#Test
import math
import time
import pyaudio
p = pyaudio.PyAudio()
print(p)
def barfrom(value, start, end, long):
    length = (value - start) / (end - start)
    length = length * long
    bar = ""
    for i in range(int(length)):
        bar += "="
    print("[", bar, "]")
def tointeger(data, position, bytecount):
    total = 0
    for i in range(bytecount):
        total = total * 256
        total += data[position + i]
    return total
def volume(audio, samplebytes):
    total = 0
    length = math.floor(len(audio) / samplebytes)
    for i in range(length):
        total += tointeger(audio, i * samplebytes, samplebytes)
    return total / length
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
stream = p.open(format=FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)
try:
    for j in range(10):
        data = stream.read(30)
        for i in range(int( len(data)/2 )):
            integer = tointeger(data, 2*i, 2)
            print(integer)
            barfrom(integer)
except KeyboardInterrupt:
    print("Stopping...")
