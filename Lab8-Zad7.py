import numpy as np

macierz = np.zeros((5, 5), dtype=int)

macierz[0, :] = 1
macierz[-1, :] = 1
macierz[:, 0] = 1
macierz[:, -1] = 1

print("Macierz z jedynkami na brzegach:\n", macierz)


def zamien(macierz):
    return 1 - macierz


odwrocona_macierz = zamien(macierz)
print("\nMacierz po zamianie:\n", odwrocona_macierz)
