import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scipy as sp
from scipy.io import wavfile
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from algos import bubbleSort,insertionSort,quickSort
from sound_generator import SoundGenerator
from array_tracker import ArrayTracker
import simpleaudio as sa
import os

ms_val = 1

algo_list = ['BubbleSort', 'SelectionSort','QuickSort','InsertionSort']

N = 30
FPS = 50
OVERSAMPLE = 2
F_SAMPLE = 44100

def genRandomNr(qty):
    arr = np.round(np.linspace(0, 1000, qty), 0)
    np.random.seed(0)
    np.random.shuffle(arr)
    arr = ArrayTracker(arr)
    np.random.seed(0)
    return arr


def main(method,A,N):
     # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "BubbleSort":
        title = "Bubble sort"
        generator = bubbleSort(A)
    elif method == "InsertionSort":
        title = "InsertionSort"
        generator = insertionSort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "QuickSort":
        title = "Quick Sort"
        generator = quickSort(A, 0, N - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(A)

    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    # bar_rects = ax.bar(range(len(A)), A, align="edge")
    bar_rects = ax.bar(np.arange(0,len(A),1),
                       A.full_copies[0], align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    
    iteration = [0]
    def update_fig(frame):
        for rect, val in zip(bar_rects.patches, A.full_copies[frame]):
            rect.set_height(val)
            rect.set_color("#1f77b4")
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

        idx, op = A.GetActivity(frame)
        if op == "get":
            bar_rects.patches[idx].set_color("magenta")
        elif op == "set":
            bar_rects.patches[idx].set_color("red")

    anim = animation.FuncAnimation(fig, update_fig, frames=range(len(A.full_copies)),
        interval=1000./FPS, repeat=False,cache_frame_data=False)
    
    sg = SoundGenerator(A,FPS)
    sg.generate()
    dir = os.getcwd() + '/sound/sound.wav'
    filename = dir
    wave_obj = sa.WaveObject.from_wave_file(filename)
    
    play_obj = wave_obj.play()
    plt.show()
    

def onClick():
    
    qty_val = int(qty_inp.get())
    alg_val = algo_inp.get()
    global ms_val
    ms_val = int(ms_inp.get())

    rnd_list = genRandomNr(qty_val)
    main(alg_val,rnd_list,qty_val)

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


