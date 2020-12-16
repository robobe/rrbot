# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import queue

q = queue.Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
# q.put(5)

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(0, 4))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 4, 4)
    y = list(q.queue)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


# Show the plot
plt.show()