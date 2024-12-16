import numpy as np

print("A")
tablica_a = np.zeros((3, 3), dtype=int)
tablica_a[-1, :] = 1
print(tablica_a)
print()

print("B")
tablica_b = np.zeros((3, 3), dtype=int)
np.fill_diagonal(tablica_b, 1)
tablica_b[0, 0] = 0
tablica_b[2, 2] = 0
tablica_b[2, 1] = 1
print(tablica_b)
print()

print("C")
tablica_c = np.zeros((3, 3), dtype=int)
tablica_c[1:, :] = 1
print(tablica_c)
print()

print("D")
tablica_d = np.zeros((3, 3), dtype=int)
tablica_d[0, 2] = 1
tablica_d[1, 2] = 1
tablica_d[0, 0] = 1
tablica_d[1, 0] = 1
print(tablica_d)
print()

print("E")
tablica_d = np.zeros((3, 3), dtype=int)
tablica_d[1, 1] = 1
tablica_d[1, 2] = 1
tablica_d[2, 1] = 1
tablica_d[2, 2] = 1
print(tablica_d)
print()
