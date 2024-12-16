import numpy as np

potegi_dwa = [2**i for i in range(7, -1, -1)]
print(potegi_dwa)

wagi = np.array(potegi_dwa)
print("Tablica wagi:", wagi)

liczba_bin = np.random.choice([0, 1], size=8)
print("Tablica liczba_bin:", liczba_bin)

def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi* liczba_bin)

wartosc = wartosc_liczby_bin(wagi, liczba_bin)
print("Wartość liczby binarnej w systemie dziesiętnym:", wartosc)