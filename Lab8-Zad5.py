import numpy as np

macierz = np.random.rand(5, 5)

print("Macierz 5x5:\n", macierz)
print("\nNajwiększy element:", macierz.max())
print("Najmniejszy element:", macierz.min())
print("\nNajwiększe w wierszach:", macierz.max(axis=1))
print("Największe w kolumnach:", macierz.max(axis=0))
print("\nSuma w wierszach:", macierz.sum(axis=1))
