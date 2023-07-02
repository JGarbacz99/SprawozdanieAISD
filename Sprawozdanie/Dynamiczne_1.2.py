def P(i, j):
    if i > 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return 1
    if i > 0 and j > 0:
        wartosc = P(i - 1, j) + 2 * P(i, j - 1)
        return wartosc


wynik = P(5, 5)
print(wynik)