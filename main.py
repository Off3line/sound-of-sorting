import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import random

algo_list = ['BubbleSort', 'SelectionSort','QuickSort','InsertionSort']

QTY_LIST = 30

def onClick():
    global ms_val
    ms_val = int(ms_inp.get())
    high_val = int(high_inp.get())
    alg_val = algo_inp.get()

    rnd_list = genRandomNr(high_val)

def genRandomNr(high):
    lst=[]
    for i in range(QTY_LIST):
        x = random.uniform(1,high)
        lst.append(x)
    print(lst)
    return lst



root = Tk(className='Sound of Sorting')

high_lbl = ttk.Label(root,text='Highest value')
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