import ggwave
import pyaudio

p = pyaudio.PyAudio()

# generate audio waveform for string "hello python"
waveform = ggwave.encode("Hello!!!", txProtocolId = 1, volume = 20)

print("Transmitting text 'hello python' ...")
stream = p.open(format=pyaudio.paFloat32, channels=2, rate=48000, output=True, frames_per_buffer=4096)
stream.write(waveform, len(waveform)//4)
stream.stop_stream()
stream.close()

p.terminate()