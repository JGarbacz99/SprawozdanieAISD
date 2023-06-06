tablica = [
    [5, 8, 3, 2],
    [10, 1, 7, 6],
    [4, 9, 2, 11]
]
for i in range(0,len(tablica)):
    min_wartosc = tablica[i][0]
    for j in range(0,len(tablica[i])):
        print("tab",tablica[i][j])
        if tablica[i][j] < min_wartosc:
            min_wartosc = tablica[i][j]
            print("min",min_wartosc)
            indeks_min = j
    print("ind_min",indeks_min)
    temp = tablica[i][0]
    print('Temp:',temp)
    tablica[i][0] = min_wartosc
    tablica[i][indeks_min] = temp

for i in range(0,len(tablica)):
  print(tablica[i])
