import matplotlib.pyplot as plt

values = [0, 0.6, 1.4, 1.6, 2.2, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=7) # valoare implicita pentru bins = 10 daca nu il declaram
plt.show()