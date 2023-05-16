import numpy as np
import scipy as sp
import os
from os.path import exists

F_SAMPLE = 44100
OVERSAMPLE = 2

dir = "d:\Privat\git\plp-assignments\Christian\Assignment_2" if os.getcwd(
) == "d:\Privat\git\plp-assignments" else os.getcwd()


class SoundGenerator():

    def __init__(self, arr, fps):
        self.array = arr
        self.fps = fps

    def generate(self):
        wav_data = np.zeros(np.int(F_SAMPLE*len(self.array.values)* 1./self.fps), dtype=np.float64)
        dN = np.int(F_SAMPLE * 1./self.fps)  # how many samples is each chunk

        for i, value in enumerate(self.array.values):

            freq = self.freq_map(value)

            sample = self.freq_sample(freq, dt=1./self.fps, samplerate=F_SAMPLE,
                                      oversample=OVERSAMPLE)

            idx_0 = np.int((i+0.5)*dN - len(sample)/2)
            idx_1 = idx_0 + len(sample)

            try:
                wav_data[idx_0:idx_1] = wav_data[idx_0:idx_1] + sample
            except ValueError:
                continue

        wav_data = (2**15*(wav_data/np.max(np.abs(wav_data)))).astype(np.int16)
        if exists(dir+'/sound/sound.wav'):
            sp.io.wavfile.write(
                f"{dir}/sound/sound.wav", F_SAMPLE, wav_data)
        else:
            os.makedirs(dir+'/sound')
            sp.io.wavfile.write(dir+ '/sound/sound.wav',F_SAMPLE,wav_data)

    def freq_map(self, x, x_min=0, x_max=1000, freq_min=120, freq_max=1200):
        """ map a value x to a frequency f and return a chunk of that frequency for the specificed time dt"""
        return np.interp(x, [x_min, x_max], [freq_min, freq_max])

    def freq_sample(self, freq, dt=1./60., samplerate=44100, oversample=2):
        """Create a sample with a specific freqency {freq} for a specified
        time {dt}"""
        mid_samples = np.int(dt * samplerate)
        pad_samples = np.int((mid_samples*(oversample-1)/2))
        total_samples = mid_samples + 2*pad_samples

        y = np.sin(2 * np.pi * freq * np.linspace(0, dt, total_samples))
        y[:pad_samples] = y[:pad_samples] * np.linspace(0, 1, pad_samples)
        y[- pad_samples:] = y[len(y) - pad_samples:] * \
            np.linspace(1, 0, pad_samples)
        return y
