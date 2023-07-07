def rozwinięcie_dziesiętne(liczba):
    cyfry = []
    while liczba > 0:
        cyfra = liczba % 10
        cyfry.insert(0, cyfra)
        liczba //= 10
    return cyfry


def sortowanie_leksykograficzne(liczby):
    posortowane_liczby = []
    for liczba in liczby:
        wstawiono = False
        for i, posortowana_liczba in enumerate(posortowane_liczby):
            if rozwinięcie_dziesiętne(liczba) < rozwinięcie_dziesiętne(posortowana_liczba):
                posortowane_liczby.insert(i, liczba)
                wstawiono = True
                break
        if not wstawiono:
            posortowane_liczby.append(liczba)
    return posortowane_liczby



wejście = [1, 2, 3, 11, 21, 111, 231]


wyjście = sortowanie_leksykograficzne(wejście)


print(wyjście)