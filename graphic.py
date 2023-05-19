import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os
from threading import Thread
import subprocess




class Graphic():

    def __init__(self, array, n, sorter, ms):
        self.array = array
        self.n = n
        self.sorter = sorter
        self.ms = ms


    def generate(self):
        fig, ax = plt.subplots()

        self.container = ax.bar(range(len(self.array)), self.array,align="edge", width=0.3)
        fig.suptitle(f"{self.sorter}")
        ax.set(xlabel="Index", ylabel="Value")
        ax.set_xlim(self.n)
        plt.xticks(np.arange(min(self.array),max(self.array)+1,1.0))
        self.txt = ax.text(0.01, 0.99, "", ha="left",
                           va="top", transform=ax.transAxes)

        ani = FuncAnimation(fig, self.update, frames=range(len(self.array.full_copies)),
                            blit=True, interval=self.ms, repeat=False)
        
        plt.show()
       
        tr = Thread(target=self.genVideo,args=ani)
        tr.start()

        fig.set_size_inches(10,8)
       

    
    def genVideo(self,ani):
        folder = "videos"
        if not os.path.exists(folder):
         os.makedirs(folder)
    
        ani.save(f'{folder}/video.mp4') 
        cmd_str = "ffmpeg -i videos/video.mp4 -i sound/sound.wav -map 0 -map 1:a -c:v copy -shortest output.mp4"
        subprocess.run(cmd_str, shell=True)
        print('Video done')


    def update(self, frame):
        self.txt.set_text(f"Nr of Operations = {frame}")
        for rectangle, height in zip(self.container.patches, self.array.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#cf6f34")

        idx, op = self.array.GetActivity(frame)
        try:

            if op == "get":
                self.container.patches[idx].set_color("magenta")
            elif op == "set":
                self.container.patches[idx].set_color("blue")
            return (self.txt, *self.container)
        except IndexError:
            pass

 