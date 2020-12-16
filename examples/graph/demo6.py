# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from collections import deque  
import random

q = deque([1,2,3,4], 4)


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(0, 4))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    q.append(random.randint(1,4))
    x = np.linspace(0, 4, 4)
    y = list(q)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


# Show the plot
plt.show()