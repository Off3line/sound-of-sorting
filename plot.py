import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class Plot():

    def __init__(self, array, n, sorter, ms,play_obj,color='orange'):
        self.array = array
        self.n = n
        self.sorter = sorter
        self.ms = ms
        self.play_obj = play_obj
        self.color = color


    def generate(self):
        fig, ax = plt.subplots()
        self.container = ax.bar(range(len(self.array)), self.array,align="edge", width=1)
        fig.suptitle(f"{self.sorter}")
        ax.set(xlabel="Index", ylabel="Value")
        ax.set_xlim(self.n)
        self.txt = ax.text(0.01, 0.99, "", ha="left",
                           va="top", transform=ax.transAxes)
        ani = FuncAnimation(fig, self.update, frames=range(len(self.array.values)),
                            blit=True, interval=self.ms, repeat=False,cache_frame_data=True)
        
        fig.set_size_inches(8,8)
        plt.show()
       
    def update(self, frame):
        self.txt.set_text(f"Nr of Operations = {frame} of {(len(self.array.values )-1)}")
        if frame == 0 and self.play_obj is not None:
                self.play_obj.play()
        for rectangle, height in zip(self.container.patches, self.array.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color(self.color)
       
        idx, op = self.array.GetActivity(frame)
        try:

            if op == "get":
                self.container.patches[idx].set_color("magenta")
            elif op == "set":
                self.container.patches[idx].set_color("blue")
            return (self.txt, *self.container)
        except IndexError:
            pass

 