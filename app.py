import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scipy as sp
from scipy.io import wavfile
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from array_tracker import ArrayTracker
from sound_generator import SoundGenerator
from algos import bubbleSort,insertionSort,quickSort
ms_val = 1

algo_list = ['BubbleSort', 'SelectionSort','InsertionSort','QuickSort']

N = 30
FPS = 60
OVERSAMPLE = 2
F_SAMPLE = 44100

# def genRandomNr(qty):
#    rnd_list = []
#    for x in range(qty):
#     x = random.randint(1,100)
#     rnd_list.append(x)
#    print(rnd_list)
#    return rnd_listA =np.round(np.linspace(0, 1000, N), 0)

def genRandomNr(qty):
    A = np.round(np.linspace(0, 1000, N), 0)
    np.random.seed(0)
    np.random.shuffle(A)
    A = ArrayTracker(A)
    return A



# def freq_map(self, x, x_min=0, x_max=1000, freq_min=120, freq_max=1200):
#         """ map a value x to a frequency f and return a chunk of that frequency for the specificed time dt"""
#         return np.interp(x, [x_min, x_max], [freq_min, freq_max])

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
    # return y

def main(method,A):
     # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "BubbleSort":
        title = "Bubble Sort"
        generator = bubbleSort(A)
    elif method == "InsertionSort":
        title = "Insertion Sort"
        generator = insertionSort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, 30 - 1) ##FIXME replace 30 with qty of generated inputs
    elif method == "QuickSort":
        title = "Quicksort"
        generator = quickSort(A, 0, 30 - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(A)



    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(A, rects, iteration):
        # for rect, val in zip(rects, A):
        #     rect.set_height(val)
        # iteration[0] += 1
        # text.set_text("# of operations: {}".format(iteration[0]))
        for rectangle, height in zip(A.container.patches, A.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#1f77b4")

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=range(len(A.full_copies)), interval=1000./FPS,
        repeat=False,cache_frame_data=False)
    
 
    # wav_data = np.zeros(np.int32(F_SAMPLE*len(A)*1./FPS), dtype=np.float64)
    # dN = np.int64(F_SAMPLE * 1./FPS)  # how many samples is each chunk
    
    # for i, value in enumerate(A):
    #     freq = freq_map(value)
    #     sample = freq_sample(freq, dt=1./FPS, samplerate=F_SAMPLE, oversample=OVERSAMPLE)

    #     idx_0 = np.int32((i+0.5)*dN - len(sample)/2)
    #     idx_1 = idx_0 + len(sample)

    #     try:
    #         wav_data[idx_0:idx_1] = wav_data[idx_0:idx_1] + sample
    #     except ValueError:
    #         print(f"Failed to generate {i:.0f}th index sample")

    # wav_data = (2**15*(wav_data/np.max(np.abs(wav_data)))).astype(np.int16)

    # sp.io.wavfile.write(f"{title}_sound.wav", F_SAMPLE, wav_data)

    sg = SoundGenerator(A,FPS)
    sg.generate()

    plt.show()

def onClick():
    
    qty_val = int(qty_inp.get())
    alg_val = algo_inp.get()
    global ms_val
    ms_val = int(ms_inp.get())

    rnd_list = genRandomNr(qty_val)
    main(alg_val,rnd_list)


root = Tk(className='Sound of Sorting')

qty_lbl = ttk.Label(root,text='Qty')
qty_inp = ttk.Entry(root)
qty_inp.insert(0,'10')

algo_lbl = ttk.Label(root,text='Enter Algo:')
algo_inp = ttk.Combobox(root,values=algo_list)
algo_inp.set('BubbleSort')

ms_lbl = ttk.Label(root,text='Delay in Ms')
ms_inp = ttk.Entry(root)
ms_inp.insert(0,'1000')
btn = ttk.Button(root,text='Start',command=onClick)

qty_lbl.grid(row=0,column=0,padx=30)
qty_inp.grid(row=0,column=1,padx=10)
algo_lbl.grid(row=1,column=0,padx=30)
algo_inp.grid(row=1,column=1,padx=10)
ms_lbl.grid(row=2,column=0,padx=30)
ms_inp.grid(row=2,column=1,padx=10)

btn.grid(row=3,column=0,padx=10)

root.mainloop()


