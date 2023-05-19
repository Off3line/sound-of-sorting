import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import numpy as np
import random
import simpleaudio as sa
import os
from algos import bubbleSort,insertionSort,quickSort
from graphic import Graphic
from sound_generator import SoundGenerator
from array_tracker import ArrayTracker
algo_list = ['BubbleSort','QuickSort','InsertionSort']
txt = ''
QTY_LIST = 0



def genRandomNr(high):
    lst=[]
    for i in range(0,high+1):
        x = i
        lst.append(x)
    random.shuffle(lst)
    print(lst)
    return lst

def onClick():
    
    ms_val = int(ms_inp.get())
    high_val = int(high_inp.get())
    QTY_LIST = high_val
    alg_val = algo_inp.get()

    rnd_list = genRandomNr(high_val)
    at = ArrayTracker(rnd_list)
    main(rnd_list,alg_val,high_val,at)

def main(randList,algo,highest,at):

    if  algo == "BubbleSort":
        title = "Bubble Sort"
        bubbleSort(at)
    
    elif algo == "InsertionSort":
        title = "Insertion Sort"
        #generator = insertionSort(randList)

    elif algo == "QuickSort":
        title = "Quick Sort"
        #generator = quickSort(randList, 0, len(randList) - 1)

    # Initialize figure and axis.
  
    SoundGenerator(at,62).generate()
    dir = os.getcwd() + '/sound/sound.wav'
    wave_obj = sa.WaveObject.from_wave_file(dir)
    play_obj = wave_obj.play()

    gr = Graphic(at,QTY_LIST,title,60)
    gr.generate()


   


root = Tk(className='Sound of Sorting')

high_lbl = ttk.Label(root,text='Define Value n')
high_inp = ttk.Entry(root)
high_inp.insert(0,'10')

algo_lbl = ttk.Label(root,text='Enter Algo:')
algo_inp = ttk.Combobox(root,values=algo_list)
algo_inp.set('BubbleSort')

ms_lbl = ttk.Label(root,text='Delay in Ms')
ms_inp = ttk.Entry(root)
ms_inp.insert(0,'16')
btn = ttk.Button(root,text='Start',command=onClick)

high_lbl.grid(row=0,column=0,padx=30)
high_inp.grid(row=0,column=1,padx=10)
algo_lbl.grid(row=1,column=0,padx=30)
algo_inp.grid(row=1,column=1,padx=10)
ms_lbl.grid(row=2,column=0,padx=30)
ms_inp.grid(row=2,column=1,padx=10)

btn.grid(row=3,column=0,padx=10)

root.mainloop()