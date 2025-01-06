#Test
import math
import time
import io
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
    print(length)
    length = math.floor(len(audio) / samplebytes)
    for i in range(length):
        total += tointeger(audio, i * samplebytes, samplebytes)
    return total / length
CHUNK = 11025
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
stream = p.open(format=FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)
file = io.open("data.bin", "ab")
try:
    while True:
        data = stream.read(44100)
        vol = volume(data, 2)
        print("Volume: ", vol)
        barfrom(vol, 32000, 33000, 10)
except KeyboardInterrupt:
    print("Stopping...")
