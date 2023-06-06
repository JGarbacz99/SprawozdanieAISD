tab = [10, 5, 8, 3, 1, 6]
min_wartosc = tab[0]
for i in range(1, len(tab)):
    if tab[i] < min_wartosc:
        min_wartosc = tab[i]
print(f'Minimalna wartość w tablicy wynosi {min_wartosc}')