import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[6,7,8,2,4]

x1=[1,3,5,7,9]
y1=[1,3,4,5,3]

plt.bar(x, y, label="bars1", color="r")
plt.bar(x1, y1, label="bars2", color="c")

plt.xlabel("x")
plt.ylabel("y")
plt.title("my data")
plt.legend()
plt.show()