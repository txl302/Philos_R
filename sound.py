import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)


while True:
    data = stream.read(CHUNK)

    print data
    stream.write(data, CHUNK)


stream.stop_stream()
stream.close()

p.terminate()