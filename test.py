import pygame
from pygame.locals import *
from tones import SINE_WAVE, SAWTOOTH_WAVE
from tones.mixer import Mixer

import math
import numpy as np
SF    = 44100         # HZ sampling frequency
DELAY = 50             # ms
MAXSOUND = 20000       # sound volumn
MAXF  = 4000           # max frequency
MINF  = 400            # min frequency
LENGTH = 15
def get_sound_list(n, min_f=MINF, max_f = MAXF, 
                    time_delay=DELAY,sampling_frequency=SF, max_sound=MAXSOUND):
    print("Preparing sound dict ...")
    step = (max_f-min_f)//n
    sound_list = []
    for idx, f in enumerate(range(min_f, max_f, step)):
        if idx<n:
            sound_list.append(make_sound(f, time_delay=time_delay))
    return sound_list

def make_sound(frequency, time_delay=DELAY,sampling_frequency=SF, max_sound=MAXSOUND):
    t = 2*np.pi*frequency*np.arange(time_delay*sampling_frequency/1000)/sampling_frequency
    marray = max_sound*np.sin(t)
    marray = marray.astype(np.int16)
    return marray

def freq_map(x, x_min=0, x_max=10, freq_min=120, freq_max=1200):
        """ map a value x to a frequency f and return a chunk of that frequency for the specificed time dt"""
        return np.interp(x, [x_min, x_max], [freq_min, freq_max])

data = [x for x in range(LENGTH)]
# marks = (1,2)
# print(data)
# pygame.mixer.init(SF,-16,1,2048)
# sndList = get_sound_list(LENGTH)
# print(sndList)
# sound_mixer = list(map(pygame.sndarray.make_sound, sndList))
# pygame.mixer.Channel.queue()
# print(sound_mixer)
# sound_mixer[data[marks[0]]].play()
mixer = Mixer(44100, 0.5)
mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)

lst = (0,1,2,3,4,5,6,7,8,9,10)

for value in lst:
     freq = freq_map(value)
     mixer.add_tone(1,freq,0.016)
     print(freq)
mixer.write_wav('tones.wav')