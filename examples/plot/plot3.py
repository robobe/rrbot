import matplotlib.pyplot as plt

population_ages = [22, 33, 44, 55, 66 , 77, 88, 90, 91, 12, 22]
bins = [0, 10 , 20 , 30 , 40 , 50,  60 , 70, 80, 90]

plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)
plt.show()