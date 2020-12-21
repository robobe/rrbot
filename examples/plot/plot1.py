import matplotlib.pyplot as plt
x=[1,2,3]
y=[1, 5, 2]
x1=[1,2,3]
y1=[5, 1, 3]
plt.plot(x, y, label="line1")
plt.plot(x1, y1, label="line2")
plt.xlabel("x-data")
plt.ylabel("y-axe")
plt.title("my data")
plt.legend()
plt.show()