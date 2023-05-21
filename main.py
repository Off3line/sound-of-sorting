from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import numpy as np
import os
import random
import simpleaudio as sa
from algos import bubbleSort,insertionSort,quickSort,cycleSort,heapSort,selectionSort,shellSort
from graphic import Graphic
from sound_writer import SoundWriter
from array_tracker import ArrayTracker
algo_list = ['BubbleSort','QuickSort','InsertionSort','CycleSort','HeapSort','SelectionSort','ShellSort']
QTY_LIST = 0


def genRandomNr(high):
    lst=[]
    for i in range(0,high+1):
        x = i
        lst.append(x)
    random.shuffle(lst)
    print(lst)
    return lst
# def genRandomNr(high):
#     arr = np.round(np.linspace(0, high, high), 0)
#     np.random.seed(0)
#     np.random.shuffle(arr)
#     arr = ArrayTracker(arr)
#     np.random.seed(0)
#     return arr


def onClick():
    
    ms_val = int(ms_inp.get())
    high_val = int(high_inp.get())
    QTY_LIST = high_val
    alg_val = algo_inp.get()

    rnd_list = genRandomNr(high_val)
    at = ArrayTracker(rnd_list)
    main(alg_val,high_val,at,ms_val)

def main(algo,highest,at,ms):

    if  algo == "BubbleSort":
        title = "Bubble Sort"
        bubbleSort(at)
    
    elif algo == "InsertionSort":
        title = "Insertion Sort"
        insertionSort(at)

    elif algo == "QuickSort":
        title = "Quick Sort"
        quickSort(at, 0, len(at) - 1)

    elif algo == 'CycleSort':
        title = 'Cycle Sort'
        cycleSort(at)

    elif algo == 'HeapSort':
        title = 'Heap Sort'
        heapSort(at)

    elif algo == 'SelectionSort':
        title = 'Selection Sort'
        selectionSort(at,len(at))

    elif algo == 'ShellSort':
        title = 'Shell Sort'
        shellSort(at)
    
    if cbox.instate(['selected']) is False:
        SoundWriter(at,10,highest,ms).generate()
        dir = os.getcwd() + '/tones.wav'
        wave_obj = sa.WaveObject.from_wave_file(dir)
        play_obj = wave_obj
        play_obj.play()


    gr = Graphic(at,QTY_LIST,title,ms)
    gr.generate()



root = Tk(className='Sound of Sorting')

high_lbl = ttk.Label(root,text='Define Value n')
high_inp = ttk.Entry(root)
high_inp.insert(0,'15')

algo_lbl = ttk.Label(root,text='Enter Algo:')
algo_inp = ttk.Combobox(root,values=algo_list)
algo_inp.set('BubbleSort')

ms_lbl = ttk.Label(root,text='Delay in Ms')
ms_inp = ttk.Entry(root)
ms_inp.insert(0,'500')
btn = ttk.Button(root,text='Start',command=onClick)

cbox = ttk.Checkbutton(root,text='Disable Sound?',takefocus=0)
cbox.state(['!alternate'])

high_lbl.grid(row=0,column=0,padx=30)
high_inp.grid(row=0,column=1,padx=10)
algo_lbl.grid(row=1,column=0,padx=30)
algo_inp.grid(row=1,column=1,padx=10)
ms_lbl.grid(row=2,column=0,padx=30)
ms_inp.grid(row=2,column=1,padx=10)
cbox.grid(row=3,column=0,padx=10)
btn.grid(row=4,column=0,padx=10)

root.mainloop()