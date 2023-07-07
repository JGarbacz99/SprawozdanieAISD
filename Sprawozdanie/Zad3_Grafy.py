def zbudujGraf():
    print("Program pozwala na zdefiniowanie grafu")
    print("Jaki rodzaj grafu chcesz zbudować?")
    print("1. Skierowany")
    print("2. Nieskierowany")
    print("3. Ważony")
    print("4. Inny możliwy")

    opcje = int(input("Wybierz, który graf chcesz zbudować (1-4): "))
    liczbaWierzch = int(input("Podaj liczbę wierzchołków: "))
    liczbPolaczenWierzch = int(input("Podaj liczbę połączeń między wierzchołkami: "))

    graf = [[] for _ in range(liczbaWierzch)]
    print("Podaj połączenia w formacie 'wierzchołek_a wierzchołek_b', indeksowane od 0:")

    for _ in range(liczbPolaczenWierzch):
        polaczenie = input().split()
        wierzcholek_a = int(polaczenie[0])
        wierzcholek_b = int(polaczenie[1])

        if opcje == 3:
            waga = float(input(f"Podaj wagę połączenia {wierzcholek_a} -> {wierzcholek_b}: "))
            graf[wierzcholek_a].append((wierzcholek_b, waga))
        elif opcje == 2:
            graf[wierzcholek_a].append(wierzcholek_b)
            graf[wierzcholek_b].append(wierzcholek_a)
        else:
            graf[wierzcholek_a].append(wierzcholek_a)

    macierz_sasiedztwa = [[0] * liczbaWierzch for _ in range(liczbaWierzch)]
    for i in range(liczbaWierzch):
        for j in graf[i]:
            if opcje == 3:
                macierz_sasiedztwa[i][j[0]] = j[1]
            else:
                macierz_sasiedztwa[i][j] = 1

    macierz_list = {i: graf[i] for i in range(liczbaWierzch)}

    print("Macierz sąsiedztwa:")
    for row in macierz_sasiedztwa:
        print(row)

    print("Lista sąsiedztwa:")
    for wierzcholek, sasiedzi in macierz_list.items():
        print(f"Wierzchołek {wierzcholek}: {sasiedzi}")

    print("Interpretacja graficzna grafu:")
    for wierzcholek, sasiedzi in macierz_list.items():
        for sasiad in sasiedzi:
            print(f"{wierzcholek} -> {sasiad}")


zbudujGraf()
