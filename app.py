import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
import random
from algos import bubbleSort


        
def btncall(*args):
    print('Hello World!')

# rnd_length = random.randint(1,100)
# print(rnd_length)

# bubble_sort_list = []

# for x in range(rnd_length):
#     x = random.randint(1,100)
#     bubble_sort_list.append(x)

# print(bubble_sort_list)
# print(len(bubble_sort_list))

# bubbleSort(bubble_sort_list)
# print(bubble_sort_list)

fig, ax = plt.subplots()

ax.set_ylabel(' Y Label')
ax.set_xlabel(' X Label')
ax.set_title('Sound of Sorting')
plt.subplots_adjust(bottom=0.20,left=0.20)

input_nr_ax = fig.add_axes([0.15,0.01,0.13,0.05])
input_nr = TextBox(input_nr_ax,'Qty Dataset',initial='4')

bubble_pos = fig.add_axes([0.8,0.01,0.13,0.05])
bubble_btn = Button(bubble_pos,label='Bubble Sort',color='green')
bubble_btn.on_clicked(btncall)


plt.show()