import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os






class Graphic():

    def __init__(self, array, n, sorter, fps):
        self.array = array
        self.n = n
        self.sorter = sorter
        self.fps = fps

    def generate(self):
        fig, ax = plt.subplots()

        self.container = ax.bar(range(len(self.array)), self.array)
        fig.suptitle(f"{self.sorter} sort")
        ax.set(xlabel="Index", ylabel="Value")
        ax.set_xlim(self.n)
        self.txt = ax.text(0.01, 0.99, "", ha="left",
                           va="top", transform=ax.transAxes)

        ani = FuncAnimation(fig, self.update, frames=range(len(self.array.full_copies)),
                            blit=True, interval=1000./self.fps, repeat=False)
        plt.show()

    def update(self, frame):
        self.txt.set_text(f"Nr of Operations = {frame}")
        for rectangle, height in zip(self.container.patches, self.array.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#cf6f34")

        idx, op = self.array.GetActivity(frame)
        if op == "get":
            self.container.patches[idx].set_color("magenta")
        elif op == "set":
            self.container.patches[idx].set_color("green")
        return (self.txt, *self.container)
