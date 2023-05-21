import numpy as np
from tones import SINE_WAVE
from tones.mixer import Mixer
F_SAMPLE = 44100
OVERSAMPLE = 2

# Some of the lines of code below are due to working together with Christian.
class SoundWriter():

    def __init__(self, arr,max,ms):
        self.array = arr
        self.max = max
        self.ms = ms
        self.mixer = Mixer(F_SAMPLE, 0.5)
        self.mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)
    def generate(self):
        
        acc = []
        for i, value in enumerate(self.array.values):
            freq = self.freq_map(value,x_max=self.max)
            acc.append(freq)
    
            self.mixer.add_tone(1,freq,duration=self.ms/1000)
            self.mixer.add_silence(1,duration=0.01)
            freq = self.freq_map(value, x_max=self.max)
       
        freq_lowest = self.freq_map(0)
        self.mixer.add_tone(1,freq_lowest,duration=self.ms/1000)
        acc.append(freq_lowest)
        for x in self.array.full_copies[-1]:
            freq = self.freq_map(x,x_max=self.max)
            self.mixer.add_tone(1,freq,duration=self.ms/1000)
            self.mixer.add_silence(1,duration=0.01)
            acc.append(freq)
        self.mixer.write_wav('tones.wav')

    def freq_map(self, x, x_min=0, x_max=100, freq_min=120, freq_max=1200):
        """ map a value x to a frequency f and return a chunk of that frequency for the specificed """
        return np.interp(x, [x_min, x_max], [freq_min, freq_max])
