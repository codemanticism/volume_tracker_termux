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
        value = audio[i * 2]
        nextvalue = audio[(i*2) + 1]
        unsigned = value + (nextvalue * 0x100)
        if nextvalue >= 0x80:
            total -= 0x10000 - unsigned 
        else:
            total += unsigned
    return math.abs( total / length)
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
        #barfrom(vol, 80, 130, 10)
except KeyboardInterrupt:
    print("Stopping...")
