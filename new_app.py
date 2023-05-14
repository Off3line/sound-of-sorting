import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from algos import bubbleSort

algo_list = ['BubbleSort', 'SelectionSort']

def genRandomNr(qty):
   rnd_list = []
   for x in range(qty):
    x = random.randint(1,100)
    rnd_list.append(x)
   print(rnd_list)
   return rnd_list

def main(method,A,N):
     # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "BubbleSort":
        title = "Bubble sort"
        generator = bubbleSort(A)
    elif method == "i":
        title = "Insertion sort"
        generator = insertionsort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = quicksort(A, 0, N - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(A)

    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)), A, align="edge")


    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))


    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()

def onClick():
    
    qty_val = int(qty_inp.get())
    alg_val = algo_inp.get()
    ms_val= int(ms_inp.get())
    
    rnd_list = genRandomNr(qty_val)
    main(alg_val,rnd_list,qty_val)


# Get user input to determine range of integers (1 to N) and desired
# sorting method (algorithm).
#  N = int(input("Enter number of integers: "))
#  method_msg = "Enter sorting method:\n(b)ubble\n(i)nsertion\n(m)erge \
#     \n(q)uick\n(s)election\n"
#  method = input(method_msg)

# # Build and randomly shuffle list of integers.
#  A = [x + 1 for x in range(N)]
#  random.seed(time.time())
#  random.shuffle(A)

root = Tk()

qty_lbl = ttk.Label(root,text='Qty')
qty_inp = ttk.Entry(root)
qty_inp.insert(0,'1')

algo_lbl = ttk.Label(root,text='Enter Algo:')
algo_inp = ttk.Combobox(root,values=algo_list)
algo_inp.set('BubbleSort')

ms_lbl = ttk.Label(root,text='MS')
ms_inp = ttk.Entry(root)
ms_inp.insert(0,'1000')
btn = ttk.Button(root,text='Start',command=onClick)

qty_lbl.grid(row=0,column=0,padx=30)
qty_inp.grid(row=0,column=1,padx=10)
algo_lbl.grid(row=1,column=0,padx=30)
algo_inp.grid(row=1,column=1,padx=10)
btn.grid(row=3,column=0,padx=10)

root.mainloop()


