import matplotlib.pyplot as plt
import numpy as np
import random
from algos import bubbleSort
bar_width = 0.25


        
# fig, ax = plt.subplots(layout='constrained',Tite)

# ax.set_ylabel(' Y Label')
# ax.set_xlabel(' X Label')
# ax.set_title('Sound of Sorting')



# plt.show()

rnd_length = random.randint(1,100)
print(rnd_length)

bubble_sort_list = []

for x in range(rnd_length):
    x = random.randint(1,100)
    bubble_sort_list.append(x)

print(bubble_sort_list)
print(len(bubble_sort_list))

bubbleSort(bubble_sort_list)
print(bubble_sort_list)