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
def volume(audio):
    total = 0
    length = math.floor(len(audio) / 16)
    for i in range(length):
        nextvalue = audio[(i * 2) + 1]
        if (nextvalue != 0x00) and (nextvalue != 0x01):
            total += audio[i * 2]
        print(audio[ (i * 2) : ((i * 2) + 2) ])
    return total / length
CHUNK = 11025
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
stream = p.open(format=FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = CHUNK)
try:
    while True:
        data = stream.read(CHUNK)
        vol = volume(data)
        print("Volume: ", vol)
        barfrom(vol, 80, 130, 10)
except KeyboardInterrupt:
    print("Stopping...")
