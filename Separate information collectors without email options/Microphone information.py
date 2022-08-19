from scipy.io.wavfile import write
import sounddevice as sd

audio_information = "audio.wav"

microphone_time = 10

file_path = "C:\Info-logger\Logged_information"
extend = "\\"
file_merge = file_path + extend

def microphone():
    fs = 44100
    seconds = microphone_time
    sd.default.samplerate = fs
    sd.default.channels = 2

    myrecording = sd.rec(int(seconds * fs))
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)
    
microphone()