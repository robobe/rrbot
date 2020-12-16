# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
import queue

q = queue.Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
# Prepare the data


# Plot the data
plt.plot(list(q.queue), list(q.queue), label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()