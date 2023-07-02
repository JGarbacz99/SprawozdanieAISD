n = 5
m = 5


def wspDwu(n, m):
    if n < 0 or m < 0:
        return print('Nieprawidłowe wartości')

    tablica = [[]]
    rzad = 0

    while rzad < n:
        kolumna = 0
        while kolumna < m:
            if kolumna == 0 or kolumna == rzad:
                tablica[rzad].append(1)
            elif kolumna > rzad:
                tablica[rzad].append("NaN")
            else:
                tablica[rzad].append(tablica[rzad - 1][kolumna] + tablica[rzad - 1][kolumna - 1])
            kolumna += 1

        rzad += 1
        tablica.append([])

    print(tablica)


wspDwu(n, m)


