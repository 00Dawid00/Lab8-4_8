import numpy as np

macierz = np.random.randint(0, 51, (5, 5))

elementy_wieksze_niz_20 = macierz[macierz > 20]
liczba_elementow = elementy_wieksze_niz_20.size

srednia = np.mean(macierz)

print("Macierz 5x5:\n", macierz)
print("\nLiczba elementów większych niż 20:", liczba_elementow)
print("Średnia dla całej tablicy:", srednia)
