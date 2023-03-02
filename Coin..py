import numpy as np
import matplotlib.pyplot as plt
""" 
0 o sa fie heads
1 o sa fie tails
"""


coin = np.random.randint(0, 2) #(1, 7)

outcomes  = []
for i in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)

tails = [0]
for i in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[-1] + coin)

print(tails)
# daca utilizam un zar pentru a determina urmatorul pas il putem numi pas aleatoriu.
# daca dam cu zarul de 100 de ori putem afirma ca avem o succesiune de pasi aleatorii adica un mers aleatoriu.


np.random.seed(123)
final_tails = []
for i in range(10000):
    ## inceperea jocului - aruncarea monedei de 10 ori
    tails = [0]
    for j in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[-1] + coin)
    ## finalizarea joculu

    final_tails.append(tails[-1])

plt.hist(final_tails, bins=10)
plt.show()

