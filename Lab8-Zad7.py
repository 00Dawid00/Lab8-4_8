import numpy as np

macierz = np.zeros((5, 5), dtype=int)

macierz[0, :] = 1  # Górny brzeg
macierz[-1, :] = 1  # Dolny brzeg
macierz[:, 0] = 1  # Lewy brzeg
macierz[:, -1] = 1  # Prawy brzeg

print("Macierz z jedynkami na brzegach:\n", macierz)


def zamien(macierz):
    return 1 - macierz  # Zamiana: 0 -> 1 i 1 -> 0


odwrocona_macierz = zamien(macierz)
print("\nMacierz po zamianie:\n", odwrocona_macierz)
