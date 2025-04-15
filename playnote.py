import numpy as np
import sounddevice as sd

#defining a function to play sound
def playnote(freq, duration=1.0, sample_rate=44100, amplitude=0.5):
    t=np.linspace(0,duration, int(sample_rate*duration), False)
    wave= amplitude*np.sin(2*np.pi*freq*t)
    sd.play(wave,samplerate=sample_rate)
    sd.wait()

#example
f=[130.8,146.8,164.8,174.6,196.0,220.0,246.9,261.6]
playnote(f[2])
playnote(f[3])
playnote(f[4])
playnote(f[2])
playnote(f[3])
playnote(f[2])
playnote(f[1])