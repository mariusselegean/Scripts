import numpy as np

# 1. Cum putem genera numere aleatirii

# 2. Cum putem genera o miscare aleatorie

# 3. Cum putem sa raspundem la intrebarea, care sunt sansele noastre de a ajunge la treapta 60 aruncand cu zarul de 100 de ori


# aceste numere generate sunt pseudo-random deoarece sunt generate dupa o formula matematica proning de la o samanta
print(np.random.rand())
print(np.random.rand())
print(np.random.rand())
print(np.random.rand())


#cand folosim o samanta, putem sa generam numere aleatorii dar sunt aceleasi numere aleatorii de fiecare data cand rulam codul.
#Astfel se asigura reproductibilitatea

print("\n")
np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

print("\n")
np.random.seed(123)
print(np.random.rand())
print(np.random.rand())
print("\n")

""" 
0 o sa fie heads
1 o sa fie tails
"""

np.random.seed(123)
coin = np.random.randint(0, 2)
print(coin)