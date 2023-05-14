import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import matplotlib.animation as animation
import numpy as np
from functools import partial
import random
from algos import bubbleSort

algo_list = ['BubbleSort', 'SelectionSort']
inpt_qty = None
iteration = [0]
bar_rects = None
generator = None


def btncall(input_nr,input_str,input_ms):
    if input_str.text_disp._text == 'BubbleSort':
        print('Hello World!')
        print(input_nr.text_disp._text)
        print(input_str.text_disp._text)
        print(input_ms.text_disp._text)
        ax.set_title(input_str.text_disp._text)

        lst = genRandomNr(int(input_nr.text_disp._text))
        generator = bubbleSort(lst)
        bar_rects = ax.bar(range(len(lst)),lst,align='edge')
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        update_fig(lst, bar_rects, iteration, text, generator)
    elif input_str.text_disp._text == 'Type':
        pass
    else:
        raise Exception('Exception Error wrong input')


def update_fig(A, rects, iteration, text, generator):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))
     



def genRandomNr(qty):
   rnd_list = []
   for x in range(qty):
    x = random.randint(1,100)
    rnd_list.append(x)
   print(rnd_list)
   return rnd_list

  

fig, ax = plt.subplots()
ax.set_ylabel(' Y Label')
ax.set_xlabel(' X Label')
ax.set_title('Sound of Sorting')
ax.text(0.15,-0.35,'Select one Algo: '+ ' '.join(algo_list))
plt.subplots_adjust(bottom=0.30,left=0.20)

input_nr_ax = fig.add_axes([0.15,0.01,0.13,0.05])
input_nr = TextBox(input_nr_ax,'Qty Dataset',initial='1')

input_str_ax = fig.add_axes([0.40,0.01,0.13,0.05])
input_str = TextBox(input_str_ax,'Algo',initial='Type')

input_ms_ax = fig.add_axes([0.6,0.01,0.13,0.05])
input_ms = TextBox(input_ms_ax,'MS',initial='1000')

bubble_pos = fig.add_axes([0.8,0.01,0.13,0.05])
bubble_btn = Button(bubble_pos,label='Start',color='red')
par = partial(btncall,input_str,input_ms)
bubble_btn.on_clicked(par)

anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)

plt.show()