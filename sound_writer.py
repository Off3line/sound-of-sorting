import numpy as np
import scipy as sp
import os
from tones import SINE_WAVE
from tones.mixer import Mixer
F_SAMPLE = 44100
OVERSAMPLE = 2

# Worked out this code together with Christian.
class SoundWriter():

    def __init__(self, arr,max,ms):
        self.array = arr
        self.max = max
        self.ms = ms
        self.mixer = Mixer(F_SAMPLE, 0.5)
        self.mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)
    def generate(self):
    
        acc = []
        print('Values from sound ',self.array.values)
        print('Value size from sound', len(self.array.values))
        for i, value in enumerate(self.array.values):
            freq = self.freq_map(value,x_max=self.max)
            acc.append(freq)
    
            # calc = len(self.array.full_copies)/ 500
            self.mixer.add_tone(1,freq,duration=self.ms/1000)
            freq = self.freq_map(value, x_max=self.max)
            # sample = self.freq_sample(freq, dt=1./self.fps, samplerate=F_SAMPLE,
            #                           oversample=OVERSAMPLE)
            # print('Sample for given freq', sample)
            # idx_0 = np.int((i+0.5)*dN - len(sample)/2)
            # idx_1 = idx_0 + len(sample)

            # try:
            #     wav_data[idx_0:idx_1] = wav_data[idx_0:idx_1] + sample
            # except ValueError:
            #     continue
       

        # wav_data = (2**15*(wav_data/np.max(np.abs(wav_data)))).astype(np.int16)
        freq_lowest = self.freq_map(0)
        self.mixer.add_tone(1,freq_lowest,duration=self.ms/1000)
        acc.append(freq_lowest)
        for x in self.array.full_copies[-1]:
            freq = self.freq_map(x,x_max=self.max)
            self.mixer.add_tone(1,freq,duration=self.ms/1000)
            acc.append(freq)
        print('Freq generated ', len(acc))
        self.mixer.write_wav('tones.wav')

        # folder = "sound"
        # if not os.path.exists(folder):
        #     os.makedirs(folder)

        # sp.io.wavfile.write(f"{folder}/sound.wav", F_SAMPLE, wav_data)


    def freq_map(self, x, x_min=0, x_max=100, freq_min=120, freq_max=1200):
        """ map a value x to a frequency f and return a chunk of that frequency for the specificed time dt"""
        return np.interp(x, [x_min, x_max], [freq_min, freq_max])

    # def freq_sample(self, freq, dt=1./60., samplerate=44100, oversample=2):
    #     """Create a sample with a specific freqency {freq} for a specified
    #     time {dt}"""
    #     mid_samples = np.int(dt * samplerate)
    #     pad_samples = np.int((mid_samples*(oversample-1)/2))
    #     total_samples = mid_samples + 2*pad_samples

    #     y = np.sin(2 * np.pi * freq * np.linspace(0, dt, total_samples))
    #     y[:pad_samples] = y[:pad_samples] * np.linspace(0, 1, pad_samples)
    #     y[- pad_samples:] = y[len(y) - pad_samples:] * \
    #         np.linspace(1, 0, pad_samples)
    #     return y
